---
layout: publication
title: Open-ended Knowledge Tracing
authors: Naiming Liu, Zichao Wang, Richard G. Baraniuk, Andrew Lan
conference: 
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2203.03716"}
   - {name: "code", url: "https://github.com/lucy66666/OKT"}
tags: ["education", "code generation"]
---
In education applications, knowledge tracing refers to the problem of estimating students' time-varying concept/skill mastery level from their past responses to questions and predicting their future performance. One key limitation of most existing knowledge tracing methods is that they treat student responses to questions as binary-valued, i.e., whether they are correct or incorrect. Response correctness analysis/prediction ignores important information on student knowledge contained in the exact content of the responses, especially for open-ended questions. In this paper, we conduct the first exploration into open-ended knowledge tracing (OKT) by studying the new task of predicting students' exact open-ended responses to questions. Our work is grounded in the domain of computer science education with programming questions. We develop an initial solution to the OKT problem, a student knowledge-guided code generation approach, that combines program synthesis methods using language models with student knowledge tracing methods. We also conduct a series of quantitative and qualitative experiments on a real-world student code dataset to validate OKT and demonstrate its promise in educational applications.
