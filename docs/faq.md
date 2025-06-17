---
layout: default
title: FAQ
nav_order: 8
published: true
---

# Frequently Asked Questions
{: .fw-500 }

Expand the sections below for answers to frequently asked questions. If you have additional questions, please email us at [ComStock@nrel.gov](mailto:ComStock@nrel.gov).

## ComStock Essentials
<ul class="jk_accordion">

  <li class="acc"><input id="accordion29" type="checkbox" /><label for="accordion29">Are these load profiles measured or simulated?</label>
    <div class="show">
      <p>The profiles are simulated using the ResStock and ComStock modeling tools, which have been validated and informed by the best available data against an array of empirical datasets. ResStock and ComStock use the EnergyPlus simulation engine. The validation results and uncertainty for quantities of interest are presented in the <a href="https://www.nrel.gov/docs/fy22osti/80889.pdf">End-Use Load Profiles final report.</a></p>
      <p>ResStock generally simulates 550,000 individual building energy models, and ComStock simulates 150,000 building energy models.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion7" type="checkbox" /><label for="accordion7">What building types does ComStock model?</label>
    <div class="show">
      <p>ComStock models 14 commercial building types. Compared to the Commercial Building Energy Consumption Survey (CBECS) estimation, ComStock datasets account for 64% of the energy use and 62% of the floor area of commercial buildings in the United States. The ComStock development team is actively working on adding more building types to the model. See the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/building_types_not_included.md %}">Building Types Not Included in ComStock</a>" for more detail.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion16" type="checkbox" /><label for="accordion16">What year does the baseline stock represent?</label>
    <div class="show">
      <p>The ComStock and ResStock datasets represent, as closely as possible, the 2018 U.S. commercial and residential building stock characteristics. The energy consumption results depend on the weather data used in the simulations. When modeled with AMY2018 weather, the datasets represent energy use for the year 2018. When TMY3 weather is used, they represent typical or average energy consumption under typical climate conditions.</p>
      <p>Emissions and utility bills in the ComStock and ResStock datasets use input data from a several years, depending on the dataset release. See the <a href="https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references">ComStock reference documentation</a> or <a href="https://nrel.github.io/ResStock.github.io/assets/trd/ResStock_Technical_Reference_Document_Final.pdf">ResStock reference documentation</a> for more details.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion4" type="checkbox" /><label for="accordion4">Are ComStock and ResStock credible?</label>
    <div class="show">
       <p>Yes. The models underwent extensive calibration as part of the End Use Load Profiles (EULP) project where we compared model load profiles to AMI data from around the country, and updated baseline model schedules, power densities, among other things using various data sources. Reference the <a href="https://www.nrel.gov/docs/fy22osti/80889.pdf">final report</a> for more details. The EULP project concluded in 2021.</p>
      <p>For every baseline update and upgrade measures since EULP, ComStock compares energy consumption and EUI to available data sources, such as CBECS and EIA. These comparisons are available on the OEDI Data Lake for each dataset. You can find links to OEDI in the Published Datasets section of the <a href="{{site.baseurl}}{% link docs/data.md %}">Data page</a>.</p>
      <p>For details about how to determine whether the models are appropriate for a specific analysis, reference the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/comstock_calibration.md %}">Considerations for ComStock Calibration, Validation, and Uncertainty</a>."</p>
    </div>
  </li>

  <li class="acc"><input id="accordion5" type="checkbox" /><label for="accordion5">Which dataset release should I use?</label>
    <div class="show">
      <p>ComStock publishes datasets on a regular basis, and we recommend using the latest release. See the <a href="{{site.baseurl}}{% link docs/data.md %}">Data page</a> for a list of available datasets and access links.</p>
      <p>New datasets include any improvements made to the baseline model, as well as new upgrade measures and all measures from previous releases. Information about upgrade measures included in dataset releases can be found on the <a href="{{site.baseurl}}{% link docs/upgrade_measures/upgrade_measures.md %}">Upgrade Measures page</a>. Baseline model improvements are captured in the release change log on our <a href="https://github.com/NREL/ComStock">public GitHub repository</a>. Note that we re-sample our input characteristic distributions for every release and as a result, the building IDs between releases will not match.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion6" type="checkbox" /><label for="accordion6">What are weights in ComStock and how are they used?</label>
    <div class="show">
      <p>Weights in ComStock represent the number of real buildings in the U.S. building stock that a ComStock model represents. Weights are determined using national floor area by building type from CBECS. Use the weights by multiplying the energy consumption column by the weight for the model. Some results columns already have the weight applied. These have the word “weighted” in the name. See the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/sampling_and_weighting.md %}">Sampling and Weighting in ComStock</a>" for more information.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion1" type="checkbox" /><label for="accordion1">How many profiles or models should be used for an analysis, and how does the number used affect uncertainty of results?</label>
    <div class="show">
      <p>The minimum sample count required for a given geography in ComStock is a function of the number of commercial buildings present in that area, as well as the quality of available input data for the ComStock model. To ensure statistical robustness in your analysis using ComStock, you may need additional building models depending on the specificity of your segmentation. A good rule of thumb is to include at least six models per segment (e.g., building type, sub-type, size, vintage, or operation hours). For example, if you’re analyzing small office buildings open more than 18 hours a day, make sure you have at least six such models.</p>
      <p>Also, cross-check ComStock’s building representation with external sources (like Google Maps or local datasets) to ensure the dataset reflects your target geography. For more detail, see the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/sample_size_considerations.md %}">Sample Size Considerations</a>"</p>
      <p>Queries in sparsely populated areas or with filters applied may have relatively few samples available. In these cases, samples from nearby locations can be grouped to increase the sample size. See the tutorial titled "<a href="{{site.baseurl}}{% link docs/resources/tutorials/local_segmentation_study.md %}">Perform an analysis by blending ComStock and local data</a>" for an example of incorporating local floor area estimates to improve representation of ComStock data at specific geographic resolutions.</p>
      <p>Users should estimate standard error for metrics of interest using the standard deviation divided by the square root of the number of samples (i.e., profiles or models). See Section 5.1.3 in the <a href="https://www.nrel.gov/docs/fy22osti/80889.pdf">End-Use Load Profiles methodology report</a> for a discussion on uncertainty calculations.
      </p>
    </div>
  </li>

  <li class="acc"><input id="accordion30" type="checkbox" /><label for="accordion30">How should I cite the datasets?</label>
    <div class="show">
      <p>ComStock and ResStock can be cited according to the suggestions <a href="{{site.baseurl}}{% link docs/citation.md %}">here for ComStock</a> and <a href="https://nrel.github.io/ResStock.github.io/docs/citation_data_attribution.html"> here for ResStock</a>.</p>
    </div>
  </li>

