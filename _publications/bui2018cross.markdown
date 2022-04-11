---
layout: publication
title: "Cross-Language Learning for Program Classification using Bilateral Tree-Based Convolutional Neural Networks"
authors: Nghi D. Q. Bui, Lingxiao Jiang, Yijun Yu
conference: NLSE
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1710.06159"}
tags: ["representation", "grammar"]
---
Towards the vision of translating code that implements an algorithm from one programming language into another, this
paper  proposes  an  approach  for  automated  program  classification using
bilateral tree-based convolutional neural networks
(BiTBCNNs).  It  is  layered  on  top  of  two  tree-based
convolutional neural networks (TBCNNs), each of which recognizes the algorithm of code written in an individual programming language. The combination layer of the networks
recognizes the similarities and differences among code in different programming languages. The BiTBCNNs are trained
using  the  source  code  in  different  languages  but  known  to
implement  the  same  algorithms  and/or  functionalities.  For
a  preliminary  evaluation,  we  use  3591  Java  and  3534  C++
code snippets from 6 algorithms we crawled systematically
from GitHub. We obtained over 90% accuracy in the cross-language binary classification task to tell whether any given
two code snippets implement a same algorithm. Also, for the
algorithm classification task, i.e., to predict which one of the
six algorithm labels is implemented by an arbitrary C++ code
snippet, we achieved over 80% precision.
