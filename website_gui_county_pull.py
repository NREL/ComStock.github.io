import pandas as pd
import geopandas as gpd
import s3fs
import re
import ipywidgets as widgets
from IPython.display import display, clear_output
import us
import requests
import datetime
import boto3
from bs4 import BeautifulSoup

# # AWS S3 Setup
# BUCKET_NAME = "bstkanalysis.bps-workflow"
# FOLDER_NAME = "user_input_comstock_gui/"
# timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
# S3_FILE_NAME = f"{FOLDER_NAME}/{timestamp}_user_queries.csv"

# s3_client = boto3.client("s3")

# # Upload File
# local_file = "/tmp/user_queries.csv"
# s3_client.upload_file(local_file, BUCKET_NAME, S3_FILE_NAME)
# print(f"File saved in S3: s3://{BUCKET_NAME}/{S3_FILE_NAME}")

# S3 Access Setup
fs = s3fs.S3FileSystem(anon=True, client_kwargs={"region_name": "us-west-2"})

# Base URLs for Dataset
BASE_URL = "https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix="
BASE_PREFIX = ("nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/"
               "2024/comstock_amy2018_release_2/metadata_and_annual_results_aggregates/"
               "by_state_and_county/full/parquet/")

BASE_S3 = ("s3://oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/"
           "2024/comstock_amy2018_release_2/metadata_and_annual_results_aggregates/"
           "by_state_and_county/full/parquet/")

# Fetch county links from OEDI
def fetch_county_links(url):
    response = requests.get(url)
    html_content = response.text  
    return list(set(re.findall(r'county=G\d+/', html_content)))  # Extract county codes

# Load County Shapefile from Census TIGER Data
url = "https://www2.census.gov/geo/tiger/TIGER2023/COUNTY/tl_2023_us_county.zip"
gdf = gpd.read_file(url)

# Ensure Correct FIPS Formatting
gdf["STATEFP"] = gdf["STATEFP"].astype(str).str.zfill(2)
gdf["COUNTYFP"] = gdf["COUNTYFP"].astype(str).str.zfill(3)

# Construct NHGIS GISJOIN for Counties
gdf["GISJOIN"] = "G" + gdf["STATEFP"] + "0" + gdf["COUNTYFP"] + "0"

# Create Lookup Dictionary (GISJOIN → County Name)
county_lookup = {row["GISJOIN"]: row["NAME"] for _, row in gdf.iterrows()}

# Debugging: Print Sample GISJOIN Keys
print("Fixed NHGIS GISJOIN Keys in Lookup Table:", list(county_lookup.keys())[:10])

# User Data Storage
user_data_list = []

# Define User Info Widgets
first_name = widgets.Text(description="First Name:", layout={'width': '50%'})
last_name = widgets.Text(description="Last Name:", layout={'width': '50%'})
email = widgets.Text(description="Email:", layout={'width': '50%'})
use_case = widgets.Textarea(description="Use Case:", layout={'width': '90%', 'height': '100px'})

persona_options = [
    "Utility - Retail or Bulk", "Utility Regulator", "City/Local Government", 
    "Consultant", "State Energy Office", "Policy Advocates", "DOE/Federal Agency", 
    "Industry Tool Provider", "Manufacturer/Startup", "NREL Internal Tools", 
    "Lab/Academia", "Business/Investor", "Building Portfolio Owner", "Media"
]
persona_type = widgets.Dropdown(options=persona_options, description="Persona:", layout={'width': '90%'})

submit_info_button = widgets.Button(description="Submit Info", button_style='success')
dataset_output = widgets.Output()

# Define Dataset Selection Widgets
state_dropdown = widgets.Dropdown(options=[state.abbr for state in us.states.STATES],
                                  description='State:', layout={'width': '50%'})

county_dropdown = widgets.SelectMultiple(description='Counties:', layout={'width': '90%', 'height': '200px'})

column_selector = widgets.SelectMultiple(
    options=[
    "bldg_id", #keep
    "upgrade", #keep
    "in.upgrade_name", #keep
    "applicability", #keep
    "weight", #keep
    "in.cejst_is_disadvantaged", #keep
    "in.comstock_building_type_group", #keep
    "in.county_name", #keep
    "in.floor_area_category", #keep
    "in.hvac_category", #keep
    "in.interior_lighting_generation", #keep
    "in.state_name", #keep
    "out.site_energy.total.energy_consumption_intensity", #keep
    "calc.segment", #keep
    "calc.weighted.emissions.total_with_cambium_mid_case_15y..co2e_mmt", #keep
    "calc.weighted.emissions.total_with_egrid..co2e_mmt", #keep
    "calc.weighted.enduse_group.district_cooling.hvac.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.district_heating.hvac.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.district_heating.water_systems.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.electricity.hvac.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.electricity.interior_equipment.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.electricity.lighting.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.electricity.refrigeration.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.electricity.water_systems.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.natural_gas.hvac.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.natural_gas.interior_equipment.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.natural_gas.water_systems.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.other_fuel.hvac.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.other_fuel.water_systems.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.site_energy.hvac.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.site_energy.interior_equipment.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.site_energy.lighting.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.site_energy.refrigeration.energy_consumption..tbtu", #keep
    "calc.weighted.enduse_group.site_energy.water_systems.energy_consumption..tbtu", #keep
    "calc.weighted.site_energy.total.energy_consumption..tbtu", #keep
    "calc.weighted.sqft" #keep
],
    value=["bldg_id", "upgrade", "in.upgrade_name"],
    description='Columns:', layout={'width': '90%', 'height': '200px'}
)

