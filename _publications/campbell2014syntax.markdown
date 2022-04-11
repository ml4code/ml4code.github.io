---
layout: publication
title: "Syntax Errors Just Aren’t Natural: Improving Error Reporting with Language Models"
authors: Joshua Charles Campbell, Abram Hindle, José Nelson Amaral
conference: MSR
year: 2014
tags: ["repair", "language model"]
---
A frustrating aspect of software development is that compiler error messages often fail to locate the actual cause of a syntax error. An errant semicolon or brace can result in
many errors reported throughout the file. We seek to find the actual source of these syntax errors by relying on the consistency of software: valid source code is usually repetitive and unsurprising. We exploit this consistency by constructing a simple N-gram language model of lexed source code tokens. We implemented an automatic Java syntax-error locator using the corpus of the project itself and evaluated its performance on mutated source code from several projects. Our tool, trained on the past versions of a project, can effectively augment the syntax error locations produced by the native compiler. Thus we provide a methodology and tool that exploits the naturalness of software source code to detect syntax errors alongside the parser.
