---
layout: publication
title: "Deep Learning Type Inference"
authors: V. J. Hellendoorn, Christian Bird, Earl T. Barr, Miltiadis Allamanis
conference: FSE 
year: 2018
tags: ["representation", "types"]
---
Dynamically typed languages such as JavaScript and Python are
increasingly popular, yet static typing has not been totally eclipsed:
Python now supports type annotations and languages like TypeScript offer a middle-ground for JavaScript: a strict superset of
JavaScript, to which it transpiles, coupled with a type system that
permits partially typed programs. However, static typing has a cost:
adding annotations, reading the added syntax, and wrestling with
the type system to fix type errors. Type inference can ease the
transition to more statically typed code and unlock the benefits of
richer compile-time information, but is limited in languages like
JavaScript as it cannot soundly handle duck-typing or runtime evaluation
via eval. We propose DeepTyper, a deep learning model
that understands which types naturally occur in certain contexts
and relations and can provide type suggestions, which can often
be verified by the type checker, even if it could not infer the type
initially. DeepTyper, leverages an automatically aligned corpus
of tokens and types to accurately predict thousands of variable
and function type annotations. Furthermore, we demonstrate that
context is key in accurately assigning these types and introduce a
technique to reduce overfitting on local cues while highlighting the
need for further improvements. Finally, we show that our model
can interact with a compiler to provide more than 4,000 additional
type annotations with over 95% precision that could not be inferred
without the aid of DeepTyper.
