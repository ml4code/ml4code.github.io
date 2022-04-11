---
layout: publication
title: "Type4Py: Deep Similarity Learning-Based Type Inference for Python"
authors: Amir M. Mir, Evaldas Latoskinas, Sebastian Proksch, Georgios Gousios
conference:
year: 2021
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2101.04470"}
   - {name: "GitHub", url: "https://github.com/saltudelft/type4py"}
tags: ["types"]
---
Dynamic languages, such as Python and Javascript, trade static typing for developer flexibility. While this allegedly enables greater productivity, lack of static typing can cause runtime exceptions, type inconsistencies, and is a major factor for weak IDE support. To alleviate these issues, PEP 484 introduced optional type annotations for Python. As retrofitting types to existing codebases is error-prone and laborious, learning-based approaches have been proposed to enable automatic type annotations based on existing, partially annotated codebases. However, the prediction of rare and user-defined types is still challenging. In this paper, we present Type4Py, a deep similarity learning-based type inference model for Python. We design a hierarchical neural network model that learns to discriminate between types of the same kind and dissimilar types in a high-dimensional space, which results in clusters of types. Nearest neighbor search suggests likely type signatures of given Python functions. The types visible to analyzed modules are surfaced using lightweight dependency analysis. The results of quantitative and qualitative evaluation indicate that Type4Py significantly outperforms state-of-the-art approaches at the type prediction task. Considering the Top-1 prediction, Type4Py obtains 19.33% and 13.49% higher precision than Typilus and TypeWriter, respectively, while utilizing a much bigger vocabulary. 
