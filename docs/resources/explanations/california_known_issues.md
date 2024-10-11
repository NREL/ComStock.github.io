---
layout: default
title: California Model Known Issues
parent: Resources
nav_order: 9
---

# California Models Known Issues

## Overestimation of ventilation in California models

**In ComStock 2023 release 2 and earlier**, for models in California, the modeled outdoor air ventilation rate was significantly above that required by Title 24. Title 24 specifies minimum ventilation rates on a per-area and per-occupant basis, with the instruction to take the higher of the two. ComStock erroneously modeled this as the sum of the two, leading to unrealistically high ventilation. This is most noticeable when plotting HVAC heating or cooling EUIs vs. heating or cooling degree days; the models in CA show a trend of heating/cooling EUIs roughly twice as high as the rest of the country. **This doubling of ventilation was corrected before ComStock 2024 release 1.**

## Likely overestimation of equipment power densities in California models

**In ComStock 2024 release 2 and earlier**, the equipment power densities in models in CA are higher than those in the same building types in the rest of the country. Roughly, mercantile building types are 150-200%, food service buildings are 100-200%, and education buildings are 200-300% of the equipment power densities in the rest of the country. Warehouse equipment is much lower, around 0.33%. This is a result of using the equipment power densities from the circa 2017 DEER prototype models. While we do not have definitive evidence to show that these values are incorrect, we do observe that the HVAC end use intensities (EUIs), particularly for cooling, are higher than CBECS and higher than the rest of the country on an area-weighted cooling degree day basis. This overestimate likely overstates the relative importance of energy consumption, associated savings potential, and emissions associated with interior equipment in California. As part of a planned change, releases of ComStock starting in mid/late 2025 will use the same equipment power density assumptions as the rest of the country instead of the values from DEER.