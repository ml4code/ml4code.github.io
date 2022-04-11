---
layout: publication
title: "AutoPandas: neural-backed generators for program synthesis"
authors: Rohan Bavishi, Caroline Lemieux, Roy Fox, Koushik Sen, Ion Stoica
conference: OOPSLA
year: 2019
tags: ["synthesis", "GNN", "API"]
---
Developers nowadays have to contend with a growing number of APIs. While in the long-term they are very useful to developers, many modern APIs have an incredibly steep learning curve, due to their hundreds of functions handling many arguments, obscure documentation, and frequently changing semantics. For APIs that perform data transformations, novices can often provide an I/O example demonstrating the desired transformation, but may be stuck on how to translate it to the API. A programming-by-example synthesis engine that takes such I/O examples and directly produces programs in the target API could help such novices. Such an engine presents unique challenges due to the breadth of real-world APIs, and the often-complex constraints over function arguments. We present a generator-based synthesis approach to contend with these problems. This approach uses a program candidate generator, which encodes basic constraints on the space of programs. We introduce neural-backed operators which can be seamlessly integrated into the program generator. To improve the efficiency of the search, we simply use these operators at non-deterministic decision points, instead of relying on domain-specific heuristics. We implement this technique for the Python pandas library in AutoPandas. AutoPandas supports 119 pandas dataframe transformation functions. We evaluate AutoPandas on 26 real-world benchmarks and find it solves 17 of them.
