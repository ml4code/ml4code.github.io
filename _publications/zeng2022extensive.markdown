---
layout: publication
title: "An Extensive Study on Pre-trained Models for Program Understanding and Generation"
authors: Zhengran Zeng, Hanzhuo Tan, Haotian Zhang, Jing Li, Yuqun Zhang, Lingming Zhang
conference: ISSTA
year: 2022
additional_links:
   - {name: "Author Version", url: "http://lingming.cs.illinois.edu/publications/issta2022.pdf"}
tags: ["Transformer", "evaluation"]
---
Automatic program understanding and generation techniques could
significantly advance the productivity of programmers and have
been widely studied by academia and industry. Recently, the advent of pre-trained paradigm enlightens researchers to develop
general-purpose pre-trained models which can be applied for a
broad range of program understanding and generation tasks. Such
pre-trained models, derived by self-supervised objectives on large
unlabelled corpora, can be fine-tuned in downstream tasks (such
as code search and code generation) with minimal adaptations. Although these pre-trained models claim superiority over the prior
techniques, they seldom follow equivalent evaluation protocols, e.g.,
they are hardly evaluated on the identical benchmarks, tasks, or settings. Consequently, there is a pressing need for a comprehensive
study of the pre-trained models on their effectiveness, versatility
as well as the limitations to provide implications and guidance for
the future development in this area. To this end, we first perform
an extensive study of eight open-access pre-trained models over
a large benchmark on seven representative code tasks to assess
their reproducibility. We further compare the pre-trained models
and domain-specific state-of-the-art techniques for validating pre-trained effectiveness. At last, we investigate the robustness of the
pre-trained models by inspecting their performance variations under adversarial attacks. Through the study, we find that while we
can in general replicate the original performance of the pre-train
models on their evaluated tasks and adopted benchmarks, subtle
performance fluctuations can refute the findings in their original
papers. Moreover, none of the existing pre-trained models can dominate over all other models. We also find that the pre-trained models
can significantly outperform non-pre-trained state-of-the-art techniques in program understanding tasks. Furthermore, we perform
the first study for natural language-programming language pre-trained model robustness via adversarial attacks and find that a
simple random attack approach can easily fool the state-of-the-art
pre-trained models and thus incur security issues. At last, we also
provide multiple practical guidelines for advancing future research
on pre-trained models for program understanding and generation.
