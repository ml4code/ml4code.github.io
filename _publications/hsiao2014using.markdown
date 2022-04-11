---
layout: publication
title: "Using Web Corpus Statistics for Program Analysis"
authors: Chun-Hung Hsiao, Michael Cafarella, Satish Narayanasamy
conference: OOPSLA
year: 2014
tags: ["defect"]
---
Several program analysis tools—such as plagiarism detection and bug finding—rely on knowing a piece of code’s
relative semantic importance. For example, a plagiarism detector should not bother reporting two programs that have
an identical simple loop counter test, but should report programs that share more distinctive code. Traditional program
analysis techniques (e.g., finding data and control dependencies) are useful, but do not say how surprising or common
a line of code is. Natural language processing researchers
have encountered a similar problem and addressed it using
an n-gram model of text frequency, derived from statistics
computed over text corpora.

We propose and compute an n-gram model for programming languages, computed over a corpus of 2.8 million
JavaScript programs we downloaded from the Web. In contrast to previous techniques, we describe a code n-gram as
a subgraph of the program dependence graph that contains
all nodes and edges reachable in n steps from the statement.
We can count n-grams in a program and count the frequency
of n-grams in the corpus, enabling us to compute tf-idf-style
measures that capture the differing importance of different
lines of code. We demonstrate the power of this approach by
implementing a plagiarism detector with accuracy that beats
previous techniques, and a bug-finding tool that discovered
over a dozen previously unknown bugs in a collection of real
deployed programs.
