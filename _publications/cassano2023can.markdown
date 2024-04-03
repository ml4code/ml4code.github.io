---
layout: publication
title: "Can It Edit? Evaluating the Ability of Large Language Models to Follow Code Editing Instructions"
authors: Federico Cassano, Luisa Li, Akul Sethi, Noah Shinn, Abby Brennan-Jones, Jacob Ginesin, Edward Berman, George Chakhnashvili, Anton Lozhkov, Carolyn Jane Anderson, Arjun Guha
conference:
year: 2023
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2312.12450"}
tags: ["editing"]
---
A significant amount of research is focused on developing and evaluating large language models for a variety of code synthesis tasks. These include synthesizing code from natural language, synthesizing tests from code, and synthesizing explanations of code. In contrast, the behavior of instructional code editing with LLMs is understudied. These are tasks in which the model is provided a block of code and an instruction to modify the code. The editing instruction may ask for a feature to be added or removed, describe a bug and ask for a fix, or ask for a different kind of solution. We introduce a carefully crafted benchmark of code editing tasks and use it to evaluate several cutting edge LLMs. Our evaluation exposes a significant gap between the capabilities of state-of-the-art open and closed models. For example, even GPT-3.5-Turbo is better than the best open model at code editing tasks. We also introduce a new, carefully curated, permissively licensed training dataset of code editing tasks coupled with natural language instructions. Using this training dataset, we show that we can fine-tune open Code LLMs to significantly improve their code editing capabilities, closing the gap between open and closed models. All code, data, and models are available at https://github.com/nuprl/CanItEdit.
