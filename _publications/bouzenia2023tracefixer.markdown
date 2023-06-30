---
layout: publication
title: "TraceFixer: Execution Trace-Driven Program Repair"
authors: Islem Bouzenia, Yangruibo Ding, Kexin Pei, Baishakhi Ray, Michael Pradel
conference:
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2304.12743"}
tags: ["Transformer", "repair", "dynamic"]
---
When debugging unintended program behavior, developers can often identify the point in the execution where the actual behavior diverges from the desired behavior. For example, a variable may get assigned a wrong value, which then negatively influences the remaining computation. Once a developer identifies such a divergence, how to fix the code so that it provides the desired behavior? This paper presents TraceFixer, a technique for predicting how to edit source code so that it does not diverge from the expected behavior anymore. The key idea is to train a neural program repair model that not only learns from source code edits but also exploits excerpts of runtime traces. The input to the model is a partial execution trace of the incorrect code, which can be obtained automatically through code instrumentation, and the correct state that the program should reach at the divergence point, which the user provides, e.g., in an interactive debugger. Our approach fundamentally differs from current program repair techniques, which share a similar goal but exploit neither execution traces nor information about the desired program state. We evaluate TraceFixer on single-line mistakes in Python code. After training the model on hundreds of thousands of code edits created by a neural model that mimics real-world bugs, we find that exploiting execution traces improves the bug-fixing ability by 13% to 20% (depending on the dataset, within the top-10 predictions) compared to a baseline that learns from source code edits only. Applying TraceFixer to 20 real-world Python bugs shows that the approach successfully fixes 10 of them.