</ul>

## Datasets and Data Access
<ul class="jk_accordion">
  <li class="acc"><input id="accordion2" type="checkbox" /><label for="accordion2">How do I access the dataset?</label>
    <div class="show">
      <p>There are several access platforms available to access ComStock and ResStock datasets. See the <a href="{{site.baseurl}}{% link docs/data.md %}">ComStock Data page</a> and <a href="https://nrel.github.io/ResStock.github.io/docs/data.html">ResStock Data page</a> for more detail about dataset access and links to the public datasets.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion17" type="checkbox" /><label for="accordion17">Are descriptions available for the end-use categories and fields available for filtering?</label>
    <div class="show">
      <p>Descriptions of each of the building characteristics and the end-use categories can be found in the “data_dictionary.tsv” file. Descriptions of the values used in those filters can be found in the “enumeration_dictionary.tsv”. Both files can be downloaded from the OEDI Data Lake and are unique to each dataset release. Use the correct data dictionary for the relevant dataset. They can be opened with Excel or a text editor.</p>
      <p>Links to the OEDI Data Lake for each dataset release can be found on the <a href="{{site.baseurl}}{% link docs/data.md %}">ComStock Data page</a> and <a href="https://nrel.github.io/ResStock.github.io/docs/data.html">ResStock Data page</a>.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion18" type="checkbox" /><label for="accordion18">What are the data units?</label>
    <div class="show">
      <p>ComStock and ResStock data have multiple units. For annual results data downloaded from the Open Energy Data Initiative (OEDI) data lake, units can be found in the "data_dictionary.tsv" file. Some fields will also have the units in the column header at the end of the name (e.g., "out.electricity.total.jan.energy_consumption..<b>kwh</b>"). Timeseries energy consumption data on OEDI are provided in kWh. Natural gas, fuel oil, and propane are output in kwh--this is intentional though unconventional.</p>
      <p>The Data Viewer provides energy data in metric units, visible in the y-axis label. Depending on the scale of energy being shown, the metric prefix will automatically adjust (T for tera, G for giga, M for mega, etc.).</p>
      <p>For Tableau dashboards, use the relevant column headers or the graph axis to see the units.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion19" type="checkbox" /><label for="accordion19">What is the timezone of the timestamps?</label>
    <div class="show">
      <p>The timestamps of all load profiles have been converted to Eastern Standard Time, to prevent issues when aggregating across time zones.</p>
      <p>The underlying modeling was conducted using local standard time for each location, with occupant schedules adjusted for daylight savings as applicable. All EnergyPlus timeseries outputs were converted from local standard time to Eastern Standard Time for publication in the web Data Viewer, Data Viewer exports, timeseries aggregates, and individual timeseries parquet files. In converting from local Standard Time to Eastern Standard Time, if necessary the last few hours of each dataset were moved to the beginning of the timeseries. For example, the first two hours of data from Colorado in Eastern Standard Time (Jan 1, midnight to 2 AM) were originally modeled as the last two hours of the year in Mountain Standard Time (Dec 31, 10 PM to midnight) using the corresponding weather.</p>
    </div>
  </li>


  <li class="acc"><input id="accordion32" type="checkbox" /><label for="accordion32">Does the timestamp represent the beginning, middle, or end of each 15-minute interval?</label>
    <div class="show">
      <p>The timestamp indicates the end of each 15-minute interval. So "12:15" represents the energy use between 12:00 and 12:15.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion20" type="checkbox" /><label for="accordion20">Do the timeseries aggregates have the sample weighting factors applied?</label>
    <div class="show">
      <p>Yes. The aggregates represent the total relevant building stock with all relevant weights applied (e.g., all small office buildings in the state of Colorado), not just the sum of the model results.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion39" type="checkbox" /><label for="accordion39">Are there load profiles available for the 16 California Climate Zones?</label>
    <div class="show">
      <p>ComStock includes commercial buildings in California. However, as of ComStock 2024 Release 2, California climate zones are not available as a characteristic in ComStock public datasets. This characteristic will be made available in an upcoming dataset release.</p>
      <p>There are a few known issues with California models in ComStock. Please see the "<a href="{{site.baseurl}}{% link docs/resources/explanations/california_known_issues.md %}">California Models Known Issues</a>" explanation for more information.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion9" type="checkbox" /><label for="accordion9">What do the codes used to describe "county_id" and other geographic fields mean?</label>
    <div class="show">
      <p>ComStock and ResStock use the National Historical GIS (NHGIS) GISJOIN standard codes for county, census PUMA, and census tract, which are based on Federal Information Processing System (FIPS) codes. The datasets use the 2010 version of the GISJOIN codes--2020 are not available at this time. For more information about the geospatial fields available in the datasets, see "<a href="{{site.baseurl}}{% link docs/resources/explanations/reference_geographic_codes.md %}">this explanation for ComStock</a>, and <a href="https://nrel.github.io/ResStock.github.io/docs/resources/explanations/Geographic_Fields_and_Codes.html">this explanation for ResStock.</a></p>
      <p>In most ComStock and ResStock datasets, county name is available in addition to the GISJOIN county code. For both tools, the column in the metadata_and_annual_results files on OEDI is called "in.county_name."
      </p>
    </div>
  </li>

  <li class="acc"><input id="accordion8" type="checkbox" /><label for="accordion8">Where can I find documentation on what technologies are available in the upgrade measures?</label>
    <div class="show">
      <p>See the <a href="{{site.baseurl}}{% link docs/upgrade_measures/upgrade_measures.md %}">Upgrade Measures</a> page for a complete list of available upgrade measures and packages in ComStock datasets, including a link to their documentation, and in which dataset release the measure was first included.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion22" type="checkbox" /><label for="accordion22">Are weather data files available in EPW format?</label>
    <div class="show">
      <p>Weather data used for the modeling have been provided in .csv format for regression modeling, forecasting, or other analyses. The TMY3 weather files in EnergyPlus input format (EPW) can be downloaded from the <a href="https://data.nrel.gov/submissions/156">NREL Data Catalog</a>, with filenames that correspond to county IDs in the ResStock and ComStock metadata. EPW format weather files for 2018 or other actual meteorological years (AMY) have not been publicly released. These files can be purchased from private sector vendors. See <a href="https://energyplus.net/weather/simulation">here</a> for a list of providers.
      </p>
    </div>
  </li>

  <li class="acc"><input id="accordion24" type="checkbox" /><label for="accordion24">Are the EnergyPlus model input files (.idf) or OpenStudio (.osm) files available?</label>
    <div class="show">
      <p>OpenStudio model input files (.osm) are available in the dataset on the OEDI data lake in the "building_energy_models" directory. Files are named by the building ID ("bldg_id").  The EnergyPlus model input files are not available.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion25" type="checkbox" /><label for="accordion25">Is there an API to access data without downloading locally?</label>
    <div class="show">
      <p>Currently, there is no API. However, we have posted a <a href="https://www.youtube.com/watch?v=qSR1MFpSiro&list=PLmIn8Hncs7bEYCZiHaoPSovoBrRGR-tRS&index=4">tutorial example</a> showing how to load the datasets into cloud services such as Amazon Web Services (AWS) so the data can be queried by analytic tools like Athena.</p>
      <p>Example notebooks and SQL queries are also available on the "<a href="{{site.baseurl}}{% link docs/resources/how_to_guides/example_scripts.md %}">Access ComStock datasets programmatically</a>" page, and more will be added as we develop them. The queries and example notebooks are a good starting point for accessing ResStock programmatically, too.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion28" type="checkbox" /><label for="accordion28">What software can I use to open the .parquet files?</label>
    <div class="show">
      <p>Parquet files can be read using programming languages such as Python, using the pyarrow package. For other options, see <a href="https://arrow.apache.org/docs/index.html">here</a>. There are a few third-party graphical tools for viewing parquet files, but we have not tested them and the third-party support is limited.</p>
      <p>See below for example Python code to convert parquet file to csv.
        <pre><code>
        import pandas as pd
        import os
        folder_path = 'C:/Users/username/Documents/EUSS/Results’
        file_name = ‘813-2’
        suffix = '.parquet'
        file = pd.read_parquet(os.path.join(folder_path, file_name+suffix))
        new_suffix = '.csv'
        file.to_csv(os.path.join(folder_path, file_name+new_suffix), index = False)
        </code></pre>
      </p>
    </div>
  </li>

  <li class="acc"><input id="accordion23" type="checkbox" /><label for="accordion23">I am trying to match buildings between releases. Why do the building IDs not match between them?</label>
    <div class="show">
      <p>The building IDs and exact building characteristics between releases will not match because we re-sample our input characteristic distributions for every release. However, you can filter the building models using building characteristics to identify similar samples between releases. For instance, using building type, size, location, and wall construction type to identify similar models. The fields with the prefix “in.” show the available model inputs that you can use to do the comparison. You can see a complete list and description of available fields in the “data_dictionary.tsv” file on the OEDI Data Lake. Links to the datasets on OEDI are in the "Published Datasets" section of the <a href="{{site.baseurl}}{% link docs/data.md %}">ComStock Data page</a> and <a href="https://nrel.github.io/ResStock.github.io/docs/data.html">ResStock data page</a>.</p>
    </div>
  </li>
  
