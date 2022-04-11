---
layout: publication
title: "OptTyper: Probabilistic Type Inference by Optimising Logical and Natural Constraints"
authors: Irene Vlassi Pandi, Earl T. Barr, Andrew D. Gordon, Charles Sutton
conference: 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.00348"}
tags: ["types", "bimodal"]
---
We present a new approach to the type inference problem for dynamic languages. Our goal is to combine logical constraints, that is, deterministic information from a type system, with natural constraints, uncertain information about types from sources like identifier names. To this end, we introduce a framework for probabilistic type inference that combines logic and learning: logical constraints on the types are extracted from the program, and deep learning is applied to predict types from surface-level code properties that are statistically associated, such as variable names. The main insight of our method is to constrain the predictions from the learning procedure to respect the logical constraints, which we achieve by relaxing the logical inference problem of type prediction into a continuous optimisation problem. To evaluate the idea, we built a tool called OptTyper to predict a TypeScript declaration file for a JavaScript library. OptTyper combines a continuous interpretation of logical constraints derived by a simple program transformation and static analysis of the JavaScript code, with natural constraints obtained from a deep learning model, which learns naming conventions for types from a large codebase. We evaluate OptTyper on a data set of 5,800 open-source JavaScript projects that have type annotations in the well-known DefinitelyTyped repository. We find that combining logical and natural constraints yields a large improvement in performance over either kind of information individually, and produces 50% fewer incorrect type predictions than previous approaches. 
