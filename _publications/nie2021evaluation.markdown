---
layout: publication
title: "Evaluation Methodologies for Code Learning Tasks"
authors: Pengyu Nie, Jiyang Zhang, Junyi Jessy Li, Raymond J. Mooney, Milos Gligoric
conference:
year: 2021
bibkey: nie2021evaluation
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2108.09619"}
tags: ["evaluation", "dataset"]
---
There has been a growing interest in developing machine learning (ML) models for code learning tasks, e.g., comment generation and method naming. Despite substantial increase in the effectiveness of ML models, the evaluation methodologies, i.e., the way people split datasets into training, validation, and testing sets, were not well designed. Specifically, no prior work on the aforementioned topics considered the timestamps of code and comments during evaluation (e.g., examples in the testing set might be from 2010 and examples from the training set might be from 2020). This may lead to evaluations that are inconsistent with the intended use cases of the ML models. In this paper, we formalize a novel time-segmented evaluation methodology, as well as the two methodologies commonly used in the literature: mixed-project and cross-project. We argue that time-segmented methodology is the most realistic. We also describe various use cases of ML models and provide a guideline for using methodologies to evaluate each use case. To assess the impact of methodologies, we collect a dataset of code-comment pairs with timestamps to train and evaluate several recent code learning ML models for the comment generation and method naming tasks. Our results show that different methodologies can lead to conflicting and inconsistent results. We invite the community to adopt the time-segmented evaluation methodology.
