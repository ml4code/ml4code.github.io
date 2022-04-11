---
layout: publication
title: "Recovering Variable Names for Minified Code with Usage Contexts"
authors: Hieu Tran, Ngoc Tran, Son Nguyen, Hoan Nguyen, Tien N. Nguyen
conference: ICSE
year: 2019
tags: ["naming", "deobfuscation"]
---
In modern Web technology, JavaScript (JS) code plays an important role. To avoid the exposure of original source code, the variable names in JS code deployed in the wild are often replaced by short, meaningless names, thus making the code extremely difficult to manually understand and analysis. This paper presents JSNeat, an information retrieval (IR)-based approach to recover the variable names in minified JS code. JSNeat follows a data-driven approach to recover names by searching for them in a large corpus of open-source JS code. We use three types of contexts to match a variable in given minified code against the corpus including the context of properties and roles of the variable, the context of that variable and relations with other variables under recovery, and the context of the task of the function to which the variable contributes. We performed several empirical experiments to evaluate JSNeat on the dataset of more than 322K JS files with 1M functions, and 3.5M variables with 176K unique variable names. We found that JSNeat achieves a high accuracy of 69.1%, which is the relative improvements of 66.1% and 43% over two state-of-the-art approaches JSNice and JSNaughty, respectively. The time to recover for a file or for a variable with JSNeat is twice as fast as with JSNice and 4x as fast as with JNaughty, respectively.