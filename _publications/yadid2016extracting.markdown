---
layout: publication
title: "Extracting Code from Programming Tutorial Videos"
authors: Shir Yadid, Eran Yahav
conference: Onward!
year: 2016
tags: ["information extraction"]
---
The number of programming tutorial videos on the web
increases daily. Video hosting sites such as YouTube host
millions of video lectures, with many programming tutorials for various languages and platforms. These videos contain a wealth of valuable information, including code that
may be of interest. However, two main challenges have so
far prevented the effective indexing of programming tutorial
videos: (i) code in tutorials is typically written on-the-fly,
with only parts of the code visible in each frame, and (ii) optical character recognition (OCR) is not precise enough to
produce quality results from videos.

We present a novel approach for extracting code from
videos that is based on: (i) consolidating code across frames,
and (ii) statistical language models for applying corrections
at different levels, allowing us to make corrections by choosing the most likely token, combination of tokens that form a
likely line structure, and combination of lines that lead to
a likely code fragment in a particular language. We implemented our approach in a tool called ACE , and used it to extract code from 40 Android video tutorials on YouTube . Our
evaluation shows that ACE extracts code with high accuracy,
enabling deep indexing of video tutorials.
