---
layout: publication
title: "Bridging Pre-trained Models and Downstream Tasks for Source Code Understanding"
authors: Deze Wang, Zhouyang Jia, Shanshan Li, Yue Yu, Yun Xiong, Wei Dong, Xiangke Liao
conference: ICSE
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2112.02268"}
   - {name: "code", url: "https://github.com/wangdeze18/DACL"}
tags: ["representation", "language model"]
---
With the great success of pre-trained models, the pretrain-then-finetune paradigm has been widely adopted on downstream tasks for source code understanding. However, compared to costly training a large-scale model from scratch, how to effectively adapt pre-trained models to a new task has not been fully explored. In this paper, we propose an approach to bridge pre-trained models and code-related tasks. We exploit semantic-preserving transformation to enrich downstream data diversity, and help pre-trained models learn semantic features that are invariant to these semantically equivalent transformations. Further, we introduce curriculum learning to organize the transformed data in an easy-to-hard manner to fine-tune existing pre-trained models.

We apply our approach to a range of pre-trained models, and they significantly outperform the state-of-the-art models on tasks for source code understanding, such as algorithm classification, code clone detection, and code search. Our experiments even show that without heavy pre-training on code data, natural language pre-trained model RoBERTa fine-tuned with our lightweight approach could outperform or rival existing code pre-trained models fine-tuned on the above tasks, such as CodeBERT and GraphCodeBERT. This finding suggests that there is still much room for improvement in code pre-trained models.
