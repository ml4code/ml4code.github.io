---
layout: publication
title: "Learning to Represent Edits"
authors: P. Yin, G. Neubig, M. Allamanis, M. Brockschmidt, A. L. Gaunt
conference: ICLR
year: 2019
bibkey: yin2019learning
additional_links:
   - {name: "data extraction", url: "https://github.com/Microsoft/msrc-dpu-learning-to-represent-edits"}
   - {name: "code edit data", url: "http://www.cs.cmu.edu/~pengchey/githubedits.zip"}
tags: ["edit"]
---
We introduce the problem of learning distributed representations of edits. By combining a
"neural editor" with an "edit encoder", our models learn to represent the salient
information of an edit and can be used to apply edits to new inputs.
We experiment on natural language and source code edit data. Our evaluation yields
promising results that suggest that our neural network models learn to capture
the structure and semantics of edits. We hope that this interesting task and
data source will inspire other researchers to work further on this problem.
