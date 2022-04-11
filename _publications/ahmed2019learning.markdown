---
layout: publication
title: "Learning Lenient Parsing & Typing via Indirect Supervision"
authors: Toufique Ahmed, Vincent Hellendoorn, Premkumar Devanbu
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.05879"}
tags: ["types"]
---
Both professional coders and teachers frequently deal with imperfect (fragmentary, incomplete, ill-formed) code. Such fragments are common in StackOverflow; students also frequently produce ill-formed code, for which instructors, TAs (or students themselves) must find repairs. In either case, the developer experience could be greatly improved if such code could somehow be parsed & typed; this makes them more amenable to use within IDEs and allows early detection and repair of potential errors. We introduce a lenient parser, which can parse & type fragments, even ones with simple errors. Training a machine learner to leniently parse & type imperfect code requires a large training set of pairs of imperfect code and its repair (and/or type information); such training sets are limited by human effort and curation. In this paper, we present a novel indirectly supervised approach to train a lenient parser, without access to such human-curated training data. We leverage the huge corpus of mostly correct code available on Github, and the massive, efficient learning capacity of Transformer-based NN architectures. Using GitHub data, we first create a large dataset of fragments of code and corresponding tree fragments and type annotations; we then randomly corrupt the input fragments (while requiring correct output) by seeding errors that mimic corruptions found in StackOverflow and student data. Using this data, we train high-capacity transformer models to overcome both fragmentation and corruption. With this novel approach, we can achieve reasonable performance on parsing & typing StackOverflow fragments; we also demonstrate that our approach achieves best-in-class performance on a large dataset of student errors. 
