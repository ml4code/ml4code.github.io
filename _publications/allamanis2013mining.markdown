---
layout: publication
title: "Mining Source Code Repositories at Massive Scale Using Language Modeling "
authors: Miltiadis Allamanis, Charles Sutton
conference: MSR
year: 2013
additional_links:
   - {name: "PDF", url: "http://homepages.inf.ed.ac.uk/csutton/publications/msr2013.pdf"}
   - {name: "data", url: "http://groups.inf.ed.ac.uk/cup/javaGithub/"}
   - {name: "data@ Edinburgh DataShare", url: "http://datashare.is.ed.ac.uk/handle/10283/2334"}
tags: ["language model"]
---
The tens of thousands of high-quality open source software projects on the Internet raise the exciting possibility of studying software development by finding patterns across truly large source code repositories. This could enable new tools for developing code, encouraging reuse, and navigating large projects. In this paper, we build the first giga-token probabilistic language model of source code, based on 352 million lines of Java. This is 100 times the scale of the pioneering work by Hindle et al. The giga-token model is significantly better at the code suggestion task than previous models. More broadly, our approach provides a new “lens” for analyzing software projects, enabling new complexity metrics based on statistical analysis of large corpora. We call these metrics data-driven complexity metrics. We propose new metrics that measure the complexity of a code module and the topical centrality of a module to a software project. In particular, it is possible to distinguish reusable utility classes from classes that are part of a program’s core logic based solely on general information theoretic criteria.
