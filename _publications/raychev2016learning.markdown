---
layout: publication
title: "Learning Programs from Noisy Data"
authors: Veselin Raychev, Pavol lBielik, Martin Vechev, Andreas Krause
conference: POPL
year: 2016
tags: ["code generation", "grammar"]
---
We present a new approach for learning programs from noisy
datasets. Our approach is based on two new concepts: a regularized
program generator which produces a candidate program based on a
small sample of the entire dataset while avoiding overfitting, and a
dataset sampler which carefully samples the dataset by leveraging
the candidate program’s score on that dataset. The two components
are connected in a continuous feedback-directed loop.

We show how to apply this approach to two settings: one where
the dataset has a bound on the noise, and another without a noise
bound. The second setting leads to a new way of performing
approximate empirical risk minimization on hypotheses classes
formed by a discrete search space.

We then present two new kinds of program synthesizers which
target the two noise settings. First, we introduce a novel regularized
bitstream synthesizer that successfully generates programs even in
the presence of incorrect examples. We show that the synthesizer
can detect errors in the examples while combating overfitting –
a major problem in existing synthesis techniques. We also show
how the approach can be used in a setting where the dataset grows
dynamically via new examples (e.g., provided by a human).

Second, we present a novel technique for constructing statistical
code completion systems. These are systems trained on massive
datasets of open source programs, also known as “Big Code”. The
key idea is to introduce a domain specific language (DSL) over
trees and to learn functions in that DSL directly from the dataset.
These learned functions then condition the predictions made by the
system. This is a flexible and powerful technique which generalizes
several existing works as we no longer need to decide a priori on
what the prediction should be conditioned (another benefit is that
the learned functions are a natural mechanism for explaining the
prediction). As a result, our code completion system surpasses the
prediction capabilities of existing, hard-wired systems.
