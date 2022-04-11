---
layout: publication
title: "Unsupervised Learning of API Aliasing Specifications"
authors: Jan Eberhardt, Samuel Steffen, Veselin Raychev, Martin Vechev
conference: PLDI
year: 2019
tags: ["API", "program analysis"]
---
Real world applications make heavy use of powerful libraries
and frameworks, posing a significant challenge for static analysis
as the library implementation may be very complex or unavailable.
Thus, obtaining specifications that summarize the behaviors of
the library is important as it enables static analyzers to precisely
track the effects of APIs on the client program, without requiring
the actual API implementation. 

In this work, we propose a novel method
for discovering aliasing specifications of APIs by learning from a large
dataset of programs. Unlike prior work, our method does not require
manual annotation, access to the library’s source code or ability to
run its APIs. Instead, it learns specifications in a fully unsupervised manner,
by statically observing usages of APIs in the dataset. The core idea is to
learn a probabilistic model of interactions between API methods and aliasing
objects, enabling identification of additional likely aliasing relations,
and to then infer aliasing specifications ofAPIs that explain these relations.
The learned specifications are then used to augment an API-aware points-to analysis.

We implemented our approach in a tool called USpec and used it to automatically
learn aliasing specifications from millions of source code files.
USpec learned over 2000 specifications of various Java and Python APIs, in the process
improving the results of the points-to analysis and its clients.
