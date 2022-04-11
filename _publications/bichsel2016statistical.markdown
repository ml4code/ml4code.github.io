---
layout: publication
title: "Statistical Deobfuscation of Android Applications"
authors: Benjamin Bichsel, Veselin Raychev, Petar Tsankov, Martin Vechev
conference: CCS
year: 2016
tags: ["deobfuscation", "naming"]
---
This work presents a new approach for deobfuscating Android APKs based on probabilistic learning of large code bases (termed "Big Code"). The key idea is to learn a probabilistic model over thousands of non-obfuscated Android applications and to use this probabilistic model to deobfuscate new, unseen Android APKs. The concrete focus of the paper is on reversing layout obfuscation, a popular transformation which renames key program elements such as classes, packages, and methods, thus making it difficult to understand what the program does. Concretely, the paper: (i) phrases the layout deobfuscation problem of Android APKs as structured prediction in a probabilistic graphical model, (ii) instantiates this model with a rich set of features and constraints that capture the Android setting, ensuring both semantic equivalence and high prediction accuracy, and (iii) shows how to leverage powerful inference and learning algorithms to achieve overall precision and scalability of the probabilistic predictions.

We implemented our approach in a tool called DeGuard and used it to: (i) reverse the layout obfuscation performed by the popular ProGuard system on benign, open-source applications, (ii) predict third-party libraries imported by benign APKs (also obfuscated by ProGuard), and (iii) rename obfuscated program elements of Android malware. The experimental results indicate that DeGuard is practically effective: it recovers 79.1% of the program element names obfuscated with ProGuard, it predicts third-party libraries with accuracy of 91.3%, and it reveals string decoders and classes that handle sensitive data in Android malware.

