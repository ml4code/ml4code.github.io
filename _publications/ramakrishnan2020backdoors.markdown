---
layout: publication
title: "Backdoors in Neural Models of Source Code"
authors: Goutham Ramakrishnan, Aws Albarghouthi
conference: ICPR
year: 2022
additional_links:
    - {name: "IEEE", url: "https://ieeexplore.ieee.org/document/9956690"}
    - {name: "ArXiV", url: "https://arxiv.org/abs/2006.06841"}
    - {name: "Code", url: "https://github.com/goutham7r/backdoors-for-code"}
tags: ["adversarial"]
---
Deep neural networks are vulnerable to a range of adversaries. A particularly pernicious class of vulnerabilities are backdoors, where model predictions diverge in the presence of subtle triggers in inputs. An attacker can implant a backdoor by poisoning the training data to yield a desired target prediction on triggered inputs. We study backdoors in the context of deep-learning for source code. (1) We define a range of backdoor classes for source-code tasks and show how to poison a dataset to install such backdoors. (2) We adapt and improve recent algorithms from robust statistics for our setting, showing that backdoors leave a spectral signature in the learned representation of source code, thus enabling detection of poisoned data. (3) We conduct a thorough evaluation on different architectures and languages, showing the ease of injecting backdoors and our ability to eliminate them.
