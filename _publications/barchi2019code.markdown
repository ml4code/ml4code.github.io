---
layout: publication
title: "Code Mapping in Heterogeneous Platforms Using Deep Learning and LLVM-IR"
authors: Francesco Barchi, Gianvito Urgese, Enrico Macii, Andrea Acquaviva
conference: DAC
year: 2019
additional_links:
   - {name: "ACM", url: "https://dl.acm.org/doi/10.1145/3316781.3317789"}
   - {name: "code", url: "https://gitlab.com/ecs-lab/deepllvm"}
tags: ["optimization", "program analysis", "static analysis", "natural language processing"]
---
Modern heterogeneous platforms require compilers capable of choosing the appropriate device for the execution of program portions. This paper presents a machine learning method designed for supporting mapping decisions through the analysis of the program source code represented in LLVM assembly language (IR) for exploiting the advantages offered by this generalised and optimised representation. To evaluate our solution, we trained an LSTM neural network on OpenCL kernels compiled in LLVM-IR and processed with our tokenizer capable of filtering less-informative tokens. We tested the network that reaches an accuracy of 85% in distinguishing the best computational unit.
