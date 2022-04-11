---
layout: publication
title: "Fix-Filter-Fix: Intuitively Connect Any Models for Effective Bug Fixing"
authors: Haiwen Hong, Jingfeng Zhang, Yin Zhang, Yao Wan, Yulei Sui
conference: EMNLP
year: 2021
additional_links:
   - {name: "Proceedings", url: "https://aclanthology.org/2021.emnlp-main.282/"}
tags: ["repair"]
---
Locating and fixing bugs is a time-consuming task. Most neural machine translation (NMT) based approaches for automatically bug fixing lack generality and do not make full use of the rich information in the source code. In NMT-based bug fixing, we find some predicted code identical to the input buggy code (called unchanged fix) in NMT-based approaches due to high similarity between buggy and fixed code (e.g., the difference may only appear in one particular line). Obviously, unchanged fix is not the correct fix because it is the same as the buggy code that needs to be fixed. Based on these, we propose an intuitive yet effective general framework (called Fix-Filter-Fix or Fˆ3) for bug fixing. Fˆ3 connects models with our filter mechanism to filter out the last model’s unchanged fix to the next. We propose an Fˆ3 theory that can quantitatively and accurately calculate the Fˆ3 lifting effect. To evaluate, we implement the Seq2Seq Transformer (ST) and the AST2Seq Transformer (AT) to form some basic Fˆ3 instances, called Fˆ3_ST+AT and Fˆ3_AT+ST. Comparing them with single model approaches and many model connection baselines across four datasets validates the effectiveness and generality of Fˆ3 and corroborates our findings and methodology.