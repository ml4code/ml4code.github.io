---
layout: publication
title: "CodeBERTScore: Evaluating Code Generation with Pretrained Models of Code"
authors: Shuyan Zhou, Uri Alon, Sumit Agarwal, Graham Neubig
conference:
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2302.05527"}
   - {name: "Code", url: "https://github.com/neulab/code-bert-score"}
tags: ["evaluation", "Transformer"]
---
Since the rise of neural models of code that can generate long expressions and statements rather than a single next-token, one of the major problems has been reliably evaluating their generated output. In this paper, we propose CodeBERTScore: an automatic evaluation metric for code generation, which builds on BERTScore (Zhang et al., 2020). Instead of measuring exact token matching as BLEU, CodeBERTScore computes a soft similarity score between each token in the generated code and in the reference code, using the contextual encodings of large pretrained models. Further, instead of encoding only the generated tokens as in BERTScore, CodeBERTScore also encodes the programmatic context surrounding the generated code. We perform an extensive evaluation of CodeBERTScore across four programming languages. We find that CodeBERTScore achieves a higher correlation with human preference and with functional correctness than all existing metrics. That is, generated code that receives a higher score by CodeBERTScore is more likely to be preferred by humans, as well as to function correctly when executed. Finally, while CodeBERTScore can be used with a multilingual CodeBERT as its base model, we release five language-specific pretrained models to use with our publicly available code at https://github.com/neulab/code-bert-score . Our language-specific models have been downloaded more than 25,000 times from the Huggingface Hub.
