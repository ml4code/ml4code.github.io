
---
layout: publication
title: "SkipAnalyzer: A Tool for Static Code Analysis with Large Language Models"
authors: Mohammad Mahdi Mohajer, Reem Aleithan, Nima Shiri Harzevili, Moshi Wei, Alvine Boaye Belle, Hung Viet Pham, Song Wang
conference:
year: 2023
additional_links:
- {name: "ArXiV", url: "https://arxiv.org/abs/2310.18532"}
tags: ["repair"]
---
We introduce SkipAnalyzer, a large language model (LLM)-powered tool for static code analysis. SkipAnalyzer has three components: 1) an LLM-based static bug detector that scans source code and reports specific types of bugs, 2) an LLM-based false-positive filter that can identify false-positive bugs in the results of static bug detectors (e.g., the result of step 1) to improve detection accuracy, and 3) an LLM-based patch generator that can generate patches for the detected bugs above. As a proof-of-concept, SkipAnalyzer is built on ChatGPT, which has exhibited outstanding performance in various software engineering tasks. To evaluate SkipAnalyzer, we focus on two types of typical and critical bugs that are targeted by static bug detection, i.e., Null Dereference and Resource Leak as subjects. We employ Infer to aid the gathering of these two bug types from 10 open-source projects. Consequently, our experiment dataset contains 222 instances of Null Dereference bugs and 46 instances of Resource Leak bugs. Our study demonstrates that SkipAnalyzer achieves remarkable performance in the mentioned static analysis tasks, including bug detection, false-positive warning removal, and bug repair. In static bug detection, SkipAnalyzer achieves accuracy values of up to 68.37% for detecting Null Dereference bugs and 76.95% for detecting Resource Leak bugs, improving the precision of the current leading bug detector, Infer, by 12.86% and 43.13%, respectively. For removing false-positive warnings, SkipAnalyzer can reach a precision of up to 93.88% for Null Dereference bugs and 63.33% for Resource Leak bugs. Additionally, SkipAnalyzer surpasses state-of-the-art false-positive warning removal tools. Furthermore, in bug repair, SkipAnalyzer can generate syntactically correct patches to fix its detected bugs with a success rate of up to 97.30%.
