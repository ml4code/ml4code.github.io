---
layout: publication
title: "Automatically Learning Semantic Features for Defect Prediction"
authors: Song Wang, Taiyue Liu, Lin Tan
conference: ICSE
year: 2016
tags: ["defect", "representation"]
---
Software defect prediction, which predicts defective code regions, can help developers find bugs and prioritize their testing efforts. To build accurate prediction models, previous
studies focus on manually designing features that encode the
characteristics of programs and exploring different machine
learning algorithms. Existing traditional features often fail
to capture the semantic differences of programs, and such a
capability is needed for building accurate prediction models.

To bridge the gap between programs’ semantics and
defect prediction features, this paper proposes to leverage a
powerful representation-learning algorithm, deep learning,
to learn semantic representation of programs automatically
from source code. Specifically, we leverage Deep Belief
Network (DBN) to automatically learn semantic features
from token vectors extracted from programs’ Abstract
Syntax Trees (ASTs).

Our evaluation on ten open source projects shows that
our automatically learned semantic features significantly improve both within-project defect prediction (WPDP) and
cross-project defect prediction (CPDP) compared to traditional features. Our semantic features improve WPDP on
average by 14.7% in precision, 11.5% in recall, and 14.2%
in F1. For CPDP, our semantic features based approach
outperforms the state-of-the-art technique TCA+ with traditional features by 8.9% in F1.
