---
layout: publication
title: "Bayesian Sketch Learning for Program Synthesis"
authors: Vijayaraghavan Murali, Letao Qi, Swarat Chaudhuri, Chris Jermaine
conference: ICLR
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1703.05698"}
tags: ["code generation", "API"]
---
We present a Bayesian statistical approach to the problem of automatic program synthesis. Our synthesizer starts
by learning, offline and from an existing corpus, a probabilistic model of real-world programs. During synthesis,
it is provided some ambiguous and incomplete evidence about the nature of the programming task that the user
wants automated, for example sets of API calls or data types that are relevant for the task. Given this input, the
synthesizer infers a posterior distribution over type-safe programs that assigns higher likelihood to programs
that, according to the learned model, are more likely to match the evidence.

We realize this approach using two key ideas. First, our learning techniques operate not over code but
syntactic abstractions, or sketches, of programs. During synthesis, we infer a posterior distribution over sketches,
then concretize samples from this distribution into type-safe programs using combinatorial techniques. Second,
our statistical model explicitly models the full intent behind a synthesis task as a latent variable. To infer
sketches, we first estimate a posterior distribution on the intent, then use samples from this posterior to generate
a distribution over possible sketches. We show that our model can be implemented effectively using the new
neural architecture of Bayesian encoder-decoders, which can be trained with stochastic gradient descent and
yields a simple inference procedure.

We implement our ideas in a system, called BAYOU , for the synthesis of API-heavy Java methods. We train
BAYOU on a large corpus of Android apps, and find that the trained system can often synthesize complex
methods given just a few API method names or data types as evidence. The experiments also justify the design
choice of using a latent intent variable and the levels of abstraction at which sketches and evidence are defined.
