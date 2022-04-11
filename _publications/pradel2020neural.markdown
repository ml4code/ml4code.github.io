---
layout: publication
title: "Neural Software Analysis"
authors: Michael Pradel, Satish Chandra
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2011.07986"}
tags: ["program analysis", "survey"]
---
Many software development problems can be addressed by program analysis tools, which traditionally are based on precise, logical reasoning and heuristics to ensure that the tools are practical. Recent work has shown tremendous success through an alternative way of creating developer tools, which we call neural software analysis. The key idea is to train a neural machine learning model on numerous code examples, which, once trained, makes predictions about previously unseen code. In contrast to traditional program analysis, neural software analysis naturally handles fuzzy information, such as coding conventions and natural language embedded in code, without relying on manually encoded heuristics. This article gives an overview of neural software analysis, discusses when to (not) use it, and presents three example analyses. The analyses address challenging software development problems: bug detection, type prediction, and code completion. The resulting tools complement and outperform traditional program analyses, and are used in industrial practice. 
