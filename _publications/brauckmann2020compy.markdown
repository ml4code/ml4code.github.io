---
layout: publication
title: "ComPy-Learn: A toolbox for exploring machine learning representations for compilers"
authors: Alexander Brauckmann, Andrés Goens, Jeronimo Castrillon
conference: FDL
year: 2020
additional_links:
   - {name: "IEEE", url: "https://ieeexplore.ieee.org/abstract/document/9232946"}
   - {name: "Code", url: "https://github.com/tud-ccc/compy-learn"}
tags: ["representation", "compilation", "optimization", "GNN"]
---
Deep Learning methods have not only shown to improve software performance in compiler heuristics, but also e.g. to improve security in vulnerability prediction or to boost developer productivity in software engineering tools. A key to the success of such methods across these use cases is the expressiveness of the representation used to abstract from the program code. Recent work has shown that different such representations have unique advantages in terms of performance. However, determining the best-performing one for a given task is often not obvious and requires empirical evaluation.
Therefore, we present ComPy-Learn, a toolbox for conveniently defining, extracting, and exploring representations of program code. With syntax-level language information from the Clang compiler frontend and low-level information from the LLVM compiler backend, the tool supports the construction of linear and graph representations and enables an efficient search for the best-performing representation and model for tasks on program code.
