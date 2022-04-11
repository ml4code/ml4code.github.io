---
layout: publication
title: "Learning to Sport and Refactor Inconsistent Method Names"
authors: Kui Liu, Dongsun Kim, Tegawendé F. Bissyandé, Taeyoung Kim, Kisub Kim, Anil Koyuncu, Suntae Kim, Yves Le Traon
conference: ICSE
year: 2019
tags: ["naming"]
---
To ensure code readability and facilitate software maintenance, program methods must be named properly. In particular, method names must be consistent with the corresponding method implementations. Debugging method names remains an important topic in the literature, where various approaches analyze commonalities among method names in a large dataset to detect inconsistent method names and suggest better ones. We note that the state-of-the-art does not analyze the implemented code itself to assess consistency. We thus propose a novel automated approach to debugging method names based on the analysis of consistency between method names and method code. The approach leverages deep feature representation techniques adapted to the nature of each artifact. Experimental results on over 2.1 million Java methods show that we can achieve up to 15 percentage points improvement over the state-of-the-art, establishing a record performance of 67.9% F1-measure in identifying inconsistent method names. We further demonstrate that our approach yields up to 25% accuracy in suggesting full names, while the state-of-the-art lags far behind at 1.1% accuracy. Finally, we report on our success in fixing 66 inconsistent method names in a live study on projects in the wild.