---
layout: publication
title: "A General Path-Based Representation for Predicting Program Properties"
authors: Uri Alon, Meital Zilberstein, Omer Levy, Eran Yahav
conference: PLDI
year: 2018
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1803.09544"}
tags: ["naming", "representation"]
---
Predicting program properties such as names or expression types has a wide range of applications. It can ease the task of programming and increase programmer productivity. A major challenge when learning from programs is how to represent programs in a way that facilitates effective learning. 
We present a general path-based representation for learning from programs. Our representation is purely syntactic and extracted automatically. The main idea is to represent a program using paths in its abstract syntax tree (AST). This allows a learning model to leverage the structured nature of code rather than treating it as a flat sequence of tokens. 
We show that this representation is general and can: (i) cover different prediction tasks, (ii) drive different learning algorithms (for both generative and discriminative models), and (iii) work across different programming languages. 
We evaluate our approach on the tasks of predicting variable names, method names, and full types. We use our representation to drive both CRF-based and word2vec-based learning, for programs of four languages: JavaScript, Java, Python and C#. Our evaluation shows that our approach obtains better results than task-specific handcrafted representations across different tasks and programming languages.
