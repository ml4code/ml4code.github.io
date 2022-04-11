---
layout: publication
title: "Intelligent Code Completion with Bayesian Networks"
authors: Sebastian Proksch, Johannes Lerch, Mira Mezini
conference: TSE
year: 2015
tags: ["autocomplete"]
---
Code completion is an integral part of modern Integrated Development Environments (IDEs). Developers
often use it to explore Application Programming Interfaces (APIs). It is also useful to reduce the required
amount of typing and to help avoid typos. Traditional code completion systems propose all type-correct
methods to the developer. Such a list is often very long with many irrelevant items. More intelligent code
completion systems have been proposed in prior work to reduce the list of proposed methods to relevant
items.

This work extends one of these existing approaches, the Best Matching Neighbor (BMN) algorithm. We
introduce Bayesian networks as an alternative underlying model, use additional context information for
more precise recommendations, and apply clustering techniques to improve model sizes. We compare our
new approach, Pattern-based Bayesian Networks (PBN), to the existing BMN algorithm. We extend previously used evaluation methodologies and, in addition to prediction quality, we also evaluate model size and
inference speed.

Our results show that the additional context information we collect improves prediction quality, especially
for queries that do not contain method calls. We also show that PBN can obtain comparable prediction
quality to BMN, while model size and inference speed scale better with large input sizes.
