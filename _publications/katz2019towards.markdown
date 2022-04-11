---
layout: publication
title: "Towards Neural Decompilation"
authors: Omer Katz, Yuval Olshaker, Yoav Goldberg, Eran Yahav
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1905.08325"}
tags: ["decompilation"]
---
We address the problem of automatic decompilation, converting a program in low-level representation back to a higher-level human-readable programming language. The problem of decompilation is extremely important for security researchers. Finding vulnerabilities and understanding how malware operates is much easier when done over source code.

The importance of decompilation has motivated the construction of hand-crafted rule-based decompilers. Such decompilers have been designed by experts to detect specific control-flow structures and idioms in low-level code and lift them to source level. The cost of supporting additional languages or new language features in these models is very high.

We present a novel approach to decompilation based on neural machine translation. The main idea is to automatically learn a decompiler from a given compiler. Given a compiler from a source language S to a target language T , our approach automatically trains a decompiler that can translate (decompile) T back to S . We used our framework to decompile both LLVM IR and x86 assembly to C code with high success rates. Using our LLVM and x86 instantiations, we were able to successfully decompile over 97% and 88% of our benchmarks respectively. 
