---
layout: publication
title: "Towards Better Program Obfuscation: Optimization via Language Models"
authors: Han Liu
conference: ICSE
year: 2016
tags: ["deobfuscation"]
---
As a common practice in software development, program
obfuscation aims at deterring reverse engineering and malicious attacks on released source or binary code. Owning ample obfuscation techniques, we have relatively little
knowledge on how to most effectively use them. The biggest
challenge lies in identifying the most useful combination of
these techniques. We propose a unified framework to automatically generate and optimize obfuscation based on an
obscurity language model and a Monte Carlo Markov Chain
(MCMC) based search algorithm. We further instantiate it
for JavaScript programs and developed the Closure tool.
Compared to the well-known Google Closure Compiler, Closure outperforms its default setting by 26%. For programs
which have already been well obfuscated, Closure can still
outperform by 22%.