load_button = widgets.Button(description="Download & Merge", button_style='success')


# Persistent UI Container for Dataset Selection
dataset_selection_ui = widgets.VBox([])

# Track if UI has been displayed
ui_displayed = False

def submit_user_info(_):
    global ui_displayed  
    with dataset_output:
        clear_output(wait=True)

        # Validate Required Fields
        missing_fields = []
        if not first_name.value.strip():
            missing_fields.append("First Name")
        if not last_name.value.strip():
            missing_fields.append("Last Name")
        if not email.value.strip():
            missing_fields.append("Email")
        if not use_case.value.strip():
            missing_fields.append("Use Case")
        if not persona_type.value.strip():
            missing_fields.append("Persona Type")

        # Prevent Proceeding if Any Field is Empty
        if missing_fields:
            print(f"Please fill out the following required fields to access data: {', '.join(missing_fields)}")
            return  # Stop execution if fields are missing

        # Proceed Only if All Fields are Filled
        if ui_displayed:
            print("Dataset selection UI is already displayed.")
            return

        print("User Information Submitted. Access Dataset Selection Below.")
        ui_displayed = True  

        # Ensure observer is attached only once
        if not hasattr(update_county_dropdown, "observer_attached"):
            state_dropdown.observe(update_county_dropdown, names='value')
            update_county_dropdown.observer_attached = True  

        # Display dataset selection UI only once
        dataset_selection_ui.children = [state_dropdown, county_dropdown, column_selector, load_button]
        display(dataset_selection_ui)

# Handle County Dropdown Update Based on State
def update_county_dropdown(*args):
    state = state_dropdown.value
    if state:
        formatted_state = f"state={state}/"
        counties_url = f"{BASE_URL}{BASE_PREFIX}{formatted_state}"
        county_links = fetch_county_links(counties_url)

        counties = {"All Counties": None}
        for county in county_links:
            try:
                county_code = county.split('=')[1].strip('/')
                state_fips = county_code[1:3]  
                county_fips = county_code[4:7]
                gisjoin_lookup = f"G{state_fips}0{county_fips}0"

                county_name = county_lookup.get(gisjoin_lookup, "Unknown County")
                counties[f"{state} - {county_name} ({county_code})"] = county_code
            except IndexError:
                continue

        county_dropdown.options = counties if counties else {"All Counties": None}
    else:
        county_dropdown.options = {"All Counties": None}

def download_and_merge_parquet(_):
    with dataset_output:
        clear_output(wait=True)
        state = state_dropdown.value
        counties = county_dropdown.value  # Ensure this is a list of selected counties
        timestamp = datetime.datetime.now().isoformat()

        if not state:
            print("Please select a state.")
            return

        if not counties:
            print("Please select at least one county.")
            return

        # Save User Query Data
        query_entry = {
            "First Name": first_name.value,
            "Last Name": last_name.value,
            "Email": email.value,
            "Use Case": use_case.value,
            "Persona": persona_type.value,
            "Selected State": state,
            "Selected Counties": ", ".join(counties),
            "Timestamp": timestamp
        }
        user_data_list.append(query_entry)

        df = pd.DataFrame(user_data_list)
        local_file = "/tmp/user_queries.csv"
        df.to_csv(local_file, index=False)

        try:
            s3_client.upload_file(local_file, BUCKET_NAME, S3_FILE_NAME)
            print(f"Query data stored in S3: {BUCKET_NAME}/{S3_FILE_NAME}")
        except Exception as e:
            print(f"Failed to upload query data to S3: {e}")

        print(f"Fetching dataset for {state} and {counties}...")

        #Dataset Download Logic
        all_dfs = []
        for county in counties:
            #Ensure county_code is correctly fetched from dropdown options
            county_code = county_dropdown.options.get(county, county)

            if county_code is None:
                print(f"County selection error: {county} has no valid county code.")
                continue  # Skip invalid selections

            files = [f"state={state}/county={county_code}/{state}_{county_code}_baseline_agg.parquet"]

            for file in files:
                s3_path = f"{BASE_S3}{file}"
                try:
                    df = pd.read_parquet(s3_path, filesystem=fs, engine='pyarrow')
                    all_dfs.append(df)
                except Exception:
                    continue

        if all_dfs:
            merged_df = pd.concat(all_dfs, ignore_index=True)
            output_file = f"merged_{state}_{'_'.join(counties)}.csv"
            merged_df.to_csv(output_file, index=False)
            print(f"Dataset saved: {output_file}")

# Link Widgets & Display
submit_info_button.on_click(submit_user_info)
load_button.on_click(download_and_merge_parquet)
state_dropdown.observe(update_county_dropdown, names='value')
display(first_name, last_name, email, use_case, persona_type, submit_info_button, dataset_output)
