---
layout: publication
title: "Graph-based, Self-Supervised Program Repair from Diagnostic Feedback"
authors: Michihiro Yasunaga, Percy Liang
conference: 
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2005.10636"}
tags: ["repair", "edit", "GNN"]
---
We consider the problem of learning to repair programs from diagnostic feedback (e.g., compiler error messages). Program repair is challenging for two reasons: First, it requires reasoning and tracking symbols across source code and diagnostic feedback. Second, labeled datasets available for program repair are relatively small. In this work, we propose novel solutions to these two challenges. First, we introduce a program-feedback graph, which connects symbols relevant to program repair in source code and diagnostic feedback, and then apply a graph neural network on top to model the reasoning process. Second, we present a self-supervised learning paradigm for program repair that leverages unlabeled programs available online to create a large amount of extra program repair examples, which we use to pre-train our models. We evaluate our proposed approach on two applications: correcting introductory programming assignments (DeepFix dataset) and correcting the outputs of program synthesis (SPoC dataset). Our final system, DrRepair, significantly outperforms prior work, achieving 66.1% full repair rate on DeepFix (+20.8% over the prior best), and 48.0% synthesis success rate on SPoC (+3.3% over the prior best). 
