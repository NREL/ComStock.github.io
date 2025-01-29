---
layout: default
title: FAQs
nav_order: 8
published: true
---

# Frequently Asked Questions
{: .fw-500 }

See below for answers to frequently asked questions. If you have additional questions, please email us at [ComStock@nrel.gov](mailto:ComStock@nrel.gov)

<details>
    <summary>How do I access the dataset?</summary>
    <p>There are several access platforms available to access ComStock datasets. See the <a href="{{site.baseurl}}{% link docs/data.md %}">Data</a> page for more detail about dataset access and links to the public dataset releases.</p>
</details>

<details>
    <summary>Where can I find information about ComStock modeling methodology and assumptions?</summary>
    <p>ComStock reference documentation is available in the <a href="https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references">References section</a> of the Resources page. We publish an updated version with every dataset release that includes changes to the core ComStock model</p>
</details>

<details>
    <summary>Is ComStock calibrated?</summary>
    <p>Yes. The models underwent extensive calibration as part of the End Use Load Profiles (EULP) project where we compared model load profiles to AMI data from around the country, and updated baseline model schedules, power densities, among other things using various data sources. Reference the <a href="https://www.nrel.gov/docs/fy22osti/80889.pdf">final report</a> for more details. The EULP project concluded in 2021.<br><br>

    For every baseline update and upgrade measures since EULP, we compare energy consumption and EUI to available data sources, such as CBECS and EIA Form 861. These comparisons are available on the <a href="{{site.baseurl}}{% link docs/data.md %}">OEDI Data Lake</a> for each dataset. High level savings observations of upgrade measures are available <a href="{{site.baseurl}}{% link docs/upgrade_measures/upgrade_measures.md %}">here</a>.<br><br>

    For details about how to determine whether the models are appropriate for a specific analysis, reference the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/comstock_calibration.md %}">Considerations for ComStock Calibration, Validation, and Uncertainty</a>."</p>
</details>

<details>
    <summary>Which dataset release should I use?</summary>
    <p>ComStock publishes datasets on a regular basis, and we recommend using the latest release. See the <a href="{{site.baseurl}}{% link docs/data.md %}">Data page</a> for a list of available datasets and access links. Each new release includes new upgrade measures, all measures from previous releases, as well as any improvements made to the baseline model.</p>
</details>

<details>
    <summary>What are weights in ComStock and how are they used?</summary>
    <p>Weights in ComStock represent the number of real buildings that the model represents in the U.S. building stock. Weights are determined using national floor area by building type from CBECS. All ComStock models of the same building type will have the same weight. Use the weights by multiplying the energy consumption column by the weight for the model. Some energy consumption columns are already weighted. These have the word “weighted” in the name. See an explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/sampling_and_weighting.md %}">Sampling and Weighting in ComStock</a>" for more information </p>
</details>

<details>
    <summary>What building types are does ComStock model?</summary>
    <p>ComStock models 14 commercial building types. Compared to the Commercial Building Energy Consumption Survey (CBECS) estimation, ComStock for 64% of the energy use and 62% of the floor area of commercial buildings in the United States. The core development team is actively working on adding more building types to the model. See the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/building_types_not_included.md %}">Building Types Not Included in ComStock</a>" for more detail.</p>
</details>

<details>
    <summary>Where can I find documentation on what technologies are available in the upgrade measures?</summary>
    <p>See the <a href="{{site.baseurl}}{% link docs/upgrade_measures/upgrade_measures.md %}">Upgrade Measures</a> page.</p>
</details>

<details>
    <summary>What do the codes used to describe "county_id" and other geographic fields mean?</summary>
    <p>These represent the NHGIS code for various geographies available in ComStock. For more information about the geospatial fields available in the ComStock dataset, see the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/reference_geographic_codes.md %}">Geographic Fields and Codes</a>".</p>
</details>

<details>
    <summary>Can I run ComStock myself?</summary>
    <p>The code required to run ComStock is available on our public <a href="https://github.com/NREL/ComStock">ComStock GitHub repository</a>. Other related code repositories are provided on our <a href="{{site.baseurl}}{% link docs/for_developers/for_developers.md %}">For Developers</a> page. We are not able to support running the model at this time.</p>
</details>

<details>
    <summary>Are there water heater upgrade measures available?</summary>
    <p>We have not published a service water heating measure due to current water draw profiles in our baseline models. The energy consumed by heat pump water heaters (HPWHs), especially, is sensitive to how quickly the water in the tank is consumed. More specifically, how to design and size a HPWH system greatly relies on realistic water draw profiles to correctly capture when the heat pump heating and, especially, backup heating elements are triggered.<br><br>

    If you are aware of water draw profile data, please let email us at <a href="mailto:ComStock@nrel.gov">ComStock@nrel.gov</a>. We are in search of 15-min to hourly water draw profiles for commercial buildings of various types and square footage.</p>
</details>

