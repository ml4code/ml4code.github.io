---
layout: publication
title: "CODIT: Code Editing with Tree-Based Neural Machine Translation"
authors: Saikat Chakraborty, Miltiadis Allamanis, Baishakhi Ray
conference: 
year: 2018
additional_links:
- {name: "ArXiV", url: "https://arxiv.org/abs/1810.00314"}
tags: ["grammar", "grammar", "repair", "code generation"]
---
The way developers edit day-to-day code tends to be repetitive, often using existing code elements. Many researchers have tried to automate repetitive code changes by learning from specific change templates which are applied to limited scope. The advancement of Neural Machine Translation (NMT) and the availability of vast open-source evolutionary data opens up the possibility of automatically learning those templates from the wild. However, unlike natural languages, for which NMT techniques were originally devised, source code and its changes have certain properties. For instance, compared to natural language, source code vocabulary can be significantly larger. Further, good changes in code do not break its syntactic structure. Thus, deploying state-of-the-art NMT models without adapting the methods to the source code domain yields sub-optimal results. To this end, we propose a novel Tree based NMT system to model source code changes and learn code change patterns from the wild. We realize our model with a change suggestion engine: CODIT and train the model with more than 30k real-world changes and evaluate it on 6k patches. Our evaluation shows the effectiveness of CODIT in learning and suggesting patches.CODIT also shows promise generating bug fix patches. 
