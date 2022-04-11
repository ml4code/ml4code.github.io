---
layout: publication
title: Predicting Vulnerability in Large Codebases With Deep Code Representation
authors: Anshul Tanwar, Krishna Sundaresan, Parmesh Ashwath, Prasanna Ganesan, Sathish Kumar Chandrasekaran, Sriram Ravi 
conference: 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.12783"}
tags: ["grammar", "program analysis", "static analysis"]
---
Currently, while software engineers write code for various modules, quite often, various types of errors - coding, logic, semantic, and others (most of which are not caught by compilation and other tools) get introduced. Some of these bugs might be found in the later stage of testing, and many times it is reported by customers on production code. Companies have to spend many resources, both money and time in finding and fixing the bugs which would have been avoided if coding was done right. Also, concealed flaws in software can lead to security vulnerabilities that potentially allow attackers to compromise systems and applications. Interestingly, same or similar issues/bugs, which were fixed in the past (although in different modules), tend to get introduced in production code again.
We developed a novel AI-based system which uses the deep representation of Abstract Syntax Tree (AST) created from the source code and also the active feedback loop to identify and alert the potential bugs that could be caused at the time of development itself i.e. as the developer is writing new code (logic and/or function). This tool integrated with IDE as a plugin would work in the background, point out existing similar functions/code-segments and any associated bugs in those functions. The tool would enable the developer to incorporate suggestions right at the time of development, rather than waiting for UT/QA/customer to raise a defect.
We assessed our tool on both open-source code and also on Cisco codebase for C and C++ programing language. Our results confirm that deep representation of source code and the active feedback loop is an assuring approach for predicting security and other vulnerabilities present in the code.
