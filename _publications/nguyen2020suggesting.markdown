---
layout: publication
title: "Suggesting Natural Method Names to Check Name Consistencies"
authors: Son Nguyen, Hung Phan, Trinh Le, Tien N. Nguyen
conference: ICSE
year: 2020
additional_links:
   - {name: "Preprint", url: "https://sonvnguyen.github.io/publications/icse20-final.pdf"}
tags: ["naming"]
---
Misleading names of the methods in a project or the APIs in a software library confuse developers about program functionality
and API usages, leading to API misuses and defects. In this paper,we introduce MNire, a machine learning approach to check the
consistency between the name of a given method and its implementation. MNire first generates a candidate name and compares the
current name against it. If the two names are sufficiently similar, we consider the method as consistent. To generate the method name,
we draw our ideas and intuition from an empirical study on the nature of method names in a large dataset. Our key finding is that
high proportions of the tokens of method names can be found in the three contexts of a given method including its body,
the interface (the method’s parameter types and return type), and the enclosing class’ name. Even when such tokens are not there,
MNire uses the contexts to predict the tokens due to the high likelihoods of their co-occurrences. Our unique idea is to treat
the name generation as an abstract summarization on the tokens collected from the names of the program entities in the three
above contexts.

We conducted several experiments to evaluate MNire in method name consistency checking and in method name
recommending on large datasets with +14M methods. In detecting inconsistency method names, MNire improves the state-of-the-art
approach by 10.4% and 11% relatively in recall and precision, respectively. In method name recommendation, MNire improves relatively
over the state-of-the-art technique, code2vec, in both recall (18.2% higher) and precision (11.1% higher). To assess MNire’s usefulness,
we used it to detect inconsistent methods and suggest new names in several active, GitHub projects. We made 50 pull requests (PRs) and received
42 responses. Among them, five PRs were merged into the main branch, and 13 were approved for later merging. In total, in 31/42 cases,
the developer teams agree that our suggested names are more meaningful than the current names, showing MNire’s usefulness.
