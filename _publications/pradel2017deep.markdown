---
layout: publication
title: "Deep Learning to Find Bugs"
authors: Michael Pradel, Koushik Sen
conference: 
year: 2017
additional_links:
   - {name: "PDF", url: "http://mp.binaervarianz.de/DeepBugs_TR_Nov2017.pdf"}
tags: ["defect", "program analysis"]
---
Automated bug detection, e.g., through pattern-based static
analysis, is an increasingly popular technique to find programming errors and other code quality issues. Traditionally,
bug detectors are program analyses that are manually written and carefully tuned by an analysis expert. Unfortunately,
the huge amount of possible bug patterns makes it difficult
to cover more than a small fraction of all bugs. This paper
presents a new approach toward creating bug detectors. The
basic idea is to replace manually writing a program analysis
with training a machine learning model that distinguishes
buggy from non-buggy code. To address the challenge that
effective learning requires both positive and negative train-
ing examples, we use simple code transformations that create likely incorrect code from existing code examples. We
present a general framework, called DeepBugs, that extracts
positive training examples from a code corpus, leverages
simple program transformations to create negative training
examples, trains a model to distinguish these two, and then
uses the trained model for identifying programming mistakes in previously unseen code. As a proof of concept, we
create four bug detectors for JavaScript that find a diverse set
of programming mistakes, e.g., accidentally swapped function arguments, incorrect assignments, and incorrect binary
operations. To find bugs, the trained models use information
that is usually discarded by program analyses, such as identifier names of variables and functions. Applying the approach
to a corpus of 150,000 JavaScript files shows that learned bug
detectors have a high accuracy, are very efficient, and reveal
132 programming mistakes in real-world code.

