---
layout: publication
title: "Self-Supervised Contrastive Learning for Code Retrieval and Summarization via Semantic-Preserving Transformations"
authors: Nghi D. Q. Bui, Yijun Yu, Lingxiao Jiang
conference: SIGIR
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2009.02731"}
tags: ["pretraining", "search"]
---
We propose Corder, a self-supervised contrastive learning framework for source code model. Corder is designed to alleviate the need of labeled data for code retrieval and code summarization tasks. The pre-trained model of Corder can be used in two ways: (1) it can produce vector representation of code which can be applied to code retrieval tasks that do not have labeled data; (2) it can be used in a fine-tuning process for tasks that might still require label data such as code summarization. The key innovation is that we train the source code model by asking it to recognize similar and dissimilar code snippets through a contrastive learning objective. To do so, we use a set of semantic-preserving transformation operators to generate code snippets that are syntactically diverse but semantically equivalent. Through extensive experiments, we have shown that the code models pretrained by Corder substantially outperform the other baselines for code-to-code retrieval, text-to-code retrieval, and code-to-text summarization tasks.
