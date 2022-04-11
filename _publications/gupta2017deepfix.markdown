---
layout: publication
title: "DeepFix: Fixing Common C Language Errors by Deep Learning"
authors: Rahul Gupta, Soham Pal, Aditya Kanade, Shirish Shevade
conference: AAAI
year: 2017
tags: ["repair", "code generation"]
---
The problem of automatically fixing programming errors is a
very active research topic in software engineering. This is a
challenging problem as fixing even a single error may require
analysis of the entire program. In practice, a number of errors
arise due to programmer’s inexperience with the programming language or lack of attention to detail. We call these
common programming errors. These are analogous to grammatical errors in natural languages. Compilers detect such errors, but their error messages are usually inaccurate. In this
work, we present an end-to-end solution, called DeepFix, that
can fix multiple such errors in a program without relying on
any external tool to locate or fix them. At the heart of DeepFix
is a multi-layered sequence-to-sequence neural network with
attention which is trained to predict erroneous program locations along with the required correct statements. On a set of
6971 erroneous C programs written by students for 93 programming tasks, DeepFix could fix 1881 (27%) programs
completely and 1338 (19%) programs partially.
