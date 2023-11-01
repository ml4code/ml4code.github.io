---
layout: publication
title: "Using Developer Discussions to Guide Fixing Bugs in Software"
authors: Sheena Panthaplackel, Milos Gligoric, Junyi Jessy Li, Raymond J. Mooney
conference: EMNLP
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2211.06335"}
tags: ["Transformer", "repair"]
---
Automatically fixing software bugs is a challenging task. While recent work showed that natural language context is useful in guiding bug-fixing models, the approach required prompting developers to provide this context, which was simulated through commit messages written after the bug-fixing code changes were made. We instead propose using bug report discussions, which are available before the task is performed and are also naturally occurring, avoiding the need for any additional information from developers. For this, we augment standard bug-fixing datasets with bug report discussions. Using these newly compiled datasets, we demonstrate that various forms of natural language context derived from such discussions can aid bug-fixing, even leading to improved performance over using commit messages corresponding to the oracle bug-fixing commits.
