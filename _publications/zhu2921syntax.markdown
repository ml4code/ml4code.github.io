---
layout: publication
title: "A Syntax-Guided Edit Decoder for Neural Program Repair"
authors: Qihao Zhu, Zeyu Sun, Yuan-an Xiao, Wenjie Zhang, Kang Yuan, Yingfei Xiong, Lu Zhang
conference: FSE
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2106.08253"}
tags: ["edit"]
---
Automated Program Repair (APR) helps improve the efficiency of software development and maintenance. Recent APR techniques use deep learning, particularly the encoder-decoder architecture, to generate patches.
Though existing DL-based APR approaches have proposed different encoder architectures, the decoder remains to be the standard one, which generates a sequence of tokens one by one to replace the faulty statement.
This decoder has multiple limitations: 1) allowing to generate syntactically incorrect programs, 2) inefficiently representing small edits, and 3) not being able to generate project-specific identifiers.
In this paper, we propose Recoder, a syntax-guided edit decoder with placeholder generation. Recoder is novel in multiple aspects: 1) Recoder generates edits rather than modified code, allowing efficient representation of small edits; 2) Recoder is syntax-guided, with the novel provider/decider architecture to ensure the syntactic correctness of the patched program and accurate generation; 3) Recoder generates placeholders that could be instantiated as project-specific identifiers later.
We conduct experiments to evaluate Recoder on 395 bugs from Defects4J v1.2, 420 additional bugs from Defects4J v2.0, 297 bugs from IntroClassJava and 40 bugs from QuixBugs. Our results show that Recoder repairs 53 bugs on Defects4J v1.2, which achieves 26.2% (11 bugs) improvement over the previous state-of-the-art approach for single-hunk bugs (TBar). Importantly, to our knowledge, Recoder is the first DL-based APR approach that has outperformed the traditional APR approaches on this benchmark. 
