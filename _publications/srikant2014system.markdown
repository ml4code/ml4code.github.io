---
layout: publication
title: "A system to grade computer programming skills using machine learning"
authors: Shashank Srikant, Varun Aggarwal
conference: KDD
year: 2014
additional_links:
   - {name: "PDF", url: "https://dl.acm.org/citation.cfm?id=2623377"}
   - {name: "website", url: "http://research.aspiringminds.com/"}
tags: ["education"]
---
The automatic evaluation of computer programs is a nascent area of research with a potential for large-scale impact. Extant program assessment systems score mostly based on the number of test-cases passed, providing no insight into the competency of the programmer. In this paper, we present a system to grade computer programs automatically. In addition to grading a program on its programming practices and complexity, the key kernel of the system is a machine-learning based algorithm which determines closeness of the logic of the given program to a correct program. This algorithm uses a set of highly-informative features, derived from the abstract representations of a given program, that capture the program's functionality. These features are then used to learn a model to grade the programs, which are built against evaluations done by experts. We show that the regression models provide much better grading than the ubiquitous test-case-pass based grading and rivals the grading accuracy of other open-response problems such as essay grading . We also show that our novel features add significant value over and above basic keyword/expression count features. In addition to this, we propose a novel way of posing computer-program grading as a one-class modeling problem and report encouraging preliminary results. We show the value of the system through a case study in a real-world industrial deployment. To the best of the authors' knowledge, this is the first time a system using machine learning has been developed and used for grading programs. The work is timely with regard to the recent boom in Massively Online Open Courseware (MOOCs), which promises to produce a significant amount of hand-graded digitized data.
