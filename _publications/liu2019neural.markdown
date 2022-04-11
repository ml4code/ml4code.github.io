---
layout: publication
title: "Neural query expansion for code search"
authors: Jason Liu, Seohyun Kim, Vijayaraghavan Murali, Swarat Chaudhuri, Satish Chandra
conference: MAPL
year: 2019
tags: ["search"]
---
Searching repositories of existing source code for code snippets is a key task in software engineering. Over the years, many approaches to this problem have been proposed. One recent tool called NCS, takes in a natural language query and outputs relevant code snippets, often being able to correctly answer Stack Overflow questions. But what happens when the developer doesn’t provide a query with a clear intent? What if shorter queries are used to demonstrate a more vague intent? 

We find that the performance of NCS regresses with shorter queries. Furthermore, data from developers’ code search history logs shows that shorter queries have a less successful code search session: there are more query reformulations and more time is spent browsing the results. These observations lead us to believe that using NCS alone with short queries may not be productive enough. 

In this paper, we explore an additional way of using neural networks in code search: the automatic expansion of queries. We present NQE, a neural model that takes in a set of keywords and predicts a set of keywords to expand the query to NCS. NQE learns to predict keywords that co-occur with the query keywords in the underlying corpus, which helps expand the query in a productive way. Our results show that with query expansion, NQE + NCS is able to perform better than using NCS alone.
