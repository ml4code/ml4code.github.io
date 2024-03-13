---
layout: publication
title: "Making the Most of Scarce Input Data in Deep Learning-Based Source Code Classification for Heterogeneous Device Mapping"
authors: Emanuele Parisi, Francesco Barchi, Andrea Bartolini, Andrea Acquaviva
journal: IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems
year: 2022
additional_links:
   - {name: "IEEE", url: "https://ieeexplore.ieee.org/document/9544064"}
   - {name: "code", url: "https://gitlab.com/ecs-lab/deepllvm"}
tags: ["optimization", "program analysis", "static analysis", "language model"]
---
Despite its relatively recent history, deep learning (DL)-based source code analysis is already a cornerstone in machine learning for compiler optimization. When applied to the classification of pieces of code to identify the best computational unit in a heterogeneous Systems-on-Chip, it can be effective in supporting decisions that a programmer has otherwise to take manually. Several techniques have been proposed exploiting different networks and input information, prominently sequence-based and graph-based representations, complemented by auxiliary information typically related to payload and device configuration. While the accuracy of DL methods strongly depends on the training and test datasets, so far no exhaustive and statistically meaningful analysis has been done on its impact on the results and on how to effectively extract the available information. This is relevant also considering the scarce availability of source code datasets that can be labeled by profiling on heterogeneous compute units. In this article, we first present such a study, which leads us to devise the contribution of code sequences and auxiliary inputs separately. Starting from this analysis, we then demonstrate that by using the normalization of auxiliary information, it is possible to improve state-of-the-art results in terms of accuracy. Finally, we propose a novel approach exploiting Siamese networks that further improve mapping accuracy by increasing the cardinality of the dataset, thus compensating for its relatively small size.