---
layout: publication
title: "Code Completion with Statistical Language Models"
authors: Veselin Raychev, Martin Vechev, Eran Yahav
conference: PLDI
year: 2014
tags: ["language model", "autocomplete", "code generation"]
---
We address the problem of synthesizing code completions for programs using APIs. Given a program with holes, we synthesize completions for holes with the most likely sequences of method calls.

Our main idea is to reduce the problem of code completion to
a natural-language processing problem of predicting probabilities
of sentences. We design a simple and scalable static analysis that
extracts sequences of method calls from a large codebase, and
index these into a statistical language model. We then employ
the language model to find the highest ranked sentences, and use
them to synthesize a code completion. Our approach is able to
synthesize sequences of calls across multiple objects together with
their arguments.

Experiments show that our approach is fast and effective. Virtually all computed completions typecheck, and the desired completion appears in the top 3 results in 90% of the cases.
