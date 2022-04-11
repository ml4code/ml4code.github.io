---
layout: publication
title: "JuICe: A Large Scale Distantly Supervised Dataset for Open Domain Context-based Code Generation"
authors: Rajas Agashe, Srinivasan Iyer, Luke Zettlemoyer
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.02216"}
   - {name: "Dataset", url: "https://drive.google.com/file/d/1xWDV__5hjTWVuJlXD42Ar7nkjU2hRTic/view?usp=sharing"}
tags: ["dataset", "bimodal"]
---
Interactive programming with interleaved code snippet cells and natural language markdown is recently gaining popularity in the form of Jupyter notebooks, which accelerate prototyping and collaboration. To study code generation conditioned on a long context history, we present JuICe, a corpus of 1.5 million examples with a curated test set of 3.7K instances based on online programming assignments. Compared with existing contextual code generation datasets, JuICe provides refined human-curated data, open-domain code, and an order of magnitude more training data. Using JuICe, we train models for two tasks: (1) generation of the API call sequence in a code cell, and (2) full code cell generation, both conditioned on the NL-Code history up to a particular code cell. Experiments using current baseline code generation models show that both context and distant supervision aid in generation, and that the dataset is challenging for current systems. 
