---
layout: default
title: Getting Started
nav_order: 1
---

# Getting Started with ComStock
{: .fw-500 }

![comstock_workflow](/assets/images/city-skyline-istock-1155981768.jpg)

The commercial building sector stock model, or ComStock™, is a highly granular, bottom-up model that uses multiple data sources, statistical sampling methods, and advanced building energy simulations to estimate the annual subhourly energy consumption of the commercial building stock across the United States.

ComStock asks and answers two questions: **(1) How is energy used in the U.S. building stock?** and **(2) What are the impact of energy saving technologies?** 

For an in depth overview of ComStock please review our [annotated introductory slide deck available here.][1]

[1]:{{ site.url }}/files/comstock_introduction_with_notes.pdf

## What Does ComStock Do?

The ComStock data sets identify where energy is being consumed geographically, in what building types and end uses, and at what times of day. Simultaneously, it identifies the impact of efficiency measures: how much energy do efficiency measures save; where, or in what use cases do measures save energy; when, or at what time of day do savings occur; and which building stock segments have the biggest savings potential.

ComStock's most notable capability is being able to tailor the results to the question at hand. The results are available in multiple formats and resolutions:

|:-------------|:------------------|
| **Spatial**| U.S., census division, climate zone, state, county, and Public Use Microdata Areas geographic resolutions|
| **Temporal**| Annual aggregations to 15-minute simulation intervals|
| **Sectoral**| 14 (and counting) building types|

## How Do I Use ComStock?

ComStock provides access to results through a web data viewer. Additionally, the raw results data sets (estimated at ~10 TB) are available for download. ComStock underwent extensive validation and calibration to both timeseries whole-building and end-use data through the [End-Use Load Profiles project](https://www.nrel.gov/buildings/end-use-load-profiles.html) and was widely released in October 2021. Finally, [How-To]({{  site.baseurl  }}{% link docs/resources/how_to_guides/how_to_guides.md %}) and [Tutorial]({{  site.baseurl  }}{% link docs/resources/tutorials/tutorials.md %}) guides are posted in the Resources section of this website to assist using the data for common use cases.

ComStock leverages and is deeply indebted to DOE's open-source building energy modeling ecosystem of [OpenStudio®](https://openstudio.net/) and [EnergyPlus®](https://energyplus.net/).

