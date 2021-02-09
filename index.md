---
layout: page
tag: k
---

Welcome to the **Formal Systems Laboratory (FSL)** of the [Department of Computer
Science] at the [University of Illinois at Urbana-Champaign] (UIUC). FSL was
founded in 2002 by [Grigore Rosu]({{site.baseurl}}people/grigore-rosu/index.html), when he joined UIUC 
(from [NASA Ames](http://www.nasa.gov/centers/ames/home/index.html)). 
In the FSL, we design and develop:

-   foundational and theoretical models,
-   specification and programming languages, techniques and methodologies,
    as well as
-   software analysis prototypes and tools,

all aiming at increasing the quality of computing systems. 

# Current Research Areas

- [Programming Language Design and Semantics]({{site.baseurl}}projects/pl/index.html)
- [Runtime Verification]({{site.baseurl}}projects/rv/index.html)
- [Behavioral Specification]({{site.baseurl}}projects/circ/index.html)

You want to work on these topics? See [Grigore Rosu]({{site.baseurl}}people/grigore-rosu/index.html)'s list of [Open Problems and Challenges]({{site.baseurl}}other-pages/open-problems.html).

# News

{% assign news = site.data.news | slice: 0,5 %}
{% for item in  news %} * **{{item.date}}:** {{item.markdown}}
{% endfor %} <!--  -->
* [All news](/fsl/news.html)


[Department of Computer Science]: https://cs.illinois.edu
[University of Illinois at Urbana-Champaign]: https://illinois.edu


