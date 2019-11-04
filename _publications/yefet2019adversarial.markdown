---
layout: publication
title: "Adversarial Examples for Models of Code"
authors: N. Yefet, U. Alon, E. Yahav
conference:
year: 2019
bibkey: yefet2019adversarial
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.07517"}
tags: ["adversarial"]
---
We introduce a novel approach for attacking trained models of code with adversarial examples. The main idea is to force a given trained model to make a prediction of the adversary's choice by introducing small perturbations that do not change program semantics. We find these perturbations by deriving the desired prediction with respect to the model's inputs while holding the model weights constant and following the gradients to slightly modify the input.

To defend a model against such attacks, we propose placing a defensive model in front of the downstream model. The defensive model detects unlikely mutations and masks them before feeding the input to the downstream model.

We show that our attack succeeds in changing a prediction to the adversary's desire ("targeted attack") up to 89% of the times, and succeeds in changing a given prediction to any incorrect prediction ("non-targeted attack") 94% of the times. By using our proposed defense, the success rate of the attack drops drastically for both targeted and non-targeted attacks, with a minor penalty of 2% relative degradation in accuracy while not performing under attack. 
