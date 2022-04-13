---
layout: publication
title: "Semantic Similarity Metrics for Evaluating Source Code Summarization"
authors: Sakib Haque, Zachary Eberhart, Aakash Bansal, Collin McMillan
conference: 
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2204.01632"}
tags: ["human evaluation", "evaluation"]
---
Source code summarization involves creating brief descriptions of source code in natural language. These descriptions are a key component of software documentation such as JavaDocs. Automatic code summarization is a prized target of software engineering research, due to the high value summaries have to programmers and the simultaneously high cost of writing and maintaining documentation by hand. Current work is almost all based on machine models trained via big data input. Large datasets of examples of code and summaries of that code are used to train an e.g. encoder-decoder neural model. Then the output predictions of the model are evaluated against a set of reference summaries. The input is code not seen by the model, and the prediction is compared to a reference. The means by which a prediction is compared to a reference is essentially word overlap, calculated via a metric such as BLEU or ROUGE. The problem with using word overlap is that not all words in a sentence have the same importance, and many words have synonyms. The result is that calculated similarity may not match the perceived similarity by human readers. In this paper, we conduct an experiment to measure the degree to which various word overlap metrics correlate to human-rated similarity of predicted and reference summaries. We evaluate alternatives based on current work in semantic similarity metrics and propose recommendations for evaluation of source code summarization. 
