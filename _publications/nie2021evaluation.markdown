---
layout: publication
title: "Impact of Evaluation Methodologies on Code Summarization"
authors: Pengyu Nie, Jiyang Zhang, Junyi Jessy Li, Raymond J. Mooney, Milos Gligoric
conference: ACL
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2108.09619"}
tags: ["evaluation", "dataset"]
---
There has been a growing interest in developing machine learning (ML) models for code summarization tasks, e.g., comment generation and method naming. Despite substantial increase in the effectiveness of ML models, the evaluation methodologies, i.e., the way people split datasets into training, validation, and test sets, were not well studied. Specifically, no prior work on code summarization considered the timestamps of code and comments during evaluation. This may lead to evaluations that are inconsistent with the intended use cases. In this paper, we introduce the time-segmented evaluation methodology, which is novel to the code summarization research community, and compare it with the mixed-project and cross-project methodologies that have been commonly used. Each methodology can be mapped to some use cases, and the time-segmented methodology should be adopted in the evaluation of ML models for code summarization. To assess the impact of methodologies, we collect a dataset of (code, comment) pairs with timestamps to train and evaluate several recent ML models for code summarization. Our experiments show that different methodologies lead to conflicting evaluation results. We invite the community to expand the set of methodologies used in evaluations. 
