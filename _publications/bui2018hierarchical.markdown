---
layout: publication
title: "Hierarchical Learning of Cross-Language Mappings through Distributed Vector Representations for Code"
authors: Nghi D. Q. Bui, Lingxiao Jiang
conference: ICSE
year: 2018
additional_links:
   - {name: "PDF", url: "https://arxiv.org/abs/1803.04715"}
   - {name: "code", url: "https://github.com/bdqnghi/hierarchical-programming-language-mapping"}
tags: ["representation"]
---
Translating a program written in one programming language to another can be useful for software development tasks that need functionality implementations in different languages. Although past studies have considered this problem, they may be either specific to the language grammars, or specific to certain kinds of code elements (e.g., tokens, phrases, API uses). This paper proposes a new approach to automatically learn cross-language representations for various kinds of structural code elements that may be used for program translation. Our key idea is two folded: First, we normalize and enrich code token streams with additional structural and semantic information, and train cross-language vector representations for the tokens (a.k.a. shared embeddings based on word2vec, a neural-network-based technique for producing word embeddings; Second, hierarchically from bottom up, we construct shared embeddings for code elements of higher levels of granularity (e.g., expressions, statements, methods) from the embeddings for their constituents, and then build mappings among code elements across languages based on similarities among embeddings. 
Our preliminary evaluations on about 40,000 Java and C# source files from 9 software projects show that our approach can automatically learn shared embeddings for various code elements in different languages and identify their cross-language mappings with reasonable Mean Average Precision scores. When compared with an existing tool for mapping library API methods, our approach identifies many more mappings accurately. The mapping results and code can be accessed at this https URL. We believe that our idea for learning cross-language vector representations with code structural information can be a useful step towards automated program translation.