</ul>

## Data Viewer
<ul class="jk_accordion">

  <li class="acc"><input id="accordion26" type="checkbox" /><label for="accordion26">In the Data Viewer, what does "sum" or "average" mean?</label>
    <div class="show">
      <p>The "sum" aggregation is the total energy consumption for all buildings that meet the filter criteria across all the occurrences of the given time step within the selected month(s). For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the sum of all energy consumption statewide between 7-7:15 AM in July, from buildings that meet the filter criteria. The "sum" view has fewer uses than the "average" view. The "average" aggregation is the total energy consumption for all buildings that meet the filter criteria, averaged across all the occurrences of the given time step within the selected month(s).</p>
      <p>For example, in a day timeseries range for a specific state for the month of July, the 7-7:15 AM hour time step shows the average statewide energy consumption between 7-7:15 AM in July, from buildings that meet the filter criteria. The "average" aggregation provides a view of the average day of total energy consumption in the state. This is the more logical view for most use cases. Note that while each time step within a day or a year has the same number of occurrences within each dataset, each time step for a week does not - some days of the week occur more times than others in each year or month range (except for February).
      </p>
    </div>
  </li>

  <li class="acc"><input id="accordion27" type="checkbox" /><label for="accordion27">In the Data Viewer, how are the peak day and min peak day defined?</label>
    <div class="show">
      <p>The peak day is the day with the highest single-hour (peak) energy consumption within the selected months.</p>
      <p>The min peak day is the day with the lowest single-hour energy consumption within the selected months.</p>
    </div>
  </li>

    <li class="acc"><input id="accordion31" type="checkbox" /><label for="accordion31">Why is the time series data sometimes slow to load after I click the update button?</label>
    <div class="show">
      <p>We query data in real time to produce the time series graphs you see on the webpage, and this can involve scanning terabytes (TB) of data. Running a baseline-only query for California, Texas, New York, or Illinois takes around a minute, while running a query for a state like Colorado or Massachusetts takes about 10-20 seconds. However, if the graphs have previously been generated we have the data cached and can typically load the data in a few seconds. That's why the load time varies.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion32" type="checkbox" /><label for="accordion32">Why can’t I click on “Explore Timeseries”?</label>
    <div class="show">
      <p>The “Explore Timeseries” option is available once a specific geography (e.g. state or PUMA region) is selected.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion31" type="checkbox" /><label for="accordion31">How do I see a profile for just one, or just a few, end uses?</label>
    <div class="show">
      <p>Clicking on the end uses in the legend will highlight the end use in the visualization.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion33" type="checkbox" /><label for="accordion33">Can I aggregate over multiple locations?</label>
    <div class="show">
      <p>The viewer allows aggregations of up to six locations (states or PUMAs, depending on the dataset). When viewing a single location, choose the “+ More Locations” option, add up to five additional locations, and choose “Update Search”.</p>
      <p>Additionally, sums of more than six locations can be created manually by downloading sums of up to six locations and summing further on your local computer.</p>
      <p>TMY3 weather is not aligned between locations. This does not affect our recommendations for working with annual data. However, if your application requires timeseries data and therefore would benefit from aligned weather, we recommend either using an AMY dataset, or filtering by weather station and summing only within a single weather station’s PUMAs.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion34" type="checkbox" /><label for="accordion34">How can I filter the data based on building characteristics?</label>
    <div class="show">
      <p>The "+ Filter" button enables users to filter the data by characteristics, such as vintage, floor area, and building type. This feature also enables aggregations of locations, including by PUMA and county.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion35" type="checkbox" /><label for="accordion35">How can I see the building characteristics associated with an aggregate load profile from the data viewer?</label>
    <div class="show">
      <p>The building characteristics are available on the Open Energy Data Initiative (OEDI) data lake. Visit the <a href="{{site.baseurl}}{% link docs/data.md %}">Data page</a> for links to the OEDI pages for each dataset. In the "metadata_and_annual_results_aggregate" directory on OEDI, navigate to the national file: metadata_and_annual_results_aggregates > national > full > csv > baseline_agg.csv.gz. Download the file, unzip it and open in Microsoft Excel. Use the filters applied on the Data Viewer to filter the spreadsheet.</p>
      <p>Note that the national file is an “aggregate,” meaning that the data in the file is consolidated by merging duplicate building models within a geography (in this case state), so each building ID appears only once with a combined weight. Columns that cannot be meaningfully aggregated from the tract level—such as Cambium grid region and CEJST designation—are excluded from the resulting low-resolution, “aggregate” files. For more information about the updated OEDI file structure as a result of the new sampling method, please see the "<a href="{{site.baseurl}}{% link docs/resources/explanations/new_sampling_method.md %}">New ComStock Sampling Method explanation</a>".</p>
    </div>
  </li>

