---
layout: publication
title: "Automatically generating features for learning program analysis heuristics"
authors: Kwonsoo Chae, Hakjoo Oh, Kihong Heo, Hongseok Yang
conference: 
year: 2016
additional_links:
- {name: "ArXiV", url: "https://arxiv.org/abs/1612.09394"}
tags: ["representation"]
---
We present a technique for automatically generating features for data-driven program analyses. Recently data-driven approaches for building a program analysis have been proposed, which mine existing codebases and automatically learn heuristics for finding a cost-effective abstraction for a given analysis task. Such approaches reduce the burden of the analysis designers, but they do not remove it completely; they still leave the highly nontrivial task of designing so called features to the hands of the designers. Our technique automates this feature design process. The idea is to use programs as features after reducing and abstracting them. Our technique goes through selected program-query pairs in codebases, and it reduces and abstracts the program in each pair to a few lines of code, while ensuring that the analysis behaves similarly for the original and the new programs with respect to the query. Each reduced program serves as a boolean feature for program-query pairs. This feature evaluates to true for a given program-query pair when (as a program) it is included in the program part of the pair. We have implemented our approach for three real-world program analyses. Our experimental evaluation shows that these analyses with automatically-generated features perform comparably to those with manually crafted features. 
