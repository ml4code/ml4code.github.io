---
layout: publication
title: "Syntax and Sensibility: Using language models to detect and correct syntax errors"
authors: Eddie Antonio Santos, Joshua Charles Campbell, Dhvani Patel, Abram Hindle, José Nelson Amaral
conference: SANER
year: 2018
additional_links:
   - {name: "PDF", url: "http://softwareprocess.es/pubs/santos2018SANER-syntax.pdf"}
   - {name: "code", url: "https://github.com/naturalness/sensibility"}
tags: ["repair", "language model"]
---
Syntax errors are made by novice and experienced programmers alike; however, novice programmers lack the years of experience that help them quickly resolve these frustrating errors. Standard LR parsers are of little help, typically resolving syntax errors and their precise location poorly. We propose a methodology that locates where syntax errors occur, and suggests possible changes to the token stream that can fix the error identified. This methodology finds syntax errors by using language models trained on correct source code to find tokens that seem out of place. Fixes are synthesized by consulting the language models to determine what tokens are more likely at the estimated error location. We compare *n*-gram and LSTM (long short-term memory) language models for this task, each trained on a large corpus of Java code collected from GitHub. Unlike prior work, our methodology does not rely that the problem source code comes from the same domain as the training data. We evaluated against a repository of real student mistakes. Our tools are able to find a syntactically-valid fix within its top-2 suggestions, often producing the exact fix that the student used to resolve the error. The results show that this tool and methodology can locate and suggest corrections for syntax errors. Our methodology is of practical use to all programmers, but will be especially useful to novices frustrated with incomprehensible syntax errors.
