---
layout: publication
title: "Source Code Classification for Energy Efficiency in Parallel Ultra Low-Power Microcontrollers"
authors: Emanuele Parisi, Francesco Barchi, Andrea Bartolini, Giuseppe Tagliavini, Andrea Acquaviva
conference: DATE
year: 2021
additional_links:
   - {name: "IEEE", url: "https://ieeexplore.ieee.org/document/9474085"}
   - {name: "ArXiV", url: "https://arxiv.org/abs/2012.06836"}
tags: ["optimization", "program analysis"]
---
The analysis of source code through machine learning techniques is an increasingly explored research topic aiming at increasing smartness in the software toolchain to exploit modern architectures in the best possible way. In the case of low-power, parallel embedded architectures, this means finding the configuration, for instance in terms of the number of cores, leading to minimum energy consumption. Depending on the kernel to be executed, the energy optimal scaling configuration is not trivial. While recent work has focused on general-purpose systems to learn and predict the best execution target in terms of the execution time of a snippet of code or kernel (e.g. offload OpenCL kernel on multicore CPU or GPU), in this work we focus on static compile-time features to assess if they can be successfully used to predict the minimum energy configuration on PULP, an ultra-low-power architecture featuring an on-chip cluster of RISC-V processors. Experiments show that using machine learning models on the source code to select the best energy scaling configuration automatically is viable and has the potential to be used in the context of automatic system configuration for energy minimisation.