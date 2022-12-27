---
layout: publication
title: "SantaCoder: don’t reach for the stars!"
authors: Loubna Ben Allal, Raymond Li, Denis Kocetkov, Chenghao Mou, Christopher Akiki, Carlos Munoz Ferrandis, Niklas Muenninghoff, Mayank Mishra, Alex Gu, Manan Den, Longesh Kumar Umapathi, Carolyn Jane Anderson, Yangtian Zi, Joel Lamy Poirier, Hailey Schoelkopf, Sergey Troshin, Dmitry Abulkhanov, Manuel Romero, Terry Yue Zhuo, Francesco De Toni, Bernanrdo Garcia del Rio, Qian Liu, Shamik Bose, Urvashi Bhattacharyya, Michael Lappert, Ian Yu, Paulo Villegas, Jia Li, David Lansy, Huu Nguyen, Danish Contractor, Luis Villa, Daniel Fried, Dzmitry Bahdanau, Yacine Jernite, Sean Hughes, Arjun Guha, Harm de Vries, Leonadro von Werra
conference:
year: 2022
tags: ["Transformer"]
---
The BigCode project is an open-scientific collaboration working on the responsible development of large language models for code.1 This tech report describes the progress of the collaboration until December 2022, outlining the current state of the Personally Identifiable Information (PII)
redaction pipeline, the experiments conducted to de-risk the model architecture, and the experiments investigating better preprocessing methods for the training data. We train 1.1B parameter models on the Java,
JavaScript, and Python subsets of The Stack (Kocetkov et al., 2022) and
evaluate the models on MultiPL-E (Cassano et al., 2022), a text2code
benchmark available in 18 programming languages. We find that more
aggressive filtering of near-duplicates can further boost performance and,
surprisingly, that selecting files from repositories with 5+ GitHub stars
deteriorates performance significantly. Our best model outperforms previous open-source multilingual code generation models (InCoder-6.7B and
CodeGen-Multi-2.7B) in both left-to-right generation and infilling on the
Java, JavaScript, and Python portions of MultiPL-E, despite being a substantially smaller model. All models are released under an OpenRAIL
license at https://hf.co/bigcode
