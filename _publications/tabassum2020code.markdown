---
layout: publication
title: "Code and Named Entity Recognition in StackOverflow"
authors: Jeniya Tabassum, Mounica Maddela, Wei Xu, Alan Ritter
conference: ACL
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.01634"}
   - {name: "Code", url: "https://github.com/jeniyat/StackOverflowNER/"}
tags: ["dataset", "information extraction"]
---
There is an increasing interest in studying natural language and computer code together, as large corpora of programming texts become readily available on the Internet. For example, StackOverflow currently has over 15 million programming related questions written by 8.5 million users. Meanwhile, there is still a lack of fundamental NLP techniques for identifying code tokens or software-related named entities that appear within natural language sentences. In this paper, we introduce a new named entity recognition (NER) corpus for the computer programming domain, consisting of 15,372 sentences annotated with 20 fine-grained entity types. We trained in-domain BERT representations (BERTOverflow) on 152 million sentences from StackOverflow, which lead to an absolute increase of +10 F-1 score over off-the-shelf BERT. We also present the SoftNER model which achieves an overall 79.10 F1 score for code and named entity recognition on StackOverflow data. Our SoftNER model incorporates a context-independent code token classifier with corpus-level features to improve the BERT-based tagging model. 
