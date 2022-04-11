---
layout: publication
title: "Are the Code Snippets What We Are Searching for? A Benchmark and an Empirical Study on Code Search with Natural-Language Queries"
authors: Shuhan Yan, Hang Yu, Yuting Chen, Beijun Shen, Lingxiao Jiang
conference: SANER
year: 2020
additional_links:
  - { name: "IEEE", url: "https://ieeexplore.ieee.org/document/9054840" }
tags: ["search"]
---

Code search methods, especially those that allow programmers to raise queries in a natural language, plays an important role in software development. It helps to improve programmers' productivity by returning sample code snippets from the Internet and/or source-code repositories for their natural-language queries. Meanwhile, there are many code search methods in the literature that support natural-language queries. Difficulties exist in recognizing the strengths and weaknesses of each method and choosing the right one for different usage scenarios, because (1) the implementations of those methods and the datasets for evaluating them are usually not publicly available, and (2) some methods leverage different training datasets or auxiliary data sources and thus their effectiveness cannot be fairly measured and may be negatively affected in practical uses. To build a common ground for measuring code search methods, this paper builds CosBench, a dataset that consists of 1000 projects, 52 code-independent natural-language queries with ground truths, and a set of scripts for calculating four metrics on code research results. We have evaluated four IR (Information Retrieval)-based and two DL (Deep Learning)-based code search methods on CosBench. The empirical evaluation results clearly show the usefulness of the CosBench dataset and various strengths of each code search method. We found that DL-based methods are more suitable for queries on reusing code, and IR-based ones for queries on resolving bugs and learning API uses.
