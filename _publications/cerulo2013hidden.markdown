---
layout: publication
title: "A Hidden Markov Model to Detect Coded Information Islands in Free Text"
authors: Luigi Cerulo, Michele Ceccarelli, Massimiliano Di Penta, Gerardo Canfora
conference: SCAM 
year: 2013
tags: ["information extraction"]
---
Emails and issue reports capture useful knowledge about development practices, bug fixing, and change activities. Extracting such a content is challenging, due to the mix-up of
source code and natural language, unstructured text.

In this paper we introduce an approach, based on Hidden Markov Models (HMMs), to extract coded information islands, such as source code, stack traces, and patches, from free text at a token level of granularity. We train a HMM for each category of information contained in the text, and adopt the Viterbi algorithm to recognize whether the sequence of tokens --- e.g., words, language keywords, numbers, parentheses, punctuation marks, etc. --- observed in a text switches among those HMMs. Although our implementation focuses on extracting source code from emails, the approach could be easily extended to include in principle any text-interleaved language.

We evaluated our approach with respect to the state of art on a set of development emails and bug reports drawn from the software repositories of well known open source systems. Results indicate an accuracy between 82% and 99%, which is in line with existing approaches which, differently from ours, require the manual definition of regular expressions or parsers.

