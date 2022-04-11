---
layout: publication
title: "Bugram: bug detection with n-gram language models"
authors: Song Wang, Devin Chollak, Dana Movshovitz-Attias, Lin Tan
conference: ASE
year: 2016
tags: ["defect", "representation"]
---

To improve software reliability, many rule-based techniques have been proposed to infer programming rules and detect violations of these rules as bugs. These rule-based approaches often rely on the highly frequent appearances of certain patterns in a project to infer rules. It is known that if a pattern does not appear frequently enough, rules are not learned, thus missing many bugs.

In this paper, we propose a new approach—Bugram—that leverages n-gram language models instead of rules to detect bugs. Bugram models program tokens sequentially, using the n-gram language model. Token sequences from the program are then assessed according to their probability in the learned model, and low probability sequences are marked as potential bugs. The assumption is that low probability token sequences in a program are unusual, which may indicate bugs, bad practices, or unusual/special uses of code of which developers may want to be aware.

We evaluate Bugram in two ways. First, we apply Bugram on the latest versions of 16 open source Java projects. Results show that Bugram detects 59 bugs, 42 of which are manually verified as correct, 25 of which are true bugs and 17 are code snippets that should be refactored. Among the 25 true bugs, 23 cannot be detected by PR-Miner. We have reported these bugs to developers, 7 of which have already been confirmed by developers (4 of them have already been fixed), while the rest await confirmation. Second, we further compare Bugram with three additional graph- and rule-based bug detection tools, i.e., JADET, Tikanga, and GrouMiner. We apply Bugram on 14 Java projects evaluated in these three studies. Bugram detects 21 true bugs, at least 10 of which cannot be detected by these three tools. Our results suggest that Bugram is complementary to existing rule-based bug detection approaches.


