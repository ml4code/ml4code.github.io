---
layout: publication
title: "Latent Predictor Networks for Code Generation"
authors: W. Ling, E. Grefenstette, K. M. Hermann, T. Kocisky, A. Senior, F. Wang, P. Blunsom
conference: ACL
year: 2016
bibkey: ling2016latent
tags: ["bimodal", "generation"]
---
Many  language  generation  tasks  require
the production of text conditioned on both
structured  and  unstructured  inputs.
We present  a  novel  neural  network  architecture  which  generates  an  output  sequence
conditioned on an arbitrary number of input  functions.
Crucially,  our  approach
allows  both  the  choice  of  conditioning
context and the granularity of generation,
for  example  characters  or  tokens,  to  be
marginalised, thus permitting scalable and
effective training.  Using this framework,
we address the problem of generating programming code from a mixed natural language  and  structured  specification.
We create two new data sets for this paradigm
derived  from  the  collectible  trading  card
games  Magic  the  Gathering  and  Hearthstone.   On  these,  and  a  third  preexisting
corpus,  we  demonstrate  that  marginalising multiple predictors allows our model
to outperform strong benchmarks.

