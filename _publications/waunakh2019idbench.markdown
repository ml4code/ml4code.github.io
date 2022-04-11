---
layout: publication
title: "IdBench: Evaluating Semantic Representations of Identifier Names in Source Code"
authors: Yaza Wainakh, Moiz Rauf, Michael Pradel
conference: ICSE
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.05177"}
tags: ["representation"]
---
Identifier names convey useful information about the intended semantics of code. Name-based program analyses use this information, e.g., to detect bugs, to predict types, and to improve the readability of code. At the core of namebased analyses are semantic representations of identifiers, e.g., in the form of learned embeddings. The high-level goal of such a representation is to encode whether two identifiers, e.g., len and size, are semantically similar. Unfortunately, it is currently unclear to what extent semantic representations match the semantic relatedness and similarity perceived by developers. This paper presents IdBench, the first benchmark for evaluating semantic representations against a ground truth created from thousands of ratings by 500 software developers. We use IdBench to study state-of-the-art embedding techniques proposed for natural language, an embedding technique specifically designed for source code, and lexical string distance functions. Our results show that the effectiveness of semantic representations varies significantly and that the best available embeddings successfully represent semantic relatedness. On the downside, no existing technique provides a satisfactory representation of semantic similarities, among other reasons because identifiers with opposing meanings are incorrectly considered to be similar, which may lead to fatal mistakes, e.g., in a refactoring tool. Studying the strengths and weaknesses of the different techniques shows that they complement each other. As a first step toward exploiting this complementarity, we present an ensemble model that combines existing techniques and that clearly outperforms the best available semantic representation.
