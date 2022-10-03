---
layout: publication
title: "Do We Need Another Explainable AI Method? Toward Unifying Post-hoc XAI Evaluation Methods into an Interactive and Multi-dimensional Benchmark"
authors: Belaid, Mohamed Karim and Hullermeier, Eyke and Rabus, Maximilian and Krestel, Ralf
conference: 
year: 2022
additional_links: 
    - {name: "ArXiv", url: "https://arxiv.org/pdf/2207.14160.pdf"}
tags: [benchmark, explainable ai]
---
In recent years, Explainable AI (xAI) attracted a lot of attention as various countries
turned explanations into a legal right. xAI allows for improving models beyond
the accuracy metric by, e.g., debugging the learned pattern and demystifying
the AI’s behavior. The widespread use of xAI brought new challenges. On the
one hand, the number of published xAI algorithms underwent a boom, and it
became difficult for practitioners to select the right tool. On the other hand, some
experiments did highlight how easy data scientists could misuse xAI algorithms
and misinterpret their results. To tackle the issue of comparing and correctly using
feature importance xAI algorithms, we propose Compare-xAI, a benchmark that
unifies all exclusive and unitary evaluation methods applied to xAI algorithms. We
propose a selection protocol to shortlist non-redundant unit tests from the literature,
i.e., each targeting a specific problem in explaining a model. The benchmark
encapsulates the complexity of evaluating xAI methods into a hierarchical scoring
of three levels, namely, targeting three end-user groups: researchers, practitioners,
and laymen in xAI. The most detailed level provides one score per unit test. The
second level regroups tests into five categories (fidelity, fragility, stability, simplicity,
and stress tests). The last level is the aggregated comprehensibility score, which
encapsulates the ease of correctly interpreting the algorithm’s output in one easy
to compare value. Compare-xAI’s interactive user interface helps mitigate errors
in interpreting xAI results by quickly listing the recommended xAI solutions for
each ML task and their current limitations. The benchmark is made available at
https://karim-53.github.io/cxai/
