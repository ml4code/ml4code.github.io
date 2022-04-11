---
layout: publication
title: "SelfAPR: Self-supervised Program Repair with Test Execution Diagnostics"
authors: He Ye, Matias Martinez, Xiapu Luo, Tao Zhang, Martin Monperrus
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2203.12755"}
tags: ["repair", "execution"]
---
Neural program repair has achieved good results in a recent series of papers. Yet, we observe that the related work fails to repair some bugs because of a lack of knowledge about 1) the program being repaired, and 2) the actual fault being repaired. In this paper, we solve both problems by changing the learning paradigm from supervised training to self-supervised training in an approach called SelfAPR. First, SelfAPR generates and constructs training samples by perturbing a previous version of the program being repaired, enforcing the neural model to capture project-specific knowledge. This is different from all the existing work based on past commits. Second, SelfAPR extracts and encodes test execution diagnostics into the input representation, steering the neural model to fix the specific kind of fault. This is different from the existing studies that only consider static source code in the input. We implement SelfAPR and evaluate it in a systematic manner. We train SelfAPR with 253 411 training samples obtained by perturbing 17 open-source projects. We evaluate SelfAPR on 818 bugs from Defects4J, SelfAPR correctly repairs 112 of them. 
