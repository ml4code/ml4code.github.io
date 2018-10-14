---
layout: publication
title: "Tree2Tree Neural Translation Model for Learning Source Code Changes"
authors: S. Chakraborty, M. Allamanis, B. Ray
conference: 
year: 2018
bibkey: chakraborty2018tree2tree
---
The way developers edit day-to-day code tend to be repetitive and often use existing code elements. Many researchers tried to automate this tedious task of code changes by learning from specific change templates and applied to limited scope. The advancement of Neural Machine Translation (NMT) and the availability of the vast open source software evolutionary data open up a new possibility of automatically learning those templates from the wild. However, unlike natural languages, for which NMT techniques were originally designed, source code and the changes have certain properties. For instance, compared to natural language source code vocabulary can be virtually infinite. Further, any good change in code should not break its syntactic structure. Thus, deploying state-of-the-art NMT models without domain adaptation may poorly serve the purpose. To this end, in this work, we propose a novel Tree2Tree Neural Machine Translation system to model source code changes and learn code change patterns from the wild. We realize our model with a change suggestion engine: CODIT. We train the model with more than 30k real-world changes and evaluate it with 6k patches. Our evaluation shows the effectiveness of CODIT in learning and suggesting abstract change templates. CODIT also shows promise in suggesting concrete patches and generating bug fixes. 
