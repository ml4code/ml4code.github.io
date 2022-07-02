---
layout: publication
title: "Code Generation Tools (Almost) for Free? A Study of Few-Shot, Pre-Trained Language Models on Code"
authors: Patrick Bareiß, Beatriz Souza, Marcelo d'Amorim, Michael Pradel
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2206.01335"}
tags: ["Transformer"]
---
Few-shot learning with large-scale, pre-trained language models is a powerful way to answer questions about code, e.g., how to complete a given code example, or even generate code snippets from scratch. The success of these models raises the question whether they could serve as a basis for building a wide range code generation tools. Traditionally, such tools are built manually and separately for each task. Instead, few-shot learning may allow to obtain different tools from a single pre-trained language model by simply providing a few examples or a natural language description of the expected tool behavior. This paper studies to what extent a state-of-the-art, pre-trained language model of code, Codex, may serve this purpose. We consider three code manipulation and code generation tasks targeted by a range of traditional tools: (i) code mutation; (ii) test oracle generation from natural language documentation; and (iii) test case generation. For each task, we compare few-shot learning to a manually built tool. Our results show that the model-based tools complement (code mutation), are on par (test oracle generation), or even outperform their respective traditionally built tool (test case generation), while imposing far less effort to develop them. By comparing the effectiveness of different variants of the model-based tools, we provide insights on how to design an appropriate input ("prompt") to the model and what influence the size of the model has. For example, we find that providing a small natural language description of the code generation task is an easy way to improve predictions. Overall, we conclude that few-shot language models are surprisingly effective, yet there is still more work to be done, such as exploring more diverse ways of prompting and tackling even more involved tasks.
