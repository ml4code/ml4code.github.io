---
layout: publication
title: "Neural Networks for Modeling Source Code Edits"
authors: Rui Zhao, David Bieber, Kevin Swersky, Daniel Tarlow
conference: 
year: 2019
additional_links:
   - {name: "OpenReview", url: "https://openreview.net/forum?id=Sklr9i09KQ"}
   - {name: "ArXiV", url: "https://arxiv.org/abs/1904.02818"}
tags: ["edit"]
---
Programming languages are emerging as a challenging and interesting domain for machine learning. A core task, which has received significant attention in recent years, is building generative models of source code. However, to our knowledge, previous generative models have always been framed in terms of generating static snapshots of code. In this work, we instead treat source code as a dynamic object and tackle the problem of modeling the edits that software developers make to source code files. This requires extracting intent from previous edits and leveraging it to generate subsequent edits. We develop several neural networks and use synthetic data to test their ability to learn challenging edit patterns that require strong generalization. We then collect and train our models on a large-scale dataset of Google source code, consisting of millions of fine-grained edits from thousands of Python developers. From the modeling perspective, our main conclusion is that a new composition of attentional and pointer network components provides the best overall performance and scalability. From the application perspective, our results provide preliminary evidence of the feasibility of developing tools that learn to predict future edits. 
