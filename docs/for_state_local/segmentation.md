---
layout: default
title: Building Segmentation Analysis
nav_order: 99
has_children: false
parent: For State and Local Government Users
---

# Building Segmentation Analysis
{: .fw-500 }

## Understanding Commercial Buildings in the U.S.
The U.S. Department of Energy has developed a series of reports that provide commercial and multifamily building characteristic and energy data for 88 local geographies, with the intention of helping policymakers at the city, county and state levels better understand commercial and multifamily building energy use. 

The reports break down the building stock for each geographic cluster by  

- building type,  
- size, 
- energy consumption, and 
- emissions.

The series has four planned topics: 

1.	Commercial Building Stock Characterization (published)
2.	Commercial Building Stock Segmentation for Retrofit Planning (published)
3.	Multifamily Building Stock Segmentation for Retrofit Planning (published)
4.	Common Retrofit Solution Data for the Retrofit Segments (in progress)

Find the reports that are relevant to your specific geography by clicking on the map below or searching by your county in [**this list**].


<div class='tableauPlaceholder' id='viz1756176448575' style='max-width: 900px; margin: auto;'>
    <noscript>
    <a href='#'><img alt=' ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bu&#47;BuildingStockSegmentationforRetrofitPlanning&#47;USMap&#47;1_rss.png' width="100%" height="700px" style='border: none' /></a>
    </noscript>
    <object class='tableauViz'  style='display:none;'><param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> <param name='embed_code_version' value='3' /> <param name='site_root' value='' /><param name='name' value='BuildingStockSegmentationforRetrofitPlanning&#47;USMap' /><param name='tabs' value='yes' /><param name='toolbar' value='yes' /><param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Bu&#47;BuildingStockSegmentationforRetrofitPlanning&#47;USMap&#47;1.png' /> <param name='animate_transition' value='yes' /><param name='display_static_image' value='yes' /><param name='display_spinner' value='yes' /><param name='display_overlay' value='yes' /><param name='display_count' value='yes' /><param name='language' value='en-US' />
    </object>
</div>
<script type='text/javascript'>                    var divElement = document.getElementById('viz1756176448575');                    var vizElement = divElement.getElementsByTagName('object')[0];                    if ( divElement.offsetWidth > 800 ) { vizElement.style.width='1466px';vizElement.style.height='700px';} else if ( divElement.offsetWidth > 500 ) { vizElement.style.width='1466px';vizElement.style.height='1050px';} else { vizElement.style.width='100%';vizElement.style.height='700px';}                     var scriptElement = document.createElement('script');                    scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);
</script>

## How Was the Segmentation for Retrofit Planning Developed?
The goal of segmentation for retrofit planning is to identify commonalities in the commercial building stock that align with retrofit strategies. Segments were created by analyzing building type, vintage, and floor area, as similar buildings often share traits like operating schedules and ownership structures. Refer to the [technical documentation](https://www.nrel.gov/docs/fy24osti/88947.pdf) for detailed segment descriptions.

## How Were the Geographic Clusters Developed?
The geographic clusters are formed on a county basis and depend on building type, age, and climate. Adjacent counties with similar commercial densities, types, and age distributions form a cluster. Clusters form regional groups if they belong to the same American Society of Heating, Refrigerating and Air-Conditioning Engineers (ASHRAE) climate zone. See the [technical reference documentation](https://www.nrel.gov/docs/fy23osti/84648.pdf) for more detail on the clustering method.

## Notes
- Topic 1 reports for California are by [California Energy Commission’s (CEC) climate zones](https://www.energy.ca.gov/programs-and-topics/programs/building-energy-efficiency-standards/climate-zone-tool-maps-and).
- Topic 2 California reports were not published due to a [known issue]({{    site.baseurl   }}{% link docs/resources/explanations/california_known_issues.md %}) in the dataset. This issue is in progress of being resolved and does not affect multifamily buildings. 
