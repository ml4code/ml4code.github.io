---
layout: publication
title: "Deep Learning Code Fragments for Code Clone Detection"
authors: Martin White, Michele Tufano, Christopher Vendome, Denys Poshyvanyk.
conference: ASE
year: 2016
tags: ["clone"]
---
Code clone detection is an important problem for software
maintenance and evolution. Many approaches consider either structure or identifiers, but none of the existing detection techniques model both sources of information. These
techniques also depend on generic, handcrafted features to
represent code fragments. We introduce learning-based detection techniques where everything for representing terms
and fragments in source code is mined from the repository.
Our code analysis supports a framework, which relies on
deep learning, for automatically linking patterns mined at
the lexical level with patterns mined at the syntactic level.
We evaluated our novel learning-based approach for code
clone detection with respect to feasibility from the point
of view of software maintainers. We sampled and manually
evaluated 398 file- and 480 method-level pairs across eight
real-world Java systems; 93% of the file- and method-level
samples were evaluated to be true positives. Among the true
positives, we found pairs mapping to all four clone types. We
compared our approach to a traditional structure-oriented
technique and found that our learning-based approach detected clones that were either undetected or suboptimally
reported by the prominent tool Deckard. Our results affirm
that our learning-based approach is suitable for clone detection and a tenable technique for researchers.
