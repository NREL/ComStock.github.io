---
layout: default
title: Data
nav_order: 4
---

# Data
{: .fw-500 }

Given the complexity of the ComStock software workflow, and the big-data skill set and computing hardware required, the pathway for professionals and researchers to use ComStock successfully is to interact with the pre-created results, rather than running the ComStock modeling tool. This section provides information about accessing ComStock data, and a list of published datasets.

<details closed markdown="block" class="level1-collapse-section">
<summary class="pub-header">Accessing Data</summary>
At the most fundamental level, the ComStock dataset is a collection of end-use load profiles of approximately 350,000 building energy models. The output of each building energy model is 1 year of energy consumption in 15-minute intervals, separated into end-use categories.

Accessing national ComStock building load profiles in the full dataset requires big-data skills that make the full dataset inaccessible for most users. To support many use cases, aggregate load profiles for the following geographic resolutions are published for ComStock releases:

- 16 ASHRAE/International Energy Conservation Code climate zones
- 5 U.S. Department of Energy Building America climate zones
- 8 Electric System independent system operator and regional transmission organization regions
- 2,400+ U.S. Census Public Use Microdata Areas
- 3,000+ U.S. counties.

The following table summarizes the various ways to access and use ComStock data.
![](..\..\assets\images\data_access_summary.PNG)

The dataset has been formatted to be accessible in four main ways to meet the needs of many different users and use cases.

1. Files of individual model characteristics together with annual results, commonly referred to as the “metadata” file

2. Timeseries load profiles (individual building and pre-aggregated) in downloadable spreadsheets

3. A web-based data viewer, customizable time scales and aggregations

4. A detailed format that can be queried with big data tools

