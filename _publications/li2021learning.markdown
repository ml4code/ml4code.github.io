---
layout: publication
title: "Learning to Extend Program Graphs to Work-in-Progress Code"
authors: Xuechen Li, Chris J. Maddison, Daniel Tarlow
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.14038"}
tags: ["Transformer", "autocomplete", "repair"]
---
Source code spends most of its time in a broken or incomplete state during software development. This presents a challenge to machine learning for code, since high-performing models typically rely on graph structured representations of programs derived from traditional program analyses. Such analyses may be undefined for broken or incomplete code. We extend the notion of program graphs to work-in-progress code by learning to predict edge relations between tokens, training on well-formed code before transferring to work-in-progress code. We consider the tasks of code completion and localizing and repairing variable misuse in a work-in-process scenario. We demonstrate that training relation-aware models with fine-tuned edges consistently leads to improved performance on both tasks.
