---
layout: publication
title: Abridging Source Code
authors: Binhang Yuan, Vijayaraghavan Murali, Christopher Jermaine
conference: OOPSLA
year: 2017
additional_links:
   - {name: "ACM", url: "https://dl.acm.org/citation.cfm?id=3133882"}
tags: ["summarization"]
---
In this paper, we consider the problem of source code abridgment, where the goal is to remove statements from a source code in order to display the source code in a small space, while at the same time leaving the ``important'' parts of the source code intact, so that an engineer can read the code and quickly understand purpose of the code. To this end, we develop an algorithm that looks at a number of examples, human-created source code abridgments, and learns how to remove lines from the code in order to mimic the human abridger. The learning algorithm takes into account syntactic features of the code, as well as semantic features such as control flow and data dependencies. Through a comprehensive user study, we show that the abridgments that our system produces can decrease the time that a user must look at code in order to understand its functionality, as well as increase the accuracy of the assessment, while displaying the code in a greatly reduced area.