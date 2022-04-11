---
layout: publication
title: "Mining Idioms from Source Code"
authors: Miltiadis Allamanis, Charles Sutton
conference: FSE
year: 2014
additional_links:
   - {name: "PDF", url: "http://homepages.inf.ed.ac.uk/csutton/publications/idioms.pdf"}
   - {name: "ArXiV", url: "http://arxiv.org/abs/1404.0417"}
   - {name: "data", url: "http://groups.inf.ed.ac.uk/cup/idioms/haggisClassUsersDataset.zip"}
tags: ["pattern mining", "grammar", "grammar"]
---
We present the first method for automatically mining code idioms from a corpus of previously written, idiomatic software projects. We take the view that a code idiom is a syntactic fragment that recurs across projects and has a single semantic purpose. Idioms may have metavariables, such as the body of a for loop. Modern IDEs commonly provide facilities for manually defining idioms and inserting them on demand, but this does not help programmers to write idiomatic code in languages or using libraries with which they are unfamiliar. We present Haggis, a system for mining code idioms that builds on recent advanced techniques from statistical natural language processing, namely, nonparametric Bayesian probabilistic tree substitution grammars. We apply Haggis to several of the most popular open source projects from GitHub. We present a wide range of evidence that the resulting idioms are semantically meaningful, demonstrating that they do indeed recur across software projects and that they occur more frequently in illustrative code examples collected from a Q&A site. Manual examination of the most common idioms indicate that they describe important program concepts, including object creation, exception handling, and resource management.
