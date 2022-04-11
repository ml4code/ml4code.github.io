---
layout: publication
title: "A Novel Neural Source Code Representation based on Abstract Syntax Tree"
authors: Jian Zhang, Xu Wang, Hongyu Zhang, Hailong Sun, Kaixuan Wang, Xudong Liu
conference: ICSE
year: 2019
additional_links:
   - {name: "PDF", url: "http://xuwang.tech/paper/astnn_icse2019.pdf"}
tags: ["representation", "grammar"]
---
Exploiting machine learning techniques for analyzing programs has attracted much attention. One key problem is how to represent code fragments well for follow-up analysis. Traditional information retrieval based methods often treat programs as natural language texts, which could miss important semantic information of source code. Recently, state-of-the-art studies demonstrate that abstract syntax tree (AST) based neural models can better represent source code. However, the sizes of ASTs are usually large and the existing models are prone to the long-term dependency problem. In this paper, we propose a novel AST-based Neural Network (ASTNN) for source code representation. Unlike existing models that work on entire ASTs, ASTNN splits each large AST into a sequence of small statement trees, and encodes the statement trees to vectors by capturing the lexical and syntactical knowledge of statements. Based on the sequence of statement vectors, a bidirectional RNN model is used to leverage the naturalness of statements and finally produce the vector representation of a code fragment. We have applied our neural network based source code representation method to two common program comprehension tasks: source code classification and code clone detection. Experimental results on the two tasks indicate that our model is superior to state-of-the-art approaches.
