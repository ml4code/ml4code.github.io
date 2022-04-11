---
layout: publication
title: "Commit Message Generation for Source Code Changes"
authors: Shengbin Xu, Yuan Yao, Feng Xu, Tianxiao Gu, Hanghang Tong, Jian Lu
conference: IJCAI
year: 2019
tags: ["edit", "summarization"]
---
Commit  messages,  which  summarize  the  source
code changes in natural language, are essential for
program comprehension and software evolution understanding.  Unfortunately, due to the lack of direct
motivation,  commit  messages  are  sometimes neglected  by  developers,  making  it  necessary  to
automatically  generate  such  messages.    State-of-the-art  adopts  learning  based  approaches  such  as
neural machine translation models for the commitmessage generation problem.  However, they tend
to  ignore  the  code  structure  information  and  suffer from the out-of-vocabulary issue.
In this paper, we  propose  CODISUM to  address  the  above  two limitations. In particular,
we first extract both code structure and code semantics from the source code changes, and then
jointly model these two sources of  information  so  as  to  better  learn  the  representations
 of  the  code  changes.   Moreover,  we  augment  the  model  with  copying  mechanism  to  further
mitigate  the  out-of-vocabulary  issue.   Experimental  evaluations  on  real  data  demonstrate  that
the  proposed  approach  significantly  outperforms the state-of-the-art in terms of accurately generating the commit messages.
