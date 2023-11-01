---
layout: publication
title: "Probing Semantic Grounding in Language Models of Code with Representational Similarity Analysis"
authors: Shounak Naik, Rajaswa Patil, Swati Agarwal, Veeky Baths
conference: International Conference on Advanced Data Mining and Applications (ADMA 2022)
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2207.07706"}
   - {name: "PDF", url: "https://link.springer.com/chapter/10.1007/978-3-031-22137-8_29"}
   - {name: "Code", url: "https://github.com/shounaknaik/Probing-Semantic-Grounding-in-Language-Models-of-Code-with-Representational-Similarity-Analysis"}
tags: ["interpretability", "language model", "evaluation", "Transformer"]
---
Representational Similarity Analysis is a method from cognitive neuroscience, which helps in comparing representations from two different sources of data. In this paper, we propose using Representational Similarity Analysis to probe the semantic grounding in language models of code. We probe representations from the CodeBERT model for semantic grounding by using the data from the IBM CodeNet dataset. Through our experiments, we show that current pre-training methods do not induce semantic grounding in language models of code, and instead focus on optimizing form-based patterns. We also show that even a little amount of fine-tuning on semantically relevant tasks increases the semantic grounding in CodeBERT significantly. Our ablations with the input modality to the CodeBERT model show that using bimodal inputs (code and natural language) over unimodal inputs (only code) gives better semantic grounding and sample efficiency during semantic fine-tuning. Finally, our experiments with semantic perturbations in code reveal that CodeBERT is able to robustly distinguish between semantically correct and incorrect code.
