---
layout: publication
title: "Can we learn from developer mistakes? Learning to localize and repair real bugs from real bug fixes"
authors: Cedric Richter, Heike Wehrheim
conference: 
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2207.00301"}
   - {name: "Code", url: "https://github.com/cedricrupb/nbfbaselines"}
tags: ["Transformer", "repair", "defect"]
---
Real bug fixes found in open source repositories seem to be the perfect source for learning to localize and repair real bugs. However, the absence of large scale bug fix collections has made it difficult to effectively exploit real bug fixes in the training of larger neural models in the past. In contrast, artificial bugs -- produced by mutating existing source code -- can be easily obtained at a sufficient scale and are therefore often preferred in the training of existing approaches. Still, localization and repair models that are trained on artificial bugs usually underperform when faced with real bugs. This raises the question whether bug localization and repair models trained on real bug fixes are more effective in localizing and repairing real bugs.

We address this question by introducing RealiT, a pre-train-and-fine-tune approach for effectively learning to localize and repair real bugs from real bug fixes. RealiT is first pre-trained on a large number of artificial bugs produced by traditional mutation operators and then fine-tuned on a smaller set of real bug fixes. Fine-tuning does not require any modifications of the learning algorithm and hence can be easily adopted in various training scenarios for bug localization or repair (even when real training data is scarce). In addition, we found that training on real bug fixes with RealiT is empirically powerful by nearly doubling the localization performance of an existing model on real bugs while maintaining or even improving the repair performance.
