---
layout: publication
title: "Deep Learning Similarities from Different Representations of Source Code"
authors: Michele Tufano, Cody Watson, Gabriele Bavota, Massimiliano Di Penta, Martin White, Denys Poshyvanyk
conference: MSR
year: 2018
tags: ["representation", "clone"]
---
Assessing the similarity between code components plays a pivotal
role in a number of Software Engineering (SE) tasks, such as clone
detection, impact analysis, refactoring, _etc._ 
Code similarity is generally measured by relying on manually defined or hand-crafted
features,  e.g.,  by analyzing the overlap among identifiers or comparing the Abstract Syntax Trees of two code components. These
features represent a  best guess at what SE researchers can utilize to
exploit and reliably assess code similarity for a given task. Recent
work has shown, when using a stream of identifiers to represent
the code, that Deep Learning (DL) can effectively replace manual
feature engineering for the task of clone detection. However, source
code can be represented at different levels of abstraction: identifiers, Abstract Syntax Trees, Control Flow Graphs, and Bytecode.
We conjecture that each code representation can provide a different,
yet orthogonal view of the same code fragment, thus, enabling a
more reliable detection of similarities in code. In this paper, we
demonstrate how SE tasks can benefit from a DL-based approach,
which can automatically learn code similarities from different representations.
