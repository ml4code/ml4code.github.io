---
layout: publication
title: "Leveraging Existing Tests in Automated Test Generation for Web Applications"
authors: A. Milani Fard, M. Mirzaaghaei, A. Mesbah
conference: ASE
year: 2014
bibkey: milanifard2014leveraging
tags: ["code mining","test generation", "test reuse", "web application"]
---
To test web applications, developers currently write test cases in frameworks such as Selenium. On the other hand, most web test generation techniques rely on a crawler to explore the dynamic states of the application. The first approach requires much manual effort, but benefits from the domain knowledge of the developer writing the test cases. The second one is automated and systematic, but lacks the domain knowledge required to be as effective. We believe combining the two can be advantageous. In this paper, we propose to (1) mine the human knowledge present in the form of input values, event sequences, and assertions, in the human-written test suites, (2) combine that inferred knowledge with the power of automated crawling, and (3) extend the test suite for uncovered/unchecked portions of the web application under test. Our approach is implemented in a tool called Testilizer. An evaluation of our approach indicates that Testilizer (1) outperforms a random test generator, and (2) on average, can generate test suites with improvements of up to 150 percent in fault detection rate and up to 30 precent in code coverage, compared to the original test suite.