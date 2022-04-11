---
layout: publication
title: "The Adverse Effects of Code Duplication in Machine Learning Models of Code"
authors: Miltiadis Allamanis
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1812.06469"}
   - {name: "Dataset Errata", url: "https://dpupublicdata.blob.core.windows.net/duplicates/errata.zip"}
   - {name: "Tool", url: "https://github.com/Microsoft/near-duplicate-code-detector"}
tags: ["dataset", "evaluation"]
---
The field of big code relies on mining large corpora of code to perform some learning task. A significant threat to this approach has been recently identified by Lopes et al. (2017) who found a large amount of code duplication on GitHub. However, the impact of code duplication has not been noticed by researchers devising machine learning models for source code. In this article, we study the effect of code duplication to machine learning models showing that reported metrics are sometimes inflated by up to 100% when testing on duplicated code corpora compared to the performance on de-duplicated corpora which more accurately represent how machine learning models of code are used by software engineers. We present an "errata" for widely used datasets, list best practices for collecting code corpora and evaluating machine learning models on them, and release tools to help the community avoid this problem in future research.
