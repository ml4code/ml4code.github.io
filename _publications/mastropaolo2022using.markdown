---
layout: publication
title: "Using Deep Learning to Generate Complete Log Statements"
authors: Antonio Mastropaolo, Luca Pascarella, Gabriele Bavota
conference:
year: 2022
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2201.04837"}
tags: ["Transformer", "logging"]
---
Logging is a practice widely adopted in several phases of the software lifecycle. For example, during software development log statements allow engineers to verify and debug the system by exposing fine-grained information of the running software. While the benefits of logging are undisputed, taking proper decisions about where to inject log statements, what information to log, and at which log level (e.g., error, warning) is crucial for the logging effectiveness. In this paper, we present LANCE (Log stAtemeNt reCommEnder), the first approach supporting developers in all these decisions. LANCE features a Text-To-Text-Transfer-Transformer (T5) model that has been trained on 6,894,456 Java methods. LANCE takes as input a Java method and injects in it a full log statement, including a human-comprehensible logging message and properly choosing the needed log level and the statement location. Our results show that LANCE is able to (i) properly identify the location in the code where to inject the statement in 65.9% of Java methods requiring it; (ii) selecting the proper log level in 66.2% of cases; and (iii) generate a completely correct log statement including a meaningful logging message in 15.2% of cases. 
