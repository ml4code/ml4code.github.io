---
layout: publication
title: "Self-Supervised Bug Detection and Repair"
authors: Miltiadis Allamanis, Henry Jackson-Flux, Marc Brockschmidt
conference: NeurIPS
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.12787"}
tags: ["GNN", "Transformer", "defect", "repair"]
---
Machine learning-based program analyses have recently shown the promise of integrating formal and probabilistic reasoning towards aiding software development. However, in the absence of large annotated corpora, training these analyses is challenging. Towards addressing this, we present BugLab, an approach for self-supervised learning of bug detection and repair. BugLab co-trains two models: (1) a detector model that learns to detect and repair bugs in code, (2) a selector model that learns to create buggy code for the detector to use as training data. A Python implementation of BugLab improves by up to 30% upon baseline methods on a test dataset of 2374 real-life bugs and finds 19 previously unknown bugs in open-source software. 
