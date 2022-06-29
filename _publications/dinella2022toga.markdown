---
layout: publication
title: "TOGA: A Neural Method for Test Oracle Generation"
authors: Elizabeth Dinella, Gabriel Ryan, Todd Mytkowicz, Shuvendu K. Lahiri
conference: ICSE
year: 2022
additional_links:
   - {name: "Preprint", url: "https://www.seas.upenn.edu/~edinella/icse-camera-ready.pdf"}
tags: ["code generation", "Transformer", "test generation"]
---
Testing is widely recognized as an important stage of the software
development lifecycle. Effective software testing can provide benefits such as bug finding, preventing regressions, and documentation.
In terms of documentation, unit tests express a unit’s intended
functionality, as conceived by the developer. A test oracle, typically expressed as an condition, documents the intended behavior
of a unit under a given test prefix. Synthesizing a functional test
oracle is a challenging problem, as it must capture the intended
functionality rather than the implemented functionality.
In this paper, we propose TOGA (a neural method for Test Oracle
GenerAtion), a unified transformer-based neural approach to infer
both exceptional and assertion test oracles based on the context of
the focal method. Our approach can handle units with ambiguous
or missing documentation, and even units with a missing implementation. We evaluate our approach on both oracle inference accuracy
and functional bug-finding. Our technique improves accuracy by
33% over existing oracle inference approaches, achieving 96% overall accuracy on a held out test dataset. Furthermore, we show that
when integrated with a automated test generation tool (EvoSuite),
our approach finds 57 real world bugs in large-scale Java programs,
including 30 bugs that are not found by any other automated testing
method in our evaluation
