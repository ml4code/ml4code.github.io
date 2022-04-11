---
layout: publication
title: "Program Classification Using Gated Graph Attention Neural Network for Online Programming Service"
authors: Mingming Lu, Dingwu Tan, Naixue Xiong, Zailiang Chen, Haifeng Li
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1903.03804"}
tags: ["GNN", "representation"]
---
The online programing services, such as Github, TopCoder, and EduCoder, have promoted a lot of social interactions among the service users. However, the existing social interactions is rather limited and inefficient due to the rapid increasing of source-code repositories, which is difficult to explore manually. The emergence of source-code mining provides a promising way to analyze those source codes, so that those source codes can be relatively easy to understand and share among those service users. Among all the source-code mining attempts,program classification lays a foundation for various tasks related to source-code understanding, because it is impossible for a machine to understand a computer program if it cannot classify the program correctly. Although numerous machine learning models, such as the Natural Language Processing (NLP) based models and the Abstract Syntax Tree (AST) based models, have been proposed to classify computer programs based on their corresponding source codes, the existing works cannot fully characterize the source codes from the perspective of both the syntax and semantic information. To address this problem, we proposed a Graph Neural Network (GNN) based model, which integrates data flow and function call information to the AST,and applies an improved GNN model to the integrated graph, so as to achieve the state-of-art program classification accuracy. The experiment results have shown that the proposed work can classify programs with accuracy over 97%.