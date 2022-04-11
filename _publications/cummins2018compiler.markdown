---
layout: publication
title: "Compiler Fuzzing through Deep Learning"
authors: Chris Cummins, Pavlos Petoumenos, Alastair Murray, Hugh Leather
conference: ISSTA
year: 2018
tags: ["fuzzing", "code generation"]
---
Random program generation — fuzzing — is an effective technique
for discovering bugs in compilers but successful fuzzers require
extensive development effort for every language supported by the
compiler, and often leave parts of the language space untested.

We introduce DeepSmith, a novel machine learning approach
to accelerating compiler validation through the inference of generative models for compiler inputs. Our approach
infers a learned
model of the structure of real world code based on a large corpus of open source code. Then, it uses the model to automatically
generate tens of thousands of realistic programs. Finally, we apply
established differential testing methodologies on them to expose
bugs in compilers. We apply our approach to the OpenCL programming language, automatically exposing bugs with little effort on our
side. In 1,000 hours of automated testing of commercial and open
source compilers, we discover bugs in all of them, submitting 67
bug reports. Our test cases are on average two orders of magnitude
smaller than the state-of-the-art, require 3.03× less time to generate
and evaluate, and expose bugs which the state-of-the-art cannot.
Our random program generator, comprising only 500 lines of code,
took 12 hours to train for OpenCL versus the state-of-the-art taking
9 man months to port from a generator for C and 50,000 lines of
code. With 18 lines of code we extended our program generator to
a second language, uncovering crashes in Solidity compilers in 12
hours of automated testing.
