---
layout: publication
title: "PPM: Automated Generation of Diverse Programming Problems for Benchmarking Code Generation Models"
authors: Simin Chen, Xiaoning Feng, Xiaohong Han, Cong Liu, Wei Yang
conference: FSE 2024
year: 2024
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2401.15545"}
   - {name: "Code", url: "https://github.com/SeekingDream/PPM"}
tags: ["benchmarking", "evaluation"]
---
In recent times, a plethora of Large Code Generation Models (LCGMs) have been proposed, showcasing significant potential in assisting developers with complex programming tasks. Benchmarking LCGMs necessitates the creation of a set of diverse programming problems, and each problem comprises the prompt (including the task description), canonical solution, and test inputs. The existing methods for constructing such a problem set can be categorized into two main types: manual methods and perturbation-based methods. However, manual methods demand high effort and lack scalability, while also risking data integrity due to LCGMs' potentially contaminated data collection, and perturbation-based approaches mainly generate semantically homogeneous problems with the same canonical solutions and introduce typos that can be easily auto-corrected by IDE, making them ineffective and unrealistic. In this work, we propose the idea of programming problem merging (PPM) and provide two implementation of this idea, we utilize our tool on two widely-used datasets and compare it against nine baseline methods using eight code generation models. The results demonstrate the effectiveness of our tool in generating more challenging, diverse, and natural programming problems, comparing to the baselines.
