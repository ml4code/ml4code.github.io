---
layout: publication
title: "Improving Automatic Source Code Summarization via Deep Reinforcement Learning"
authors: Yao Wan, Zhou Zhao, Min Yang, Guandong Xu, Haochao Ying, Jian Wu, Philip S. Yu
conference: ASE
year: 2018
additional_links:
   - {name: "ACM", url: "https://dl.acm.org/citation.cfm?id=3238206"}
tags: ["summarization", "documentation"]
---
Code summarization provides a high level natural language description of the function performed by code, as it can benefit the software maintenance, code categorization and retrieval. To the best of our knowledge, most state-of-the-art approaches follow an encoder-decoder framework which encodes the code into a hidden space and then decode it into natural language space, suffering from two major drawbacks: a) Their encoders only consider the sequential content of code, ignoring the tree structure which is also critical for the task of code summarization; b) Their decoders are typically trained to predict the next word by maximizing the likelihood of next ground-truth word with previous ground-truth word given. However, it is expected to generate the entire sequence from scratch at test time. This discrepancy can cause an exposure bias issue, making the learnt decoder suboptimal. In this paper, we incorporate an abstract syntax tree structure as well as sequential content of code snippets into a deep reinforcement learning framework (i.e., actor-critic network). The actor network provides the confidence of predicting the next word according to current state. On the other hand, the critic network evaluates the reward value of all possible extensions of the current state and can provide global guidance for explorations. We employ an advantage reward composed of BLEU metric to train both networks. Comprehensive experiments on a real-world dataset show the effectiveness of our proposed model when compared with some state-of-the-art methods.
