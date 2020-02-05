---
layout: publication
title: Oreo: detection of clones in the twilight zone
authors: V. Saini, F. Farmahinifarahani, Y. Lu, P. Baldi, C. Lopes
conference: ESEC/FSE
year: 2018
bibkey: saini2018oreo
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1806.05837"}
   - {name: "website", url: "https://dl.acm.org/doi/abs/10.1145/3236024.3236026"}
   - {name: "code", url: "https://github.com/Mondego/oreo-artifact"}
tags: ["Clone detection", "Neural networks", "Software metrics"]
---
Source code clones are categorized into four types of increasingdifficulty of detection, ranging from purely textual (Type-1) topurely semantic (Type-4). Most clone detectors reported in theliterature work well up to Type-3, which accounts for syntacticdifferences. In between Type-3 and Type-4, however, there lies aspectrum of clones that, although still exhibiting some syntacticsimilarities, are extremely hard to detect – the Twilight Zone. Mostclone detectors reported in the literature fail to operate in this zone.We present Oreo, a novel approach to source code clone detectionthat not only detects Type-1 to Type-3 clones accurately, but is alsocapable of detecting harder-to-detect clones in the Twilight Zone.Oreo is built using a combination of machine learning, informationretrieval, and software metrics. We evaluate the recall of Oreo onBigCloneBench, and perform manual evaluation for precision. Oreohas both high recall and precision. More importantly, it pushes theboundary in detection of clones with moderate to weak syntacticsimilarity in a scalable manner.
