---
layout: publication
title: "Exploring API Embedding for API Usages and Applications"
authors: Trong Duc Nguyen, Anh Tuan Nguyen, Hung Dang Phan, Tien N. Nguyen
conference: ICSE
year: 2017
tags: ["API", "representation"]
---
Word2Vec is a class of neural network models that
as being trained from a large corpus of texts, they can produce for
each unique word a corresponding vector in a continuous space in
which linguistic contexts of words can be observed. In this work,
we study the characteristics of Word2Vec vectors, called API 2 VEC
or API embeddings, for the API elements within the API sequences in source code. Our empirical study shows that the close
proximity of the API 2 VEC vectors for API elements reflects the
similar usage contexts containing the surrounding APIs of those
API elements. Moreover, API 2 VEC can capture several similar
semantic relations between API elements in API usages via vector
offsets. We demonstrate the usefulness of API 2 VEC vectors for
API elements in three applications. First, we build a tool that mines the pairs of API elements that share the same usage relations
among them. The other applications are in the code migration
domain. We develop API 2 API , a tool to automatically learn the
API mappings between Java and C# using a characteristic of the
API 2 VEC vectors for API elements in the two languages: semantic
relations among API elements in their usages are observed in the
two vector spaces for the two languages as similar geometric
arrangements among their API 2 VEC vectors. Our empirical
evaluation shows that API 2 API relatively improves 22.6% and
40.1% top-1 and top-5 accuracy over a state-of-the-art mining
approach for API mappings. Finally, as another application in
code migration, we are able to migrate equivalent API usages
from Java to C# with up to 90.6% recall and 87.2% precision.
