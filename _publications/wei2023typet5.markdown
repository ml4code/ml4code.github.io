---
layout: publication
title: "TypeT5: Seq2seq Type Inference using Static Analysis"
authors: Jiayi Wei, Greg Durrett, Isil Dillig
conference: ICLR
year: 2023
additional_links:
   - {name: "ArXiV", url: "https://arxiv.org/abs/2303.09564"}
tags: ["types", "Transformer"]
---
There has been growing interest in automatically predicting missing type annotations in programs written in Python and JavaScript. While prior methods have achieved impressive accuracy when predicting the most common types, they often perform poorly on rare or complex types. In this paper, we present a new type inference method that treats type prediction as a code infilling task by leveraging CodeT5, a state-of-the-art seq2seq pre-trained language model for code. Our method uses static analysis to construct dynamic contexts for each code element whose type signature is to be predicted by the model. We also propose an iterative decoding scheme that incorporates previous type predictions in the model's input context, allowing information exchange between related code elements. Our evaluation shows that the proposed approach, TypeT5, not only achieves a higher overall accuracy (particularly on rare and complex types) but also produces more coherent results with fewer type errors -- while enabling easy user intervention. 
