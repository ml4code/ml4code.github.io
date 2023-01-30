---
layout: publication
title: "CodeScore: Evaluating Code Generation by Learning Code Execution"
authors: Yihong Dong, Jiazheng Ding, Xue Jiang, Zhuo Li, Ge Li, Zhi Jin
conference:
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2301.09043"}
tags: ["Transformer", "evaluation"]
---
A proper code evaluation metric (CEM) profoundly impacts the evolution of code generation, which is an important research field in NLP and software engineering. Prevailing CEMs can be categorized into match-based CEMs (e.g., BLEU, Accuracy, and CodeBLEU) and execution-based CEMs (e.g., AvgPassRatio and Pass@k), but both of them suffer from some issues. The former only measures differences in surface form regardless of the functional equivalence of codes, while the latter has huge execution overheads, including collecting expensive test cases, resolving tedious execution dependencies, and enormous execution time. To address these issues, in this paper, we propose CodeScore, an efficient and effective CEM for code generation, which estimates test case PassRatio of generated code without executing code. We also present a framework named UniCE for training unified code evaluation models by learning code execution, i.e., learning PassRatio and Executability of generated code. In order to learn code execution comprehensively, we construct more than 100 test cases for each task in several popular benchmark datasets, covering MBPP, APPS, and HumanEval. Experimental results show that CodeScore has obtained a state-of-the-art correlation with execution-based CEMs. CodeScore is strongly correlated with AvgPassPatio, and binary CodeScore is moderately correlated with Pass@1. In particular, CodeScore eliminates the need for test cases and execution dependencies in inference, and CodeScore reduces execution time by three orders of magnitude compared to AvgPassPatio and Pass@1.
