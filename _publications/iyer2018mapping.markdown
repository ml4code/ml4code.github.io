---
layout: publication
title: "Mapping Language to Code in Programmatic Context"
authors: Srinivasan Iyer, Ioannis Konstas, Alvin Cheung, Luke Zettlemoyer
conference: EMNLP
year: 2018
tags: ["bimodal", "code generation"]
---
Source code is rarely written in isolation. It depends significantly on the programmatic context, such as the class that the code would reside in. To study this phenomenon, we introduce the task of generating class member functions given English documentation and the programmatic context provided by the rest of the class. This task is challenging because the desired code can vary greatly depending on the functionality the class provides (e.g., a sort function may or may not be available when we are asked to "return the smallest element" in a particular member variable list). We introduce CONCODE, a new large dataset with over 100,000 examples consisting of Java classes from online code repositories, and develop a new encoder-decoder architecture that models the interaction between the method documentation and the class environment. We also present a detailed error analysis suggesting that there is significant room for future work on this task.
