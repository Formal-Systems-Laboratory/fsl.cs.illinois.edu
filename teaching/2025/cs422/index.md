---
layout: default
title: CS422 - Programming Language Design (Fall 2025)
---

# CS422 - Programming Language Design (Fall 2025)

Students enrolled in this class are expected to check this web page regularly. 
Complete lecture notes will be posted here, following the same model as in [CS422 in Fall 2024](https://fsl.cs.illinois.edu/teaching/2024/cs422/).

## Zoom Link

We may sometimes meet online on zoom, eg when traveling to professional events:
[https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)

### Lecture Recordings

When we meet online, we will record the lectures and post the links here:

[Aug 28]

## Course Description

CS422 is an advanced course on principles of programming language design. Major semantic approaches to programming languages will be discussed, such as structural operational semantics (various kinds), denotational semantics, and rewriting-based semantics. Programming language paradigms will be investigated and rigorously defined, including: imperative, functional, object-oriented, and logic programming languages; parameter binding and evaluation strategies; type checking and type inference; concurrency. Since the definitional framework used in this class will be executable, interpreters for the designed languages will be obtained for free. Software analysis tools reasoning about programs in these languages will also arise naturally. Major theoretical models will be discussed.

- Meetings: Tu/Th 12:30-13:45, Siebel 1214
- Credit: 3 or 4 credits
- Professor: [Grigore Rosu]({{site.baseurl}}/people/grigore-rosu/index.html) (Office: SC 2110)
- Office hours: Held by Grigore Rosu on Zoom or in SC 2110; by appointment.

## Lecture Notes, Useful Material

The links below provide you with useful material for this class, including complete lecture notes. These materials will be added by need.

- ***Introduction.*** [Slides](CS422-Fall-2025-01.pdf)
- ***Structural Operational Semantics.*** [Slides](CS422-Fall-2025-02-Conventional-Executable-Semantics.pdf)
  - Book lecture notes on the IMP language, big-step SOS, and small-step SOS (you can skip the rewriting logic and Maude parts; comments welcome!): [IMP-BigStep-SmallStep](CS422-Fall-2025-02a-IMP-BigStep-SmallStep.pdf)

---
<b><em><span style="color:red">HW1 (due date: Thursday, Sept 11th, AoE)</span></em></b>

***Exercise 1 (10 points):*** Modify IMP (its Big-Step and its Small-Step SOS) to halt when a division-by-zero takes place, returning a configuration holding the state in which the division by zero took place.

***Exercise 2 (10 points):*** Add a variable increment construct, `++x` (increment `x` and return the incremented value), to IMP: first add it to the formal BNF syntax, then to the Big-Step SOS, then to the type-system, and then to the Small-Step SOS.

***Exercise 3 (10 points):*** Add I/O constructs, `read()` and `print(AExp)` to IMP: first add these to the formal BNF syntax (`read()` is an `AExp` construct and `print(AExp)` is a `Stmt` construct), then to the Big-Step SOS, then to the type-system, and then to the Small-Step SOS.

***Exercise 4 (10 points):*** Combine the three above: add division-by-zero halting, an increment construct, and the two I/O constructs to IMP. Feel free to comment on what's going on, particularly on how inconvenient it is to do certain things in SOS (one of the points of this HW is to understand the limitations of SOS, so you will appreciate K).

---

- ***K Framework*** (Official website: [http://kframework.org](http://kframework.org); all generated from [Github repo](https://github.com/runtimeverification/k/tree/master/k-distribution/k-tutorial))
  - [K Tutorial, Section 1: Basic K Concepts](https://kframework.org/k-distribution/k-tutorial/1_basic/)
  - [K Tutorial, Section 2: Intermediate K Concept](https://kframework.org/k-distribution/k-tutorial/2_intermediate/)
  - [K User Manual](https://kframework.org/docs/user_manual/)
  
---
<b><em><span style="color:red">HW2 (due date: Thursday, Oct 2nd, AoE)</span></em></b>

Pick and do one exercise in each K Tutorial Lesson that we covered in class.  Create a github repo, possibly as a clone of the K tutorial, and add the exercises there in the appropriate folders using any naming convention you prefer.  When done, give me access to view your repo and send me an email to confirm that I have access.  My github ID is `grosu`.

---

- ***[PL Tutorial](https://github.com/runtimeverification/pl-tutorial/tree/master)***
  - [PL Tutorial, Part 1: Defining LAMBDA](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/1_lambda)
  - [PL Tutorial, Part 2: Defining IMP](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/2_imp)
  - [PL Tutorial, Part 3: Defining LAMBDA++](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B)
  - [PL Tutorial, Part 4: Defining IMP++](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/4_imp%2B%2B)
  - [K Overview]({{site.baseurl}}/assets/CS422-K-Overview.pdf) paper to learn more about K. Sections 1 and 2 (the other sections are optional now; they are covered below)
