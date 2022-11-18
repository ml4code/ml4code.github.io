---
layout: publication
title: "SPT-Code: Sequence-to-Sequence Pre-Training for Learning Source Code Representations"
authors: Changan Niu, Chuanyi Li, Vincent Ng, Jidong Ge, Liguo Huang, Bin Luo
conference: ICSE
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2201.01549"}
   - {name: "code", url: "https://github.com/NougatCA/SPT-Code"}
tags: ["Transformer", "representation"]
---
Recent years have seen the successful application of large pre-trained modelsto code representation learning, resulting in substantial improvements on many code-related downstream tasks. But there are issues surrounding theirapplication to SE tasks. First, the majority of the pre-trained models focus on pre-training only the encoder of the Transformer. For generation tasks that are addressed using models with the encoder-decoder architecture, however, there is no reason why the decoder should be left out during pre-training. Second, many existing pre-trained models, including state-of-the-art models such as T5-learning, simply reuse the pre-training tasks designed for natural languages. Moreover, to learn the natural language description of source code needed eventually for code-related tasks such as code summarization, existingpre-training tasks require a bilingual corpus composed of source code and the associated natural language description, which severely limits the amount of data for pre-training. To this end, we propose SPT-Code, a sequence-to-sequence pre-trained model for source code. In order to pre-train SPT-Code in a sequence-to-sequence manner and address the aforementioned weaknesses associated with existing pre-training tasks, we introduce three pre-training tasks that are specifically designed to enable SPT-Code to learn knowledge of source code, the corresponding code structure, as well as a natural language description of the code without relying on any bilingual corpus, and eventually exploit these three sources of information when it is applied to downstreamt asks. Experimental results demonstrate that SPT-Code achieves state-of-the-artperformance on five code-related downstream tasks after fine-tuning.
