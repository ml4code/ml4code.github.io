---
layout: publication
title: "Path-Based Function Embedding and its Application to Specification Mining"
authors: Daniel DeFreez, Aditya V. Thakur, Cindy Rubio-González
conference: ICSE
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1802.07779"}
tags: ["program analysis", "representation"]
---
Identifying the relationships among program elements is useful
for program understanding, debugging, and analysis. One such
relationship is synonymy. Function synonyms are functions that
play a similar role in code, e.g. functions that perform initialization
for different device drivers, or functions that implement different
symmetric-key encryption schemes. Function synonyms are not
necessarily semantically equivalent and can be syntactically dissimilar; consequently, approaches for identifying code clones or
functional equivalence cannot be used to identify them. This paper presents `func2vec`, an algorithm that maps each function to a vector in a vector space such that function synonyms are grouped
together. We compute the function embedding by training a neu-
ral network on sentences generated from random walks over an
encoding of the program as a labeled pushdown system (ℓ-PDS).
We demonstrate that `func2vec`
is effective at identifying function
synonyms in the Linux kernel. Furthermore, we show how function
synonyms enable mining error-handling specifications with high
support in Linux file systems and drivers.
