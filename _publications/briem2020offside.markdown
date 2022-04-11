---
layout: publication
title: "OffSide: Learning to Identify Mistakes in Boundary Conditions"
authors: Jón Arnar Briem, Jordi Smit, Hendrig Sellik, Pavel Rapoport, Georgios Gousios, Maurício Aniche.
conference: "2nd Workshop on Testing for Deep Learning and Deep Learning for Testing"
year: 2020
additional_links:
   - {name: "Preprint", url: "https://pure.tudelft.nl/portal/files/71196834/deeptest_2020.pdf"}
tags: ["defect"]
---
Mistakes in boundary conditions are the cause of many bugs in software.
These mistakes happen when, e.g., developers make use of `<` or `>` in cases
where they should have used `<=` or `>=`. Mistakes in boundary conditions
are often hard to find and manually detecting them might be very time-consuming
for developers. While researchers have been proposing techniques to cope with
mistakes in the boundaries for a long time, the automated detection of such bugs still
remains a challenge. We conjecture that, for a tool to be able to precisely identify mistakes
in boundary conditions, it should be able to capture the overall context of the source code
under analysis. In this work, we propose a deep learning model that learn mistakes in boundary
conditions and, later, is able to identifythem in unseen code snippets. We train and test a
model on over 1.5 million code snippets, with and without mistakes in different boundary conditions.
Our model shows an accuracy from 55% up to 87%. The model is also able to detect 24 out of 41
real-world bugs;however, with a high false positive rate. The existing state-of-the-practice linter
tools are not able to detect any of the bugs. We hope this paper can pave the road towards deep
learning models that will be able to support developers in detecting mistakes in boundary conditions.
