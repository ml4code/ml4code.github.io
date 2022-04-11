---
layout: publication
title: "NLyze: Interactive Programming by Natural Language for SpreadSheet Data Analysis and Manipulation"
authors: Sumit Gulwani, Mark Marron
conference: SIGMOD
year: 2014
tags: ["code generation", "bimodal", "synthesis"]
---
Millions of computer end users need to perform tasks over tabular spreadsheet data, yet lack the programming knowledge to do such tasks automatically. This paper describes
the design and implementation of a robust natural language
based interface to spreadsheet programming. Our methodology involves designing a typed domain-specific language
(DSL) that supports an expressive algebra of map, filter, reduce, join, and formatting capabilities at a level of abstraction appropriate for non-expert users. The key algorithmic
component of our methodology is a translation algorithm
for converting a natural language specification in the context of a given spreadsheet to a ranked set of likely programs
in the DSL. The translation algorithm leverages the spreadsheet spatial and temporal context to assign interpretations
to specifications with implicit references, and is thus robust
to a variety of ways in which end users can express the same
task. The translation algorithm builds over ideas from keyword programming and semantic parsing to achieve both
high precision and high recall. We implemented the system
as an Excel add-in called NLyze that supports a rich user
interaction model including annotating the user’s natural
language specification and explaining the synthesized DSL
programs by paraphrasing them into structured English. We
collected a total of 3570 English descriptions for 40 spreadsheet tasks and our system was able to generate the intended
interpretation as the top candidate for 94% (97% for the top
3) of those instances.

