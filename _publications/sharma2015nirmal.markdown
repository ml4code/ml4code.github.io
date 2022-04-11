---
layout: publication
title: "NIRMAL: Automatic Identification of Software Relevant Tweets Leveraging Language Model"
authors: Abhishek Sharma, Yuan Tian, David Lo
conference: SANER
year: 2015
tags: ["information extraction"]
---
Twitter is one of the most widely used social media
platforms today. It enables users to share and view short 140-character messages called “tweets”. About 284 million active
users generate close to 500 million tweets per day. Such rapid
generation of user generated content in large magnitudes results
in the problem of information overload. Users who are interested
in information related to a particular domain have limited means
to filter out irrelevant tweets and tend to get lost in the huge
amount of data they encounter. A recent study by Singer et
al. found that software developers use Twitter to stay aware of
industry trends, to learn from others, and to network with other
developers. However, Singer et al. also reported that developers
often find Twitter streams to contain too much noise which is a
barrier to the adoption of Twitter. In this paper, to help developers
cope with noise, we propose a novel approach named NIRMAL,
which automatically identifies software relevant tweets from a
collection or stream of tweets. Our approach is based on language
modeling which learns a statistical model based on a training
corpus (i.e., set of documents). We make use of a subset of posts
from StackOverflow, a programming question and answer site, as
a training corpus to learn a language model. A corpus of tweets
was then used to test the effectiveness of the trained language
model. The tweets were sorted based on the rank the model
assigned to each of the individual tweets. The top 200 tweets
were then manually analyzed to verify whether they are software
related or not, and then an accuracy score was calculated. The
results show that decent accuracy scores can be achieved by
various variants of NIRMAL, which indicates that NIRMAL can
effectively identify software related tweets from a huge corpus of
tweets.
