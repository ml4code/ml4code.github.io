---
layout: publication
title: "Autofolding for Source Code Summarization"
authors: Jaroslav Fowkes, Razan Ranca, Miltiadis Allamanis, Mirella Lapata, Charles Sutton
conference: TSE
year: 2017
tags: ["summarization"]
---
Developers spend much of their time reading and browsing source code, raising new opportunities for summarization methods. Indeed, modern code editors provide code folding, which allows one to selectively hide blocks of code. However this is impractical to use as folding decisions must be made manually or based on simple rules. We introduce the
autofolding problem, which is to automatically create a code summary by folding less informative code regions. We present a novel solution by formulating the problem as a sequence of AST folding decisions, leveraging a scoped topic model for code tokens. On an annotated set of popular open source projects, we show that our summarizer outperforms simpler baselines, yielding a 28% error reduction. Furthermore, we find through a case study that our summarizer is strongly preferred by experienced developers. More broadly, we hope this work will aid program comprehension by turning code folding into a usable and valuable tool.