</ul>

## Analysis
<ul class="jk_accordion">
  <li class="acc"><input id="accordion10" type="checkbox" /><label for="accordion10">Can I run ComStock or ResStock myself?</label>
    <div class="show">
      <p>The code required to run ComStock and ResStock is available on the <a href="https://github.com/NREL/ComStock">ComStock</a> and <a href="https://github.com/NREL/ResStock">ResStock</a> public GitHub repositories. Other related code repositories are provided on the "For Developers" page for <a href="{{site.baseurl}}{% link docs/for_developers/for_developers.md %}">ComStock</a> and <a href="https://nrel.github.io/ResStock.github.io/docs/developers.html">ResStock.</a></p>
      <p>While these resources are available, ComStock and ResStock are complex modeling tools and there is no documentation for running the model other than what exists in the codebase, and we are not able to support running the models at this time. We generally do not recommend running the model unless you have a deep understanding of the methodology and objectives. Please email us at <a href="mailto:ComStock@nrel.gov">ComStock@nrel.gov</a> or <a href="mailto:ResStock@nrel.gov">ResStock@nrel.gov</a> if you have suggestions for improvements or specific needs.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion15" type="checkbox" /><label for="accordion15">I am interested in an upgrade measure combination that is not currently available as an upgrade package in the public datasets. Can I combine results from the individual measures?</label>
    <div class="show">
      <p>Our general guidance is to <b>NOT</b> combine measure results. There are interactions between most upgrade measures that affect the amount of savings and make results of multiple measures together misleading.</p>
      <p>For an explanation and examples on this topic, see the linked <a href="{{site.baseurl}}{% link docs/resources/explanations/combining_measure_results.md %}">ComStock</a> and <a href="https://nrel.github.io/ResStock.github.io/docs/resources/explanations/Individual_Measures_Not_Combined.html">ResStock</a> resources.</p>
      <p>If you have questions about combining specific measures, please email us at <a href="mailto:ComStock@nrel.gov">ComStock@nrel.gov</a> or <a href="mailto:ResStock@nrel.gov">ResStock@nrel.gov</a></p>
    </div>
  </li>

