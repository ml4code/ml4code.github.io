---
layout: default
title: A Survey of Machine Learning for Big Code and Naturalness
---
### Machine Learning on Source Code

The billions of lines of source code that have been written contain
implicit knowledge about how to write good code, code that is
easy to read and to debug.
A recent line of research aims to find statistical patterns in large
corpora of code to drive *new software development tools and program
analyses*.

This website and the accompanying [article](https://arxiv.org/abs/1709.06182) surveys the work in this emerging area.

Like writing and speaking, software development is an act of human communication.
At its core,
the naturalness of software employs statistical modeling over big code to
reason about rich variety of programs developers write.  This new line of
research is inherently interdisciplinary, uniting the machine learning and
natural language processing communities with software engineering
and programming language communities.

#### 🏷 Browse Papers by Tag
{% assign rawtags = Array.new %}
{% for publication in site.publications %}
  {% assign ttags = publication.tags  %}  
  {% assign rawtags = rawtags | concat: ttags %}  
{% endfor %}
{% assign rawtags = rawtags | uniq | sort_natural %}
{% for tag in rawtags %}<tag><a href="/tags.html#{{ tag }}">{{ tag }}</a></tag> {% endfor %}

### About This Site

This site is an experiment: a [living literature review](https://en.wikipedia.org/wiki/Living_review) that allows
you explore, [search and navigate]({% link papers.html %}) the literature in this area.
The full survey is available [as a research paper](https://arxiv.org/abs/1709.06182).
Please cite as
<pre>
@article{allamanis2018survey,
  title={A survey of machine learning for big code and naturalness},
  author={Allamanis, Miltiadis and Barr, Earl T and Devanbu, Premkumar and Sutton, Charles},
  journal={ACM Computing Surveys (CSUR)},
  volume={51},
  number={4},
  pages={81},
  year={2018},
  publisher={ACM}
}
</pre>

### Contributing

This research area is evolving so fast that a static review cannot keep up.
But a website can! We hope to make this site a living document.
Anyone can add a paper to this web site, essentially by creating one Markdown file.
 To contribute, open a pull request in GitHub, by following [these instructions 
for contributing](contributing.html).

### Contributors

The core survey and the original taxonomy was created by

* [Miltos Allamanis](https://miltos.allamanis.com) Microsoft Research, Cambridge, UK
* [Earl T. Barr](http://earlbarr.com) University College London, London, UK
* [Prem Devanbu](http://web.cs.ucdavis.edu/~devanbu/) University of California, Davis, USA
* [Charles Sutton](http://homepages.inf.ed.ac.uk/csutton/) University of Edinburgh and The Alan Turing Institute, UK

#### Contributors to the website
This website accepts external [contributions](/contributing.html).
Please, feel free to add your name below, once you contribute to this
website. A comprehensive list can be found [here](https://github.com/ml4code/ml4code.github.io/graphs/contributors).

* [Uri Alon](http://www.cs.technion.ac.il/~urialon/) Technion, Israel
* [Shaked Brody](https://shakedbr.cswp.cs.technion.ac.il/) Technion, Israel
* [Nghi D. Q. Bui](https://bdqnghi.github.io/) Singapore Management University, Singapore
* [Rajaswa Patil](https://rajaswa.github.io/) Microsoft PROSE
