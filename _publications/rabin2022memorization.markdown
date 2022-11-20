---
layout: publication
title: "Memorization and Generalization in Neural Code Intelligence Models"
authors: Md Rafiqul Islam Rabin, Aftab Hussain, Mohammad Amin Alipour, Vincent J. Hellendoorn
conference: IST
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2106.08704"}
   - {name: "code", url: "https://github.com/mdrafiqulrabin/CI-Memorization"}
tags: ["evaluation", "memorization", "generalizability", "refactoring", "language model"]
---
Deep Neural Networks (DNNs) are increasingly being used in software engineering and code intelligence tasks. These are powerful tools that are capable of learning highly generalizable patterns from large datasets through millions of parameters. At the same time, their large capacity can render them prone to memorizing data points. Recent work suggests that the memorization risk manifests especially strongly when the training dataset is noisy, involving many ambiguous or questionable samples, and memorization is the only recourse. The goal of this paper is to evaluate and compare the extent of memorization and generalization in neural code intelligence models. It aims to provide insights on how memorization may impact the learning behavior of neural models in code intelligence systems. To observe the extent of memorization in models, we add random noise to the original training dataset and use various metrics to quantify the impact of noise on various aspects of training and testing. We evaluate several state-of-the-art neural code intelligence models and benchmarks based on Java, Python, and Ruby codebases. Our results highlight important risks: millions of trainable parameters allow the neural networks to memorize anything, including noisy data, and provide a false sense of generalization. We observed all models manifest some forms of memorization. This can be potentially troublesome in most code intelligence tasks where they rely on rather noise-prone and repetitive data sources, such as code from GitHub. To the best of our knowledge, we provide the first study to quantify memorization effects in the domain of software engineering and code intelligence systems. This work raises awareness and provides new insights into important issues of training neural models in code intelligence systems that are usually overlooked by software engineering researchers.
