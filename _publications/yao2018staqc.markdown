---
layout: publication
title: "StaQC: A Systematically Mined Question-Code Dataset from Stack Overflow"
authors: Ziyu Yao, Daniel S. Weld, Wei-Peng Chen, Huan Sun
conference: WWW 2018
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1803.09371"}
   - {name: "code", url: "https://github.com/LittleYUYU/StackOverflow-Question-Code-Dataset"}
tags: ["dataset"]
---
Stack Overflow (SO) has been a great source of natural language questions and their code solutions (i.e., question-code pairs), which are critical for many tasks including code retrieval and annotation. In most existing research, question-code pairs were collected heuristically and tend to have low quality. In this paper, we investigate a new problem of systematically mining question-code pairs from Stack Overflow (in contrast to heuristically collecting them). It is formulated as predicting whether or not a code snippet is a standalone solution to a question. We propose a novel Bi-View Hierarchical Neural Network which can capture both the programming content and the textual context of a code snippet (i.e., two views) to make a prediction. On two manually annotated datasets in Python and SQL domain, our framework substantially outperforms heuristic methods with at least 15% higher F1 and accuracy. Furthermore, we present StaQC (Stack Overflow Question-Code pairs), the largest dataset to date of ∼148K Python and ∼120K SQL question-code pairs, automatically mined from SO using our framework. Under various case studies, we demonstrate that StaQC can greatly help develop data-hungry models for associating natural language with programming language.
