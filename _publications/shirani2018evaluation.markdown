---
layout: publication
title: "Evaluation of Type Inference with Textual Cues"
authors: Amirreza A. Shirani, A. Pastor Lopez-Monroy, Fabio Gonzalez, Thamar Solorio, Mohammad Amin Alipour
conference: NLSE
year: 2018
additional_links:
   - {name: "PDF", url: "https://alipourm.github.io/pub/nl4se18.pdf"}
tags: ["information extraction"]
---
Type information plays an important role in the success of information retrieval and recommendation systems in software
engineering. Thus, the absence of types in dynamically-typed
languages poses a challenge to adapt these systems to support
dynamic languages.


In this paper, we explore the viability of type inference using
textual cues.  That is, we formulate the type inference problem as a classification problem which uses the textual features
in  the  source  code  to  predict  the type  of  variables.   In  this
approach, a classifier learns a model to distinguish between
types of variables in a program.  The model is subsequently
used to (approximately) infer the types of other variables.


We  evaluate  the  feasibility  of  this  approach  on  four  Java
projects wherein type information is already available in the
source code and can be used to train and test a classifier. Our
experiments show this approach can predict the type of new
variables  with  relatively  high  accuracy  (80% F-measure).
These results suggest that textual cues can be
complementary
tools in inferring types for dynamic languages.
