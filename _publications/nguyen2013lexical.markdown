---
layout: publication
title: "Lexical Statistical Machine Translation for Language Migration"
authors: Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen
conference: FSE
year: 2013
tags: ["migration", "API"]
---
Prior research has shown that source code also exhibits naturalness, i.e. it is written by humans and is likely to be
repetitive. The researchers also showed that the n-gram language model is useful in predicting the next token in a source
file given a large corpus of existing source code. In this paper, we investigate how well statistical machine translation
(SMT) models for natural languages could help in migrating source code from one programming language to another.
We treat source code as a sequence of lexical tokens and
apply a phrase-based SMT model on the lexemes of those
tokens. Our empirical evaluation on migrating two Java
projects into C# showed that lexical, phrase-based SMT
could achieve high lexical translation accuracy ( BLEU from
81.3-82.6%). Users would have to manually edit only 11.9-15.8% of the total number of tokens in the resulting code to
correct it. However, a high percentage of total translation
methods (49.5-58.6%) is syntactically incorrect. Therefore,
our result calls for a more program-oriented SMT model that
is capable of better integrating the syntactic and semantic
information of a program to support language migration.
