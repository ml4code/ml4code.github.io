---
layout: publication
title: "On Multi-Modal Learning of Editing Source Code"
authors: Saikat Chakraborty, Baishakhi Ray
conference: 
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2108.06645"}
tags: ["Transformer", "edit"]
---
In recent years, Neural Machine Translator (NMT) has shown promise in automatically editing source code. Typical NMT based code editor only considers the code that needs to be changed as input and suggests developers with a ranked list of patched code to choose from - where the correct one may not always be at the top of the list. While NMT based code editing systems generate a broad spectrum of plausible patches, the correct one depends on the developers' requirement and often on the context where the patch is applied. Thus, if developers provide some hints, using natural language, or providing patch context, NMT models can benefit from them. As a proof of concept, in this research, we leverage three modalities of information: edit location, edit code context, commit messages (as a proxy of developers' hint in natural language) to automatically generate edits with NMT models. To that end, we build MODIT, a multi-modal NMT based code editing engine. With in-depth investigation and analysis, we show that developers' hint as an input modality can narrow the search space for patches and outperform state-of-the-art models to generate correctly patched code in top-1 position.
