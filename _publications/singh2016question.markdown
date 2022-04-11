---
layout: publication
title: "Question Independent Grading using Machine Learning: The Case of Computer Program Grading"
authors: Gursimran Singh, Shashank Srikant, Varun Aggarwal
conference: KDD
year: 2016
additional_links:
   - {name: "PDF", url: "https://dl.acm.org/citation.cfm?id=2939696"}
   - {name: "website", url: "http://research.aspiringminds.com/"}
tags: ["education"]
---
Learning supervised models to grade open-ended responses is an expensive process. A model has to be trained for every prompt/question separately, which in turn requires graded samples. In automatic programming evaluation specifically, the focus of this work, this issue is amplified. The models have to be trained not only for every question but also for every language the question is offered in. Moreover, the availability and time taken by experts to create a labeled set of programs for each question is a major bottleneck in scaling such a system. We address this issue by presenting a method to grade computer programs which requires no manually assigned labeled samples for grading responses to a new, unseen question. We extend our previous work (by Srikant, Aggarwal; KDD 2014) wherein we introduced a grammar of features to learn question specific models. In this work, we propose a method to transform those features into a set of features that maintain their structural relation with the labels across questions. Using these features we learn one supervised model, across questions for a given language, which can then be applied to an ungraded response to an unseen question. We show that our method rivals the performance of both, question specific models and the consensus among human experts while substantially outperforming extant ways of evaluating codes. We demonstrate the system single s value by deploying it to grade programs in a high stakes assessment. The learning from this work is transferable to other grading tasks such as math question grading and also provides a new variation to the supervised learning approach.
