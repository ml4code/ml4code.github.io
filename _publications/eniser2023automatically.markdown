---
layout: publication
title: "Automatically Testing Functional Properties of Code Translation Models"
authors: Hasan Ferit Eniser, Valentin Wüstholz, Maria Christakis
conference: AAAI
year: 2023
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2309.12813"}
tags: ["translation"]
---
Large language models are becoming increasingly practical for translating code across programming languages, a process known as $transpiling$. Even though automated transpilation significantly boosts developer productivity, a key concern is whether the generated code is correct. Existing work initially used manually crafted test suites to test the translations of a small corpus of programs; these test suites were later automated. In contrast, we devise the first approach for automated, functional, property-based testing of code translation models. Our general, user-provided specifications about the transpiled code capture a range of properties, from purely syntactic to purely semantic ones. As shown by our experiments, this approach is very effective in detecting property violations in popular code translation models, and therefore, in evaluating model quality with respect to given properties. We also go a step further and explore the usage scenario where a user simply aims to obtain a correct translation of some code with respect to certain properties without necessarily being concerned about the overall quality of the model. To this purpose, we develop the first property-guided search procedure for code translation models, where a model is repeatedly queried with slightly different parameters to produce alternative and potentially more correct translations. Our results show that this search procedure helps to obtain significantly better code translations.
