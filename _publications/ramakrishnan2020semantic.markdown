---
layout: publication
title: "Semantic Robustness of Models of Source Code"
authors: Jordan Henkel, Goutham Ramakrishnan, Zi Wang, Aws Albarghouthi, Somesh Jha, Thomas Reps
conference: SANER
year: 2022
additional_links:
   - {name: "PDF", url: "https://pages.cs.wisc.edu/~jjhenkel/papers/saner22-semantic-robustness.pdf"}
   - {name: "IEEE", url: "https://ieeexplore.ieee.org/document/9825895"}
   - {name: "ArXiV", url: "https://arxiv.org/abs/2002.03043"}
   - {name: "Code", url: "https://github.com/jjhenkel/averloc"}
tags: ["adversarial", "naming"]
---
Deep neural networks are vulnerable to adversarial examples - small input perturbations that result in incorrect predictions. We study this problem for models of source code, where we want the neural network to be robust to source-code modifications that preserve code functionality. To facilitate training robust models, we define a powerful and generic adversary that can employ sequences of parametric, semantics-preserving program transformations. We then explore how, with such an adversary, one can train models that are robust to adversarial program transformations. We conduct a thorough evaluation of our approach and find several surprising facts: we find robust training to beat dataset augmentation in every evaluation we performed; we find that a state-of-the-art architecture (code2seq) for models of code is harder to make robust than a simpler baseline; additionally, we find code2seq to have surprising weaknesses not present in our simpler baseline model; finally, we find that robust models perform better against unseen data from different sources (as one might hope) - however, we also find that robust models are not clearly better in the cross-language transfer task. To the best of our knowledge, we are the first to study the interplay between robustness of models of code and the domain-adaptation and cross-language transfer tasks.
