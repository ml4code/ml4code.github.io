---
layout: publication
title: "Semantic Source Code Models Using Identifier Embeddings"
authors: Vasiliki Efstathiou, Diomidis Spinellis
conference: MSR
year: 2019
tags: ["representation"]
---
The emergence of online open source repositories in the recent years has led to an explosion in the volume of openly available source code, coupled with metadata that relate to a variety of software development activities. As an effect, in line with recent advances in machine learning research, software maintenance activities are switching from symbolic formal methods to data-driven methods. In this context, the rich semantics hidden in source code identifiers provide opportunities for building semantic representations of code which can assist tasks of code search and reuse. To this end, we deliver in the form of pretrained vector space models, distributed code representations for six popular programming languages, namely, Java, Python, PHP, C, C++, and C#. The models are produced using fastText, a state-of-the-art library for learning word representations. Each model is trained on data from a single programming language; the code mined for producing all models amounts to over 13.000 repositories. We indicate dissimilarities between natural language and source code, as well as variations in coding conventions in between the different programming languages we processed. We describe how these heterogeneities guided the data preprocessing decisions we took and the selection of the training parameters in the released models. Finally, we propose potential applications of the models and discuss limitations of the models. 
