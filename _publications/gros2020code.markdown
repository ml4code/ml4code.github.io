---
layout: publication
title: "Code to Comment \"Translation\": Data, Metrics, Baselining & Evaluation"
authors: David Gros, Hariharan Sezhiyan, Premkumar Devanbu, Zhou Yu
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2010.01410"}
tags: ["bimodal", "documentation"]
---
The relationship of comments to code, and in particular, the task of generating useful comments given the code, has long been of interest. The earliest approaches have been based on strong syntactic theories of comment-structures, and relied on textual templates. More recently, researchers have applied deep learning methods to this task, and specifically, trainable generative translation models which are known to work very well for Natural Language translation (e.g., from German to English). We carefully examine the underlying assumption here: that the task of generating comments sufficiently resembles the task of translating between natural languages, and so similar models and evaluation metrics could be used. We analyze several recent code-comment datasets for this task: CodeNN, DeepCom, FunCom, and DocString. We compare them with WMT19, a standard dataset frequently used to train state of the art natural language translators. We found some interesting differences between the code-comment data and the WMT19 natural language data. Next, we describe and conduct some studies to calibrate BLEU (which is commonly used as a measure of comment quality). using "affinity pairs" of methods, from different projects, in the same project, in the same class, etc; Our study suggests that the current performance on some datasets might need to be improved substantially. We also argue that fairly naive information retrieval (IR) methods do well enough at this task to be considered a reasonable baseline. Finally, we make some suggestions on how our findings might be used in future research in this area. 
