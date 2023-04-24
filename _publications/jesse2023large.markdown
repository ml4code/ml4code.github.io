---
layout: publication
title: "Large Language Models and Simple, Stupid Bugs"
authors: Kevin Jesse, Toufique Ahmed, Premkumar T. Devanbu, Emily Morgan
conference: 
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2303.11455"}
tags: ["Transformer", "defect"]
---
With the advent of powerful neural language models, AI-based systems to assist developers in coding tasks are becoming widely available; Copilot is one such system. Copilot uses Codex, a large language model (LLM), to complete code conditioned on a preceding "prompt". Codex, however, is trained on public GitHub repositories, viz., on code that may include bugs and vulnerabilities. Previous studies [1], [2] show Codex reproduces vulnerabilities seen in training. In this study, we examine how prone Codex is to generate an interesting bug category, single statement bugs, commonly referred to as simple, stupid bugs or SStuBs in the MSR community. We find that Codex and similar LLMs do help avoid some SStuBs, but do produce known, verbatim SStuBs as much as 2x as likely than known, verbatim correct code. We explore the consequences of the Codex generated SStuBs and propose avoidance strategies that suggest the possibility of reducing the production of known, verbatim SStubs, and increase the possibility of producing known, verbatim fixes. 
