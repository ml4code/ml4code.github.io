---
layout: publication
title: "Sorting and Transforming Program Repair Ingredients via Deep Learning Code Similarities"
authors: Martin White, Michele Tufano, Matias Martinez, Martin Monperrus, Denys Poshyvanyk
conference: SANER
year: 2017
tags: ["repair"]
---
In  the  field  of  automated  program  repair,  the  redundancy  assumption  claims  large  programs  contain  the  seeds
of  their  own  repair.  However,  most  redundancy-based  program
repair  techniques  do  not  reason  about  the  repair  ingredients—the code that is reused to craft a patch. We aim to reason about
the repair ingredients by using code similarities to prioritize and
transform  statements  in  a  codebase  for  patch  generation.  Our
approach,  DeepRepair,  relies  on  deep  learning  to  reason  about
code  similarities.  Code  fragments  at  well-defined  levels  of  granularity in a codebase can be sorted according to their similarity
to suspicious elements (i.e., code elements that contain suspicious
statements) and statements can be transformed by mapping out-of-scope  identifiers  to  similar  identifiers  in  scope.  We  examined
these new search strategies for patch generation with respect to
effectiveness  from  the  viewpoint  of  a  software  maintainer.  Our
comparative experiments were executed on six open-source Java
projects  including  374  buggy  program  revisions  and  consisted
of  19,949  trials  spanning  2,616  days  of  computation  time.  DeepRepair’s  search  strategy  using  code  similarities  generally  found
compilable  ingredients  faster  than  the  baseline,  jGenProg,  but
this improvement neither yielded test-adequate patches in fewer
attempts (on average) nor found significantly more patches than
the  baseline.  Although  the  patch  counts  were  not  statistically
different,  there  were  notable  differences  between  the  nature  of
DeepRepair  patches  and  baseline  patches.  The  results  demonstrate that our learning-based approach finds patches that cannot
be  found  by  existing  redundancy-based  repair  techniques
