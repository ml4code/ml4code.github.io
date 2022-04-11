---
layout: publication
title: "Copy that! Editing Sequences by Copying Spans"
authors: Sheena Panthaplackel, Miltiadis Allamanis, Marc Brockschmidt
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2006.04771"}
tags: ["edit"]
---
Neural sequence-to-sequence models are finding increasing use in editing of documents, for example in correcting a text document or repairing source code. In this paper, we argue that common seq2seq models (with a facility to copy single tokens) are not a natural fit for such tasks, as they have to explicitly copy each unchanged token. We present an extension of seq2seq models capable of copying entire spans of the input to the output in one step, greatly reducing the number of decisions required during inference. This extension means that there are now many ways of generating the same output, which we handle by deriving a new objective for training and a variation of beam search for inference that explicitly handle this problem.

In our experiments on a range of editing tasks of natural language and source code, we show that our new model consistently outperforms simpler baselines. 
