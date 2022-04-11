---
layout: publication
title: "DreamCoder: bootstrapping inductive program synthesis with wake-sleep library learning"
authors: Kevin Ellis, Catherine Wong, Maxwell Nye, Mathias Sable-Meyer, Luc Cary, Lucas Morales, Luke Hewitt, Armando Solar-Lezama, Joshua B. Tenenbaum
conference: 42nd ACM SIGPLAN International Conference on Programming Language Design and Implementation (PLDI 2021)
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2006.08381"}
   - {name: "Paper", url: "https://dl.acm.org/doi/10.1145/3453483.3454080"}
   - {name: "Code", url: "https://github.com/ellisk42/ec"}
tags: ["synthesis", "search"]
---
We present a system for inductive program synthesis called DreamCoder, which inputs a corpus of synthesis problems each specified by one or a few examples, and automatically derives a library of program components and a neural search policy that can be used to efficiently solve other similar synthesis problems. The library and search policy bootstrap each other iteratively through a variant of "wake-sleep" approximate Bayesian learning. A new refactoring algorithm based on E-graph matching identifies common sub-components across synthesized programs, building a progressively deepening library of abstractions capturing the structure of the input domain. We evaluate on eight domains including classic program synthesis areas and AI tasks such as planning, inverse graphics, and equation discovery. We show that jointly learning the library and neural search policy leads to solving more problems, and solving them more quickly.