---
layout: publication
title: "T5APR: Empowering Automated Program Repair across Languages through Checkpoint Ensemble"
authors: Reza Gharibi, Mohammad Hadi Sadreddini, Seyed Mostafa Fakhrahmad
journal:
year: 2024
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2309.15742"}
  - {name: "Code", url: "https://github.com/h4iku/T5APR"}
tags: ["repair", "Transformer"]
---
Automated program repair (APR) using deep learning techniques has become an important area of research in recent years, aiming to automatically generate bug-fixing patches that can improve software reliability and maintainability. However, most existing methods either target a single language or require high computational resources to train multilingual models. In this paper, we propose T5APR, a novel neural program repair approach that provides a unified solution for bug fixing across multiple programming languages. T5APR leverages CodeT5, a powerful pre-trained text-to-text transformer model, and adopts a checkpoint ensemble strategy to improve patch recommendation. We conduct comprehensive evaluations on six well-known benchmarks in four programming languages (Java, Python, C, JavaScript), demonstrating T5APR's competitiveness against state-of-the-art techniques. T5APR correctly fixes 1,985 bugs, including 1,442 bugs that none of the compared techniques has fixed. We further support the effectiveness of our approach by conducting detailed analyses, such as comparing the correct patch ranking among different techniques. The findings of this study demonstrate the potential of T5APR for use in real-world applications and highlight the importance of multilingual approaches in the field of APR.
