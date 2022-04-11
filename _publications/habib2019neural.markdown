---
layout: publication
title: "Neural Bug Finding: A Study of Opportunities and Challenges"
authors: Andrew Habib, Michael Pradel
conference: 
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1906.00307"}
tags: ["program analysis"]
---
Static analysis is one of the most widely adopted techniques to find software bugs before code is put in production. Designing and implementing effective and efficient static analyses is difficult and requires high expertise, which results in only a few experts able to write such analyses. This paper explores the opportunities and challenges of an alternative way of creating static bug detectors: neural bug finding. The basic idea is to formulate bug detection as a classification problem, and to address this problem with neural networks trained on examples of buggy and non-buggy code. We systematically study the effectiveness of this approach based on code examples labeled by a state-of-the-art, static bug detector. Our results show that neural bug finding is surprisingly effective for some bug patterns, sometimes reaching a precision and recall of over 80%, but also that it struggles to understand some program properties obvious to a traditional analysis. A qualitative analysis of the results provides insights into why neural bug finders sometimes work and sometimes do not work. We also identify pitfalls in selecting the code examples used to train and validate neural bug finders, and propose an algorithm for selecting effective training data. 
