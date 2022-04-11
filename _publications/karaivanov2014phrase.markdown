---
layout: publication
title: "Phrase-Based Statistical Translation of Programming Languages"
authors: S. Karaivanov, Veselin Raychev, Martin Vechev
conference: Onward
year: 2014
tags: ["migration", "code generation"]
---
Phrase-based statistical machine translation approaches have been
highly successful in translating between natural languages and are
heavily used by commercial systems (e.g. Google Translate).

The main objective of this work is to investigate the applicability of
these approaches for translating between programming languages.
Towards that, we investigated several variants of the phrase-based
translation approach: i) a direct application of the approach to
programming languages, ii) a novel modification of the approach
to incorporate the grammatical structure of the target programming
language (so to avoid generating target programs which do not
parse), and iii) a combination of ii) with custom rules added to
improve the quality of the translation.

To experiment with the above systems, we investigated machine
translation from C# to Java. For the training, which takes about
60 hours, we used a parallel corpus of 20, 499 C#-to-Java method
translations. We then evaluated each of the three systems above by
translating 1,000 C# methods. Our experimental results indicate
that with the most advanced system, about 60% of the translated
methods compile (the top ranked) and out of a random sample of 50
correctly compiled methods, 68% (34 methods) were semantically
equivalent to the reference solution.
