---
layout: publication
title: "A Factor Graph Model for Software Bug Finding"
authors: Ted Kremenek, Andrew Y. Ng, Dawson R. Engler. 
conference: IJCAI
year: 2007
tags: ["program analysis"]
---
Automatic tools for finding software errors require
knowledge of the rules a program must obey, or
“specifications,” before they can identify bugs. We
present a method that combines factor graphs and
static program analysis to automatically infer specifications directly from programs. We illustrate the
approach on inferring functions in C programs that
allocate and release resources, and evaluate the approach on three codebases: SDL, OpenSSH, and
the OS kernel for Mac OS X (XNU). The inferred
specifications are highly accurate and with them we
have discovered numerous bugs.

