---
layout: publication
title: "SAR: Learning Cross-Language API Mappings with Little Knowledge"
authors: N. D. Q. Bui, Y. Yu, L. Jiang
conference: FSE
year: 2019
additional_links:
   - {name: "PDF", url: "https://bdqnghi.github.io/files/FSE_2019.pdf"}
   - {name: "code", url: "https://github.com/bdqnghi/SAR_API_mapping"}
tags: ["representation", "API"]
---
To save manual effort, developers often translate programs from one programming language to another, instead of implementing it from scratch. Translating application program interfaces (APIs) used in one language to functionally equivalent ones available in another language is an important aspect of program translation. Existing approaches facilitate the translation by automatically identifying the API mappings across programming languages. However, all these approaches still require large amount of manual effort in preparing parallel program corpora, ranging from pairs of APIs, to manually identified code in different languages that are considered as functionally equivalent. To minimize the manual effort in identifying parallel program corpora and API mappings, this paper aims at an automated approach to map APIs across languages with much less knowledge a priori needed than other existing approaches. The approach is based on an realization of the notion of domain adaption combined with code embedding, which can better align two vector spaces: taking as input large sets of programs, our approach first generates numeric vector representations of the programs, especially the APIs used in each language, and it adapts generative adversarial networks (GAN) to align the vectors from the spaces of two languages. For a better alignment, we initialize the GAN with parameters derived from optional API mapping seeds that can be identified accurately with a simple automatic signature-based matching heuristic. Then the cross-language API mappings can be identified via nearest-neighbors queries in the aligned vector spaces.
