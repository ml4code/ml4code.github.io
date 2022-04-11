---
layout: publication
title: "SampleFix: Learning to Correct Programs by Sampling Diverse Fixes"
authors: Hossein Hajipour, Apratim Bhattacharyya, Cristian-Alexandru Staicu, Mario Fritz
conference: 
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1906.10502"}
tags: ["repair", "code generation"]
---
Automatic program correction is an active topic of research, which holds the potential of dramatically improving productivity of programmers during the software development process and correctness of software in general. Recent advances in machine learning, deep learning and NLP have rekindled the hope to eventually fully automate the process of repairing programs. A key challenges is ambiguity, as multiple codes -- or fixes -- can implement the same functionality. In addition, dataset by nature fail to capture the variance introduced by such ambiguities. Therefore, we propose a deep generative model to automatically correct programming errors by learning a distribution of potential fixes. Our model is formulated as a deep conditional variational autoencoder that samples diverse fixes for the given erroneous programs. In order to account for ambiguity and inherent lack of representative datasets, we propose a novel regularizer to encourage the model to generate diverse fixes. Our evaluations on common programming errors show for the first time the generation of diverse fixes and strong improvements over the state-of-the-art approaches by fixing up to 61% of the mistakes. 
