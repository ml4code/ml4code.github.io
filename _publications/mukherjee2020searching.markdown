---
layout: publication
title: "Searching a Database of Source Codes Using Contextualized Code Search"
authors: Rohan Mukherjee, Swarat Chaudhuri, Chris Jermaine
conference: 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2001.03277"}
tags: ["search", "representation"]
---
We assume a database containing a large set of program source codes and consider the problem of contextualized code search over that database. A programmer has written some part of a program, but has left part of the program (such as a method or a function body) incomplete. The goal is to use the context surrounding the missing code to automatically 'figure out' which of the codes in the database would be useful to the programmer in order to help complete the missing code, in the sense that the programmer could either re-purpose the retrieved code and use the re-purposed code to fill the missing spot in the program. Or, the user could use the retrieved code as a model for implementing the missing code. The search is 'contextualized' in the sense that the search engine should use clues in the partially-completed code to figure out which database code is most useful. The user should not be required to formulate an explicit query.

We cast contextualized code search as a learning problem, where the goal is to learn a distribution function computing the likelihood that each database code completes the program, and propose a neural model for predicting which database code is likely to be most useful. Because it will be prohibitively expensive to apply a neural model to each code in a database of millions or billions of codes at search time, one of our key technical concerns is ensuring a speedy search. We address this by learning a 'reverse encoder' that can be used to reduce the problem of evaluating each database code to computing a convolution of two normal distributions, making it possible to search a large database of codes in a reasonable time. 
