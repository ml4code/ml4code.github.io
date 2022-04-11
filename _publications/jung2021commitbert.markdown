---
layout: publication
title: "CommitBERT: Commit Message Generation Using Pre-Trained Programming Language Model"
authors: Tae Hwan Jung
conference: NLP4Prog
year: 2021
additional_links:
   - {name: "PDF", url: "https://aclanthology.org/2021.nlp4prog-1.3.pdf"}
tags: ["dataset", "language model", "Transformer"]
---
Commit message is a document that summarizes source code changes in natural language. A good commit message clearly shows the source code changes, so this enhances collaboration between developers. Therefore, our work is to develop a model that automatically writes the commit message. To this end, we release 345K datasets consisting of code modification and commit messages in six programming languages (Python, PHP, Go, Java, JavaScript, and Ruby). Similar to the neural machine translation (NMT) model, using our dataset, we feed the code modification to the encoder input and the commit message to the decoder input and measure the result of the generated commit message with BLEU-4. Also, we propose the following two training methods to improve the result of generating the commit message: (1) A method of preprocessing the input to feed the code modification to the encoder input. (2) A method that uses an initial weight suitable for the code domain to reduce the gap in contextual representation between programming language (PL) and natural language (NL).
