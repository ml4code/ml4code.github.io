---
layout: publication
title: "DLFix: Context-based Code Transformation Learning for Automated Program Repair"
authors: Yi Li, Shaohua Wang, Tien N. Nguyen
conference: ICSE
year: 2020
tags: ["edit", "repair", "grammar"]
---
Automated Program Repair (APR) is very useful in helping developers in the process of software development and maintenance. Despite recent advances in deep learning (DL), the DL-based APR approaches still have limitations in learning bug-fixing code changes and the context of the surrounding source code of the bug-fixing code changes. These limitations lead to incorrect fixing locations or fixes. In this paper, we introduce DLFix, a two-tier DL model that treats APR as code transformation learning from the prior bug fixes and the surrounding code contexts of the fixes. The first layer is a tree-based RNN model that learns the contexts of bug fixes and its result is used as an additional weighting input for the second layer designed to learn the bug-fixing code transformations. 

We conducted several experiments to evaluate DLFix in two benchmarks: Defect4J and Bugs.jar, and a newly built bug datasets with a total of +20K real-world bugs in eight projects. We compared DLFix against a total of 13 state-of-the-art pattern-based APR tools. Our results show that DLFix can auto-fix more bugs than 11 of them, and is comparable and complementary to the top two pattern-based APR tools in which there are 7 and 11 unique bugs that they cannot detect, respectively, but we can. Importantly, DLFix is fully automated and data-driven, and does not require hard-coding of bug-fixing patterns as in those tools. We compared DLFix against 4 state-of-the-art deep learning based APR models. DLFix is able to fix 2.5 times more bugs than the best performing~baseline.
