---
layout: publication
title: "DeepMerge: Learning to Merge Programs"
authors: Elizabeth Dinella, Todd Mytkowicz, Alexey Svyatkovskiy, Christian Bird, Mayur Naik, Shuvendu K. Lahiri
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2105.07569"}
tags: ["edit", "repair"]
---
Program merging is ubiquitous in modern software development. Although commonly used in most version control systems, text-based merge algorithms are prone to producing spurious merge conflicts: they report a conflict even when program changes do not interfere with each other semantically. Spurious merge conflicts are costly to development as the need for manual intervention stalls modern continuous integration pipelines. We propose a novel data-driven approach to identify and resolve spurious merge conflicts with a sequence-to-sequence machine learning model. We realize our approach in a tool DeepMerge that uses a novel combination of (i) an edit-aware embedding of merge inputs and (ii) a variation of pointer networks to construct resolutions from input segments. We also propose an algorithm to extract ground truth manual resolutions from a code corpus and employ it to curate a dataset comprising 10,729 non-trivial resolutions in Javascript programs. Our evaluation shows that DeepMerge can predict correct resolutions with high precision (72%) and modest recall (34%) on the dataset overall, and high recall (78%) on merges comprising of upto 3 lines that comprise 24% of the dataset. 
