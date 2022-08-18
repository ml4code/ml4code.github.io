---
layout: publication
title: "CoditT5: Pretraining for Source Code and Natural Language Editing"
authors: Jiyang Zhang, Sheena Panthaplackel, Pengyu Nie, Junyi Jessy Li, Milos Gligoric
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2208.05446"}
tags: ["Transformer", "edit"]
---
Pretrained language models have been shown to be effective in many software-related generation tasks; however, they are not well-suited for editing tasks as they are not designed to reason about edits. To address this, we propose a novel pretraining objective which explicitly models edits and use it to build CoditT5, a large language model for software-related editing tasks that is pretrained on large amounts of source code and natural language comments. We fine-tune it on various downstream editing tasks, including comment updating, bug fixing, and automated code review. By outperforming pure generation-based models, we demonstrate the generalizability of our approach and its suitability for editing tasks. We also show how a pure generation model and our edit-based model can complement one another through simple reranking strategies, with which we achieve state-of-the-art performance for the three downstream editing tasks.
