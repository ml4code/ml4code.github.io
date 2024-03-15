---
layout: publication
title: "RepoFusion: Training Code Models to Understand Your Repository"
authors: Disha Shrivastava, Denis Kocetkov, Harm de Vries, Dzmitry Bahdanau, Torsten Scholak
conference:
year: 2023
additional_links:
  - {name: "ArXiV", url: "https://arxiv.org/abs/2306.10998"}
tags: ["completion"]
---
Despite the huge success of Large Language Models (LLMs) in coding assistants like GitHub Copilot, these models struggle to understand the context present in the repository (e.g., imports, parent classes, files with similar names, etc.), thereby producing inaccurate code completions. This effect is more pronounced when using these assistants for repositories that the model has not seen during training, such as proprietary software or work-in-progress code projects. Recent work has shown the promise of using context from the repository during inference. In this work, we extend this idea and propose RepoFusion, a framework to train models to incorporate relevant repository context. Experiments on single-line code completion show that our models trained with repository context significantly outperform much larger code models as CodeGen-16B-multi ($\sim73\times$ larger) and closely match the performance of the $\sim 70\times$ larger StarCoderBase model that was trained with the Fill-in-the-Middle objective. We find these results to be a novel and compelling demonstration of the gains that training with repository context can bring. We carry out extensive ablation studies to investigate the impact of design choices such as context type, number of contexts, context length, and initialization within our framework. Lastly, we release Stack-Repo, a dataset of 200 Java repositories with permissive licenses and near-deduplicated files that are augmented with three types of repository contexts. Additionally, we are making available the code and trained checkpoints for our work. Our released resources can be found at \url{https://huggingface.co/RepoFusion}.
