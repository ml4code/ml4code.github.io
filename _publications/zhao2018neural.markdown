---
layout: publication
title: "Neural-Augumented Static Analysis of Android Communication"
authors: Jinman Zhao, Aws Albarghouthi, Vaibhav Rastogi, Somesh Jha, Damien Octeau
conference: FSE
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1809.04059"}
tags: ["program analysis"]
---
We address the problem of discovering communication links between applications in the popular Android mobile operating system, an important problem for security and privacy in Android. Any scalable static analysis in this complex setting is bound to produce an excessive amount of false-positives, rendering it impractical. To improve precision, we propose to augment static analysis with a trained neural-network model that estimates the probability that a communication link truly exists. We describe a neural-network architecture that encodes abstractions of communicating objects in two applications and estimates the probability with which a link indeed exists. At the heart of our architecture are type-directed encoders (TDE), a general framework for elegantly constructing encoders of a compound data type by recursively composing encoders for its constituent types. We evaluate our approach on a large corpus of Android applications, and demonstrate that it achieves very high accuracy. Further, we conduct thorough interpretability studies to understand the internals of the learned neural networks. 
