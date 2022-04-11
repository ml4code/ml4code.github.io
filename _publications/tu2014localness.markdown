---
layout: publication
title: "On the Localness of Software"
authors: Zhaopeng Tu, Zhendong Su, Premkumar Devanbu
conference: FSE
year: 2014
tags: ["language model"]
---
The n-gram language model, which has its roots in statistical natural
language processing, has been shown to successfully capture the
repetitive and predictable regularities (“naturalness") of source code,
and help with tasks such as code suggestion, porting, and designing
assistive coding devices. However, we show in this paper that this
natural-language-based model fails to exploit a special property of
source code: localness. We find that human-written programs are
localized: they have useful local regularities that can be captured
and exploited. We introduce a novel cache language model that
consists of both an n-gram and an added “cache" component to
exploit localness. We show empirically that the additional cache
component greatly improves the n-gram approach by capturing
the localness of software, as measured by both cross-entropy and
suggestion accuracy. Our model’s suggestion accuracy is actually
comparable to a state-of-the-art, semantically augmented language
model; but it is simpler and easier to implement. Our cache language
model requires nothing beyond lexicalization, and thus is applicable
to all programming languages.
