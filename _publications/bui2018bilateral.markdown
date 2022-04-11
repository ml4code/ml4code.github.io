---
layout: publication
title: "Bilateral Dependency Neural Networks for Cross-Language Algorithm Classification"
authors: Nghi D. Q. Bui, Yijun Yu, Lingxiao Jiang
conference: SANER
year: 2018
additional_links:
   - {name: "TR", url: "http://oro.open.ac.uk/58410/1/bui19saner.pdf"}
tags: ["representation"]
---
Algorithm  classification  is  to  automatically  identify
the  classes  of  a  program  based  on  the  algorithm(s)  and/or  data
structure(s)  implemented  in  the  program.  It  can  be  useful  for
various tasks, such as code reuse, code theft detection, and malware detection. Code similarity metrics, on the basis of features
extracted from syntax and semantics, have been used to classify
programs.  Such  features,  however,  often  need  manual  selection
effort  and  are  specific  to  individual  programming  languages,
limiting  the  classifiers  to  programs  in  the  same  language.
To recognize the similarities and differences among algorithms
implemented   in   different   languages,   this   paper   describes   a
framework  of  Bilateral  Neural  Networks  (Bi-NN)  that  builds  a
neural  network  on  top  of  two  underlying  sub-networks,  each  of
which encodes syntax and semantics of code in one language. A
whole  Bi-NN  can  be  trained  with  bilateral  programs  that  implement the same algorithms and/or data structures in different
languages  and  then  be  applied  to  recognize  algorithm  classes
across  languages.

We  have  instantiated  the  framework  with  several  kinds  of
token-,  tree-  and  graph-based  neural  networks  that  encode  and
learn  various  kinds  of  information  in  code.  We  have  applied
the  instances  of  the  framework  to  a  code  corpus  collected  from
GitHub containing thousands of Java and C++ programs imple-
menting 50 different algorithms and data structures. Our evalua-
tion results show that the use of Bi-NN indeed produces promising
algorithm  classification  results  both  within  one  language  and
across  languages,  and  the  encoding  of  dependencies  from  code
into  the  underlying  neural  networks  helps  improve  algorithm
classification  accuracy  further.  In  particular,  our  custom-built
dependency trees with tree-based convolutional neural networks
achieve  the  highest  classification  accuracy  among  the  different
instances  of  the  framework  that  we  have  evaluated.  Our  study
points  to  a  possible  future  research  direction  to  tailor  bilateral
and  multilateral  neural  networks  that  encode  more  relevant
semantics  for  code  learning,  mining  and  analysis  tasks
