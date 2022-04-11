---
layout: publication
title: "Learning a Classifier for False Positive Error Reports Emitted by Static Code Analysis Tools"
authors: Ugur Koc, Parsa Saadatpanah, Jeffrey S. Foster, Adam A. Porter.
conference: MAPL
year: 2017
tags: ["static analysis"]
---
The large scale and high complexity of modern software systems
make perfectly precise static code analysis (SCA) infeasible. Therefore SCA tools often over-approximate, so not to miss any real
problems. This, however, comes at the expense of raising false
alarms, which, in practice, reduces the usability of these tools.

To partially address this problem, we propose a novel learning
process whose goal is to discover program structures that cause
a given SCA tool to emit false error reports, and then to use this
information to predict whether a new error report is likely to be a
false positive as well. To do this, we first preprocess code to isolate
the locations that are related to the error report. Then, we apply
machine learning techniques to the preprocessed code to discover
correlations and to learn a classifier.

We evaluated this approach in an initial case study of a widely-used SCA tool for Java. Our results showed that for our dataset
we could accurately classify a large majority of false positive error
reports. Moreover, we identified some common coding patterns that
led to false positive errors. We believe that SCA developers may be
able to redesign their methods to address these patterns and reduce
false positive error reports.
