---
layout: publication
title: "Automated Correction for Syntax Errors in Programming Assignments using Recurrent Neural Networks"
authors: Sahil Bhatia, Rishabh Singh
conference: 
year: 2016
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1603.06129"}
tags: ["repair"]
---
We present a method for automatically generating repair feedback for syntax errors for introductory programming problems. Syntax errors constitute one of the largest classes of errors (34%) in our dataset of student submissions obtained from a MOOC course on edX. The previous techniques for generating automated feedback on programming assignments have focused on functional correctness and style considerations of student programs. These techniques analyze the program AST of the program and then perform some dynamic and symbolic analyses to compute repair feedback. Unfortunately, it is not possible to generate ASTs for student programs with syntax errors and therefore the previous feedback techniques are not applicable in repairing syntax errors. We present a technique for providing feedback on syntax errors that uses Recurrent neural networks (RNNs) to model syntactically valid token sequences. Our approach is inspired from the recent work on learning language models from Big Code (large code corpus). For a given programming assignment, we first learn an RNN to model all valid token sequences using the set of syntactically correct student submissions. Then, for a student submission with
syntax errors, we query the learnt RNN model with the prefix token sequence to predict token sequences that can fix the error by either replacing or inserting the predicted token sequence at the error location. We evaluate our technique on over 14, 000 student submissions with syntax errors. Our technique can completely repair 31.69% (4501/14203) of submissions with syntax errors and in addition partially correct 6.39% (908/14203) of the submissions.
