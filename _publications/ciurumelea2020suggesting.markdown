---
layout: publication
title: "Suggesting Comment Completions for Python using Neural Language Models"
authors: Adelina Ciurumelea; Sebastian Proksch; Harald C. Gall
conference: SANER
year: 2020
additional_links:
   - {name: "IEEE Xplore", url: "https://ieeexplore.ieee.org/abstract/document/9054866"}
tags: ["bimodal", "autocomplete", "documentation"]
---
Source-code comments are an important communication medium between developers to better understand and maintain software. Current research focuses on auto-generating comments by summarizing the code. However, good comments contain additional details, like important design decisions or required trade-offs, and only developers can decide on the proper comment content. Automated summarization techniques cannot include information that does not exist in the code, therefore fully-automated approaches while helpful, will be of limited use. In our work, we propose to empower developers through a semi-automated system instead. We investigate the feasibility of using neural language models trained on a large corpus of Python documentation strings to generate completion suggestions and obtain promising results. By focusing on confident predictions, we can obtain a top-3 accuracy of over 70%, although this comes at the cost of lower suggestion frequency. Our models can be improved by leveraging context information like the signature and the full body of the method. Additionally, we are able to return good accuracy completions even for new projects, suggesting the generalizability of our approach.
