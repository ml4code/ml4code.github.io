---
layout: publication
title: "Leveraging Language to Learn Program Abstractions and Search Heuristics"
authors: Catherine Wong, Kevin Ellis, Joshua B. Tenenbaum, Jacob Andreas
conference: Thirty-eighth International Conference on Machine Learning (ICML 2021)
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2106.11053"}
   - {name: "Poster", url: "https://icml.cc/Conferences/2021/ScheduleMultitrack?event=10372"}
tags: ["synthesis", "search"]
---
Inductive program synthesis, or inferring programs from examples of desired behavior, offers a general paradigm for building interpretable, robust, and generalizable machine learning systems. Effective program synthesis depends on two key ingredients: a strong library of functions from which to build programs, and an efficient search strategy for finding programs that solve a given task. We introduce LAPS (Language for Abstraction and Program Search), a technique for using natural language annotations to guide joint learning of libraries and neurally-guided search models for synthesis. When integrated into a state-of-the-art library learning system (DreamCoder), LAPS produces higher-quality libraries and improves search efficiency and generalization on three domains -- string editing, image composition, and abstract reasoning about scenes -- even when no natural language hints are available at test time.