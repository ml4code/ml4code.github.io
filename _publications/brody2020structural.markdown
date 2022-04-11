---
layout: publication
title: "A Structural Model for Contextual Code Changes"
authors: Shaked Brody, Uri Alon, Eran Yahav
conference: OOPSLA
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.13209"}
   - {name: "Code", url: "https://github.com/tech-srl/c3po"}
tags: ["edit", "grammar", "autocomplete"]
---
We address the problem of predicting edit completions based on a learned model that was trained on past edits. Given a code snippet that is partially edited, our goal is to predict a completion of the edit for the rest of the snippet. We refer to this task as the EditCompletion task and present a novel approach for tackling it. The main idea is to directly represent structural edits. This allows us to model the likelihood of the edit itself, rather than learning the likelihood of the edited code. We represent an edit operation as a path in the program's Abstract Syntax Tree (AST), originating from the source of the edit to the target of the edit. Using this representation, we present a powerful and lightweight neural model for the EditCompletion task. We conduct a thorough evaluation, comparing our approach to a variety of representation and modeling approaches that are driven by multiple strong models such as LSTMs, Transformers, and neural CRFs. Our experiments show that our model achieves 28% relative gain over state-of-the-art sequential models and 2× higher accuracy than syntactic models that learn to generate the edited code instead of modeling the edits directly. Our code, dataset, and trained models are publicly available at https://github.com/tech-srl/c3po/ . 
