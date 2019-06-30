---
layout: publication
title: "Context2Name: A Deep Learning-Based Approach to Infer Natural Variable Names from Usage Contexts"
authors: R. Bavishi, M. Pradel, K. Sen
conference: 
year: 2017
bibkey: bavishi2017context2name
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/pdf/1809.05193.pdf"}
tags: ["naming"]
---
Most of the JavaScript code deployed in the wild has been minified, a process in which identifier names are replaced
with short, arbitrary and meaningless names. Minified code occupies less space, but also makes the code extremely difficult to manually inspect and understand. This paper presents Context2Name, a deep learning-based technique that partially reverses the effect of minification by predicting natural
identifier names for minified names. The core idea is to predict from the usage context of a variable a name that captures
the meaning of the variable. The approach combines a lightweight, token-based static analysis with an auto-encoder
neural network that summarizes usage contexts and a recurrent neural network that predict natural names for a given
usage context. We evaluate Context2Name
with a large corpus of real-world JavaScript code and show that it successfully predicts 60.4% of all minified identifiers. A comparison
with the state-of-the-art tools JSNice and JSNaughty shows
that our approach predicts 17% and 43% more names than the
best existing approaches, while taking only 2.6 milliseconds
to predict a name, on average.
