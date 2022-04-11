---
layout: publication
title: "A Statistical Semantic Language Model for Source Code"
authors: Tung Thanh Nguyen, Anh Tuan Nguyen, Hoan Anh Nguyen, Tien N. Nguyen
conference: FSE
year: 2013
tags: ["language model"]
---
Recent research has successfully applied the statistical n-gram language model to show that source code exhibits a
good level of repetition. The n-gram model is shown to have
good predictability in supporting code suggestion and completion. However, the state-of-the-art n-gram approach to
capture source code regularities/patterns is based only on
the lexical information in a local context of the code units.
To improve predictability, we introduce SLAMC, a novel statistical semantic language model for source code. It incorporates semantic information into code tokens and models the
regularities/patterns of such semantic annotations, called sememes, rather than their lexemes. It combines the local context in semantic n-grams with the global technical concerns/functionality into an n-gram topic model, together with pairwise associations of program elements. Based on SLAMC,
we developed a new code suggestion method, which is empirically evaluated on several projects to have relatively 18–68%
higher accuracy than the state-of-the-art approach.

