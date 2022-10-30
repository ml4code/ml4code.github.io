---
layout: publication
title: "The Stack: 3TB of permissively licensed source code"
authors: Denis Kocetkov, Raymond Li, Loubna Ben Allal, Jia Li, Chenghao Mou, Carlos Muñoz Ferrandis, Sean Hughes, Thomas Wolf, Dzmitry Bahdanau, Leandro von Werra, Harm de Vries
conference:
year: 2022
additional_links:
   - {name: "Preprint", url: "https://drive.google.com/file/d/17J-0KXTDzY9Esp-JqXYHIcy--i_7G5Bb/view"}
tags: ["dataset"]
---
Large Language Models (LLMs) play an ever-increasing role in the field of
Artificial Intelligence (AI)–not only for natural language processing but also
for code understanding and generation. To stimulate open and responsible
research on LLMs for code, we introduce The Stack, a 3.1 TB dataset
consisting of permissively licensed source code in 30 programming languages.
We describe how we collect the full dataset, construct a permissively licensed
subset, and present promising results on text2code benchmarks by training 350M-parameter decoders on different Python subsets. We find that
(1) near-deduplicating the data significantly boosts performance across all
experiments, and (2) it is possible to match previously reported HumanEval
and MBPP performance using only permissively licensed data. We make the
dataset available at https://hf.co/BigCode and give developers the possi-
bility to have their code removed from the dataset by following the instruc-
tions at https://www.bigcode-project.org/docs/about/the-stack/.
