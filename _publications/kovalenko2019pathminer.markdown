---
layout: publication
title: "PathMiner : A Library for Mining of Path-Based Representations of Code"
authors: Vladimir Kovalenko, Egor Bogomolov, Timofey Bryksin, Alberto Bacchelli.
conference: MSR
year: 2019
additional_links:
   - {name: "Zenodo", url: "https://zenodo.org/record/2595271#.XMlqHKQo_mF"}
tags: ["representation", "grammar"]
---
One recent, significant advance in modeling source code for machine learning algorithms has been the introduction of path-based representation -- an approach consisting in representing a snippet of code as a collection of paths from its syntax tree. Such representation efficiently captures the structure of code, which, in turn, carries its semantics and other information.
Building the path-based representation involves parsing the code and extracting the paths from its syntax tree; these steps build up to a substantial technical job. With no common reusable toolkit existing for this task, the burden of mining diverts the focus of researchers from the essential work and hinders newcomers in the field of machine learning on code.


In this paper, we present PathMiner -- an open-source library for mining path-based representations of code. PathMiner is fast, flexible, well-tested, and easily extensible to support input code in any common programming language. Preprint [https://doi.org/10.5281/zenodo.2595271]; released tool [https://doi.org/10.5281/zenodo.2595257].
