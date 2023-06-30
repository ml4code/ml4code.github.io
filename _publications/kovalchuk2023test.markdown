---
layout: publication
title: Test-based and metric-based evaluation of code generation models for practical question answering
authors: S. Kovalchuk, D. Fedrushkov, V. Lomshakov, A. Aliev
conference: ICCQ
year: 2023
additional_links:
   - {name: "IEEE", url: "https://ieeexplore.ieee.org/document/10114665"}
tags: ["code generation", "test generation", "natural language generation", "evaluation", "metrics", "natural language processing"]
---
We performed a comparative analysis of code generation model performance with evaluation using common NLP metrics in comparison to a test-based evaluation. The investigation was performed in the context of question answering with code (test-to-code problem) and was aimed at applicability checking both ways for generated code evaluation in a fully automatic manner. We used CodeGen and GPTNeo pretrained models applied to a problem of question answering using Stack Overflow-based corpus (APIzation). For test-based evaluation, industrial test-generation solutions (Machinet, UTBot) were used for providing automatically generated tests. The analysis showed that the performance evaluation based solely on NLP metrics or on tests provides a rather limited assessment of generated code quality. We see the evidence that predictions with both high and low NLP metrics exist that pass and don't pass tests. With the early results of our empirical study being discussed in this paper, we believe that the combination of both approaches may increase possible ways for building, evaluating, and training code generation models.