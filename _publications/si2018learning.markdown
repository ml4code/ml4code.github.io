---
layout: publication
title: "Learning Loop Invariants for Program Verification"
authors: Xujie Si, Hanjun Dai, Mukund Raghothaman, Mayur Naik, Le Song
conference: NeurIPS
year: 2018
additional_links:
   - {name: "Preprint", url: "https://www.cis.upenn.edu/~mhnaik/papers/nips18.pdf"}
tags: ["program analysis", "verification"]
---
A fundamental problem in program verification concerns inferring loop invariants.
The problem is undecidable and even practical instances are challenging. Inspired
by how human experts construct loop invariants, we propose a reasoning framework
CODE2INV
that constructs the solution by multi-step decision making and querying
an external program graph memory block. By training with reinforcement learning,
CODE2INV
captures rich program features and avoids the need for ground truth
solutions as supervision.  Compared to previous learning tasks in domains with
graph-structured data, it addresses unique challenges, such as a binary objective
function and an extremely sparse reward that is given by an automated theorem
prover only after the complete loop invariant is proposed. We evaluate
CODE2INV on
a suite of 133 benchmark problems and compare it to three state-of-the-art systems.
It solves 106 problems compared to 73 by a stochastic search-based system, 77 by
a heuristic search-based system, and 100 by a decision tree learning-based system.
Moreover, the strategy learned can be generalized to new programs: compared to
solving new instances from scratch, the pre-trained agent is more sample efficient
in finding solutions.
