---
layout: default
title: Upgrade Measures
nav_order: 2
has_children: false
has_toc: false
---

# Upgrade Measures
{: .fw-500 }
See the table, below, for a complete list of available upgrade measures and packages in ComStock datasets, including a link to their documentation, and in which dataset release the measure was first included.

The measure documentation describes the modeling methodology, assumptions, relevant ComStock baseline features, and observations from results. The assumptions used for the measures represent one of multiple possible approaches for a technology. They are intended to be reasonable but not necessarily optimal. Assumptions can be modified as our understanding of the technologies improves. The ComStock model is continuously updated with new information, methods, and improved quality assurance/quality control procedures.

New datasets include new upgrade measures as well as updates to the ComStock baseline model. Some dataset releases and new measures are introduced with a webinar presentation. The webinars provide an overview of the ComStock process, high-level national observations for each new upgrade measure, and guidance for accessing various features of the dataset. Though not presented on the release webinar, each new dataset release includes all existing measures from the previous releases.

In ComStock datasets, the upgrades are assigned an "upgrade_id." This ID may change across dataset releases for a given upgrade. We make a **measure_name_crosswalk.csv** file available that relates the universal "Measure ID" in the table, below, and the upgrade_ids for each release. The **measure_name_crosswalk.csv** is available on the OEDI Data Lake, or you can download the latest file, [here][1].

