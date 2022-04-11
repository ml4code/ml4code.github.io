---
layout: publication
title: "A Retrieve-and-Edit Framework for Predicting Structured Outputs"
authors: Tatsunori B. Hashimoto, Kelvin Guu, Yonatan Oren, Percy S. Liang
conference: NeurIPS
year: 2018
tags: ["bimodal", "search", "code generation"]
---
For the task of generating complex outputs such as source code, editing existing
outputs can be easier than generating complex outputs from scratch.  With this
motivation, we propose an approach that first retrieves a training example based on
the input (e.g., natural language description) and then edits it to the desired output
(e.g., code). Our contribution is a computationally efficient method for learning
a retrieval model that embeds the input in a task-dependent way without relying
on a hand-crafted metric or incurring the expense of jointly training the retriever
with the editor.  Our retrieve-and-edit framework can be applied on top of any
base model. We show that on a new autocomplete task for GitHub Python code
and the Hearthstone cards benchmark, retrieve-and-edit significantly boosts the
performance of a vanilla sequence-to-sequence model on both tasks.
