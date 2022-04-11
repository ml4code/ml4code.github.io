---
layout: publication
title: "Graph-based Statistical Language Model for Code"
authors: Anh Tuan Nguyen, Tien N. Nguyen
conference: ICSE
year: 2015
tags: ["representation", "language model", "autocomplete"]
---
n-gram statistical language model has been successfully applied to capture programming patterns to support code
completion and suggestion. However, the approaches using n-gram face challenges in capturing the patterns at higher levels
of abstraction due to the mismatch between the sequence nature
in n-grams and the structure nature of syntax and semantics
in source code. This paper presents GraLan, a graph-based
statistical language model and its application in code suggestion. GraLan can learn from a source code corpus and compute
the appearance probabilities of any graphs given the observed
(sub)graphs. We use GraLan to develop an API suggestion
engine and an AST-based language model, ASTLan. ASTLan
supports the suggestion of the next valid syntactic template
and the detection of common syntactic templates. Our empirical
evaluation on a large corpus of open-source projects has shown
that our engine is more accurate in API code suggestion than
the state-of-the-art approaches, and in 75% of the cases, it can
correctly suggest the API with only five candidates. ASTLan also
has high accuracy in suggesting the next syntactic template and
is able to detect many useful and common syntactic templates.
