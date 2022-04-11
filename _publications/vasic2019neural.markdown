---
layout: publication
title: "Neural Program Repair by Jointly Learning to Localize and Repair"
authors: Marko Vasic, Aditya Kanade, Petros Maniatis, David Bieber, Rishabh Singh
conference: ICLR
year: 2019
tags: ["repair", "program analysis", "variable misuse"]
---
Due to its potential to improve programmer productivity and software quality, automated program repair has been an active topic of research. Newer techniques harness neural networks to learn directly from examples of buggy programs and their fixes. In this work, we consider a recently identified class of bugs called variable-misuse bugs. The state-of-the-art solution for variable misuse enumerates potential fixes for all possible bug locations in a program, before selecting the best prediction. We show that it is beneficial to train a model that jointly and directly localizes and repairs variable-misuse bugs. We present multi-headed pointer networks for this purpose, with one head each for localization and repair. The experimental results show that the joint model significantly outperforms an enumerative solution that uses a pointer based model for repair alone.
