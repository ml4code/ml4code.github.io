---
layout: publication
title: "Cross-Language Binary-Source Code Matching with Intermediate Representations"
authors: Yi Gui, Yao Wan, Hongyu Zhang, Huifang Huang, Yulei Sui, Guandong Xu, Zhiyuan Shao, Hai Jin
conference: SANER
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2201.07420"}
   - {name: "Code", url: "https://github.com/CGCL-codes/naturalcc"}
tags: ["code similarity", "clone"]
---
Binary-source code matching plays an important role in many security and software engineering related tasks such as malware detection, reverse engineering and vulnerability assessment. Currently, several approaches have been proposed for binary-source code matching by jointly learning the embeddings of binary code and source code in a common vector space. Despite much effort, existing approaches target on matching the binary code and source code written in a single programming language. However, in practice, software applications are often written in different programming languages to cater for different requirements and computing platforms. Matching binary and source code across programming languages introduces additional challenges when maintaining multi-language and multi-platform applications. To this end, this paper formulates the problem of cross-language binary-source code matching, and develops a new dataset for this new problem. We present a novel approach XLIR, which is a Transformer-based neural network by learning the intermediate representations for both binary and source code. To validate the effectiveness of XLIR, comprehensive experiments are conducted on two tasks of cross-language binary-source code matching, and cross-language source-source code matching, on top of our curated dataset. Experimental results and analysis show that our proposed XLIR with intermediate representations significantly outperforms other state-of-the-art models in both of the two tasks.
