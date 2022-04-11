---
layout: publication
title: "Learning Type Annotation: Is Big Data Enough?"
authors: Kevin Jesse, Premkumar Devanbu, Toufique Ahmed
conference: FSE
year: 2021
tags: ["Transformer", "types"]
---
TypeScript is a widely used optionally-typed language where developers can adopt “pay as you go” typing: they can add types as
desired, and benefit from static typing. The “type annotation tax”
or manual effort required to annotate new or existing TypeScript
can be reduced by a variety of automatic methods. Probabilistic
machine-learning (ML) approaches work quite well. ML approaches
use different inductive biases, ranging from simple token sequences
to complex graphical neural network (GNN) models capturing syntax and semantic relations. More sophisticated inductive biases are
hand-engineered to exploit the formal nature of software. Rather
than deploying fancy inductive biases for code, can we just use “big
data” to learn natural patterns relevant to typing? We find evidence
suggesting that this is the case. We present TypeBert, demonstrating that even with simple token-sequence inductive bias used in
BERT-style models and enough data, type-annotation performance
of the most sophisticated models can be surpassed.
