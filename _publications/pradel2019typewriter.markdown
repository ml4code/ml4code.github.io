---
layout: publication
title: "TypeWriter: Neural Type Prediction with Search-based Validation"
authors: Michael Pradel, Georgios Gousios, Jason Liu, Satish Chandra.
conference:
year: 2019
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/1912.03768"}
tags: ["types", "bimodal"]
---
Maintaining large code bases written in dynamically typed languages, such as JavaScript or Python, can be challenging: simple data compatibility errors proliferate, IDE support is lacking and APIs are harder to comprehend. Recent work attempts to address those issues through either static analysis or probabilistic type inference. Unfortunately, static type inference for dynamic languages is inherently limited, while probabilistic approaches suffer from imprecision. This paper presents TypeWriter, the first combination of probabilistic prediction with search-based refinement of predicted types. TypeWriter's predictor learns to infer the return and argument types for functions from partially annotated code bases by combining the natural language properties of code with programming language-level information. To validate predicted types, TypeWriter invokes a gradual type checker with different combinations of the predicted types, while navigating the space of possible type combinations in a feedback-directed manner. We implement the TypeWriter approach for Python and evaluate it on two code corpora: a multi-million line code base at Facebook and a collection of 500 popular open-source projects. We show that TypeWriter's type predictor achieves a precision of 64% (91%) and a recall of 52% (68%) in the top-1 (top-5) predictions, and demonstrate that usage contexts are a helpful addition to neural type predictors. By combining predictions with search-based validation, TypeWriter can fully annotate between 42% to 64% of the files in a randomly selected corpus, while ensuring type correctness. A comparison with a static type inference tool shows that TypeWriter adds many more non-trivial types. Overall, TypeWriter provides developers with an effective way to help with the transition to fully type-annotated code. 
