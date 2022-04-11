---
layout: publication
title: "A Deep Learning Approach to Identifying Source Code in Images and Video"
authors: Jordan Ott, Abigail Atchison, Paul Harnack, Adrienne Bergh, Erik Linstead.
conference: MSR
year: 2018
tags: ["information extraction"]
---
While substantial progress has been made in mining code on an
Internet scale, efforts to date have been overwhelmingly focused on
data sets where source code is represented natively as text. Large
volumes of source code available online and embedded in technical
videos have remained largely unexplored, due in part to the complexity of extraction when code is represented with images. Existing
approaches to code extraction and indexing in this environment rely
heavily on computationally intense optical character recognition.
To improve the ease and efficiency of identifying this embedded
code, as well as identifying similar code examples, we develop a
deep learning solution based on convolutional neural networks and
autoencoders. Focusing on Java for proof of concept, our technique
is able to identify the presence of typeset and handwritten source
code in thousands of video images with 85.6%-98.6% accuracy based
on syntactic and contextual features learned through deep architectures. When combined with traditional approaches, this provides
a more scalable basis for video indexing that can be incorporated
into existing software search and mining tools.
