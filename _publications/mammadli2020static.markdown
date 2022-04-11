---
layout: publication
title: "Static Neural Compiler Optimization via Deep Reinforcement Learning"
authors: Rahim Mammadli, Ali Jannesari, Felix Wolf
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2008.08951"}
tags: ["compilation"]
---
The phase-ordering problem of modern compilers has received a lot of attention from the research community over the years, yet remains largely unsolved. Various optimization sequences exposed to the user are manually designed by compiler developers. In designing such a sequence developers have to choose the set of optimization passes, their parameters and ordering within a sequence. Resulting sequences usually fall short of achieving optimal runtime for a given source code and may sometimes even degrade the performance when compared to unoptimized version. In this paper, we employ a deep reinforcement learning approach to the phase-ordering problem. Provided with sub-sequences constituting LLVM's O3 sequence, our agent learns to outperform the O3 sequence on the set of source codes used for training and achieves competitive performance on the validation set, gaining up to 1.32x speedup on previously-unseen programs. Notably, our approach differs from autotuning methods by not depending on one or more test runs of the program for making successful optimization decisions. It has no dependence on any dynamic feature, but only on the statically-attainable intermediate representation of the source code. We believe that the models trained using our approach can be integrated into modern compilers as neural optimization agents, at first to complement, and eventually replace the hand-crafted optimization sequences.
