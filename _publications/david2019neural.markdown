---
layout: publication
title: "Neural Reverse Engineering of Stripped Binaries"
authors: Yaniv David, Uri Alon, Eran Yahav
conference: ICLR
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1902.09122"}
tags: ["naming", "deobfuscation", "GNN"]
---
We address the problem of predicting procedure names in stripped executables which contain no debug information.
Predicting procedure names can dramatically ease the task of reverse engineering, saving precious time and human effort. 
We present a novel approach that leverages static analysis of binaries with encoder-decoder-based neural networks.
The main idea is to use static analysis to obtain enriched representations of API call sites; encode a set of sequences
of these call sites; and finally, attend to the encoded sequences while decoding the target name token-by-token. 
We evaluate our model by predicting procedure names over 60,000 procedures in 10,000 stripped executables.
Our model achieves 81.70 precision and 80.12 recall in predicting procedure names within GNU packages, and 55.48
precision and 51.31 recall in a diverse, cross-package, dataset. Comparing to previous approaches,
the predictions made by our model are much more accurate and informative. 
