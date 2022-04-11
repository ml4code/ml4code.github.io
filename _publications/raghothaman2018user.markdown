---
layout: publication
title: "User-guided program reasoning using Bayesian inference"
authors: Mukund Raghothaman, Sulekha Kulkarni, Kihong Heo, Mayur Naik
conference: PLDI
year: 2018
additional_links:
   - {name: "Paper", url: "https://www.cis.upenn.edu/~kheo/paper/pldi18-rakuhena.pdf"}
tags: ["program analysis"]
---
Program analyses necessarily make approximations that often lead them to report true alarms interspersed with many false alarms. We propose a new approach to leverage user feedback to guide program analyses towards true alarms and away from false alarms. Our approach associates each alarm with a confidence value by performing Bayesian inference on a probabilistic model derived from the analysis rules. In each iteration, the user inspects the alarm with the highest confidence and labels its ground truth, and the approach recomputes the confidences of the remaining alarms given this feedback. It thereby maximizes the return on the effort by the user in inspecting each alarm. We have implemented our approach in a tool named Bingo for program analyses expressed in Datalog. Experiments with real users and two sophisticated analyses---a static datarace analysis for Java programs and a static taint analysis for Android apps---show significant improvements on a range of metrics, including false alarm rates and number of bugs found.
