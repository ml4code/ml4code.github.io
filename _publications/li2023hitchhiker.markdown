---
layout: publication
title: "The Hitchhiker's Guide to Program Analysis: A Journey with Large Language Models"
authors: Haonan Li, Yu Hao, Yizhuo Zhai, Zhiyun Qian
conference:
year: 2023
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2308.00245"}
tags: ["static analysis"]
---
Static analysis is a widely used technique in software engineering for identifying and mitigating bugs. However, a significant hurdle lies in achieving a delicate balance between precision and scalability. Large Language Models (LLMs) offer a promising alternative, as recent advances demonstrate remarkable capabilities in comprehending, generating, and even debugging code. Yet, the logic of bugs can be complex and require sophisticated reasoning and a large analysis scope spanning multiple functions. Therefore, at this point, LLMs are better used in an assistive role to complement static analysis. In this paper, we take a deep dive into the open space of LLM-assisted static analysis, using use-before-initialization (UBI) bugs as a case study. To this end, we develop LLift, a fully automated agent that interfaces with both a static analysis tool and an LLM. By carefully designing the agent and the prompts, we are able to overcome a number of challenges, including bug-specific modeling, the large problem scope, the non-deterministic nature of LLMs, etc. Tested in a real-world scenario analyzing nearly a thousand potential UBI bugs produced by static analysis, LLift demonstrates an extremely potent capability, showcasing a high precision (50%) and recall rate (100%). It even identified 13 previously unknown UBI bugs in the Linux kernel. This research paves the way for new opportunities and methodologies in the use of LLMs for bug discovery in extensive, real-world datasets.
