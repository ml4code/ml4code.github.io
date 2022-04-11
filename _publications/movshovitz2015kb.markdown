---
layout: publication
title: "KB-LDA: Jointly Learning a Knowledge Base of Hierarchy, Relations, and Facts"
authors: Dana Movshovitz-Attias, William W. Cohen
conference: ACL
year: 2015
tags: ["pattern mining"]
---
Many existing knowledge bases (KBs), including Freebase, Yago, and NELL, rely
on a fixed ontology, given as an input
to the system, which defines the data to
be cataloged in the KB, i.e., a hierarchy of categories and relations between
them. The system then extracts facts that
match the predefined ontology. We propose an unsupervised model that jointly
learns a latent ontological structure of an
input corpus, and identifies facts from the
corpus that match the learned structure.
Our approach combines mixed membership stochastic block models and topic
models to infer a structure by jointly modeling text, a latent concept hierarchy, and
latent semantic relationships among the
entities mentioned in the text. As a case
study, we apply the model to a corpus
of Web documents from the software domain, and evaluate the accuracy of the various components of the learned ontology.
