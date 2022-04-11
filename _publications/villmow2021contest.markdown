---
layout: publication
title: "ConTest: A Unit Test Completion Benchmark featuring Context"
authors: Johannes Villmow, Jonas Depoix, Adrian Ulges
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.2.pdf"}
tags: ["benchmark", "dataset", "verification", "Transformer"]
---
We introduce CONTEST, a benchmark for NLP-based unit test completion, the task of predicting a test’s assert statements given its setup and focal method, i.e. the method to be tested. ConTest is large-scale (with 365k datapoints). Besides the test code and tested code, it also features context code called by either. We found context to be crucial for accurately predicting assertions. We also introduce baselines based on transformer encoder-decoders, and study the effects of including syntactic information and context. Overall, our models achieve a BLEU score of 38.2, while only generating unparsable code in 1.92% of cases.
