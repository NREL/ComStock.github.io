---
layout: default
title: Resources
nav_order: 3
has_children: false
has_toc: false
---

# Resources
{: .fw-500 }

This section provides tutorials, how-to guides explanations and reference material designed to aid users in answering questions about the ComStock dataset.

## Tutorials
This section provides lessons for understanding certain capabilities and functions of ComStock, as well as for learning a specific analysis skill.

- [Joining Data from an External Dataset to ComStock using Geospatial Fields]({{  site.baseurl  }}{% link docs/resources/tutorials/join_geospatial_data.md %})
- [Perform an analysis by blending ComStock and local data]({{  site.baseurl  }}{% link docs/resources/tutorials/local_segmentation_study.md %})

## How-to Guides
This section provides a collection of step-by-step guides for using the ComStock dataset to answer a given question. 

- [Filter the building characteristics dashboard for a county]({{  site.baseurl  }}{% link docs/resources/how_to_guides/characteristics_dashboard.md %})<span class="label label-blue">NEW</span>
- [Understand the annual energy use by building type for a city]({{  site.baseurl  }}{% link docs/resources/how_to_guides/puma_level_analysis.md %})
- [Access the ComStock datasets programmatically - Example scripts]({{  site.baseurl  }}{% link docs/resources/how_to_guides/example_scripts.md %})
- [Perform a basic commercial building stock segmentation analysis in Excel]({{  site.baseurl  }}{% link docs/resources/how_to_guides/basic_stock_characterization_workbook.md %})

## Explanations
These documents provide explanations focusing on the *how* and *why* of various parts of the ComStock data sets. While this section does not provide explicit advice on how to achieve a specific outcome, the documentation here will help users understand specific and important aspects the data sets. If while using ComStock there are aspects of the data sets that seem counterintuitive and / or confusing, please [email us](mailto:ComStock@nrel.gov) to recommend an additional piece of explanation documentation.

### General
- [Building Type Crosswalks]({{  site.baseurl  }}{% link docs/resources/explanations/building_type_crosswalks.md %})
- [Considerations for ComStock Calibration, Validation, and Uncertainty]({{  site.baseurl  }}{% link docs/resources/explanations/comstock_calibration.md %})
- [Geographic Fields and Codes]({{  site.baseurl  }}{% link docs/resources/explanations/reference_geographic_codes.md %})
- [New ComStock Sampling Method]({{  site.baseurl  }}{% link docs/resources/explanations/new_sampling_method.md %})<span class="label label-blue">NEW</span>
- [Sampling and Weighting in ComStock]({{  site.baseurl  }}{% link docs/resources/explanations/sampling_and_weighting.md %})
- [Using ComStock to Analyze Cost]({{  site.baseurl  }}{% link docs/resources/explanations/costing_analysis.md %})<span class="label label-green">UPDATE</span>
- [Why Individual ComStock Measure Results Should Not Be Combined]({{  site.baseurl  }}{% link docs/resources/explanations/combining_measure_results.md %})

### ComStock Limitations and Known Issues
- [Building Types Not Included in ComStock]({{  site.baseurl  }}{% link docs/resources/explanations/building_types_not_included.md %})
- [California Models Known Issues]({{    site.baseurl   }}{% link docs/resources/explanations/california_known_issues.md %})
- [Gas Consumption Underrepresented]({{  site.baseurl  }}{% link docs/resources/explanations/gas_consumption_underrepresented.md %})
- [Sample Size Considerations]({{  site.baseurl  }}{% link docs/resources/explanations/sample_size_considerations.md %})
- [Utility Bill and Emissions Known Issue]({{  site.baseurl  }}{% link docs/resources/explanations/utility_bills_emissions_known_issue.md %})<span class="label label-blue">NEW</span>



## References
These documents describe various aspects of ComStock, including the baseline and upgrade model documentation, as well as geographic clustering methodology.

<details markdown="block" class="level1-collapse-section" open>
<summary><b>ComStock Reference Documentation</b></summary>
This document serves as a guide to and resource for the methodology and assumptions behind ComStock. The Reference Documentation will be updated as major changes to the baseline models are incorporated.

| Reference Documentation Version               | Release Date | Corresponding ComStock Dataset Release(s)                            |
|-----------------------------------------------|--------------|----------------------------------------------------------------------|
| [ComStock Reference Documentation: Version 3]({{  site.baseurl  }}{% link assets/files/comstock_reference_documentation_2024_2.pdf %}) | Feb. 2025      | 2024/comstock_amy2018_release_2                                      |
| [ComStock Reference Documentation: Version 2]({{  site.baseurl  }}{% link assets/files/comstock_reference_documentation_2024_1.pdf %}) | May 2024       | 2024/comstock_amy2018_release_1                                      |
| [ComStock Reference Documentation: Version 1](https://www.nrel.gov/docs/fy23osti/83819.pdf) | March 2023     | 2023/comstock_amy2018_release_1<br>2023/comstock_amy2018_release_2   |

</details>


<details markdown="block" class="level1-collapse-section">
<summary><b>Upgrade Measures</b></summary>
The measure documentation describes the modeling methodology, assumptions, relevant ComStock baseline features, and observations from results.

[**Upgrade Measures**]({{  site.baseurl  }}{% link docs/upgrade_measures/upgrade_measures.md %})

</details>


<details markdown="block" class="level1-collapse-section">
<summary><b>Geographic Clustering Reference Documentation</b></summary>
These documents provide reference documentation for the clustering methodology developed by ComStock. The clustering algorithm described in this technical report resulted in 88 clusters across the United States. The clusters are used as the geographic basis for the “U.S. Building Stock Segmentation Series” published by DOE’s Building Technologies Office. This series will provide geographically relevant insight into building stock characteristics, energy and emissions performance, and, eventually, common end use technologies. The cluster definitions file maps counties to building stock segmentation clusters.

[**Building Stock Segmentation Cluster Development**](https://www.nrel.gov/docs/fy23osti/84648.pdf)

**June 2023**

[**Building Stock Segmentation Cluster Definitions**](https://oedi-data-lake.s3.amazonaws.com/nrel-pds-building-stock/end-use-load-profiles-for-us-building-stock/2023/comstock_amy2018_release_1/geographic_information/stock_cluster_definition_2023.11.29.csv)

**July 2023**

</details>

<details markdown="block" class="level1-collapse-section">
<summary><b>Building Stock Segmentation</b></summary>
This document discusses the development of a segmentation approach for the U.S. commercial building stock that focuses on identifying similarities. The resulting nine-segment approach primarily uses similarities in heating, ventilating, and air-conditioning systems, service water heating
systems, and the presence of cooking equipment to separate buildings into categories.

[**Commercial Building Stock Segmentation**](https://www.nrel.gov/docs/fy24osti/88947.pdf)

**May 2024**

</details>