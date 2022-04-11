---
layout: publication
title: "Generating commit messages from diffs using pointer-generator network"
authors: Qin Liu, Zihe Liu, Hongming Zhu, Hongfei Fan, Bowen Du, Yu Qian. 
conference: MSR
year: 2019
tags: ["edit"]
---
The commit messages in source code repositories are valuable but not easy to be generated manually in time for tracking issues, reporting bugs, and understanding codes. Recently published works indicated that the deep neural machine translation approaches have drawn considerable attentions on automatic generation of commit messages. However, they could not deal with out-of-vocabulary (OOV) words, which are essential context-specific identifiers such as class names and method names in code diffs. In this paper, we propose PtrGNCMsg, a novel approach which is based on an improved sequence-to-sequence model with the pointer-generator network to translate code diffs into commit messages. By searching the smallest identifier set with the highest probability, PtrGNCMsg outperforms recent approaches based on neural machine translation, and first enables the prediction of OOV words. The experimental results based on the corpus of diffs and manual commit messages from the top 2,000 Java projects in GitHub show that PtrGNCMsg outperforms the state-of-the-art approach with improved BLEU by 1.02, ROUGE-1 by 4.00 and ROUGE-L by 3.78, respectively.
