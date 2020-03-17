---
layout: publication
title: "Semantic Robustness of Models of Source Code"
authors: G. Ramakrishnan, J. Henkel, Z. Wang, A. Albarghouthi, S. Jha, T. Reps
conference:
year: 2020
bibkey: ramakrishnan2020semantic
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2002.03043"}
tags: ["adversarial", "naming"]
---
Deep neural networks are vulnerable to adversarial examples - small input perturbations that result in incorrect predictions. We study this problem in the context of models of source code, where we want the network to be robust to source-code modifications that preserve code functionality. We define a natural notion of robustness, k-transformation robustness, in which an adversary performs up to k semantics-preserving transformations to an input program. We show how to train robust models using an adversarial training objective inspired by that of Madry et al. (2018) for continuous domains.

We implement an extensible framework for adversarial training over source code, and conduct a thorough evaluation on a number of datasets and two different architectures. Our results show (1) the increase in robustness following adversarial training, (2) the ability of training on weak adversaries to provide robustness to attacks by stronger adversaries, and (3) the shift in attribution focus of adversarially trained models towards semantic vs. syntactic features. 
