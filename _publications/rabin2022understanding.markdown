---
layout: publication
title: "Syntax-Guided Program Reduction for Understanding Neural Code Intelligence Models"
authors: Md Rafiqul Islam Rabin, Aftab Hussain, Mohammad Amin Alipour
conference: MAPS
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2205.14374"}
   - {name: "code", url: "https://github.com/mdrafiqulrabin/ci-dd-perses"}
tags: ["interpretability", "refactoring", "adversarial"]
---
Neural code intelligence (CI) models are opaque black-boxes and offer little insight on the features they use in making predictions. This opacity may lead to distrust in their prediction and hamper their wider adoption in safety-critical applications. Recently, input program reduction techniques have been proposed to identify key features in the input programs to improve the transparency of CI models. However, this approach is syntax-unaware and does not consider the grammar of the programming language. In this paper, we apply a syntax-guided program reduction technique that considers the grammar of the input programs during reduction. Our experiments on multiple models across different types of input programs show that the syntax-guided program reduction technique is faster and provides smaller sets of key tokens in reduced programs. We also show that the key tokens could be used in generating adversarial examples for up to 65% of the input programs.
