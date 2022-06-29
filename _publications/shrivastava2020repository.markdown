---
layout: publication
title: "Repository-Level Prompt Generation for Large Language Models of Code"
authors: Disha Shrivastava, Hugo Larochelle, Daniel Tarlow
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2206.12839"}
tags: ["Transformer", "code completion"]
---
With the success of large language models (LLMs) of code and their use as code assistants (e.g. Codex used in GitHub Copilot), techniques for introducing domain-specific knowledge in the prompt design process become important. In this work, we propose a framework called Repo-Level Prompt Generator that learns to generate example-specific prompts using a set of rules. These rules take context from the entire repository, thereby incorporating both the structure of the repository and the context from other relevant files (e.g. imports, parent class files). Our technique doesn't require any access to the weights of the LLM, making it applicable in cases where we only have black-box access to the LLM. We conduct experiments on the task of single-line code-autocompletion using code repositories taken from Google Code archives. We demonstrate that an oracle constructed from our proposed rules gives up to 36% relative improvement over Codex, showing the quality of the rules. Further, we show that when we train a model to select the best rule, we can achieve significant performance gains over Codex. The code for our work can be found at: https://github.com/shrivastavadisha/repo_level_prompt_generation .
