---
layout: default
title: Utility Bills and Emissions in ComStock 2024.2
parent: Resources
nav_order: 9
---

# Utility Bills and Emissions in ComStock 2024.2

## Summary of Issue
In ComStock’s new sampling method (effective starting with 2024 Release 2), a single energy model may be used multiple times to represent similar buildings across distinct but comparable geographies (e.g., census tracts) (see a description of the new sampling method here). Utility bills and emissions due to electricity are based on the utility and grid region where the original model was sampled. When a model is reallocated to a different location, the utility and grid region of the original model may no longer reflect those of the new location, resulting in incorrect utility bill and emissions values for the reallocated models. Natural gas, fuel oil, and propane utility bills are calculated using state-level data and may also be affected by this issue.

**Note:** This issue only affects emissions associated with electricity use. Non-electric emissions are calculated using national average emission factors found in *Table 5.1.2(1) National Average Emission Factors for Household Fuels defined in ANSI/RESNET/ICCC 301 Standard for the Calculation and Labeling of the Energy Performance of Dwelling and Sleeping Units using an Energy Rating Index* and are not affected by this issue.[^1]

## Status
Impacts ComStock 2024 Release 2 only.

## Details
ComStock’s new sampling method (effective starting with 2024 Release 2) involves the reuse of a single energy model to represent similar buildings across distinct but comparable geographies (e.g., census tracts). This approach improves the dataset's granularity but the existing utility bill and emissions calculation workflow and structure of the results files lead to potential inaccuracies in utility bill and emissions calculations. These inaccuracies arise because utility rates and emissions factors are calculated based on the location of the original energy model's sampling. When a model is reallocated to a different location, the utility and grid region of the original model may no longer reflect those of the new location. Users should exercise caution when analyzing certain fields in the dataset, as they may contain incorrect or misleading values. The ComStock team is working to address this issue in future dataset releases.

For more details about how utility bills and emissions are calculated in ComStock, see the [reference documentation](https://nrel.github.io/ComStock.github.io/docs/resources/resources.html#references).

### Utility Bill Fields
The following fields related to utility bills are directly impacted by the reallocation of energy models to new locations. Since utility rates vary significantly by geography, these fields may not accurately represent the characteristics of the reallocated location:

- out.utility_bills.electricity_utility_eia_id
- out.utility_bills.electricity_bill_intensity
- out.utility_bills.electricity_bill_max
- out.utility_bills.electricity_bill_mean
- out.utility_bills.electricity_bill_median
- out.utility_bills.electricity_bill_min
- out.utility_bills.electricity_bill_number_of_rates
- out.utility_bills.electricity_energy_rate
- out.utility_bills.fuel_oil_bill
- out.utility_bills.fuel_oil_bill_intensity
- out.utility_bills.fuel_oil_rate_name
- out.utility_bills.natural_gas_bill
- out.utility_bills.natural_gas_bill_intensity
- out.utility_bills.natural_gas_energy_rate
- out.utility_bills.natural_gas_rate_name
- out.utility_bills.propane_bill
- out.utility_bills.propane_bill_intensity
- out.utility_bills.propane_rate_name

## Impacts


## Recommendations


[^1]: <https://www.resnet.us/wp-content/uploads/archive/resblog/2019/01/ANSIRESNETICC301-2019_vf1.23.19.pdf>