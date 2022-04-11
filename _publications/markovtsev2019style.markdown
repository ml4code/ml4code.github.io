---
layout: publication
title: "STYLE-ANALYZER: fixing code style inconsistencies with interpretable unsupervised algorithms"
authors: Vadim Markovtsev, Waren Long, Hugo Mougard, Konstantin Slavnov, Egor Bulychev
conference: MSR
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1904.00935"}
tags: ["style"]
---
Source code reviews are manual, time-consuming, and expensive. Human involvement should be focused on analyzing the most relevant aspects of the program, such as logic and maintainability, rather than amending style, syntax, or formatting defects. Some tools with linting capabilities can format code automatically and report various stylistic violations for supported programming languages. They are based on rules written by domain experts, hence, their configuration is often tedious, and it is impractical for the given set of rules to cover all possible corner cases. Some machine learning-based solutions exist, but they remain uninterpretable black boxes. This paper introduces STYLE-ANALYZER, a new open source tool to automatically fix code formatting violations using the decision tree forest model which adapts to each codebase and is fully unsupervised. STYLE-ANALYZER is built on top of our novel assisted code review framework, Lookout. It accurately mines the formatting style of each analyzed Git repository and expresses the found format patterns with compact human-readable rules. STYLE-ANALYZER can then suggest style inconsistency fixes in the form of code review comments. We evaluate the output quality and practical relevance of STYLE-ANALYZER by demonstrating that it can reproduce the original style with high precision, measured on 19 popular JavaScript projects, and by showing that it yields promising results in fixing real style mistakes. STYLE-ANALYZER includes a web application to visualize how the rules are triggered. We release STYLE-ANALYZER as a reusable and extendable open source software package on GitHub for the benefit of the community. 
