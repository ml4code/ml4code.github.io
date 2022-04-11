---
layout: publication
title: "Generating Bug-Fixes Using Pretrained Transformers"
authors: Dawn Drain, Chen Wu, Alexey Svyatkovskiy, Neel Sundaresan
conference: 
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2104.07896"}
tags: ["Transformer", "repair"]
---
Detecting and fixing bugs are two of the most important yet frustrating parts of the software development cycle. Existing bug detection tools are based mainly on static analyzers, which rely on mathematical logic and symbolic reasoning about the program execution to detect common types of bugs. Fixing bugs is typically left out to the developer. In this work we introduce DeepDebug: a data-driven program repair approach which learns to detect and fix bugs in Java methods mined from real-world GitHub repositories. We frame bug-patching as a sequence-to-sequence learning task consisting of two steps: (i) denoising pretraining, and (ii) supervised finetuning on the target translation task. We show that pretraining on source code programs improves the number of patches found by 33% as compared to supervised training from scratch, while domain-adaptive pretraining from natural language to code further improves the accuracy by another 32%. We refine the standard accuracy evaluation metric into non-deletion and deletion-only fixes, and show that our best model generates 75% more non-deletion fixes than the previous state of the art. In contrast to prior work, we attain our best results when generating raw code, as opposed to working with abstracted code that tends to only benefit smaller capacity models. Finally, we observe a subtle improvement from adding syntax embeddings along with the standard positional embeddings, as well as with adding an auxiliary task to predict each token's syntactic class. Despite focusing on Java, our approach is language agnostic, requiring only a general-purpose parser such as tree-sitter. 
