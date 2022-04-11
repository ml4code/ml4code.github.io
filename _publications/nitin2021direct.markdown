---
layout: publication
title: "DIRECT : A Transformer-based Model for Decompiled Identifier Renaming"
authors: Vikram Nitin, Anthony Saieva, Baishakhi Ray, Gail Kaiser
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.6.pdf"}
tags: ["Transformer", "decompilation"]
---
Decompiling binary executables to high-level code is an important step in reverse engineering scenarios, such as malware analysis and legacy code maintenance. However, the generated high-level code is difficult to understand since the original variable names are lost. In this paper, we leverage transformer models to reconstruct the original variable names from decompiled code. Inherent differences between code and natural language present certain challenges in applying conventional transformer-based architectures to variable name recovery. We propose DIRECT, a novel transformer-based architecture customized specifically for the task at hand. We evaluate our model on a dataset of decompiled functions and find that DIRECT outperforms the previous state-of-the-art model by up to 20%. We also present ablation studies evaluating the impact of each of our modifications. We make the source code of DIRECT available to encourage reproducible research.
