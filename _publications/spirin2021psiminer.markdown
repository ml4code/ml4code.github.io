---
layout: publication
title: "PSIMiner: A Tool for Mining Rich Abstract Syntax Trees from Code"
authors: Egor Spirin, Egor Bogomolov, Vladimir Kovalenko, Timofey Bryksin
conference: MSR
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2103.12778"}
   - {name: "website", url: "https://research.jetbrains.org/groups/ml_methods/publications/"}
   - {name: "code", url: "https://github.com/JetBrains-Research/psiminer"}
tags: ["tool"]
---
The application of machine learning algorithms to source code has grown in the past years. Since these algorithms are quite sensitive to input data, it is not surprising that researchers experiment with input representations. Nowadays, a popular starting point to represent code is abstract syntax trees (ASTs). Abstract syntax trees have been used for a long time in various software engineering domains, and in particular in IDEs. The API of modern IDEs allows to manipulate and traverse ASTs, resolve references between code elements, etc. Such algorithms can enrich ASTs with new data and therefore may be useful in ML-based code analysis. In this work, we present PSIMINER— a tool for processing PSI trees from the IntelliJ Platform. PSI trees contain code syntax trees as well as functions to work with them, and therefore can be used to enrich code representation using static analysis algorithms of modern IDEs. To showcase this idea, we use our tool to infer types of identifiers in Java ASTs and extend the code2seq model for the method name prediction problem.
