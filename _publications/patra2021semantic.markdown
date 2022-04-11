---
layout: publication
title: "A Semantic Bug Seeding: A Learning-Based Approach for Creating Realistic Bugs"
authors: Jibesh Patra, Michael Pradel
conference: FSE
year: 2021
tags: ["repair", "edit"]
---
When working on techniques to address the wide-spread problem
of software bugs, one often faces the need for a large number of
realistic bugs in real-world programs. Such bugs can either help
evaluate an approach, e.g., in form of a bug benchmark or a suite
of program mutations, or even help build the technique, e.g., in
learning-based bug detection. Because gathering a large number ofreal bugs is difficult,
a common approach is to rely on automatically
seeded bugs. Prior work seeds bugs based on syntactic transformation patterns,
which often results in unrealistic bugs and typically 
cannot introduce new, application-specific code tokens. This paper
presents SemSeed, a technique for automatically seeding bugs in
a semantics-aware way. The key idea is to imitate how a given
real-world bug would look like in other programs by semantically
adapting the bug pattern to the local context. To reason about the
semantics of pieces of code, our approach builds on learned token embeddings
that encode the semantic similarities of identifiers and literals. Our
evaluation with real-world JavaScript softwares
hows that the approach effectively reproduces real bugs and clearly
outperforms a semantics-unaware approach. The seeded bugs are
useful as training data for learning-based bug detection, where
they significantly improve the bug detection ability. Moreover, we
show that SemSeed-created bugs complement existing mutation
testing operators, and that our approach is efficient enough to seed
hundreds of thousands of bugs within an hour.
