---
layout: publication
title: "Exploring Dimensions of Generalizability and Few-shot Transfer for Text-to-SQL Semantic Parsing"
authors: Rajaswa Patil, Manasi Patwardhan, Shirish Karande, Lovekesh Vig, Gautam Shroff
conference: The 1st Transfer Learning for Natural Language Processing Workshop (TL4NLP 2022)
year: 2022
additional_links:
   - {name: "PDF", url: "https://proceedings.mlr.press/v203/patil23a.html"}
   - {name: "Data", url: "https://github.com/ManasiPat/Spider-Gen"}
tags: ["dataset", "evaluation", "Transformer", "benchmark", "generalizability"]
---
Existing work on generalization in Text-to-SQL semantic parsing has been restricted to a zero-shot cross-domain setting. In this paper, we introduce Spider-Gen: a Text-to-SQL benchmark to develop a paradigm of transfer learning across distinct dimensions of generalization in Text-to-SQL semantic parsing. The Spider-Gen benchmark focuses on few-shot adaption for Cross-domain, Lexical, and Structural generalization of Text-to-SQL models. Through our experiments with the Spider-Gen dataset, we show that Seq2Seq language models struggle to generalize against change in data distribution, lexical changes in database schema, and changes in SQL query complexity. Our experiments also reveal that performing few-shot fine-tuning helps Text-to-SQL models to generalize across these changes. However, such few-shot adaptation comes with a negative effect on the knowledge learnt during training. Hence, we also explore Parameter-efficient Fine-tuning methods to overcome the limitations of Seq2Seq Text-to-SQL models. We release the Spider-Gen dataset publicly to facilitate further research in generalization and transfer learning across various dimensions in Text-to-SQL semantic parsing.
