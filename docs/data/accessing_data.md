---
layout: default
title: Accessing Data
parent: Data
---

# Accessing Data
{: .fw-500 }
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

Visit the [Published Datasets]({{site.baseurl}}{% link docs/data/published_datasets.md %}) page for a summary of published ComStock datasets and links to access the data for each release.

Please note, there are separate public datasets available for residential and commercial building stocks. 

## Open Energy Initiative Data Lake
OpenEI is an energy information portal, and is developed and maintained by the National Renewable Energy Laboratory with funding and support from the U.S. Department of Energy and a network of International Partners & Sponsors. The OpenEI data lake contains comprehensive aggregate data for ComStock releases. This includes metadata and timeseries energy consumption results (baseline and upgrades, if applicable), individual building energy models, weather files, geographic information, and data dictionaries. 

The ComStock release directory structure of the data lake is summarized in the table, below. For more detailed information about the contents of the ComStock OpenEI data lake, visit the [README](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/README.md).

### Directory Structure and Contents

| **Name**                          | **Contents**|
|-----------------------------------|--------|
|building_energy_models             | Building energy models, in [OpenStudio](https://www.openstudio.net/) format, that were run to create the dataset.|
|geographic_information             | Information on various geographies used in the dataset provided for convenience. Includes map files showing the shapes of the geographies (states, PUMAs) used for partitioning and a lookup table mapping between census tracts and various other geographies. |
|metadata                           | Building characteristics (age, area, HVAC system type, etc.) for each of the building energy models run to create the timeseries data and annual energy results. Descriptions of the characteristics are included in `data_dictionary.tsv`, `enumeration_dictionary.tsv`, and `upgrade_dictionary.tsv`.|
|timeseries_aggregates              | Aggregate end-use load profiles by building type and geography that can be opened and analyzed in Excel, python, or other common data analysis tools.|
|timeseries_aggregates_metadata     | Building characteristics for `timeseries_aggregates` building energy models. Follows the same format at `metadata`.|
|timeseries_individual_buildings    | The raw individual building timeseries data.  **This is a large number of individual files!**|
|weather                            | Key weather data used as an input to run the building energy models to create the dataset.|
|citation.txt                       | Citation to use when referencing this work.|
|data_dictionary.tsv                | Describes the column names found in the metadata and timeseries data files.|
|enumeration_dictionary.tsv         | Expands the definitions of the enumerations used in the metadata files.|
|upgrade_dictionary.tsv             | Expands the definitions of the upgrades. |

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
