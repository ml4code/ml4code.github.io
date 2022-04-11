---
layout: publication
title: "Generating Accurate Assert Statements for Unit Test Cases using Pretrained Transformers"
authors: Michele Tufano, Dawn Drain, Alexey Svyatkovskiy, Shao Kun Deng, Neel Sundaresan
conference: ICSE
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2009.05634"}
tags: ["code generation", "synthesis", "test generation"]
---
Unit testing represents the foundational basis of the software testing pyramid, beneath integration and end-to-end testing. Automated software testing researchers have proposed a variety of techniques to assist developers in this time-consuming task. In this paper we present an approach to support developers in writing unit test cases by generating accurate and useful assert statements. Our approach is based on a state-of-the-art transformer model initially pretrained on an English textual corpus. This semantically rich model is then trained in a semi-supervised fashion on a large corpus of source code. Finally, we finetune this model on the task of generating assert statements for unit tests. The resulting model is able to generate accurate assert statements for a given method under test. In our empirical evaluation, the model was able to predict the exact assert statements written by developers in 62% of the cases in the first attempt. The results show 80% relative improvement for top-1 accuracy over the previous RNN-based approach in the literature. We also show the substantial impact of the pretraining process on the performances of our model, as well as comparing it with assert auto-completion task. Finally, we demonstrate how our approach can be used to augment EvoSuite test cases, with additional asserts leading to improved test coverage.
