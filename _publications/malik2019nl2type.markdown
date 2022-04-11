---
layout: publication
title: "NL2Type: Inferring JavaScript Function Types from Natural Language Information"
authors: Rabee Sohail Malik, Jibesh Patra, Michael Pradel
conference: ICSE
year: 2019
tags: ["bimodal", "types"]
---
JavaScript is dynamically typed and hence lacks thetype safety  of  statically  typed  languages,
leading  to  suboptimal IDE support, difficult to understand APIs, and unexpected run-time behavior.
Several gradual type systems have been proposed, e.g., Flow and TypeScript, but they rely on developers
to annotatecode with types. This paper presents NL2Type, a learning-based approach for predicting likely
type signatures of JavaScript functions. The key idea is to exploit natural language information in
source code, such as comments, function names, and parameternames,  a  rich  source  of  knowledge
that  is  typically  ignored by  type  inference  algorithms.  We  formulate  the  problem  of predicting
types as a classification problem and train a recurrent, LSTM-based neural model that, after learning
from an annotatedcode  base,  predicts  function  types  for  unannotated  code.  We evaluate   the 
approach   with   a   corpus   of   162,673   JavaScript files  from  real-world  projects. 
NL2Type  predicts  types  with  aprecision of 84.1% and a recall of 78.9% when considering only
the  top-most  suggestion,  and  with  a  precision  of  95.5%  and  arecall  of  89.6%  when
considering  the  top-5  suggestions.  The
approach  outperforms  both  JSNice,  a  state-of-the-art  approach that  analyzes  implementations 
of  functions  instead  of  natural language  information,  and  DeepTyper,  a  recent  type  prediction
approach that is also based on deep learning. Beyond predicting types,  NL2Type  serves  as  a
consistency  checker  for  existing type  annotations.  We  show  that  it  discovers  39  inconsistencies
that  deserve  developer  attention  (from  a  manual  analysis  of  50 warnings), most of which 
are due to incorrect type annotations.
