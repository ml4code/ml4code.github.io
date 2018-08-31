---
layout: publication
title: "code2seq: Generating Sequences from Structured Representations of Code"
authors: U. Alon, O. Levy, E. Yahav
conference:
year: 2018
bibkey: alon2018code2seq
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1808.01400"}
---
The ability to generate natural language sequences from source code snippets can be used for code summarization, documentation, and retrieval. Sequence-to-sequence (seq2seq) models, adopted from neural machine translation (NMT), have achieved state-of-the-art performance on these tasks by treating source code as a sequence of tokens. We present CODE2SEQ: an alternative approach that leverages the syntactic structure of programming languages to better encode source code. Our model represents a code snippet as the set of paths in its abstract syntax tree (AST) and uses attention to select the relevant paths during decoding, much like contemporary NMT models. We demonstrate the effectiveness of our approach for two tasks, two programming languages, and four datasets of up to 16M examples. Our model significantly outperforms previous models that were specifically designed for programming languages, as well as general state-of-the-art NMT models.
