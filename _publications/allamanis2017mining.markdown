---
layout: publication
title: Mining Semantic Loop Idioms from Big Code
authors: Miltiadis Allamanis, Earl T. Barr, Christian Bird, Mark Marron, Charles Sutton
conference: "TSE"
year: 2017
additional_links:
   - {name: "MSR Technical Report", url: "https://www.microsoft.com/en-us/research/publication/mining-semantic-loop-idioms-big-code/"}
   - {name: "website", url: "http://groups.inf.ed.ac.uk/cup/semantic-idioms/"}
tags: ["pattern mining", "grammar"]
---
During maintenance, developers spend a lot of time transforming existing code: refactoring, optimizing, and adding checks to make it more robust. Much of this work is the drudgery of identifying and replacing specific patterns, yet it resists automation, because of meaningful patterns are hard to automatically find. We present a technique for mining loop idioms, surprisingly probable semantic patterns that occur in loops, from big code to find meaningful patterns. First, we show that automatically identifiable patterns exist, in great numbers, with a large scale empirical study of loop over 25 MLOC. We find that loops in this corpus are simple and predictable: 90% of them have fewer than 15LOC and 90% have no nesting and very simple control structure. Encouraged by this result, we coil loops to abstract away syntactic diversity to define information rich loop idioms. We show that only 50 loop idioms cover 50% of the concrete loops. We show how loop idioms can help a tool developers identify and prioritize refactorings. We also show how our framework opens the door to data-driven tool and language design discovering opportunities to introduce new API calls and language constructs: loop idioms show that LINQ would benefit from an Enumerate operator, a result confirmed by the fact that precisely this feature is one of the most requested features on StackOverflow with 197 votes and 95k views.
