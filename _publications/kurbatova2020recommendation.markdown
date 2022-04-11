---
layout: publication
title: "Recommendation of Move Method Refactoring Using Path-Based Representation of Code"
authors: Zarina Kurbatova, Ivan Veselov, Yaroslav Golubev, Timofey Bryksin
conference:
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2002.06392"}
tags: ["refactoring"]
---
Software refactoring plays an important role in increasing code quality. One of the most popular refactoring types is the Move Method refactoring. It is usually applied when a method depends more on members of other classes than on its own original class. Several approaches have been proposed to recommend Move Method refactoring automatically. Most of them are based on heuristics and have certain limitations (e.g., they depend on the selection of metrics and manually-defined thresholds). In this paper, we propose an approach to recommend Move Method refactoring based on a path-based representation of code called code2vec that is able to capture the syntactic structure and semantic information of a code fragment. We use this code representation to train a machine learning classifier suggesting to move methods to more appropriate classes. We evaluate the approach on two publicly available datasets: a manually compiled dataset of well-known open-source projects and a synthetic dataset with automatically injected code smell instances. The results show that our approach is capable of recommending accurate refactoring opportunities and outperforms JDeodorant and JMove, which are state of the art tools in this field.
