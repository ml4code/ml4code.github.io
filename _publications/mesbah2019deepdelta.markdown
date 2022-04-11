---
layout: publication
title: "DeepDelta: Learning to Repair Compilation Errors"
authors: Ali Mesbah, Andrew Rice, Emily Johnston, Nick Glorioso, Edward Aftandilian.
conference: 
year: 2019
tags: ["repair", "edit", "compilation"]
---
Programmers spend a substantial amount of time manually repairing
code that does not compile. We observe that the repairs for
any particular error class typically follow a pattern and are highly
mechanical. We propose a novel approach that automatically learns
these patterns with a deep neural network and suggests program
repairs for the most costly classes of build-time compilation failures.
We describe how we collect all build errors and the human-authored,
in-progress code changes that cause those failing builds to transition
to successful builds at Google. We generate an AST diff from the
textual code changes and transform it into a domain-specific
language called Delta that encodes the change that must be made
to make the code compile. We then feed the compiler diagnostic
information (as source) and the Delta changes that resolved the
diagnostic (as target) into a Neural Machine Translation network for
training. For the two most prevalent and costly classes of Java compilation errors,
namely missing symbols and mismatched methodsignatures, our system called DeepDelta,
generates the correct repair changes for 19,314 out of 38,788 (50%) of unseen compilation
errors. The correct changes are in the top three suggested axes 86% of the time on average.
