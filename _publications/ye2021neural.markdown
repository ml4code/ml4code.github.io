---
layout: publication
title: "Neural Program Repair with Execution-based Backpropagation"
authors: He Ye, Matias Martinez, Monperrus Martin
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.04123"}
tags: ["repair"]
---
Neural machine translation (NMT) architectures have achieved promising results for automatic program repair. Yet, they have the limitation of generating low-quality patches (e.g., not compilable patches). This is because the existing works only optimize a purely syntactic loss function based on characters and tokens without incorporating program-specific information during neural net weight optimization. In this paper, we propose a novel program repair model called RewardRepair. The core novelty of RewardRepair is to improve NMT-based program repair with a loss function based on program compilation and test execution information, rewarding the network to produce patches that compile and that do not overfit. We conduct several experiments to evaluate RewardRepair showing that it is feasible and effective to use compilation and test execution results to optimize the underlying neural repair model. In total, RewardRepair correctly repairs 43 Defects4J bugs including eight that are fixed for the first time.
