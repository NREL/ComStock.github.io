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

# AWS S3 Setup
BUCKET_NAME = "bstkanalysis.bps-workflow"
FOLDER_NAME = "user_input_comstock_gui"
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
S3_FILE_NAME = f"{FOLDER_NAME}/{timestamp}_user_queries.csv"

s3_client = boto3.client("s3")

# S3 Access Setup
fs = s3fs.S3FileSystem(anon=True, client_kwargs={"region_name": "us-west-2"})

# Base URLs for Dataset
BASE_URL = "https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix="
BASE_PREFIX = ("nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/"
               "2024/comstock_amy2018_release_2/metadata_and_annual_results_aggregates/"
               "by_state_and_county/full/parquet/")
BASE_S3 = "s3://oedi-data-lake/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2024/comstock_amy2018_release_2/metadata_and_annual_results_aggregates/by_state_and_county/full/parquet/"

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

county_dropdown = widgets.SelectMultiple(description='Counties:', layout={'width': '95%', 'height': '200px'})

upgrade_selector = widgets.SelectMultiple(
    options=["Baseline"] + [f"upgrade{str(i).zfill(2)}" for i in range(1, 41)],  
    value=["Baseline"],  
    description="Datasets:", layout={'width': '90%', 'height': '200px'}
)

column_selector = widgets.SelectMultiple(
    options=["bldg_id", "upgrade", "in.upgrade_name", "applicability", "weight", "in.county_name",
             "out.site_energy.total.energy_consumption_intensity", "calc.segment", "calc.weighted.sqft"],
    value=["bldg_id", "upgrade", "in.upgrade_name"],
    description='Columns:', layout={'width': '90%', 'height': '200px'}
)

load_button = widgets.Button(description="Download & Merge", button_style='success')

# UI Container for Dataset Selection
dataset_selection_ui = widgets.VBox([])

# Track if UI has been displayed
ui_displayed = False

# Validate email format
def validate_email(email):
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_pattern, email)

# Handle user info submission
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
        if not email.value.strip() or not validate_email(email.value):
            missing_fields.append("Valid Email")
        if not use_case.value.strip():
            missing_fields.append("Use Case")

        if missing_fields:
            print(f"Please fill out the following fields: {', '.join(missing_fields)}")
            return

        if ui_displayed:
            print("Dataset selection UI is already displayed.")
            return

        print("User Information Submitted. Access Dataset Selection Below.")
        ui_displayed = True  

        # Attach observer only once
        if not hasattr(update_county_dropdown, "observer_attached"):
            state_dropdown.observe(update_county_dropdown, names='value')
            update_county_dropdown.observer_attached = True  

        dataset_selection_ui.children = [
            state_dropdown, county_dropdown, upgrade_selector, column_selector, load_button
        ]
        display(dataset_selection_ui)

def update_county_dropdown(*args):
    """Update the county dropdown options when the state is selected."""
    state = state_dropdown.value
    if state:
        state_fips = us.states.lookup(state).fips.zfill(2)
        county_options = {"All Counties": "All"}

        for gisjoin, county_name in county_lookup.items():
            if gisjoin.startswith(f"G{state_fips}0"):
                county_options[f"{county_name} ({gisjoin})"] = gisjoin  

        county_dropdown.options = county_options
    else:
        county_dropdown.options = {"All Counties": "All"}

def download_and_merge_parquet(_):
    """Fetch dataset based on user selection."""
    with dataset_output:
        clear_output(wait=True)
        state = state_dropdown.value
        counties = county_dropdown.value
        selected_datasets = upgrade_selector.value  
        selected_columns = list(column_selector.value)
        timestamp = datetime.datetime.now().isoformat()

        if not state:
            print("Please select a state.")
            return
        if not counties:
            print("Please select at least one county.")
            return

        cleaned_counties = [c for c in counties if c]  

        # Save user query details
        query_entry = {
            "First Name": first_name.value,
            "Last Name": last_name.value,
            "Email": email.value,
            "Use Case": use_case.value,
            "Persona": persona_type.value,
            "Selected State": state,
            "Selected Counties": ", ".join(cleaned_counties),  
            "Selected Datasets": ", ".join(selected_datasets),
            "Timestamp": timestamp
        }
        user_data_list.append(query_entry)

        # # Store user data in S3
        # df = pd.DataFrame(user_data_list)
        # local_file = "/tmp/user_queries.csv"
        # df.to_csv(local_file, index=False)

        # try:
        #     s3_client.upload_file(local_file, BUCKET_NAME, S3_FILE_NAME)
        #     print(f"Query data stored in S3: {BUCKET_NAME}/{S3_FILE_NAME}")
        # except Exception as e:
        #     print(f"Failed to upload query data to S3: {e}")

        # Dataset download logic
        print(f"Fetching dataset for {state} and {cleaned_counties}...")
        all_dfs = []
        for county in cleaned_counties:
            county_code = county_dropdown.options.get(county, county)
            if county_code is None or county_code == "All":
                continue

            files = [f"state={state}/county={county_code}/{state}_{county_code}_baseline_agg.parquet"]
            for upgrade in selected_datasets:
                if upgrade != "Baseline":
                    files.append(f"state={state}/county={county_code}/{state}_{county_code}_{upgrade}_agg.parquet")

            for file in files:
                s3_path = f"{BASE_S3}{file}"
                try:
                    df = pd.read_parquet(s3_path, filesystem=fs, engine='pyarrow')
                    df = df[selected_columns]  # Filter columns
                    all_dfs.append(df)
                    print(f"Loaded: {s3_path}")
                except Exception:
                    print(f"Skipped missing file: {s3_path}")
                    continue

        if all_dfs:
            merged_df = pd.concat(all_dfs, ignore_index=True)
            output_file = f"merged_{state}_{'_'.join(cleaned_counties)}.csv"
            merged_df.to_csv(output_file, index=False)
            print(f"Dataset saved: {output_file}")
        else:
            print("No data could be downloaded.")

submit_info_button.on_click(submit_user_info)
load_button.on_click(download_and_merge_parquet)
state_dropdown.observe(update_county_dropdown, names='value')
display(first_name, last_name, email, use_case, persona_type, submit_info_button, dataset_output)
