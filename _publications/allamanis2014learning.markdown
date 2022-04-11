---
layout: publication
title: Learning Natural Coding Conventions
authors: Miltiadis Allamanis, Earl T. Barr, Christian Bird, Charles Sutton
conference: FSE
year: 2014
additional_links:
   - {name: "PDF", url: "http://homepages.inf.ed.ac.uk/csutton/publications/naturalize.pdf"}
   - {name: "ArXiV", url: "http://arxiv.org/abs/1402.4182"}
   - {name: "website", url: "http://groups.inf.ed.ac.uk/naturalize/"}
   - {name: "code", url: "https://github.com/mast-group/naturalize"}
tags: ["naming", "language model", "style"]
---
Every programmer has a characteristic style, ranging from preferences
about identifier naming to preferences about object relationships and
design patterns. Coding conventions define a consistent syntactic style,
fostering readability and hence maintainability. When collaborating,
programmers strive to obey a project’s coding conventions. However,
one third of reviews of changes contain feedback about coding conventions,
indicating that programmers do not always follow them and that project
members care deeply about adherence. Unfortunately, programmers are
often unaware of coding conventions because inferring them requires a
global view, one that aggregates the many local decisions programmers
make and identifies emergent consensus on style. We present Naturalize,
a framework that learns the style of a codebase, and suggests revisions
to improve stylistic consistency. Naturalize builds on recent work in
applying statistical natural language processing to source code. We
apply Naturalize to suggest natural identifier names and formatting
conventions. We present four tools focused on ensuring natural code
during development and release management, including code review.
Naturalize achieves 94% accuracy in its top suggestions for identifier
names. We used Naturalize to generate 18 patches for 5 open source
projects: 14 were accepted.
