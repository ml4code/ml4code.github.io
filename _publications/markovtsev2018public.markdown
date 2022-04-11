---
layout: publication
title: "Public Git Archive: a Big Code dataset for all"
authors: Vadim Markovtsev, Waren Long
conference: MSR
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1803.10144"}
   - {name: "GitHub", url: "https://github.com/src-d/datasets/tree/master/PublicGitArchive"}
   - {name: "data", url: "http://pga.sourced.tech/"}
tags: ["dataset"]
---
The number of open source software projects has been growing exponentially. The major online software repository host, GitHub, has accumulated tens of millions of publicly available Git version-controlled repositories. Although the research potential enabled by the available open source code is clearly substantial, no significant large-scale open source code datasets exist. In this paper, we present the Public Git Archive -- dataset of 182,014 top-bookmarked Git repositories from GitHub. We describe the novel data retrieval pipeline to reproduce it. We also elaborate on the strategy for performing dataset updates and legal issues. The Public Git Archive occupies 3.0 TB on disk and is an order of magnitude larger than the current source code datasets. The dataset is made available through HTTP and provides the source code of the projects, the related metadata, and development history. The data retrieval pipeline employs an optimized worker queue model and an optimized archive format to efficiently store forked Git repositories, reducing the amount of data to download and persist. Public Git Archive aims to open a myriad of new opportunities for Big Code research. 
