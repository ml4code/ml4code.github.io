---
layout: publication
title: "CodePatchLLM: Configuring code generation using a static analyzer"
authors: Danil Shaikhelislamov, Mikhail Drobyshevskiy, Andrey Belevantsev
conference: KDD2024
year: 2024
additional_links:
  - {name: "website", url: "https://genai-evaluation-kdd2024.github.io/genai-evalution-kdd2024/assets/papers/GenAI_Evaluation_KDD2024_paper_25.pdf"}
  - {name: "code", url: "https://github.com/dsshay/CodePatchLLM"}
tags: ["LLM", "static analysis", "verification"]
---
The development of large language models (LM) has significantly advanced the field of code generation. A survey of developers by Stack Overflow has found that 70% of respondents are using or plan to use AI coding tools this year. Current approaches mainly rely on supervised fine-tuning objectives borrowed from text generation, neglecting unique sequence-level characteristics of code, including but not limited to compilability as well as syntactic and functional correctness. To address this limitation, we propose a new approach to code generation that synergistically combines pre-trained LLM models with software analysis tools, which are widely used to check or vulnerabilities while validating the code. By utilizing expanded messages from code compilation and analysing, proposed approach seamlessly integrates external code-specific knowledge into the prompt chaining process. We develop CodePatchLLM, an extension for LLM that utilizes Svace feedback for code generation. It is important to note that CodePatchLLM is a model-agnostic framework that can be used across different program languages. Extensive experiments on LeetCode dataset demonstrate the effectiveness of our proposed approach compared to backbone model, CodeLlama, achieving significant improvements in compilation success rates and functional correctness across Java, Python and Kotlin languages. Our CodePatchLLM code is available online: https://github.com/dsshay/CodePatchLLM
