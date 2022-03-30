---
layout: publication
title: "Big Code != Big Vocabulary: Open-Vocabulary Models for Source Code"
authors: Rafael-Michael Karampatsis, Hlib Babii, Romain Robbes Charles Sutton, Andrea Janes
conference: ICSE
year: 2020
bibkey: karampatsis2020
additional_links:
   - {name: "Link", url: "https://research.google/pubs/pub48933/"}
tags: ["language model"]
---
Statistical language modeling techniques have successfully been applied to large source code corpora, yielding a variety of new software development tools, such as tools for code suggestion, improving readability, and API migration. A major issue with these techniques is that code introduces new vocabulary at a far higher rate than natural language, as new identifier names proliferate. Both large vocabularies and out-of-vocabulary issues severely affect Neural Language Models (NLMs) of source code, degrading their performance and rendering them unable to scale. In this paper, we address this issue by: 1) studying how various modelling choices impact the resulting vocabulary on a large-scale corpus of 13,362 projects; 2) presenting an open vocabulary source code NLM that can scale to such a corpus, 100 times larger than in previous work; and 3) showing that such models outperform the state of the art on three distinct code corpora (Java, C, Python). To our knowledge, these are the largest NLMs for code that have been reported.
