---
layout: publication
title: "Exploring the Naturalness of Buggy Code with Recurrent Neural Network"
authors: Jack Lanchantin, Ji Gao
conference: 
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1803.08793"}
tags: ["language model", "defect"]
---
Statistical   language   models   are   powerful   tools
which  have  been  used  for  many  tasks  within  natural language processing. Recently, they have been
used for other sequential data such as source code.
(Ray et al., 2015) showed that it is possible train an
n-gram
source code language mode,  and use it to
predict buggy lines in code by determining “unnatural” lines via entropy with respect to the language
model.  In this work, we propose using a more advanced language modeling technique, Long Short-term Memory recurrent neural networks, to model
source code and classify buggy lines based on entropy.   We  show  that  our  method  slightly  outperforms an
n-gram model in the buggy line classification task using AUC
