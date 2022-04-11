---
layout: publication
title: "Finding Likely Errors with Bayesian Specifications"
authors: Vijayaraghavan Murali, Swarat Chaudhuri, Chris Jermaine
conference:
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1703.01370"}
year: 2017
tags: ["program analysis", "API"]
---
We present a Bayesian framework for learning probabilistic specifications from large, unstructured code corpora, and
a method to use this framework to statically detect anomalous, hence likely buggy, program behavior. The distinctive
insight here is to build a statistical model that correlates all
specifications hidden inside a corpus with the syntax and
observed behavior of programs that implement these specifications. During the analysis of a particular program, this
model is conditioned into a posterior distribution that prioritizes specifications that are relevant to this program. This
allows accurate program analysis even if the corpus is highly
heterogeneous. The problem of finding anomalies is now
framed quantitatively, as a problem of computing a distance
between a “reference distribution” over program behaviors
that our model expects from the program, and the distribution over behaviors that the program actually produces.

We present a concrete embodiment of our framework that
combines a topic model and a neural network model to learn
specifications, and queries the learned models to compute
anomaly scores. We evaluate this implementation on the
task of detecting anomalous usage of Android APIs. Our
encouraging experimental results show that the method can
automatically discover subtle errors in Android applications
in the wild, and has high precision and recall compared to
competing probabilistic approaches.
