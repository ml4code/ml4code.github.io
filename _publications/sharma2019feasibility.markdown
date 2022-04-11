---
layout: publication
title: "On the Feasibility of Transfer-learning Code Smells using Deep Learning"
authors: Tushar Sharma, Vasiliki Efstathiou, Panos Louridas, Diomidis Spinellis
conference: 
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1904.03031"}
tags: ["representation", "program analysis"]
---
**Context**: A substantial amount of work has been done to detect smells in source code using metrics-based and heuristics-based methods. Machine learning methods have been recently applied to detect source code smells; however, the current practices are considered far from mature.

**Objective**: First, explore the feasibility of applying deep learning models to detect smells without extensive feature engineering, just by feeding the source code in tokenized form. Second, investigate the possibility of applying transfer-learning in the context of deep learning models for smell detection. 

**Method**: We use existing metric-based state-of-the-art methods for detecting three implementation smells and one design smell in C# code. Using these results as the annotated gold standard, we train smell detection models on three different deep learning architectures. These architectures use Convolution Neural Networks (CNNs) of one or two dimensions, or Recurrent Neural Networks (RNNs) as their principal hidden layers. For the first objective of our study, we perform training and evaluation on C# samples, whereas for the second objective, we train the models from C# code and evaluate the models over Java code samples. We perform the experiments with various combinations of hyper-parameters for each model.

**Results**: We find it feasible to detect smells using deep learning methods. Our comparative experiments find that there is no clearly superior method between CNN-1D and CNN-2D. We also observe that performance of the deep learning models is smell-specific. Our transfer-learning experiments show that transfer-learning is definitely feasible for implementation smells with performance comparable to that of direct-learning. This work opens up a new paradigm to detect code smells by transfer-learning especially for the programming languages where the comprehensive code smell detection tools are not available. 
