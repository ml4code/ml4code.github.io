---
layout: publication
title: "Code Translation with Compiler Representations"
authors: Marc Szafraniec, Baptiste Roziere, Hugh Leather, Francois Charton, Patrick Labatut, Gabriel Synnaeve
conference: 
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2207.03578"}
tags: ["Transformer", "migration", "decompilation"]
---
In this paper, we leverage low-level compiler intermediate representations (IR) to improve code translation. Traditional transpilers rely on syntactic information and handcrafted rules, which limits their applicability and produces unnatural-looking code. Applying neural machine translation (NMT) approaches to code has successfully broadened the set of programs on which one can get a natural-looking translation. However, they treat the code as sequences of text tokens, and still do not differentiate well enough between similar pieces of code which have different semantics in different languages. The consequence is low quality translation, reducing the practicality of NMT, and stressing the need for an approach significantly increasing its accuracy. Here we propose to augment code translation with IRs, specifically LLVM IR, with results on the C++, Java, Rust, and Go languages. Our method improves upon the state of the art for unsupervised code translation, increasing the number of correct translations by 11% on average, and up to 79% for the Java - Rust pair. We extend previous test sets for code translation, by adding hundreds of Go and Rust functions. Additionally, we train models with high performance on the problem of IR decompilation, generating programming source code from IR, and study using IRs as intermediary pivot for translation.
