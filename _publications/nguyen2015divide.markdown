---
layout: publication
title: "Divide-and-Conquer Approach for Multi-phase Statistical Migration for Source Code"
authors: Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen
conference: ASE
year: 2014
tags: ["migration"]
---
Prior research shows that directly applying phrase-based SMT on lexical tokens to migrate Java to C# produces
much semantically incorrect code. A key limitation is the use of
sequences in phrase-based SMT to model and translate source
code with well-formed structures. We propose mppSMT, a divideand-conquer technique to address that with novel training and migration algorithms using phrase-based SMT in three phases. First,
mppSMT treats a program as a sequence of syntactic units and
maps/translates such sequences in two languages to one another.
Second, with a syntax-directed fashion, it deals with the tokens
within syntactic units by encoding them with semantic symbols to
represent their data and token types. This encoding via semantic
symbols helps better migration of API usages. Third, the lexical
tokens corresponding to each sememe are mapped or migrated.
The resulting sequences of tokens are merged together to form
the final migrated code. Such divide-and-conquer and syntax-direction strategies enable phrase-based SMT to adapt well to
syntactical structures in source code, thus, improving migration
accuracy. Our empirical evaluation on several real-world systems
shows that 84.8–97.9% and 70–83% of the migrated methods are
syntactically and semantically correct, respectively. 26.3–51.2%
of total migrated methods are exactly matched to the human-written C# code in the oracle. Compared to Java2CSharp, a rule-based migration tool, it achieves higher semantic accuracy from
6.6–57.7% relatively. Importantly, it does not require manual
labeling for training data or manual definition of rules.
