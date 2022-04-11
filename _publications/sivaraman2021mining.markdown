---
layout: publication
title: "Mining Idioms in the Wild"
authors: Aishwarya Sivaraman, Rui Abreu, Andrew Scott, Tobi Akomolede, Satish Chandra
conference: 
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2107.06402"}
tags: ["pattern mining", "refactoring"]
---
Existing code repositories contain numerous instances of code patterns that are idiomatic ways of accomplishing a particular programming task. Sometimes, the programming language in use supports specific operators or APIs that can express the same idiomatic imperative code much more succinctly. However, those code patterns linger in repositories because the developers may be unaware of the new APIs or have not gotten around to them. Detection of idiomatic code can also point to the need for new APIs.

We share our experiences in mine idiomatic patterns from the Hack repo at Facebook. We found that existing techniques either cannot identify meaningful patterns from syntax trees or require test-suite-based dynamic analysis to incorporate semantic properties to mine useful patterns. The key insight of the approach proposed in this paper -- Jezero -- is that semantic idioms from a large codebase can be learned from canonicalized dataflow trees. We propose a scalable, lightweight static analysis-based approach to construct such a tree that is well suited to mine semantic idioms using nonparametric Bayesian methods.

Our experiments with Jezero on Hack code shows a clear advantage of adding canonicalized dataflow information to ASTs: Jezero was significantly more effective than a baseline that did not have the dataflow augmentation in being able to effectively find refactoring opportunities from unannotated legacy code. 
