---
layout: publication
title: "Learning Code-Query Interaction for Enhancing Code Searches"
authors: Wei Li, Haozhe Qin, Shuhan Yan, Beijun Shen, Yuting Chen
conference: ICSME
year: 2020
additional_links:
  - { name: "IEEE", url: "https://ieeexplore.ieee.org/document/9240627" }
tags: ["search"]
---

Code search plays an important role in software development and maintenance. In recent years, deep learning (DL) has achieved a great success in this domain-several DL-based code search methods, such as DeepCS and UNIF, have been proposed for exploring deep, semantic correlations between code and queries; each method usually embeds source code and natural language queries into real vectors followed by computing their vector distances representing their semantic correlations. Meanwhile, deep learning-based code search still suffers from three main problems, i.e., the OOV (Out of Vocabulary) problem, the independent similarity matching problem, and the small training dataset problem. To tackle the above problems, we propose CQIL, a novel, deep learning-based code search method. CQIL learns code-query interactions and uses a CNN (Convolutional Neural Network) to compute semantic correlations between queries and code snippets. In particular, CQIL employs a hybrid representation to model code-query correlations, which solves the OOV problem. CQIL also deeply learns the code-query interaction for enhancing code searches, which solves the independent similarity matching and the small training dataset problems. We evaluate CQIL on two datasets (CODEnn and CosBench). The evaluation results show the strengths of CQIL-it achieves the MAP@1 values, 0.694 and 0.574, on CODEnn and CosBench, respectively. In particular, it outperforms DeepCS and UNIF, two state-of-the-art code search methods, by 13.6% and 18.1% in MRR, respectively, when the training dataset is insufficient.
