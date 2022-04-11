---
layout: publication
title: "Toward Deep Learning Software Repositories"
authors: Martin White, Christopher Vendome, Mario Linares-Vasquez, Denys Poshyvanyk
conference: MSR
year: 2015
tags: ["representation"]
---
Deep learning subsumes algorithms that automatically learn compositional representations. The ability of these
models to generalize well has ushered in tremendous advances
in many fields such as natural language processing (NLP).
Recent research in the software engineering (SE) community
has demonstrated the usefulness of applying NLP techniques to
software corpora. Hence, we motivate deep learning for software
language modeling, highlighting fundamental differences between
state-of-the-practice software language models and connectionist
models. Our deep learning models are applicable to source
code files (since they only require lexically analyzed source
code written in any programming language) and other types
of artifacts. We show how a particular deep learning model
can remember its state to effectively model sequential data,
e.g., streaming software tokens, and the state is shown to be
much more expressive than discrete tokens in a prefix. Then we
instantiate deep learning models and show that deep learning
induces high-quality models compared to n-grams and cache-based n-grams on a corpus of Java projects. We experiment
with two of the models’ hyperparameters, which govern their
capacity and the amount of context they use to inform predictions,
before building several committees of software language models
to aid generalization. Then we apply the deep learning models to
code suggestion and demonstrate their effectiveness at a real SE
task compared to state-of-the-practice models. Finally, we propose
avenues for future work, where deep learning can be brought to
bear to support model-based testing, improve software lexicons,
and conceptualize software artifacts. Thus, our work serves as
the first step toward deep learning software repositories.
