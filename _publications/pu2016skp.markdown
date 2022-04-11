---
layout: publication
title: "sk_p: a neural program corrector for MOOCs"
authors: Yewen Pu, Karthik Narasimhan, Armando Solar-Lezama, Regina Barzilay
conference: SPLASH 
year: 2016
tags: ["repair"]
---
We present a novel technique for automatic program correction in MOOCs, capable of fixing both syntactic and semantic errors without manual, problem specific correction strategies. Given an incorrect student program, it generates candidate programs from a distribution of likely corrections, and checks each candidate for correctness against a test suite.

The key observation is that in MOOCs many programs share similar code fragments, and the seq2seq neural network model, used in the natural-language processing task of machine translation, can be modified and trained to recover these fragments.

Experiment shows our scheme can correct 29% of all incorrect submissions and out-performs state of the art approach which requires manual, problem specific correction strategies.
