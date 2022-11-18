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
Recent years have seen the successful application of large pre-trained modelsto code representation learning, resulting in substantial improvements on manycode-related downstream tasks. But there are issues surrounding theirapplication to SE tasks. First, the majority of the pre-trained models focus onpre-training only the encoder of the Transformer. For generation tasks that areaddressed using models with the encoder-decoder architecture, however, there isno reason why the decoder should be left out during pre-training. Second, manyexisting pre-trained models, including state-of-the-art models such asT5-learning, simply reuse the pre-training tasks designed for naturallanguages. Moreover, to learn the natural language description of source codeneeded eventually for code-related tasks such as code summarization, existingpre-training tasks require a bilingual corpus composed of source code and theassociated natural language description, which severely limits the amount ofdata for pre-training. To this end, we propose SPT-Code, a sequence-to-sequencepre-trained model for source code. In order to pre-train SPT-Code in asequence-to-sequence manner and address the aforementioned weaknessesassociated with existing pre-training tasks, we introduce three pre-trainingtasks that are specifically designed to enable SPT-Code to learn knowledge ofsource code, the corresponding code structure, as well as a natural languagedescription of the code without relying on any bilingual corpus, and eventuallyexploit these three sources of information when it is applied to downstreamtasks. Experimental results demonstrate that SPT-Code achieves state-of-the-artperformance on five code-related downstream tasks after fine-tuning.
