---
layout: publication
title: "Embedding Java Classes with code2vec: Improvements from Variable Obfuscation"
authors: Rhys Compton, Eibe Frank, Panos Patros, Abigail Koay
conference: MSR
year: 2020
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2004.02942"}
tags: ["naming", "adversarial"]
---
Automatic source code analysis in key areas of software engineering, such as code security, can benefit from Machine Learning (ML). However, many standard ML approaches require a numeric representation of data and cannot be applied directly to source code. Thus, to enable ML, we need to embed source code into numeric feature vectors while maintaining the semantics of the code as much as possible. code2vec is a recently released embedding approach that uses the proxy task of method name prediction to map Java methods to feature vectors. However, experimentation with code2vec shows that it learns to rely on variable names for prediction, causing it to be easily fooled by typos or adversarial attacks. Moreover, it is only able to embed individual Java methods and cannot embed an entire collection of methods such as those present in a typical Java class, making it difficult to perform predictions at the class level (e.g., for the identification of malicious Java classes). Both shortcomings are addressed in the research presented in this paper. We investigate the effect of obfuscating variable names during the training of a code2vec model to force it to rely on the structure of the code rather than specific names and consider a simple approach to creating class-level embeddings by aggregating sets of method embeddings. Our results, obtained on a challenging new collection of source-code classification problems, indicate that obfuscating variable names produces an embedding model that is both impervious to variable naming and more accurately reflects code semantics. The datasets, models, and code are shared for further ML research on source code. 
