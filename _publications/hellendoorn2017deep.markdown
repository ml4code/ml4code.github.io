---
layout: publication
title: "Are Deep Neural Networks the Best Choice for Modeling Source Code?"
authors: Vincent J. Hellendoorn, Premkumar Devanbu
conference: FSE 
year: 2017
additional_links:
   - {name: "Paper", url: "http://vhellendoorn.github.io/PDF/fse2017.pdf"}
   - {name: "Slides", url: "http://vhellendoorn.github.io/PPT/FSE17Presentation.pptx"}
   - {name: "Code", url: "https://github.com/SLP-Team/SLP-Core"}
tags: ["language model"]
---
Current statistical language modeling techniques, including deep-learning based models, have proven to be quite effective for source
code. We argue here that the special properties of source code can
be exploited for further improvements. In this work, we enhance
established language modeling approaches to handle the special
challenges of modeling source code, such as: frequent changes,
larger, changing vocabularies, deeply nested scopes, etc. We present
a fast, nested language modeling toolkit specifically designed for
software, with the ability to add & remove text, and mix & swap out
many models. Specifically, we improve upon prior cache-modeling
work and present a model with a much more expansive, multi-level
notion of locality that we show to be well-suited for modeling
software. We present results on varying corpora in comparison
with traditional N -gram, as well as RNN, and LSTM deep-learning
language models, and release all our source code for public use.
Our evaluations suggest that carefully adapting N-gram models for
source code can yield performance that surpasses even RNN and
LSTM based deep-learning models.
