---
layout: publication
title: Learning-based Recursive Aggregation of Abstract Syntax Trees for Code Clone Detection
authors: Lutz Büch, Artur Andrzejak
conference: SANER
year: 2019
additional_links:
   - {name: "IEEEexplore", url: "https://ieeexplore.ieee.org/document/8668039"}
   - {name: "website_pdf", url: "https://pvs.ifi.uni-heidelberg.de/publications/"}
   - {name: "TR", url: "https://pvs.ifi.uni-heidelberg.de/fileadmin/papers/2019/Buech-Andrzejak-SANER2019.pdf"}
tags: ["grammar", "grammar", "clone"]
---
Code clone detection remains a crucial challenge in maintaining software projects. Many classic approaches rely on handcrafted aggregation schemes, while recent work uses supervised or unsupervised learning. In this work, we study several aspects of aggregation schemes for code clone detection based on supervised learning. To this aim, we implement an AST-based Recursive Neural Network. Firstly, our ablation study shows the influence of model choices and hyperparameters. We introduce error scaling as a way to effectively and efficiently address the class imbalance problem arising in code clone detection. Secondly, we study the influence of pretrained embeddings representing nodes in ASTs. We show that simply averaging all node vectors of a given AST yields strong baseline aggregation scheme. Further, learned AST aggregation schemes greatly benefit from pretrained node embeddings. Finally, we show the importance of carefully separating training and test data by clone clusters, to reliably measure generalization of models learned with supervision.