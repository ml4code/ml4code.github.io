---
layout: publication
title: "Code to Comment Translation: A Comparative Study on Model Effectiveness & Errors"
authors: Junayed Mahmud, Fahim Faisal, Raihan Islam Arnob, Antonios Anastasopoulos, Kevin Moran
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.1.pdf"}
tags: ["survey", "summarization", "Transformer"]
---
Automated source code summarization is a popular software engineering research topic wherein machine translation models are employed to “translate” code snippets into relevant natural language descriptions. Most evaluations of such models are conducted using automatic reference-based metrics. However, given the relatively large semantic gap between programming languages and natural language, we argue that this line of research would benefit from a qualitative investigation into the various error modes of current state-of-the-art models. Therefore, in this work, we perform both a quantitative and qualitative comparison of three recently proposed source code summarization models. In our quantitative evaluation, we compare the models based on the smoothed BLEU-4, METEOR, and ROUGE-L machine translation metrics, and in our qualitative evaluation, we perform a manual open-coding of the most common errors committed by the models when compared to ground truth captions. Our investigation reveals new insights into the relationship between metric-based performance and model prediction errors grounded in an error taxonomy that can be used to drive future research efforts.
