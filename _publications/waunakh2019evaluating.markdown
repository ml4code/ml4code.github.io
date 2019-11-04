---
layout: publication
title: "Evaluating Semantic Representations of Source Code"
authors: Y. Wainakh, M. Rauf, M. Pradel
conference:
year: 2019
bibkey: waunakh2019evaluating
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1910.05177"}
tags: ["representation"]
---
Learned representations of source code enable various software developer tools, e.g., to detect bugs or to predict program properties. At the core of code representations often are word embeddings of identifier names in source code, because identifiers account for the majority of source code vocabulary and convey important semantic information. Unfortunately, there currently is no generally accepted way of evaluating the quality of word embeddings of identifiers, and current evaluations are biased toward specific downstream tasks. This paper presents IdBench, the first benchmark for evaluating to what extent word embeddings of identifiers represent semantic relatedness and similarity. The benchmark is based on thousands of ratings gathered by surveying 500 software developers. We use IdBench to evaluate state-of-the-art embedding techniques proposed for natural language, an embedding technique specifically designed for source code, and lexical string distance functions, as these are often used in current developer tools. Our results show that the effectiveness of embeddings varies significantly across different embedding techniques and that the best available embeddings successfully represent semantic relatedness. On the downside, no existing embedding provides a satisfactory representation of semantic similarities, e.g., because embeddings consider identifiers with opposing meanings as similar, which may lead to fatal mistakes in downstream developer tools. IdBench provides a gold standard to guide the development of novel embeddings that address the current limitations. 
