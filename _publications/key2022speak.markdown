---
layout: publication
title: "I Speak, You Verify: Toward Trustworthy Neural Program Synthesis"
authors: Darren Key, Wen-Ding Li, Kevin Ellis
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2210.00848"}
tags: ["synthesis"]
---
We develop an approach for improving the trustworthiness and overall accuracy of program synthesizers based on large language models for source code. Given a natural language description of a programming problem, our method samples both candidate programs as well as candidate predicates specifying how the program should behave. We learn to analyze the agreement between programs and predicates to judge both which program is most likely to be correct, and also judge whether the language model is able to solve the programming problem in the first place. This latter capacity allows favoring high precision over broad recall: fostering trust by only proposing a program when the system is certain that it is correct.
