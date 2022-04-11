---
layout: publication
title: "Neuro-symbolic program corrector for introductory programming assignments"
authors: Sahil Bhatia, Pushmeet Kohli, Rishabh Singh
conference: ICSE
year: 2018
tags: ["repair"]
---
Automatic correction of programs is a challenging problem with numerous real world applications in security, verification, and education. One application that is becoming increasingly important is the correction of student submissions in online courses for providing feedback. Most existing program repair techniques analyze Abstract Syntax Trees (ASTs) of programs, which are unfortunately unavailable for programs with syntax errors. In this paper, we propose a novel Neuro-symbolic approach that combines neural networks with constraint-based reasoning. Specifically, our method first uses a Recurrent Neural Network (RNN) to perform syntax repairs for the buggy programs; subsequently, the resulting syntactically-fixed programs are repaired using constraint-based techniques to ensure functional correctness. The RNNs are trained using a corpus of syntactically correct submissions for a given programming assignment, and are then queried to fix syntax errors in an incorrect programming submission by replacing or inserting the predicted tokens at the error location. We evaluate our technique on a dataset comprising of over 14,500 student submissions with syntax errors. Our method is able to repair syntax errors in 60% (8689) of submissions, and finds functionally correct repairs for 23.8% (3455) submissions.
