---
layout: publication
title: "PLUR: A Unifying, Graph-Based View of Program Learning, Understanding, and Repair"
authors: Zimin Chen, Vincent J Hellendoorn, Pascal Lamblin, Petros Maniatis, Pierre-Antoine Manzagol, Daniel Tarlow, Subhodeep Moitra
conference: NeurIPS
year: 2021
additional_links:
   - {name: "NeurIPS Proceedings", url: "https://proceedings.neurips.cc/paper/2021/hash/c2937f3a1b3a177d2408574da0245a19-Abstract.html"}
tags: ["repair"]
---
Machine learning for understanding and editing source code has recently attracted significant interest, with many developments in new models, new code representations, and new tasks.This proliferation can appear disparate and disconnected, making each approach seemingly unique and incompatible, thus obscuring the core machine learning challenges and contributions.In this work, we demonstrate that the landscape can be significantly simplified by taking a general approach of mapping a graph to a sequence of tokens and pointers.Our main result is to show that 16 recently published tasks of different shapes can be cast in this form, based on which a single model architecture achieves near or above state-of-the-art results on nearly all tasks, outperforming custom models like code2seq and alternative generic models like Transformers.This unification further enables multi-task learning and a series of cross-cutting experiments about the importance of different modeling choices for code understanding and repair tasks.The full framework, called PLUR, is easily extensible to more tasks, and will be open-sourced (https://github.com/google-research/plur).
