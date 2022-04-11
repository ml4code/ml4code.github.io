---
layout: publication
title: Suggesting Accurate Method and Class Names
authors: Miltiadis Allamanis, Earl T. Barr, Christian Bird, Charles Sutton
conference: FSE
year: 2015
additional_links:
   - {name: "PDF", url: "http://homepages.inf.ed.ac.uk/csutton/publications/accurate-method-and-class.pdf"}
   - {name: "website", url: "http://groups.inf.ed.ac.uk/cup/naturalize"}
tags: ["naming"]
---
Descriptive names are a vital part of readable, and hence maintainable, code. Recent progress on automatically suggesting names for local variables tantalizes with the prospect of replicating that success with method and class names.  However, suggesting names for methods and classes is much more difficult. This is because good method and class names need to be functionally descriptive, but suggesting such names requires that the model goes beyond local context. We introduce a neural probabilistic language model for source code that is specifically designed for the method naming problem. Our model learns which names are semantically similar by assigning them to locations, called embeddings, in a high-dimensional continuous space, in such a way that names with similar embeddings tend to be used in similar contexts. These embeddings seem to contain semantic information about tokens, even though they are learned only from statistical co-occurrences of tokens.  Furthermore, we introduce a variant of our model
that is, to our knowledge, the first that can propose neologisms, names that have not appeared in the training corpus. We obtain state of the art results on the method, class, and even the simpler variable naming tasks. More broadly, the continuous embeddings that are learned by our model have the potential for wide application within software engineering.

