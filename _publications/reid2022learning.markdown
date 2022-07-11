---
layout: publication
title: "Learning to Model Editing Processes"
authors: Machel Reid, Graham Neubig
conference: 
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2205.12374"}
tags: ["Transformer", "edit"]
---
Most existing sequence generation models produce outputs in one pass, usually left-to-right. However, this is in contrast with a more natural approach that humans use in generating content; iterative refinement and editing. Recent work has introduced edit-based models for various tasks (such as neural machine translation and text style transfer), but these generally model a single edit step. In this work, we propose modeling editing processes, modeling the whole process of iteratively generating sequences. We form a conceptual framework to describe the likelihood of multi-step edits, and describe neural models that can learn a generative model of sequences based on these multistep edits. We introduce baseline results and metrics on this task, finding that modeling editing processes improves performance on a variety of axes on both our proposed task and related downstream tasks compared to previous single-step models of edits.
