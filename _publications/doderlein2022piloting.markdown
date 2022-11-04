---
layout: publication
title: "Piloting Copilot and Codex: Hot Temperature, Cold Prompts, or Black Magic?"
authors: Jean-Baptiste Döderlein, Mathieu Acher, Djamel Eddine Khelladi, Benoit Combemale
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2210.14699"}
tags: ["Transformer"]
---
Language models are promising solutions for tackling increasing complex problems. In software engineering, they recently attracted attention in code assistants, with programs automatically written in a given programming language from a programming task description in natural language. They have the potential to save time and effort when writing code. However, these systems are currently poorly understood, preventing them from being used optimally. In this paper, we investigate the various input parameters of two language models, and conduct a study to understand if variations of these input parameters (e.g. programming task description and the surrounding context, creativity of the language model, number of generated solutions) can have a significant impact on the quality of the generated programs. We design specific operators for varying input parameters and apply them over two code assistants (Copilot and Codex) and two benchmarks representing algorithmic problems (HumanEval and LeetCode). Our results showed that varying the input parameters can significantly improve the performance of language models. However, there is a tight dependency when varying the temperature, the prompt and the number of generated solutions, making potentially hard for developers to properly control the parameters to obtain an optimal result. This work opens opportunities to propose (automated) strategies for improving performance.