Aggregate ComStock datasets can be accessed via the [Open Energy Initiative (OpenEI) Data Lake](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2F) and the [ComStock data viewer](https://comstock.nrel.gov/). There are two versions of the datasets published with each release: one with actual weather data (AMY), and another with typical weather data (TMY3). Note: The TMY3 15-minute energy data should not be used for larger geographies because weather events are not regionally aligned.

For information on how to query the full ComStock dataset, please refer to this [documentation](https://github.com/openEDI/documentation/blob/main/NREL_Building_Stock/Query_ComStock_Athena.md).

Please note, there are separate public datasets available for residential and commercial building stocks. 

## Open Energy Initiative Data Lake
OpenEI is an energy information portal, and is developed and maintained by the National Renewable Energy Laboratory with funding and support from the U.S. Department of Energy and a network of International Partners & Sponsors. The OpenEI data lake contains comprehensive aggregate data for ComStock releases. This includes metadata and timeseries energy consumption results (baseline and upgrades, if applicable), individual building energy models, weather files, geographic information, and data dictionaries. 

The ComStock release directory structure of the data lake is summarized in the table, below. For more detailed information about the contents of the ComStock OpenEI data lake, visit the [README](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/README.md).

### Directory Structure and Contents
<table class="tg">
<thead>
  <tr>
    <th class="tg-583i"><span style="font-weight:bolder">Name</span></th>
    <th class="tg-583i"><span style="font-weight:bolder">Contents</span></th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">building_energy_models</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">Building energy models, in</span> <a href="https://www.openstudio.net/"><span style="text-decoration:underline rgb(0, 88, 133);color:#005885;background-color:transparent">OpenStudio</span></a> <span style="background-color:#FFF">format, that were run to create the dataset.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">geographic_information</span></td>
    <td class="tg-5afv"><span style="background-color:#FFF">Information on various geographies used in the dataset provided for convenience. Includes map files showing the shapes of the geographies (states, PUMAs) used for partitioning and a lookup table mapping between census tracts and various other geographies.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">metadata</span></td>
    <td class="tg-5afv"><span style="background-color:#FFF">Building characteristics (age, area, HVAC system type, etc.) for each of the building energy models run to create the timeseries data and annual energy results. Descriptions of the characteristics are included in <b>enumeration_dictionary.tsv</b>, and <b>upgrade_dictionary.tsv</b></span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">timeseries_aggregates</span></td>
    <td class="tg-5afv"><span style="background-color:#FFF">Aggregate end-use load profiles by building type and geography that can be opened and analyzed in Excel, python, or other common data analysis tools.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">timeseries_aggregates_metadata</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">Building characteristics for</span> <b>timeseries_aggregates</b> building energy models. Follows the same format as <b>metadata</b>.</td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">timeseries_individual_buildings</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">The raw individual building timeseries data.</span> <b>This is a large number of individual files!</b></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">weather</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">Key weather data used as an input to run the building energy models to create the dataset.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">citation.txt</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">Citation to use when referencing this work.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">data_dictionary.tsv</span></td>
    <td class="tg-5afv"><span style="background-color:#FFF">Describes the column names found in the metadata and timeseries data files.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">enumeration_dictionary.tsv</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">Expands the definitions of the enumerations used in the metadata files.</span></td>
  </tr>
  <tr>
    <td class="tg-uhsv"><span style="background-color:#FFF">upgrade_dictionary.tsv</span></td>
    <td class="tg-uhsv"><span style="background-color:#FFF">Expands the definitions of the upgrades.</span></td>
  </tr>
</tbody>
</table>

## ComStock Data Viewer
The ComStock data viewer exists to quickly filter, slice, combine, visualize, and download the results in custom ways. This platform is available at [comstock.nrel.gov](https://comstock.nrel.gov). Multiple geographic views of the datasets on the data viewer have been created: by state, and by Census region by PUMA.

![](..\..\assets\images\data_viewer_screenshot.PNG)

## Dataset Naming Convention
ComStock releases on OpenEI data lake and the data viewer use the following naming convention.
```
         <dataset type>_<weather data>_<year of publication>_release_<release number>
 example:   comstock   _   amy2018    _         2021        _release_       1
  result:   comstock_amy2018_2021_release_1
```
  - dataset type
    - resstock = residential buildings stock
    - comstock = commercial building stock
  - weather data
    - amy2018 = actual meteorological year 2018 (2018 weather data from NOAA ISD, NSRDB, and MesoWest)
    - tmy3 = typical weather from 1991-2005 (see [this publication](https://www.nrel.gov/docs/fy08osti/43156.pdf) for details)
  - year of publication
    - 2021 = dataset was published in 2021
    - 2022 = dataset was published in 2022
    - etc.
  - release
    - release_1 = first release of the dataset during the year of publication
    - release_2 = second release of the dataset during the year of publication
    - etc.

## Field Naming Convention

The field naming convention is fairly simple. At the highest level there is – “in.” for inputs, “out.” for outputs, “calc.” for calculated fields, then a handful of columns that provide simulation information.

For the "out." prefix there is a second level that includes – fuel type, emissions, model parameter and statistic fields, and site energy. The "in." prefix does not have a second level.

The third level of “out.” is where you’ll find the end uses.

Finally, units are denoted by a “..” with the unit following.

![](..\..\assets\images\field_naming_convention.png)
</details>


## Published Datasets
These datasets describe the timeseries energy consumption of the U.S. commercial building stock at the end-use level. For details on how it was created and validated, please see the project’s [final report](https://www.nrel.gov/buildings/end-use-load-profiles.html). Click the **Accessing Data** dropdown at the top of this page for more details about the data.

ComStock dataset releases are summarized in the following table with links for accessing the aggregate results.

|      |   **ComStock End Use Savings Shape 2023 Release 2 - 2018 Weather** |   **ComStock End Use Savings Shape 2023 Release 1 - 2018 Weather**   |   **ComStock End Use Load Profiles - 2018 Weather**   |   **ComStock End Use Load Profiles - Typical Weather**   |
|   **OEDI Name**   |   2023/comstock_amy2018_release_2   |   2023/comstock_amy2018_release_1   |   2021/comstock_amy2018_release_1   |   2021/comstock_tmy3_release_1   |
|---------|--------|--------|--------|--------|
|	**Data Viewer Links<br>Annual and Timeseries Energy**	|	[by_state]( https://comstock.nrel.gov/dataviewer/?datasetName=vizstock_comstock_amy2018_r2_2023_by_state_vu){: .table_link_text }|	[by_state](https://comstock.nrel.gov/dataviewer/?datasetName=vizstock_comstock_amy2018_r1_2023_by_state_vu){: .table_link_text } |	[by_state](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_amy2018_release_1_by_state_vu){: .table_link_text },<br>[by_puma_northeast](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_amy2018_release_1_by_puma_northeast_vu){: .table_link_text },<br>[by_puma_midwest](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_amy2018_release_1_by_puma_midwest_vu){: .table_link_text },<br>[by_puma_south](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_amy2018_release_1_by_puma_south_vu){: .table_link_text },<br>[by_puma_west](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_amy2018_release_1_by_puma_west_vu){: .table_link_text }	|	[by_state](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_tmy3_release_1_by_state_vu){: .table_link_text },<br>[by_puma_northeast](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_tmy3_release_1_by_puma_northeast_vu){: .table_link_text },<br>[by_puma_midwest](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_tmy3_release_1_by_puma_midwest_vu){: .table_link_text },<br>[by_puma_south](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_tmy3_release_1_by_puma_south_vu){: .table_link_text },<br>[by_puma_west](https://comstock.nrel.gov/dataviewer?datasetName=vizstock_comstock_tmy3_release_1_by_puma_west_vu){: .table_link_text }	|
|	**Data Table with<br>Characteristics and<br>Annual Energy Use**	|	[metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2023%2Fcomstock_amy2018_release_2%2F){: .table_link_text }	|	[metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2023%2Fcomstock_amy2018_release_1%2F){: .table_link_text }	| [metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fcomstock_amy2018_release_1%2Ftimeseries_aggregates_metadata%2F){: .table_link_text }	|	[metadata](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fcomstock_tmy3_release_1%2Ftimeseries_aggregates_metadata%2F){: .table_link_text }	|
|	**OpenEI Data Lake**	|	[suppl_data_dict](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2023%2Fcomstock_amy2018_release_2%2F){: .table_link_text }	|	[suppl_data_dict](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2023%2Fcomstock_amy2018_release_1%2F){: .table_link_text }	|	[suppl_data_dict](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fcomstock_amy2018_release_1%2F){: .table_link_text }	|	[suppl_data_dict](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fcomstock_tmy3_release_1%2F){: .table_link_text }	|
|	**Publication Date**	|   Sept-23|   March-23  |	Oct-21	|	Oct-21	|
|	**Release #**	|	2023_2  |	2023_1	|	2021_1	|	2021_1	|
|	**Building Stock<br>Represented**	|	U.S. commercial sector circa 2018	|	U.S. commercial sector circa 2018	|	U.S. commercial sector circa 2018	|	U.S. commercial sector circa 2018	|
|	**Upgrades Available**	|	1. HP RTU, Electric Backup;<br>2. HP RTU, Original Heating Fuel Backup;<br>3. VRF with DOAS;<br>4. DOAS HP Minisplits;<br>5. HP Boiler, Electric Backup;<br>6. HP Boiler, Gas Backup;<br>8. Demand Control Ventilation;<br>9. Energy Recovery;<br>10. LED Lighting;<br>11. Wall Insulation;<br>12. Roof Insulation;<br>13. Secondary Windows;<br>14. Window Film;<br>15. New Windows;<br>16. Package 1, Wall & Roof Insulation + New Windows;<br>17. Package 2, LED Lighting + HP RTU or HP Boilers;<br>18. Package 3, Package 1 + Package 2	|	1. HP-RTU<br>2. DOAS HP Minisplits<br>3. Heat Pump Boiler<br>5. LED Lighting<br>6. Exterior Wall Insulation<br>7. Roof Insulation<br>8. Secondary Windows<br>9.Window Film<br>10. New Windows	|	None	|	None	|
|	**Weather Year**	|   [amy2018](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2023%2Fcomstock_amy2018_release_2%2Fweather%2F){: .table_link_text }	|   [amy2018](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2023%2Fcomstock_amy2018_release_1%2Fweather%2F){: .table_link_text }	|	[amy2018](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fcomstock_amy2018_release_1%2Fweather%2F){: .table_link_text }	|	[tmy3](https://data.openei.org/s3_viewer?bucket=oedi-data-lake&prefix=nrel-pds-building-stock%2Fend-use-load-profiles-for-us-building-stock%2F2021%2Fcomstock_tmy3_release_1%2Fweather%2F){: .table_link_text }	|