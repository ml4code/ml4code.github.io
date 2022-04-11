---
layout: publication
title: "Learning to Fuzz: Application-Independent Fuzz Testing with Probabilistic, Generative Models of Input Data"
authors: Jibesh Patra, Michael Pradel
conference: 
year: 2016
tags: ["fuzzing"]
---
Fuzzing is a popular technique to create test inputs for software that processes structured data. It has been successfully
applied in various domains, ranging from compilers and interpreters over program analyses to rendering engines, image manipulation tools, and word processors. Existing fuzz
testing techniques are tailored for a particular purpose and
rely on a carefully crafted model of the data to be generated.
This paper presents TreeFuzz, a generic approach for generating structured data without an a priori known model. The
key idea is to exploit a given corpus of example data to au-
tomatically infer probabilistic, generative models that create
new data with properties similar to the corpus. To support a
wide range of different properties, TreeFuzz is designed as a
framework with an extensible set of techniques to infer generative models. We apply the idea to JavaScript programs
and HTML documents and show that the approach generates mostly valid data for both of them: 96.3% of the generated JavaScript programs are syntactically valid and there are
only 2.06 validation errors per kilobyte of generated HTML.
The performance of both learning and generation scales linearly w.r.t. the size of the corpus. Using TreeFuzz-generated
JavaScript programs for differential testing of JavaScript engines exposes various inconsistencies among browsers, including browser bugs and unimplemented language features.
