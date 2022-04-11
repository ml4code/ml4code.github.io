---
layout: publication
title: "RefiNym: Using Names to Refine Types"
authors: Santanu Dash, Miltiadis Allamanis, Earl T. Barr
conference: FSE
year: 2018
tags: ["program analysis", "types"]
---
Source code is bimodal: it combines a formal algorithmic channel and a natural language channel of identifiers and comments. In this work, we model the bimodality of code with name lows, an assignment low graph augmented to track identiier names. Conceptual types are logically distinct types that do not always coincide with program types. Passwords and URLs are example conceptual types that can share the program type string. Our tool, RefiNym, is an unsupervised method that mines a lattice of conceptual types from name lows and reiies them into distinct nominal types. For string, RefiNym inds and splits conceptual types originally merged into a single type, reducing the number of same-type variables per scope from 8.7 to 2.2 while eliminating 21.9% of scopes that have more than one same-type variable in scope. This makes the code more self-documenting and frees the type system to prevent a developer from inadvertently assigning data across conceptual types.
