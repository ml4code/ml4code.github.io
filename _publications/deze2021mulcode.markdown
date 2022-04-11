---
layout: publication
title: "MulCode: A Multi-task Learning Approach for Source Code Understanding"
authors: Deze Wang, Yue Yu, Shanshan Li, Wei Dong, Ji Wang, Liao Qing
conference: SANER
year: 2021
additional_links:
   - {name: "PDF", url: "https://yuyue.github.io/res/paper/mulcode_saner2021.pdf"}
tags: ["representation"]
---
Recent years have witnessed the significant rise of Deep Learning (DL) techniques applied to source code. Researchers exploit DL for a multitude of tasks and achieve impressive results. However, most tasks are explored separately, resulting in a lack of generalization of the solutions. In this work, we propose MulCode, a multi-task learning approach for source code understanding that learns unified representation space for tasks, with the pre-trained BERT model for the token sequence and the Tree-LSTM model for abstract syntax trees. Furthermore, we integrate two source code views into a hybrid representation via the attention mechanism and set learnable uncertainty parameters to adjust the tasks’ relationship. We train and evaluate MulCode in three downstream tasks: comment classification, author attribution, and duplicate function detection. In all tasks, MulCode outperforms the state-of-theart techniques. Moreover, experiments on three unseen tasks demonstrate the generalization ability of MulCode compared with state-of-the-art embedding methods.