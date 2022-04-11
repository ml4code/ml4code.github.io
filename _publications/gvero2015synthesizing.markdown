---
layout: publication
title: "Synthesizing Java expressions from free-form queries"
authors: Tihomir Gvero, Viktor Kuncak
conference: OOPSLA
year: 2015
tags: ["synthesis", "code generation", "bimodal"]
---
We present a new code assistance tool for integrated development environments. Our system accepts as input free-form queries containing a mixture of English and Java, and produces Java code expressions that take the query into account and respect syntax, types, and scoping rules of Java, as well as statistical usage patterns. In contrast to solutions based on code search, the results returned by our tool need not directly correspond to any previously seen code fragment. As part of our system we have constructed a probabilistic context free grammar for Java constructs and library invocations, as well as an algorithm that uses a customized natural language processing tool chain to extract information from free-form text queries. We present the results on a number of examples showing that our technique (1) often produces the expected code fragments, (2) tolerates much of the flexibility of natural language, and (3) can repair incorrect Java expressions that use, for example, the wrong syntax or missing arguments. 