<details>
    <summary>What changes are made to the model between dataset releases?</summary>
    <p>ComStock publishes datasets on a regular basis. New datasets include new upgrade measures and baseline improvements, as well as all existing upgrade measures. Information about upgrade measures included in dataset releases can be found on the <a href="{{site.baseurl}}{% link docs/upgrade_measures/upgrade_measures.md %}">Upgrade Measures</a> page. Baseline model improvements are captured in the release change log on our public <a href="https://github.com/NREL/ComStock">ComStock GitHub repository</a>.</p>
</details>

<details>
    <summary>Does ComStock model rooftop solar PV?</summary>
    <p>ComStock does not currently model rooftop solar PV. We recommend using <a href="https://pvwatts.nrel.gov/"> PVWatts</a> to evaluate commercial solar PV opportunities.</p>
</details>

<details>
    <summary>Does ComStock model data centers?</summary>
    <p>We do not currently model data centers as a building type in ComStock. Some large office buildings include data center loads, but these do not capture the characteristics, performance, HVAC system, etc. of standalone data centers and we do not recommend extrapolating results from these models.</p>
</details>

<details>
    <summary>I am interested in an upgrade measure combination that is not currently available as an upgrade package in the public datasets. Can I combine results from the individual measures?</summary>
    <p>Our guidance is to <b>NOT</b> combine individual measure results. There are interactions between most upgrade measures (e.g., heat transfer impacts) that affect the amount of savings and make results of multiple measures together misleading. When considering envelope and heat pump measures, especially, there will be interactions that are not captured by combining results, and we recommend presenting these results separately.<br><br>

    See an explanation and examples on this topic in an explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/combining_measure_results.md %}">Why Individual ComStock Measure Results Should Not Be Combined</a>".</p>
</details>

<details>
    <summary>What year does the baseline stock represent?</summary>
    <p>The building stock represents, as closely as possible, the U.S. building stock as it was in 2018.</p>
</details>

<details>
    <summary>Are descriptions available for the end-use categories and fields available for filtering?</summary>
    <p>Descriptions of each of the building characteristics filters and the end-use categories can be found in the "data_dictionary.tsv" file. Descriptions of the values used in those filters can be found in the "enumeration_dictionary.tsv." Both files can be downloaded from the <a href="{{site.baseurl}}{% link docs/data.md %}">OEDI Data Lake</a> and can be opened with Excel or a text editor.</p>
</details>

<details>
    <summary>What are the data units?</summary>
    <p>All downloaded energy data is in kWh, including all electricity, natural gas, propane, and fuel oil end uses, as documented in the data_dictionary.tsv files which can be found on the OEDI Data Lake.<br><br>

    Timeseries energy consumption data viewed on the website are in metric units. The metric prefix is on the y-axis label (T for tera, G for giga, M for mega, etc.) and the rest of the unit information is in the y-axis label.</p>
</details>

<details>
    <summary>What is the timezone of timestamps?</summary>
    <p>The timestamps of all load profiles have been converted to Eastern Standard Time, to prevent issues when aggregating across time zones.<br><br>

    The underlying modeling was done using local Standard Time for each location. In converting from local Standard Time to Eastern Standard Time, if necessary the last few hours of each dataset were moved to the beginning of the timeseries. For example, the first two hours of data from Colorado in Eastern Standard Time (Jan 1, midnight to 2 AM) were originally modeled as the last two hours of the year in Mountain Standard Time (Dec 31, 10 PM to midnight) using the corresponding weather.</p>
</details>

<details>
    <summary>Do the timeseries aggregates have the sample weighting factors applied?</summary>
    <p>Yes, the aggregates represent the total "floor_area_represented."</p>
</details>

<details>
    <summary>Are there electric vehicle (EV) charging profiles in the dataset?</summary>
    <p>No, ComStock does not currently model EV charging in the dataset. For modeling aggregate EV load profiles for a city or state, we suggest using <a href="https://afdc.energy.gov/evi-pro-lite/load-profile">EVI-Pro Lite</a>. Measured charging profile data for individual homes can be found in the <a href="https://neea.org/data/nw-end-use-load-research-project/energy-metering-study-data">NEEA HEMS data</a> and <a href="https://www.pecanstreet.org/dataport/">Pecan Street Dataport</a>. Email us at <a href="mailto:ComStock@nrel.gov">ComStock@nrel.gov</a> if you have suggestions for other EV charging data sources.</p>
</details>

<details>
    <summary>Are weather data files available in EPW format?</summary>
    <p>Weather data used for the modeling have been provided in .csv format for regression modeling, forecasting, or other analyses. EPW format weather files for 2018 or other actual meteorological years have not been publicly released. These files can be purchased from private sector vendors. See <a href="https://energyplus.net/weather/simulation">https://energyplus.net/weather/simulation</a> for a list of providers.</p>
</details>

<details>
    <summary>How many profiles or models should be used, and how does the number used affect uncertainty of results?</summary>
    <p>The ComStock team recommends a minimum of 350 building ID samples and at least 1 building from all 14 building types when filtering or down-selecting the dataset. For more detail, see the explanation titled "<a href="{{site.baseurl}}{% link docs/resources/explanations/sample_size_considerations.md %}">Sample Size Considerations</a>".</p>
</details>