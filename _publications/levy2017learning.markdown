---
layout: publication
title: "Learning to Align the Source Code to the Compiled Object Code"
authors: Dor Levy, Lior Wolf
conference: ICML
year: 2017
tags: ["decompilation"]
---
We propose a new neural network architecture
and use it for the task of statement-by-statement
alignment of source code and its compiled object code. Our architecture learns the alignment
between the two sequences – one being the translation of the other – by mapping each statement
to a context-dependent representation vector and
aligning such vectors using a grid of the two sequence domains. Our experiments include short
C functions, both artificial and human-written,
and show that our neural network architecture
is able to predict the alignment with high accuracy, outperforming known baselines. We also
demonstrate that our model is general and can
learn to solve graph problems such as the Traveling Salesman Problem.
