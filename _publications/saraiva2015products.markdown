---
layout: publication
title: "Products, Developers, and Milestones: How Should I Build My N-Gram Language Model"
authors: Juliana Saraiva, Christian Bird, Thomas Zimmermann
conference: FSE
year: 2015
tags: ["language model"]
---
Recent work has shown that although programming languages en-
able source code to be rich and complex, most code tends to be
repetitive and predictable. The use of natural language processing
(NLP) techniques applied to source code such as n-gram language
models show great promise in areas such as code completion, aiding impaired developers, and code search. In this paper, we address
three questions related to different methods of constructing lan-
guage models in an industrial context. Specifically, we ask: (1) Do
application specific, but smaller language models perform better
than language models across applications? (2) Are developer specific language models effective and do they differ depending on
what parts of the codebase a developer is working in? (3) Finally,
do language models change over time, i.e., does a language model
from early development model change later on in development?
The answers to these questions enable techniques that make use of
programming language models in development to choose the model
training corpus more effectively.

We evaluate these questions by building 28 language models across
developers, time periods, and applications within Microsoft Office
and present the results in this paper. We find that developer and
application specific language models perform better than models
from the entire codebase, but that temporality has little to no effect
on language model performance.
