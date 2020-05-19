---
layout: publication
title: "Code and Named Entity Recognition in StackOverflow"
authors: Jeniya Tabassum, Mounica Maddela, Wei Xu, Alan Ritter
conference: ACL
year: 2020
bibkey: tabassum2020code
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.01634"}
tags: ["dataset", "information extraction"]
---
There is an increasing interest in studying natural language and computer code together, as large corpora of programming texts become readily available on the Internet. For example, StackOverflow currently has over 15 million programming related questions written by 8.5 million users. Meanwhile, there is still a lack of fundamental NLP techniques for identifying code tokens or software-related named entities that appear within natural language sentences. In this paper, we introduce a new named entity recognition (NER) corpus for the computer programming domain, consisting of 15,372 sentences annotated with 20 fine-grained entity types. We also present the SoftNER model that combines contextual information with domain specific knowledge using an attention network. The code token recognizer combined with an entity segmentation model we proposed, consistently improves the performance of the named entity tagger. Our proposed SoftNER tagger outperforms the BiLSTM-CRF model with an absolute increase of +9.73 F-1 score on StackOverflow data. 
