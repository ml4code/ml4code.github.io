---
layout: publication
title: "Hoppity: Learning Bug Detection and Repair"
authors: Elizabeth Dinella, Hanjun Dai, Ziyang Li, Mayur Naik, Le Song, Ke Wang
conference: ICLR
year: 2020
additional_links:
   - {name: "OpenReview", url: "https://openreview.net/forum?id=SJeqs6EFvB&noteId=SJeqs6EFvB"}
   - {name: "Demo", url: "https://hoppity.seas.upenn.edu/demo"}
tags: ["edit", "repair"]
---
We present a learning-based approach to detect and fix a broad range of bugs in Javascript programs. We frame the problem in terms of learning a sequence of graph transformations: given a buggy program modeled by a graph structure, our model makes a sequence of predictions including the position of bug nodes and corresponding graph edits to produce a fix. Unlike previous works that use deep neural networks, our approach targets bugs that are more complex and semantic in nature (i.e.~bugs that require adding or deleting statements to fix). We have realized our approach in a tool called HOPPITY. By training on 338,877 Javascript code change commits on Github, HOPPITY correctly detects and fixes bugs in 9,612 out of 42,365 programs in an end-to-end fashion. Given the bug location and type of the fix, HOPPITY also outperforms the baseline approach by a wide margin.
