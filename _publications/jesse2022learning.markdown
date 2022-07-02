---
layout: publication
title: "Learning To Predict User-Defined Types"
authors: Kevin Jesse, Premkumar T. Devanbu, Anand Sawant
conference: TSE
year: 2022
tags: ["Transformer", "types"]
---
TypeScript is a widely adopted gradual typed language where developers can optionally type variables, functions, parameters and more. Probabilistic type inference approaches with ML (machine learning) work well especially for commonly occurring types such as boolean, number, and string. TypeScript permits a wide range of types including developer defined class names and type interfaces. These developer defined types, termed user-defined types, can be written within the realm of language naming conventions. The set of user-defined types is boundless and existing bounded type guessing approaches are an imperfect solution. Existing works either under perform in user-defined types or ignore user-defined types altogether. This work leverages a BERT-style pre-trained model, with multi-task learning objectives, to learn how to type user-defined classes and interfaces. Thus we present DIVERSETYPER, a solution that explores the diverse set of user-defined types by uniquely aligning classes and interfaces declarations to the places in which they are used. DIVERSETYPER surpasses all existing works including those that model user-defined types.
