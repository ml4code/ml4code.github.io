---
layout: publication
title: "Function Assistant: A Tool for NL Querying of APIs"
authors: Kyle Richardson, Jonas Kuhn
conference: EMNLP
year: 2017
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1706.00468"}
tags: ["bimodal", "API"]
---
In this paper, we describe Function Assistant, a lightweight Python-based toolkit for querying and exploring source code repositories using natural language. The toolkit is designed to help end-users of a target API quickly find information about functions through high-level natural language queries and descriptions. For a given text query and background API, the tool finds candidate functions by performing a translation from the text to known representations in the API using the semantic parsing approach of Richardson and Kuhn (2017). Translations are automatically learned from example text-code pairs in example APIs. The toolkit includes features for building translation pipelines and query engines for arbitrary source code projects. To explore this last feature, we perform new experiments on 27 well-known Python projects hosted on Github.
