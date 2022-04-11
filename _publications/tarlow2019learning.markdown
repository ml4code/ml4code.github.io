---
layout: publication
title: "Learning to Fix Build Errors with Graph2Diff Neural Networks"
authors: Daniel Tarlow, Subhodeep Moitra, Andrew Rice, Zimin Chen, Pierre-Antoine Manzagol, Charles Sutton, Edward Aftandilian
conference: 
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1911.01205"}
   - {name: "preprint", url: "http://www.cs.toronto.edu/~dtarlow/papers/graph2diff_preprint.pdf"}
tags: ["edit", "repair"]
---
Professional software developers spend a significant amount oftime fixing builds, but this has received little attention as a prob-lem in automatic program repair. We present a new deep learningarchitecture, called Graph2Diff, for automatically localizing andfixing build errors. We represent source code, build configurationfiles, and compiler diagnostic messages as a graph, and then use aGraph Neural Network model to predict a diff. A diff specifies howto modify the code’s abstract syntax tree, represented in the neuralnetwork as a sequence of tokens and of pointers to code locations.Our network is an instance of a more general abstraction which wecall Graph2Tocopo, which is potentially useful in any developmenttool for predicting source code changes. We evaluate the model ona dataset of over 500k real build errors and their resolutions fromprofessional developers. Compared to the approach of DeepDelta, our approach tackles the harder task of predicting a moreprecise diff but still achieves over double the accuracy.
