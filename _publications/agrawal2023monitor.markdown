---
layout: publication
title: Monitor-Guided Decoding of Code LMs with Static Analysis of Repository Context
authors: Lakshya A Agrawal, Aditya Kanade, Navin Goyal, Shuvendu K Lahiri, Sriram Rajamani
conference: NeurIPS
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2306.10763"}
   - {name: "NeurIPS website", url: "https://neurips.cc/virtual/2023/poster/70362"}
   - {name: "code", url: "https://github.com/microsoft/monitors4codegen"}
tags: ["autocomplete", "benchmark", "code completion", "code generation", "compilation", "completion", "dataset", "evaluation", "language model", "large language models", "program analysis", "static analysis", "tool"]
---
Language models of code (LMs) work well when the surrounding code provides sufficient context. This is not true when it becomes necessary to use types, functionality or APIs defined elsewhere in the repository or a linked library, especially those not seen during training. LMs suffer from limited awareness of such global context and end up hallucinating.

Integrated development environments (IDEs) assist developers in understanding repository context using static analysis. We extend this assistance, enjoyed by developers, to LMs. We propose monitor-guided decoding (MGD) where a monitor uses static analysis to guide the decoding. We construct a repository-level dataset PragmaticCode for method-completion in Java and evaluate MGD on it. On models of varying parameter scale, by monitoring for type-consistent object dereferences, MGD consistently improves compilation rates and agreement with ground truth. Further, LMs with fewer parameters, when augmented with MGD, can outperform larger LMs. With MGD, SantaCoder-1.1B achieves better compilation rate and next-identifier match than the much larger text-davinci-003 model.

We also conduct a generalizability study to evaluate the ability of MGD to generalize to multiple programming languages (Java, C# and Rust), coding scenarios (e.g., correct number of arguments to method calls), and to enforce richer semantic constraints (e.g., stateful API protocols). Our data and implementation are available at https://github.com/microsoft/monitors4codegen.
