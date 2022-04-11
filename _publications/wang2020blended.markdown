---
layout: publication
title: "Blended, precise semantic program embeddings"
authors: Ke Wang, Zhendong Su
conference: PLDI
year: 2020
tags: ["dynamic"]
---
Learning neural program embeddings is key to utilizing deep neural networks in program languages research --- precise and efficient program representations enable the application of deep models to a wide range of program analysis tasks. Existing approaches predominately learn to embed programs from their source code, and, as a result, they do not capture deep, precise program semantics. On the other hand, models learned from runtime information critically depend on the quality of program executions, thus leading to trained models with highly variant quality. This paper tackles these inherent weaknesses of prior approaches by introducing a new deep neural network, Liger, which learns program representations from a mixture of symbolic and concrete execution traces. We have evaluated Liger on two tasks: method name prediction and semantics classification. Results show that Liger is significantly more accurate than the state-of-the-art static model code2seq in predicting method names, and requires on average around 10x fewer executions covering nearly 4x fewer paths than the state-of-the-art dynamic model DYPRO in both tasks. Liger offers a new, interesting design point in the space of neural program embeddings and opens up this new direction for exploration.
