---
layout: publication
title: "Program Synthesis from Natural Language Using Recurrent Neural Networks"
authors: Xi Victoria Lin, Chenglong Wang, Deric Pang, Kevin Vu, Michael D. Ernst
conference: Technical Report UW-CSE-17-03-01, University of Washington Department of Computer Science and Engineering
year: 2017
additional_links:
   - {name: "PDF", url: "http://victorialin.net/pubs/tellina_tr180201.pdf"}
   - {name: "Tool", url: "http://tellina.rocks/"}
tags: ["bimodal", "code generation"]
---
Oftentimes, a programmer may have difficulty implementing a
desired operation. Even when the programmer can describe her
goal in English, it can be difficult to translate into code. Existing
resources, such as question-and-answer websites, tabulate specific
operations that someone has wanted to perform in the past, but
they are not effective in generalizing to new tasks, to compound
tasks that require combining previous questions, or sometimes even
to variations of listed tasks.

Our goal is to make programming easier and more productive by
letting programmers use their own words and concepts to express
the intended operation, rather than forcing them to accommodate
the machine by memorizing its grammar. We have built a system
that lets a programmer describe a desired operation in natural language, then automatically translates it to a programming language
for review and approval by the programmer. Our system, Tellina,
does the translation using recurrent neural networks (RNNs), a
state-of-the-art natural language processing technique that we augmented with slot (argument) filling and other enhancements.

We evaluated Tellina in the context of shell scripting. We trained
Tellina’s RNNs on textual descriptions of file system operations
and bash one-liners, scraped from the web. Although recovering
completely correct commands is challenging, Tellina achieves top-3
accuracy of 80% for producing the correct command structure. In a
controlled study, programmers who had access to Tellina outperformed those who did not, even when Tellina’s predictions were
not completely correct, to a statistically significant degree.
