---
layout: publication
title: "Learning to Reverse DNNs from AI Programs Automatically"
authors: Simin Chen, Hamed Khanpour, Cong Liu, Wei Yang
conference: IJCAI-ECAI 2022
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/pdf/2205.10364"}
tags: ["Reverse Engineering", "Binary Code"]
---
With the privatization deployment of DNNs on edge devices, the security of on-device DNNs has raised significant concern. To quantify the model leakage risk of on-device DNNs automatically, we propose NNReverse, the first learning-based method which can reverse DNNs from AI programs without domain knowledge. NNReverse trains a representation model to represent the semantics of binary code for DNN layers. By searching the most similar function in our database, NNReverse infers the layer type of a given function’s binary code. To represent assembly instructions semantics precisely, NNReverse proposes a more finegrained embedding model to represent the textual and structural-semantic of assembly functions.
