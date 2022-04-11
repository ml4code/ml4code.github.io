---
layout: publication
title: "Statistical Learning Approach for Mining API Usage Mappings for Code Migration"
authors: Anh Tuan Nguyen, Hoan Anh Nguyen, Tung Thanh Nguyen, Tien N. Nguyen
conference: ASE
year: 2014
tags: ["migration", "API"]
---
The same software product nowadays could appear in multiple platforms and devices. To address business needs, software companies
develop a software product in a programming language and then
migrate it to another one. To support that process, semi-automatic
migration tools have been proposed. However, they require users
to manually define the mappings between the respective APIs of
the libraries used in two languages. To reduce such manual effort,
we introduce StaMiner, a novel data-driven approach that statistically learns the mappings between APIs from the corpus of the
corresponding client code of the APIs in two languages Java and
C#. Instead of using heuristics on the textual or structural similarity
between APIs in two languages to map API methods and classes
as in existing mining approaches, StaMiner is based on a statistical
model that learns the mappings in such a corpus and provides mappings for APIs with all possible arities. Our empirical evaluation
on several projects shows that StaMiner can detect API usage mappings with higher accuracy than a state-of-the-art approach. With
the resulting API mappings mined by StaMiner, Java2CSharp, an
existing migration tool, could achieve a higher level of accuracy.
