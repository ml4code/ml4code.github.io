---
layout: publication
title: A large-scale benchmark for few-shot program induction and synthesis
authors: Ferran Alet, Javier Lopez-Contreras,  James Koppel,  Maxwell Nye,   Armando Solar-Lezama,  Tomas Lozano-Perez,  Leslie Kaelbling, Joshua Tenenbaum
conference: ICML
year: 2021
additional_links:
   - {name: "PMLR", url: "http://proceedings.mlr.press/v139/alet21a.html"}
   - {name: "website", url: "https://lis.csail.mit.edu/progres"}
tags: ["dataset", "synthesis"]
---
A landmark challenge for AI is to learn flexible, powerful representations from small numbers of examples. 
On an important class of tasks, hypotheses in the form of programs provide extreme generalization capabilities from surprisingly few examples. However, whereas large natural few-shot learning image benchmarks have spurred progress in meta-learning for deep networks, there is no comparably big, natural program-synthesis dataset that can play a similar role. This is because, whereas images are relatively easy to label from internet meta-data or annotated by non-experts, generating meaningful input-output examples for program induction has proven hard to scale. In this work, we propose a new way of leveraging unit tests and natural inputs for small programs as meaningful input-output examples for each sub-program of the overall program. This allows us to create a large-scale naturalistic few-shot program-induction benchmark and propose new challenges in this domain. The evaluation of multiple program induction and synthesis algorithms points to shortcomings of current methods and suggests multiple avenues for future work.
