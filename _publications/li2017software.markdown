---
layout: publication
title: "Software Defect Prediction via Convolutional Neural Network"
authors: Jian Li, Pinjia He, Jieming Zhu, Michael R. Lyu
conference: QRS
year: 2017
tags: ["defect"]
---
To improve software reliability, software defect prediction is utilized to assist developers in finding potential bugs
and allocating their testing efforts. Traditional defect prediction
studies mainly focus on designing hand-crafted features, which
are input into machine learning classifiers to identify defective
code. However, these hand-crafted features often fail to capture
the semantic and structural information of programs. Such
information is important in modeling program functionality and
can lead to more accurate defect prediction.
In this paper, we propose a framework called Defect Prediction
via Convolutional Neural Network (DP-CNN), which leverages
deep learning for effective feature generation. Specifically, based
on the programs’ Abstract Syntax Trees (ASTs), we first extract
token vectors, which are then encoded as numerical vectors
via mapping and word embedding. We feed the numerical
vectors into Convolutional Neural Network to automatically
learn semantic and structural features of programs. After that,
we combine the learned features with traditional hand-crafted
features, for accurate software defect prediction. We evaluate our
method on seven open source projects in terms of F-measure in
defect prediction. The experimental results show that in average,
DP-CNN improves the state-of-the-art method by 12%.

