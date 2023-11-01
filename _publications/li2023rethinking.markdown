---
layout: publication
title: Rethinking Negative Pairs in Code Search
authors: Haochen Li, Xin Zhou, Luu Anh Tuan, Chunyan Miao
conference: EMNLP
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2310.08069"}
   - {name: "code", url: "https://github.com/Alex-HaochenLi/Soft-InfoNCE"}
tags: ["search", "Transformer", "retrieval", "optimization", "representation"]
---
Recently, contrastive learning has become a key component in fine-tuning code search models for software development efficiency and effectiveness. It pulls together positive code snippets while pushing negative samples away given search queries. Among contrastive learning, InfoNCE is the most widely used loss function due to its better performance. However, the following problems in negative samples of InfoNCE may deteriorate its representation learning: 1) The existence of false negative samples in large code corpora due to duplications. 2). The failure to explicitly differentiate between the potential relevance of negative samples. As an example, a bubble sorting algorithm example is less ``negative'' than a file saving function for the quick sorting algorithm query. In this paper, we tackle the above problems by proposing a simple yet effective Soft-InfoNCE loss that inserts weight terms into InfoNCE. In our proposed loss function, we apply three methods to estimate the weights of negative pairs and show that the vanilla InfoNCE loss is a special case of Soft-InfoNCE. Theoretically, we analyze the effects of Soft-InfoNCE on controlling the distribution of learnt code representations and on deducing a more precise mutual information estimation. We furthermore discuss the superiority of proposed loss functions with other design alternatives. Extensive experiments demonstrate the effectiveness of Soft-InfoNCE and weights estimation methods under state-of-the-art code search models on a large-scale public dataset consisting of six programming languages.