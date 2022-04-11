---
layout: publication
title: "Topic modeling of public repositories at scale using names in source code"
authors: Vadim Markovtsev, Eiso Kant
conference:
year: 2017
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1704.00135"}
   - {name: "website", url: "https://blog.sourced.tech/post/github_topic_modeling"}
   - {name: "code", url: "https://github.com/src-d/ast2vec/blob/master/topic_modeling.md"}
tags: ["topic modeling", "pattern mining"]
---
 Programming languages themselves have a limited number of reserved keywords and character based tokens that
define the language specification. However, programmers have a rich use of natural language within their code
through comments, text literals and naming entities. The programmer defined names that can be found in source
code are a rich source of information to build a high level understanding of the project. The goal of this paper
is to apply topic modeling to names used in over 13.6 million repositories and perceive the inferred topics.
One of the problems in such a study is the occurrence of duplicate repositories not officially marked as forks (obscure forks).
We show how to address it using the same identifiers which are extracted for topic modeling.

We open with a discussion on naming in source code, we then elaborate on our approach to remove exact duplicate
and fuzzy duplicate repositories using Locality Sensitive Hashing on the bag-of-words model and then discuss our work
on topic modeling; and finally present the results from our data analysis together with open-access to the source code,
tools and datasets.
