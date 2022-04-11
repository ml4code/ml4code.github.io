---
layout: publication
title: "Intelligent code reviews using deep learning"
authors: Anshul Gupta, Neel Sundaresan
conference: KDD
year: 2018
tags: ["representation", "review"]
---
Peer code review is a best practice in Software Engineering where source code is reviewed manually by one or more peers(reviewers) of the code author. It is widely acceptable both in industry and open-source software (OSS) systems as a process for early detection and reduction of software defects. A larger chunk of reviews given during peer reviews are related to common issues such as coding style, documentations, and best practices. This makes the code review process less effective as reviewers focus less on finding important defects. Hence, there is a need to automatically find such common issues and help reviewers perform focused code reviews. Some of this is solved by rule based systems called linters but they are rigid and needs a lot of manual effort to adapt them for a new issue.

In this work, we present an automatic, flexible, and adaptive code analysis system called DeepCodeReviewer (DCR). DCR learns how to recommend code reviews related to common issues using historical peer reviews and deep learning. DCR uses deep learning to learn review relevance to a code snippet and recommend the right review from a repository of common reviews. DCR is trained on histroical peer reviews available from internal code repositories at Microsoft. Experiments demonstrate strong performance of developed deep learning model in classifying relevant and non-relevant reviews w.r.t to a code snippet, and ranking reviews given a code snippet. We have also evaluated DCR recommentations using a user study and survey. The results of our user study show good acceptance rate and answers of our survey questions are strongly correlated with our system’s goal of making code reviews focused on finding defects.
