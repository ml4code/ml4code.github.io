---
layout: publication
title: "Improved Automatic Summarization of Subroutines via Attention to File Context"
authors: Sakib Haque, Alexander LeClair, Lingfei Wu, Collin McMillan
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.04881"}
tags: ["summarization"]
---
Software documentation largely consists of short, natural language summaries of the subroutines in the software. These summaries help programmers quickly understand what a subroutine does without having to read the source code him or herself. The task of writing these descriptions is called "source code summarization" and has been a target of research for several years. Recently, AI-based approaches have superseded older, heuristic-based approaches. Yet, to date these AI-based approaches assume that all the content needed to predict summaries is inside subroutine itself. This assumption limits performance because many subroutines cannot be understood without surrounding context. In this paper, we present an approach that models the file context of subroutines (i.e. other subroutines in the same file) and uses an attention mechanism to find words and concepts to use in summaries. We show in an experiment that our approach extends and improves several recent baselines. 
