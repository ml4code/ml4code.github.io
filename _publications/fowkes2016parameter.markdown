---
layout: publication
title: "Parameter-Free Probabilistic API Mining across GitHub"
authors: Jaroslav Fowkes, Charles Sutton
conference: FSE
year: 2016
tags: ["API", "pattern mining"]
---
Existing API mining algorithms can be difficult to use as they require expensive parameter tuning and the returned set of API calls can be large, highly redundant and difficult to understand. To address this, we present PAM (Probabilistic API Miner), a near parameter-free probabilistic algorithm for mining the most interesting API call patterns. We show that PAM significantly outperforms both MAPO and UPMiner, achieving 69% test-set precision, at retrieving relevant API call sequences from GitHub. Moreover, we focus on libraries for which the developers have explicitly provided code examples, yielding over 300,000 LOC of hand-written API example code from the 967 client projects in the data set. This evaluation suggests that the hand-written examples actually have limited coverage of real API usages.

