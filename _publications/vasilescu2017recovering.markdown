---
layout: publication
title: "Recovering Clear, Natural Identifiers from Obfuscated JS Names"
authors: Bogdan Vasilescu, Casey Casalnuovo, Premkumar Devanbu
conference: FSE
year: 2017
tags: ["deobfuscation", "naming"]
---
 Well-chosen variable names are critical to source code readability, reusability, and maintainability. Unfortunately, in deployed JavaScript code (which is ubiquitous on the web) the identifier names are frequently minified and overloaded. This is done both for efficiency and also to protect potentially proprietary intellectual property. In this paper, we describe an approach based on statistical machine translation (SMT) that recovers some of the original names from the JavaScript programs minified by the very popular UglifyJS. This simple tool, Autonym, performs comparably to the best currently available deobfuscator for JavaScript, JSNice, which uses sophisticated static analysis. In fact, Autonym is quite complementary to JSNice, performing well when it does not, and vice versa. We also introduce a new tool, JSNaughty, which blends Autonym and JSNice, and significantly outperforms both at identifier name recovery, while remaining just as easy to use as JSNice. JSNaughty is available online at http://jsnaughty.org.
