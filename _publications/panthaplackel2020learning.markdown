---
layout: publication
title: "Learning to Update Natural Language Comments Based on Code Changes"
authors: Sheena Panthaplackel, Pengyu Nie, Milos Gligoric, Raymond J. Mooney, Junyi Jessy Li
conference: ACL
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.12169"}
tags: ["bimodal", "edit", "documentation"]
---
We formulate the novel task of automatically updating an existing natural language comment based on changes in the body of code it accompanies. We propose an approach that learns to correlate changes across two distinct language representations, to generate a sequence of edits that are applied to the existing comment to reflect the source code modifications. We train and evaluate our model using a dataset that we collected from commit histories of open-source software projects, with each example consisting of a concurrent update to a method and its corresponding comment. We compare our approach against multiple baselines using both automatic metrics and human evaluation. Results reflect the challenge of this task and that our model outperforms baselines with respect to making edits.
