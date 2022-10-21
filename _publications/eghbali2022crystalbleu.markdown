---
layout: publication
title: "CrystalBLEU: Precisely and Efficiently Measuring the Similarity of Code"
authors: Aryaz Eghbali, Michael Pradel
conference: ASE
year: 2022
additional_links:
   - {name: "Preprint", url: "https://www.software-lab.org/publications/ase2022_CrystalBLEU.pdf"}
tags: ["evaluation"]
---
Recent years have brought a surge of work on predicting pieces
of source code, e.g., for code completion, code migration, program
repair, or translating natural language into code. All this work faces
the challenge of evaluating the quality of a prediction w.r.t. some
oracle, typically in the form of a reference solution. A common
evaluation metric is the BLEU score, an n-gram-based metric originally proposed for evaluating natural language translation, but
adopted in software engineering because it can be easily computed
on any programming language and enables automated evaluation at
scale. However, a key difference between natural and programming
languages is that in the latter, completely unrelated pieces of code
may have many common n-grams simply because of the syntactic
verbosity and coding conventions of programming languages. We
observe that these trivially shared n-grams hamper the ability of
the metric to distinguish between truly similar code examples and
code examples that are merely written in the same language. This
paper presents CrystalBLEU, an evaluation metric based on BLEU,
that allows for precisely and efficiently measuring the similarity of
code. Our metric preserves the desirable properties of BLEU, such
as being language-agnostic, able to handle incomplete or partially
incorrect code, and efficient, while reducing the noise caused by
trivially shared n-grams. We evaluate CrystalBLEU on two datasets
from prior work and on a new, labeled dataset of semantically equivalent programs. Our results show that CrystalBLEU can distinguish
similar from dissimilar code examples 1.9–4.5 times more effectively, when compared to the original BLEU score and a previously
proposed variant of BLEU for code.
