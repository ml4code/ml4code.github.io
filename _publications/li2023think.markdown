---
layout: publication
title: "Think Outside the Code: Brainstorming Boosts Large Language Models in Code Generation"
authors: Xin-Ye Li, Jiang-Tian Xue, Zheng Xie, Ming Li
conference:
year: 2023
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2305.10679"}
tags: ["generation", "Transformer"]
---
Code generation aims to automatically generate source code from high-level task specifications, which can significantly increase productivity of software engineering. Recently, approaches based on large language models (LLMs) have shown remarkable code generation abilities on simple tasks. However, generate code for more complex tasks, such as competition-level problems, remains challenging. In this paper, we introduce Brainstorm framework for code generation. It leverages a brainstorming step that generates and selects diverse thoughts on the problem to facilitate algorithmic reasoning, where the thoughts are possible blueprint of solving the problem. We demonstrate that Brainstorm significantly enhances the ability of LLMs to solve competition-level programming problems, resulting in a more than 50% increase in the pass@$k$ metrics for ChatGPT on the CodeContests benchmark, achieving state-of-the-art performance. Furthermore, our experiments conducted on LeetCode contests show that our framework boosts the ability of ChatGPT to a level comparable to that of human programmers.
