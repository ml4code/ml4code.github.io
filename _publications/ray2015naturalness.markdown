---
layout: publication
title: "On the “Naturalness” of Buggy Code"
authors: Baishakhi Ray, Vincent Hellendoorn, Saheel Godhane, Zhaopeng Tu, Alberto Bacchelli, Premkumar Devanbu
conference: ICSE
year: 2015
tags: ["defect"]
---
Real software, the kind working programmers produce by the kLOC
to solve real-world problems, tends to be “natural”, like speech or
natural language; it tends to be highly repetitive and predictable.
Researchers have captured this naturalness of software through statistical models and used them to good effect in suggestion engines,
porting tools, coding standards checkers, and idiom miners. This
suggests that code that appears improbable, or surprising, to a good
statistical language model is “unnatural” in some sense, and thus
possibly suspicious. In this paper, we investigate this hypothesis. We consider a large corpus of bug fix commits (ca. 8,296),
from 10 different Java projects, and we focus on its language statistics, evaluating the naturalness of buggy code and the corresponding fixes. We find that code with bugs tends to be more entropic
(i.e. unnatural), becoming less so as bugs are fixed. Focusing on
highly entropic lines is similar in cost-effectiveness to some well-known static bug finders (PMD, FindBugs) and ordering warnings
from these bug finders using an entropy measure improves the cost-effectiveness of inspecting code implicated in warnings. This suggests that entropy may be a valid language-independent and simple
way to complement the effectiveness of PMD or FindBugs, and
that search-based bug-fixing methods may benefit from using entropy both for fault-localization and searching for fixes.

