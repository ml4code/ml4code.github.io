---
layout: publication
title: "ManyTypes4Py: A Benchmark Python Dataset for Machine Learning-based Type Inference"
authors: Amir M. Mir, Evaldas Latoskinas, Georgios Gousios
conference: MSR
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2104.04706"}
   - {name: "Dataset", url: "https://zenodo.org/record/4479714"}
tags: ["dataset", "types"]
---
In this paper, we present ManyTypes4Py, a large Python dataset for machine learning (ML)-based type inference. The dataset contains a total of 5,382 Python projects with more than 869K type annotations. Duplicate source code files were removed to eliminate the negative effect of the duplication bias. To facilitate training and evaluation of ML models, the dataset was split into training, validation and test sets by files. To extract type information from abstract syntax trees (ASTs), a lightweight static analyzer pipeline is developed and accompanied with the dataset. Using this pipeline, the collected Python projects were analyzed and the results of the AST analysis were stored in JSON-formatted files. The ManyTypes4Py dataset is shared on zenodo and its tools are publicly available on GitHub. 
