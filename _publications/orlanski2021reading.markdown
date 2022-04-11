---
layout: publication
title: "Reading StackOverflow Encourages Cheating: Adding Question Text Improves Extractive Code Generation"
authors: Gabriel Orlanski, Alex Gittens
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.8.pdf"}
tags: ["dataset", "Transformer"]
---
Answering a programming question with only its title is difficult as salient contextual information is left out. To address this, we present a corpus of over 40,000 StackOverflow question texts to be used in conjunction with the corresponding intents from the CoNaLa dataset (Yin et al., 2018). Using both the intent and the question body, we use BART to establish a baseline BLEU score of 34.35 for this new task. We then find further improvements of 2.8% by combining the mined CoNaLa data with the labeled data to achieve a 35.32 BLEU score. We then evaluate the prior state-of-the-art CoNaLa models with this additional data. We find that our proposed method of using the body and mined data beats that of the previous state-of-the-art by a 71.96% BLEU score. Finally, we perform ablations that prove that BART is an unsupervised multimodal learner and examine its extractive behavior.
