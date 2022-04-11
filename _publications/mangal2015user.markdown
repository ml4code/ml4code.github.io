---
layout: publication
title: "A User-Guided Approach to Program Analysis"
authors: Ravi Mangal, Xin Zhang, Aditya V. Nori, Mayur Naik
conference: FSE
year: 2015
tags: ["program analysis"]
---
Program analysis tools often produce undesirable output
due to various approximations. We present an approach
and a system Eugene that allows user feedback to guide
such approximations towards producing the desired output.
We formulate the problem of user-guided program analysis in terms of solving a combination of hard rules and soft
rules: hard rules capture soundness while soft rules capture
degrees of approximations and preferences of users. Our
technique solves the rules using an off-the-shelf solver in a
manner that is sound (satisfies all hard rules), optimal (maximally satisfies soft rules), and scales to real-world analy-
ses and programs. We evaluate Eugene on two different
analyses with labeled output on a suite of seven Java pro-
grams of size 131–198 KLOC. We also report upon a user
study involving nine users who employ Eugene to guide an
information-flow analysis on three Java micro-benchmarks.
In our experiments, Eugene significantly reduces misclassified reports upon providing limited amounts of feedback.
