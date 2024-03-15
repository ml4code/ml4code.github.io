---
layout: publication
title: "Generative Type Inference for Python"
authors: Yun Peng, Chaozheng Wang, Wenxuan Wang, Cuiyun Gao, Michael R. Lyu
conference:
year: 2023
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2307.09163"}
tags: ["types"]
---
Python is a popular dynamic programming language, evidenced by its ranking as the second most commonly used language on GitHub. However, its dynamic type system can lead to potential type errors, leading researchers to explore automatic type inference approaches for Python programs. The rule-based type inference approaches can ensure the accuracy of predicted variable types, but they suffer from low coverage problems. Supervised type inference approaches, while feature-agnostic, require large, high-quality annotated datasets and are limited to pre-defined types. As zero-shot approaches, the cloze-style approaches reformulate the type inference problem into a fill-in-the-blank problem. However, their performance is limited.   This paper introduces TypeGen, a few-shot generative type inference approach that incorporates static domain knowledge from static analysis. TypeGen creates chain-of-thought (COT) prompts by translating the type inference steps of static analysis into prompts based on the type dependency graphs (TDGs), enabling language models to learn from how static analysis infers types. By combining COT prompts with code slices and type hints, TypeGen constructs example prompts from human annotations. TypeGen only requires very few annotated examples to teach language models to generate similar COT prompts via in-context learning. Moreover, TypeGen enhances the interpretability of results through the use of the input-explanation-output strategy. Experiments show that TypeGen outperforms the best baseline Type4Py by 10.0% for argument type prediction and 22.5% in return value type prediction in terms of top-1 Exact Match by using only five examples. Furthermore, TypeGen achieves substantial improvements of 27% to 84% compared to the zero-shot performance of large language models with parameter sizes ranging from 1.3B to 175B in terms of top-1 Exact Match.
