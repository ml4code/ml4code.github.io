---
layout: publication
title: "Learning to Generate Corrective Patches using Neural Machine Translation"
authors: Hideaki Hata, Emad Shihab, Graham Neubig
conference: 
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1812.07170"}
tags: ["repair", "code generation"]
---
Bug fixing is generally a manually-intensive task. However, recent work has proposed the idea of automated program repair, which aims to repair (at least a subset of) bugs in different ways such as code mutation, etc. Following in the same line of work as automated bug repair, in this paper we aim to leverage past fixes to propose fixes of current/future bugs. Specifically, we propose Ratchet, a corrective patch generation system using neural machine translation. By learning corresponding pre-correction and post-correction code in past fixes with a neural sequence-to-sequence model, Ratchet is able to generate a fix code for a given bug-prone code query. We perform an empirical study with five open source projects, namely Ambari, Camel, Hadoop, Jetty and Wicket, to evaluate the effectiveness of Ratchet. Our findings show that Ratchet can generate syntactically valid statements 98.7% of the time, and achieve an F1-measure between 0.41-0.83 with respect to the actual fixes adopted in the code base. In addition, we perform a qualitative validation using 20 participants to see whether the generated statements can be helpful in correcting bugs. Our survey showed that Ratchet's output was considered to be helpful in fixing the bugs on many occasions, even if fix was not 100% correct.