</ul>

## Modeling Methods, Assumptions and Documentation
<ul class="jk_accordion">

  <li class="acc"><input id="accordion3" type="checkbox" /><label for="accordion3">Where can I find information about ComStock modeling methodology and assumptions?</label>
    <div class="show">
      <p>ComStock reference documentation is available in the <a href="https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references">References section</a> of the <a href="{{site.baseurl}}{% link docs/resources/resources.md %}">Resources page</a>. We publish an updated version with every dataset release that includes changes to the ComStock model.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion36" type="checkbox" /><label for="accordion36">What emissions scenarios are modeled?</label>
    <div class="show">
      <p>ComStock calculates the greenhouse gas emissions from the building stock and savings from measures using both historical and projected emissions data. Historical electricity emissions use the CO<sub>2</sub>-equivalent total output emission rate from EPA’s Emissions and Generation Resource Integrated Database (eGRID). Projected electricity emissions use data from NREL’s Cambium dataset. Projected emissions consider both the average emissions rate (AER) and the long-run marginal emission rate (LRMER).</p>
      <p>Natural gas, propane, and fuel oil emissions use the emission factors defined in ANSI/RESNET/ICCC 301-2022 Addendum B-2022 Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units using an Energy Rating Index.</p>
      <p>Emissions input data are updated as they become available and do not always match the ComStock dataset release simulation year (typically 2018). Please see the <a href="https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references">ComStock reference documentation</a> for more detail and specifics about which emissions input data years were used for a given dataset release.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion38" type="checkbox" /><label for="accordion38">Are costs modeled?</label>
    <div class="show">
      <p>As of the 2024 Release 1, ComStock includes utility cost data using current electricity rates from the Utility Rate Database (URDB), matched by utility ID, demand, and usage. Annual utility bills are reported as the min, max, mean, and median of all applicable rates for each model. Natural gas, propane, and fuel oil prices are based on volumetric pricing due to limited rate data, using EIA price and heat content data. See the <a href="https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references">ComStock reference documentation</a> for details.</p>
      <p>ComStock does not calculate first costs (i.e., upgrade or measure costs). However, many ComStock output variables can be used to estimate first cost. See the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/costing_analysis.md %}">Using ComStock to Analyze Cost</a>" for more detail about cost assessments, including a discussion of output variables that can be used to estimate first costs.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion13" type="checkbox" /><label for="accordion13">Does ComStock model rooftop solar PV?</label>
    <div class="show">
      <p>ComStock does not currently model rooftop solar PV, though this capability is coming soon. We recommend using <a href="https://pvwatts.nrel.gov/">PVWatts</a> or <a href="https://reopt.nrel.gov/tool">REopt</a> to evaluate commercial solar PV opportunities.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion21" type="checkbox" /><label for="accordion21">Are there electric vehicle (EV) charging profiles in the dataset?</label>
    <div class="show">
      <p>No, ComStock does not currently model EV charging in the dataset. For modeling aggregate EV load profiles for a city or state, we suggest using <a href="https://afdc.energy.gov/evi-pro-lite/load-profile">EVI-Pro Lite</a>. Measured charging profile data for individual homes can be found in the <a href="https://neea.org/data/nw-end-use-load-research-project/energy-metering-study-data">NEEA HEMS data</a> and <a href="https://www.pecanstreet.org/dataport/">Pecan Street Dataport</a>. Email us at <a href="mailto:ComStock@nrel.gov">ComStock@nrel.gov</a> if you have suggestions for other EV charging data sources.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion11" type="checkbox" /><label for="accordion11">Are there water heater upgrade measures available?</label>
    <div class="show">
      <p>We have not published a service water heating measure due to current water draw profiles in our baseline models. The energy consumed by heat pump water heaters (HPWHs), especially, is sensitive to how quickly the water in the tank is consumed. More specifically, how to design and size a HPWH system greatly relies on realistic water draw profiles to correctly capture when the heat pump heating and, especially, backup heating elements are triggered.</p>
      <p>If you are aware of water draw profile Fdata, please let email us at <a href="mailto:ComStock@nrel.gov">ComStock@nrel.gov</a>! We are in search of 15-min to hourly water draw profiles for commercial buildings of various types and square footage.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion14" type="checkbox" /><label for="accordion14">Does ComStock model data centers?</label>
    <div class="show">
      <p>We do not currently model data centers as a building type in ComStock. Some large office buildings include data center loads, but these do not capture the characteristics, performance, HVAC system, etc. of standalone data centers and we do not recommend extrapolating results from these models.</p>
    </div>
  </li>

  <li class="acc"><input id="accordion37" type="checkbox" /><label for="accordion37">How are leap years modeled?</label>
    <div class="show">
      <p>To date, ComStock public dataset releases include AMY2018 and TMY3 weather years, neither of which are leap years.</p>
      <p>If ComStock were to simulate a leap year, the workflow would be as follows. The default simulation setting is a one-year, 8,760-hour simulation, starting on January 1 and ending on December 31. If the calendar year of simulation is a leap year, the end of the simulation period will be input as December 30 instead of December 31 to ensure 8,760 hours of simulation results. In years with February 29, December 31 will not be included in the simulation.</p>
      <p>For more detail, please see the <a href="https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references">ComStock reference documentation</a>.</p>
    </div>
  </li>

</ul>