Release webinar recordings and slides can be found at the [bottom of the page](#release-webinar-recordings-and-slides). Please note that webinars are not held for every ComStock dataset release.

**[Join our mailing list](https://www.nrel.gov/buildings/end-use-load-profiles.html#contact)** to receive notifications on upcoming releases and for invitations to the live webinar presentations.

## Measure Documentation and Details

| Measure ID | Measure Name and Documentation Link                                                                                                      | Initial Dataset Release* |
|------------|------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| env_0001   | [Exterior Wall Insulation]({{site.baseurl}}{% link docs/upgrade_measures/env_ext_wall_insulation.md%})                                   | 2023 Release 1 |
| env_0002   | [Roof Insulation]({{site.baseurl}}{% link docs/upgrade_measures/env_roof_insulation.md %})                                               | 2023 Release 1 |
| env_0003   | [Secondary Window System]({{site.baseurl}}{% link docs/upgrade_measures/env_ext_secondary_window.md %})                                  | 2023 Release 1 |
| env_0004   | [Window Film]({{site.baseurl}}{% link docs/upgrade_measures/env_window_film.md %})                                                       | 2023 Release 1 |
| env_0005   | [Window Replacement]({{site.baseurl}}{% link docs/upgrade_measures/env_ext_window_replacement.md %})                                     | 2023 Release 1 |
| hvac_0001  | [Air-Source Heat Pump Boiler](https://www.nrel.gov/docs/fy24osti/86199.pdf)                                                              | 2023 Release 1 |
| hvac_0002  | [Air-Source Heat Pump Boiler and Natural Gas Boiler Backup](https://www.nrel.gov/docs/fy24osti/87536.pdf)                                | 2023 Release 2 |
| hvac_0003  | [DOAS with Mini Split Heat Pumps]({{site.baseurl}}{% link docs/upgrade_measures/hvac_doas_mshp.md %})                                    | 2023 Release 1 |
| hvac_0004  | [Heat Pump RTU with Original Fuel Backup](https://www.nrel.gov/docs/fy24osti/87570.pdf)                                                  | 2023 Release 2 |
| hvac_0005  | [Heat Pump RTU](https://www.nrel.gov/docs/fy24osti/86585.pdf)                                                                            | 2023 Release 1 |
| hvac_0006  | [VRF Heat Recovery with DOAS](https://www.nrel.gov/docs/fy24osti/86103.pdf)                                                              | 2023 Release 2 |
| hvac_0007  | [Demand Control Ventilation](https://www.nrel.gov/docs/fy24osti/86897.pdf)                                                               | 2023 Release 2 |
| hvac_0008  | [Exhaust Air Heat/Energy Recovery](https://www.nrel.gov/docs/fy24osti/87542.pdf)                                                         | 2023 Release 2 |
| hvac_0009  | [Economizers](https://www.nrel.gov/docs/fy24osti/86105.pdf)                                                                              | 2024 Release 1 |
| hvac_0010  | [Variable Refrigerant Flow With 25% Upsizing Allowance for Heating](https://www.nrel.gov/docs/fy24osti/89040.pdf)                        | 2024 Release 1 |
| hvac_0012  | [Improved Fan Scheduling and Control of Outdoor Air During Unoccupied Periods](https://www.nrel.gov/docs/fy24osti/89120.pdf)             | 2024 Release 1 |
| hvac_0013  | [Heat Pump RTU with Exhaust Air Energy Recovery](https://www.nrel.gov/docs/fy24osti/89481.pdf)                                           | 2024 Release 1 |
| hvac_0014  | [Advanced Rooftop Unit Control](https://www.nrel.gov/docs/fy24osti/89117.pdf)                                                            | 2024 Release 1 |
| hvac_0015  | [Central Ground-Source Water-to-Water Heat Pump](https://www.nrel.gov/docs/fy24osti/89239.pdf)                                           | 2024 Release 1 |
| hvac_0016  | [Packaged Water-to-Air Geothermal Heat Pump](https://www.nrel.gov/docs/fy24osti/89131.pdf)                                               | 2024 Release 1 |
| hvac_0017  | [Ground-Coupled Console Water-to-Air Heat Pump](https://www.nrel.gov/docs/fy24osti/89132.pdf)                                            | 2024 Release 1 |
| hvac_0018  | [Heat Pump Rooftop Units With Standard Performance](https://www.nrel.gov/docs/fy25osti/89042.pdf)                                        | 2024 Release 2 |
| hvac_0019  | [Standard Performance Heat Pump Rooftop Unit with New Roof](https://www.nrel.gov/docs/fy25osti/92618.pdf)                                | 2024 Release 2 |
| hvac_0020  | Heat Pump Rooftop Units With Higher Compressor Lockout Temperature for Heating**                                            | 2024 Release 2 |
| hvac_0021  | Heat Pump Rooftop Units Compliant With the Commercial Building Heat Pump Technology Challenge Specification**                            | 2024 Release 2 |
| hvac_0022  | [Ideal Thermal Air Loads](https://www.nrel.gov/docs/fy25osti/92546.pdf)                                                                  | 2024 Release 2 |
| hvac_0023  | Reduced Thermostat Setbacks for Heat Pumps**                                                     | 2025 Release 1 |
| hvac_0024  | Chiller Replacement**                                                     | 2025 Release 1 |
| hvac_0025  | Laboratory-Informed Modeling of Standard Performance Heat Pump Rooftop Units**                                                     | 2025 Release 1 |
| hvac_0026  | Condensing Gas Boilers**                                                     | 2025 Release 1 |
| hvac_0027  | Electric Resistance Boilers**                                                     | 2025 Release 1 |
| ltg_0001   | [LED Lighting](https://www.nrel.gov/docs/fy24osti/86100.pdf)                                                                             | 2023 Release 1 |
| ppl_0001   | [Electric Cooking Equipment](https://www.nrel.gov/docs/fy24osti/89130.pdf)                                                               | 2024 Release 1 |
| gen_0001   | Photovoltaics With 40% Rooftop Coverage**                | 2025 Release 1 |
| dr_0001    | [Thermostat Control for Load Shedding](https://www.nrel.gov/docs/fy24osti/89340.pdf)                                                     | 2024 Release 1 |
| dr_0002    | [Thermostat Control for Load Shifting](https://www.nrel.gov/docs/fy24osti/89341.pdf)                                                     | 2024 Release 1 |
| dr_0003    | Lighting Control for Load Shedding**                                                     | 2024 Release 2 |
| dr_0004    | Lighting Control for Emission Reduction**                                                     | 2024 Release 2 |
| dr_0005 / dr_0006    | Thermostat and Lighting Control for Load Shedding**                                                     | 2025 Release 1 |
| dr_0007    | Low Priority Device Switching During Peak Hours**                                                     | 2025 Release 1 |
| dr_0008    | Dim Lighting During Peak Hours**                                                     | 2025 Release 1 |
| dr_0009    | Electric HVAC Temperature Setpoint Adjustment During Peak Hours**                                                     | 2025 Release 1 |
| dr_0010    | Electric HVAC Preheating by Thermostat Control**                                                     | 2025 Release 1 |
| dr_0011    | Electric HVAC Precooling by Thermostat Control**                                                     | 2025 Release 1 |
| pkg_0001   | [Wall and Roof Insulation and New Windows](https://www.nrel.gov/docs/fy24osti/86599.pdf)                                                 | 2023 Release 2 |
| pkg_0002   | [LED Lighting, HP-RTU and ASHP-Boiler](https://www.nrel.gov/docs/fy24osti/86601.pdf)                                                     | 2023 Release 2 |
| pkg_0003   | [Wall and Roof Insulation, New Windows, LED Lighting, HP-RTU and ASHP-Boiler](https://www.nrel.gov/docs/fy24osti/86602.pdf)              | 2023 Release 2 |
| pkg_0004   | [LED Lighting, Standard Performance HP-RTU and ASHP-Boiler](https://www.nrel.gov/docs/fy25osti/89126.pdf)                                | 2024 Release 2 |
| pkg_0005   | [HP-RTU + ASHP Boiler + Demand Control Ventilation + Heat/Energy Recovery + Economizers](https://www.nrel.gov/docs/fy24osti/89128.pdf)   | 2024 Release 1 |
| pkg_0006   | [Comprehensive Geothermal Heat Pump Package, Hydronic GHP, Packaged GHP, or Console GHP](https://www.nrel.gov/docs/fy24osti/89133.pdf)   | 2024 Release 1 |
| pkg_0007   | Thermostat and Lighting Control for Load Shedding**   | 2025 Release 1 |
| pkg_0008   | Thermostat and Lighting Control for Load Shedding + Photovoltaics With 40% Rooftop Coverage**   | 2025 Release 1 |
| pkg_0009   | Demand Flexibility, Lighting + Thermostat Control, Load Shed for Daily Bldg Peak Reduction**   | 2024 Release 2 |
| pkg_0010   | Geothermal Heat Pumps + High -Efficiency Envelope Package**   | 2025 Release 1 |
| pkg_0011   | Geothermal Heat Pumps + High -Efficiency Envelope + LED Lighting Package**   | 2025 Release 1 |

*Measures are included in the initial dataset release and all subsequent releases<br>**Measure documentation expected soon

## Supplemental Documentation
[Dispatch Schedule Generation for Demand Flexibility Measures](https://www.nrel.gov/docs/fy24osti/89343.pdf)

## Release Webinar Recordings and Slides
Note: Webinars are not held for every ComStock dataset release.

| Dataset Release | Webinar Recording                                        | Webinar Slides                                         |
|-----------------|----------------------------------------------------------|--------------------------------------------------------|
| 2024 Release 2  | [Recording](https://www.youtube.com/watch?v=QeeD6clu4zo) | [Slides](https://www.nrel.gov/docs/fy25osti/92766.pdf) |
| 2024 Release 1  | [Recording](https://www.youtube.com/watch?v=ffybn3Xzk0E) | [Slides](https://www.nrel.gov/docs/fy24osti/89653.pdf) |
| 2023 Release 2  | [Recording](https://www.youtube.com/watch?v=uA8bThraO_E) | [Slides](https://www.nrel.gov/docs/fy24osti/87746.pdf) |
| 2023 Release 1  | [Recording](https://www.youtube.com/watch?v=7BHQfk6kvso) | [Slides](https://www.nrel.gov/docs/fy23osti/85853.pdf) |


[1]:../../assets/files/measure_name_crosswalk_2025_1.csv
