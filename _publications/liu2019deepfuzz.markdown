---
layout: publication
title: "DeepFuzz: Automatic Generation of Syntax Valid C Programs for Fuzz Testing"
authors: Xiao Liu, Xiaoting Li, Rupesh Prajapati, Dinghao Wu
conference: AAAI
year: 2019
tags: ["fuzzing", "code generation"]
---
Compilers  are among  the  most  fundamental  programming
tools for building software. However, production compilers
remain  buggy.  Fuzz  testing  is  often  leveraged  with  newly-generated,
or  mutated  inputs  in  order  to  find  new  bugs  or security vulnerabilities.
In this paper, we propose a grammar-based fuzzing tool called DeepFuzz. Based on a generative
Sequence-to-Sequence model, DeepFuzz automatically and continuously generates well-formed
C programs. We use this set of new C programs to fuzz off-the-shelf C compilers, e.g. GCC and Clang/LLVM.
We present a detailed case study to analyze  the  success  rate  and  coverage  improvement  of  the
generated C programs for fuzz testing. We analyze the performance of DeepFuzz with three types of sampling
methods  as  well  as  three  types  of  generation  strategies.  Consequently, DeepFuzz 
improved the testing efficacy in regards to the line, function, and branch coverage. In our preliminary
study, we found and reported 8 bugs of GCC, all of which are actively being addressed by developers.
