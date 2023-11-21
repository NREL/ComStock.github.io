---
layout: default
title: For Developers
nav_order: 8
has_children: false
---

# Public ComStock GitHub Repository
{: .fw-500 }

[ComStock GitHub Repository](https://github.com/NREL/ComStock){: .pub-link}

This repository contains the source code used to build and execute ComStock models, including upgrade scenarios. In addition, the sampling of buildings characteristics used for the initial ComStock (V1.0) release is provided. The ComStock model is under active calibration and development, which is publicly visible on this repository.

Execution of the ComStock workflow is managed through the [buildstockbatch repository](https://github.com/NREL/buildstockbatch), a shared asset of ResStock and ComStock, specifically developed to scale to execution of tens of millions of simulations through multiple infrastructure providers.

This repository is publicly available for use, but we are not able to provide technical support or documentation for running ComStock at this time. We strongly suggest and support using the public datasets. The dataset outputs from the initial ComStock (V1.0) release can be found by visiting [Published Datasets]({{site.baseurl}}{% link docs/data/published_datasets.md %}).
