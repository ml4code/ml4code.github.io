---
layout: publication
title: "Where should I comment my code? A dataset and model for predicting locations that need comments"
authors: Annie Louis, Santanu Kumar Dash, Earl T. Barr, Charles Sutton
conference: International Conference on Software Engineering (ICSE; NIER track)
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1806.04616"}
   - {name: "Data", url: "http://groups.inf.ed.ac.uk/cup/comment-locator"}
tags: ["bimodal", "documentation"]
---
Programmers should write code comments, but not on every line
of code. We have created a machine learning model that suggests
locations where a programmer should write a code comment. We
trained it on existing commented code to learn locations that are
chosen by developers. Once trained, the model can predict locations
in new code. Our models achieved precision of 74% and recall of
13% in identifying comment-worthy locations. This first success
opens the door to future work, both in the new where-to-comment
problem and in guiding comment generation.