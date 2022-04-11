---
layout: publication
title: "Deep API Learning"
authors: Xiaodong Gu, Hongyu Zhang, Dongmei Zhang, Sunghun Kim.
conference: FSE
year: 2016
tags: ["API", "search"]
---
Developers often wonder how to implement a certain functionality (e.g., how to parse XML files) using APIs. Obtaining an API usage sequence based on an API-related natural language query is very helpful in this regard. Given a query, existing approaches utilize information retrieval models to search for matching API sequences. These approaches treat queries and APIs as bag-of-words (i.e., keyword matching or word-to-word alignment) and lack a deep understanding of the semantics of the query.

We propose DeepAPI, a deep learning based approach to generate API usage sequences for a given natural language query. Instead of a bags-of-words assumption, it learns the
sequence of words in a query and the sequence of associated APIs. DeepAPI adapts a neural language model named RNN Encoder-Decoder. It encodes a word sequence (user query) into a fixed-length context vector, and generates an API sequence based on the context vector. We also augment the RNN Encoder-Decoder by considering the importance of individual APIs. We empirically evaluate our approach with more than 7 million annotated code snippets collected from GitHub. The results show that our approach generates largely accurate API sequences and outperforms the related approaches.

