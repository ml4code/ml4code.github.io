---
layout: publication
title: "Learning to Generate Pseudo-code from Source Code using Statistical Machine Translation"
authors: Yusuke Oda, Hiroyuki Fudaba, Graham Neubig, Hideaki Hata, Sakriani Sakti, Tomoki Toda, Satoshi Nakamura
conference: ASE
year: 2015
tags: ["representation", "bimodal", "grammar"]
---
Pseudo-code written in natural language can aid
the comprehension of source code in unfamiliar programming
languages. However, the great majority of source code has no
corresponding pseudo-code, because pseudo-code is redundant
and laborious to create. If pseudo-code could be generated
automatically and instantly from given source code, we could
allow for on-demand production of pseudo-code without human
effort. In this paper, we propose a method to automatically
generate pseudo-code from source code, specifically adopting the
statistical machine translation (SMT) framework. SMT, which
was originally designed to translate between two natural languages, allows us to automatically learn the relationship between
source code/pseudo-code pairs, making it possible to create a
pseudo-code generator with less human effort. In experiments,
we generated English or Japanese pseudo-code from Python
statements using SMT, and find that the generated pseudo-code
is largely accurate, and aids code understanding.
