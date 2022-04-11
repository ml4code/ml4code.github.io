---
layout: publication
title: "Import2vec - Learning Embeddings for Software Libraries"
authors: Bart Theeten, Frederik Vandeputte, Tom Van Cutsem
conference: MSR
year: 2019
tags: ["representation"]
---
We consider the problem of developing suitable learning representations (embeddings) for library packages that capture semantic similarity among libraries. Such representations are known to improve the performance of downstream learning tasks (e.g. classification) or applications such as contextual search and analogical reasoning.

We apply word embedding techniques from natural language processing (NLP) to train embeddings for library packages ("library vectors"). Library vectors represent libraries by similar context of use as determined by import statements present in source code. Experimental results obtained from training such embeddings on three large open source software corpora reveals that library vectors capture semantically meaningful relationships among software libraries, such as the relationship between frameworks and their plug-ins and libraries commonly used together within ecosystems such as big data infrastructure projects (in Java), front-end and back-end web development frameworks (in JavaScript) and data science toolkits (in Python). 
