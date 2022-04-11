---
layout: publication
title: "PHOG: Probabilistic Model for Code"
authors: Pavol Bielik, Veselin Raychev, Martin Vechev
conference: ICML
year: 2016
tags: ["grammar", "code generation", "language model"]
---
We introduce a new generative model for code called probabilistic higher order grammar (PHOG). PHOG generalizes probabilistic context free grammars (PCFGs) by allowing conditioning of a production rule beyond the parent non-terminal, thus capturing rich contexts relevant to programs. Even though PHOG is more powerful than a PCFG, it can be learned from data just as efficiently. We trained a PHOG model on a large JavaScript code corpus and show that it is more precise than existing models, while similarly fast. As a result, PHOG can immediately benefit existing programming tools based on probabilistic models of code.
