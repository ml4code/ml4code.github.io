---
layout: publication
title: "Scalable Taint Specification Inference with Big Code"
authors: V. Chibotaru, B. Bichsel, Veselin Raychev, Martin Vechev
conference: PLDI
year: 2019
tags: ["defect", "program analysis"]
---
We present a new scalable, semi-supervised method for inferring
taint analysis specifications by learning from a large dataset of programs.
Taint specifications capture the role of library APIs (source, sink, sanitizer)
and are a critical ingredient of any taint analyzer that aims to detect
security violations based on information flow.

The core idea of our method
is to formulate the taint specification learning problem as a linear
optimization task over a large set of information flow constraints.
The resulting constraint system can then be efficiently solved with
state-of-the-art solvers. Thanks to its scalability, our method can infer
many new and interesting taint specifications by simultaneously learning from
a large dataset of programs (e.g., as found on GitHub), while requiring 
few manual annotations.

We implemented our method in an end-to-end system,
called Seldon, targeting Python, a language where static specification
inference is particularly hard due to lack of typing information.
We show that Seldon is practically effective: it learned almost 7,000 API
roles from over 210,000 candidate APIs with very little supervision
(less than 300 annotations) and with high estimated precision (67%).
Further,using the learned specifications, our taint analyzer flagged more than
20,000 violations in open source projects, 97% of which were
undetectable without the inferred specifications.