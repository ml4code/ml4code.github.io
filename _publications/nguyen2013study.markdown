---
layout: publication
title: "A Study of Repetitiveness of Code Changes in Software Evolution"
authors: Hoan Anh Nguyen, Anh Tuan Nguyen, Tung Thanh Nguyen, Tien N. Nguyen, and Hridesh Rajan
conference: ASE
year: 2013
tags: ["edit"]
---
In this paper, we present a large-scale study of
repetitiveness of code changes in software evolution. We collected
a large data set of 2,841 Java projects, with 1.7 billion source lines
of code (SLOC) at the latest revisions, 1.8 million code change
revisions (0.4 million fixes), 6.2 million changed files, and 2.5
billion changed SLOCs. A change is considered repeated within
or cross-project if it matches another change having occurred
in the history of the project or another project, respectively. We
report the following important findings. First, repetitiveness of
changes could be as high as 70–100% at small sizes and decreases
exponentially as size increases. Second, repetitiveness is higher
and more stable in the cross-project setting than in the project-within one. Third, fixing changes repeat similarly to general
changes. Importantly, learning code changes and recommending
them in software evolution is beneficial with accuracy for top-1
recommendation of over 30% and top-3 of nearly 35%. Repeated
fixing changes could also be useful for automatic program repair.

