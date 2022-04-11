---
layout: publication
title: "Learning How to Mutate Source Code from Bug-Fixes"
authors: Michele Tufano, Cody Watson, Gabriele Bavota, Massimiliano Di Penta, Martin White, Denys Poshyvanyk
conference: 
year: 2018
tags: ["repair", "edit"]
---
Mutation testing has been widely accepted as an approach to guide test case generation or to assess the effectiveness of test suites. Empirical studies have shown that mutants are representative of real faults; yet they also indicated a clear need for better, possibly customized, mutation operators and strategies. While some recent papers have tried to devise domain-specific or general purpose mutator operators by manually analyzing real faults, such an activity is effort- (and error-) prone and does not deal with an important practical question as to how to really mutate a given source code element. We propose a novel approach to automatically learn mutants from faults in real programs. First, our approach processes bug fixing changes using fine-grained differencing, code abstraction, and change clustering. Then, it learns mutation models using a deep learning strategy. We have trained and evaluated our technique on a set of ~787k bugs mined from GitHub. Starting from code fixed by developers in the context of a bug-fix, our empirical evaluation showed that our models are able to predict mutants that resemble original fixed bugs in between 9% and 45% of the cases (depending on the model). Moreover, over 98% of the automatically generated mutants are lexically and syntactically correct.
