---
layout: publication
title: "LLM4Decompile: Decompiling Binary Code with Large Language Models"
authors: Hanzhuo Tan, Qi Luo, Jing Li, Yuqun Zhang
conference:
year: 2024
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2403.05286"}
   - {name: "code", url: "https://github.com/albertan017/LLM4Decompile"}
tags: ["decompilation", "translation", "evaluation", "large language models", "LLM"]
---
Decompilation aims to restore compiled code to human-readable source code, but struggles with details like names and structure. Large language models (LLMs) show promise for programming tasks, motivating their application to decompilation. However, there does not exist any open-source LLM for decompilation. Moreover, existing decompilation evaluation systems mainly consider token-level accuracy and largely ignore code executability, which is the most important feature of any program. Therefore, we release the first open-access decompilation LLMs ranging from 1B to 33B pre-trained on 4 billion tokens of C source code and the corresponding assembly code. The open-source LLMs can serve as baselines for further development in the field. To ensure practical program evaluation, we introduce Decompile-Eval, the first dataset that considers re-compilability and re-executability for decompilation. The benchmark emphasizes the importance of evaluating the decompilation model from the perspective of program semantics. Experiments indicate that our LLM4Decompile has demonstrated the capability to accurately decompile 21% of the assembly code, which achieves a 50% improvement over GPT-4. Our code, dataset, and models are released at this [https URL](https://github.com/albertan017/LLM4Decompile)
