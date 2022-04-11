---
layout: publication
title: "Learning API Usages from Bytecode: A Statistical Approach"
authors: Tam The Nguyen, Hung Viet Pham, Phong Minh Vu, Tung Thanh Nguyen
conference: ICSE
year: 2016
tags: ["representation", "API"]
---
Mobile app developers rely heavily on standard API frameworks and libraries. However, learning API usages is often challenging due to the fast-changing nature of API frameworks for mobile systems and the insufficiency of API documentation and source code examples. In this paper, we propose a novel approach to learn API usages from bytecode of Android mobile apps. Our core contributions include HAPI, a statistical model of API usages and three algorithms to extract method call sequences from apps' bytecode, to train HAPI based on those sequences, and to recommend method calls in code completion using the trained HAPIs. Our empirical evaluation shows that our prototype tool can effectively learn API usages from 200 thousand apps containing 350 million method sequences. It recommends next method calls with top-3 accuracy of 90% and outperforms baseline approaches on average 10-20%.
