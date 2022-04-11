---
layout: publication
title: "Neural Attribute Machines for Program Generation"
authors: Matthew Amodio, Swarat Chaudhuri, Thomas W. Reps
conference: 
year: 2017
tags: ["grammar", "code generation", "representation"]
---
Recurrent neural networks have achieved remarkable success at generating sequences with complex structures, thanks to advances that include richer embeddings of input and cures for vanishing gradients. Trained only on sequences from a known grammar, though, they can still struggle to learn rules and constraints of the grammar. Neural Attribute Machines (NAMs) are equipped with a logical machine that represents the underlying grammar, which is used to teach the constraints to the neural machine by (i) augmenting the input sequence, and (ii) optimizing a custom loss function. Unlike traditional RNNs, NAMs are exposed to the grammar, as well as samples from the language of the grammar. During generation, NAMs make significantly fewer violations of the constraints of the underlying grammar than RNNs trained only on samples from the language of the grammar.

