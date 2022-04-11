---
layout: publication
title: "Predicting Program Properties from “Big Code”"
authors: Veselin Raychev, Martin Vechev, Andreas Krause
conference: POPL
year: 2015
tags: ["program analysis", "naming", "types", "deobfuscation"]
---
We present a new approach for predicting program properties from
massive codebases (aka “Big Code”). Our approach first learns a
probabilistic model from existing data and then uses this model to
predict properties of new, unseen programs.

The key idea of our work is to transform the input program into
a representation which allows us to phrase the problem of inferring program properties as structured prediction in machine learning. This formulation enables us to leverage powerful probabilistic
graphical models such as conditional random fields (CRFs) in order
to perform joint prediction of program properties.

As an example of our approach, we built a scalable prediction
engine called JSNICE 1 for solving two kinds of problems in the
context of JavaScript: predicting (syntactic) names of identifiers
and predicting (semantic) type annotations of variables. Experimentally, JSNICE predicts correct names for 63% of name identifiers and its type annotation predictions are correct in 81% of the
cases. In the first week since its release, JSN ICE was used by more
than 30,000 developers and in only few months has become a popular tool in the JavaScript developer community.

By formulating the problem of inferring program properties as
structured prediction and showing how to perform both learning
and inference in this context, our work opens up new possibilities
for attacking a wide range of difficult problems in the context of
“Big Code” including invariant generation, de-compilation, synthesis and others.
