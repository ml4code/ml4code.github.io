---
layout: publication
title: "Learning a Strategy for Adapting a Program Analysis via Bayesian Optimisation"
authors: Hakjoo Oh, Hongseok Yang, Kwangkeun Yi.
conference: OOPSLA 
year: 2015
tags: ["program analysis"]
---
Building a cost-effective static analyser for real-world programs is still regarded an art. One key contributor to this
grim reputation is the difficulty in balancing the cost and the
precision of an analyser. An ideal analyser should be adap-
tive to a given analysis task, and avoid using techniques that
unnecessarily improve precision and increase analysis cost.
However, achieving this ideal is highly nontrivial, and it requires a large amount of engineering efforts.

In this paper we present a new approach for building
an adaptive static analyser. In our approach, the analyser
includes a sophisticated parameterised strategy that decides, for each part of a given program, whether to apply
a precision-improving technique to that part or not. We
present a method for learning a good parameter for such
a strategy from an existing codebase via Bayesian optimisation. The learnt strategy is then used for new, unseen programs. Using our approach, we developed partially flow-
and context-sensitive variants of a realistic C static analyser.
The experimental results demonstrate that using Bayesian
optimisation is crucial for learning from an existing codebase. Also, they show that among all program queries that
require flow- or context-sensitivity, our partially flow- and
context-sensitive analysis answers the 75% of them, while
increasing the analysis cost only by 3.3x of the baseline
flow- and context-insensitive analysis, rather than 40x or
more of the fully sensitive version.
