---
layout: publication
title: "Neural Program Generation Modulo Static Analysis"
authors: Rohan Mukherjee, Yeming Wen, Dipak Chaudhari, Thomas W. Reps, Swarat Chaudhuri, Chris Jermaine
conference: NeurIPS
year: 2021
additional_links:
   - {name: "Preprint", url: "https://www.cs.utexas.edu/~swarat/pubs/neurips21-nsg.pdf"}
tags: ["synthesis", "language model"]
---
State-of-the-art neural models of source code tend to be evaluated on the generation
of individual expressions and lines of code, and commonly fail on long-horizon
tasks such as the generation of entire method bodies. We propose to address this
deficiency using weak supervision from a static program analyzer. Our neurosymbolic method allows a deep generative model to symbolically compute, using calls
to a static-analysis tool, long-distance semantic relationships in the code that it
has already generated. During training, the model observes these relationships
and learns to generate programs conditioned on them. We apply our approach to
the problem of generating entire Java methods given the remainder of the class
that contains the method. Our experiments show that the approach substantially
outperforms state-of-the-art transformers and a model that explicitly tries to learn
program semantics on this task, both in terms of producing programs free of basic
semantic errors and in terms of syntactically matching the ground truth.
