---
layout: default
title: CS422 - Programming Language Design (Fall 2024)
---

# CS422 - Programming Language Design (Fall 2024)

Students enrolled in this class are expected to check this web page regularly. 
Complete lecture notes will be posted here, following the same model as in [CS422 in Fall 2023](https://fsl.cs.illinois.edu/teaching/2023/cs422/).

## Zoom Link

We may sometimes meet online on zoom, eg when traveling to professional events:
[https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)

### Lecture Recordings

When we meet online, we will record the lectures and post the links here:

[Sept 3](https://illinois.zoom.us/rec/share/PbuJGlCTYhvCxTuDijRvFkaveC6eMExM7wMHEIyhtXTALqq3n9AZX8IIjqqsav9q.LawSiNxgJ5QhicQa)

## Course Description

CS422 is an advanced course on principles of programming language design. Major semantic approaches to programming languages will be discussed, such as structural operational semantics (various kinds), denotational semantics, and rewriting-based semantics. Programming language paradigms will be investigated and rigorously defined, including: imperative, functional, object-oriented, and logic programming languages; parameter binding and evaluation strategies; type checking and type inference; concurrency. Since the definitional framework used in this class will be executable, interpreters for the designed languages will be obtained for free. Software analysis tools reasoning about programs in these languages will also arise naturally. Major theoretical models will be discussed.

- Meetings: Tu/Th 12:30-13:45, Siebel 1214
- Credit: 3 or 4 credits
- Professor: [Grigore Rosu]({{site.baseurl}}/people/grigore-rosu/index.html) (Office: SC 2110)
- Office hours: Held by Grigore Rosu on Zoom or in SC 2110; by appointment.

## Lecture Notes, Useful Material

The links below provide you with useful material for this class, including complete lecture notes. These materials will be added by need.

- ***Introduction.*** [Slides](CS422-Fall-2024-01.pdf)
- ***Structural Operational Semantics.*** [Slides](CS422-Fall-2024-02-Conventional-Executable-Semantics.pdf)
  - Book lecture notes on the IMP language, big-step SOS, and small-step SOS (you can skip the rewriting logic and Maude parts; comments welcome!): [IMP-BigStep-SmallStep](CS422-Fall-2024-02a-IMP-BigStep-SmallStep.pdf)

---
<b><em><span style="color:red">HW1 (due date: Tuesday, Sept 17th, AoE)</span></em></b>

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
<b><em><span style="color:red">HW2 (due date: Tuesday, Oct 8th, AoE)</span></em></b>

Do the exercises in the K Tutorial.  They are spread through the lessons in Section 1, as well as in Section 2.1 (the other lessons are not finished yet).  Create a github repo, possibly as a clone of the K tutorial, and add the exercises there in the appropriate folders using any naming convention you prefer.  When done, give me access to view your repo and send me an email to confirm that I have access.  My github ID is `grosu`.

---

- ***[PL Tutorial](https://github.com/runtimeverification/pl-tutorial/tree/master)***
  - [PL Tutorial, Part 1: Defining LAMBDA](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/1_lambda)
  - [PL Tutorial, Part 2: Defining IMP](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/2_imp)
  - [PL Tutorial, Part 3: Defining LAMBDA++](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B)
  - [PL Tutorial, Part 4: Defining IMP++](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/4_imp%2B%2B)
  - [K Overview]({{site.baseurl}}/assets/CS422-K-Overview.pdf) paper to learn more about K. Sections 1 and 2 (the other sections are optional now; they are covered below)

---
<b><em><span style="color:red">HW3 (due date: Tuesday, October 22, AoE)</span></em></b>

***Exercise 1 (10 points):*** The current K LAMBDA semantics of mu (in Lesson 8) is based on substitution, and then letrec is defined as a derived operation using `mu`. Give `mu` a different semantics, as a derived construct by translation into other LAMBDA constructs, like we defined `letrec` in Lesson 7. To test it, use the same definition of letrec in terms of mu (from Lesson 8) and write 3 recursive programs, like the provided `factorial-letrec.lambda`.

Note: See the [mu-derived](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/1_lambda/lesson_8/exercises/mu-derived) exercise in the nightly built for details and test programs.

***Exercise 2 (10 points):*** Modify the K definition of IMP to not automatically initialize variables to 0. Instead, declared variables should stay uninitialized until assigned a value, and the execution should get stuck when an uninitialized variable is looked up.

Note: See the [uninitialized-variables](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/2_imp/lesson_4/exercises/uninitialized-variables) exercise in the nightly built for details and test programs.

***Exercise 3 (10 points):*** Mofify IMP so that the K "followed by" arrow, `~>`, does not explicitly occur in the definition (it currently occurs in the semantics of sequential composition). Hint: make sequential composition `strict(1)` or `seqstrict`, and have statements reduce to `{}` instead of `.`, ... and don't forget to make `{}` a `KResult` (you may need a new syntactic category for that, which only includes `{}` and is included in `KResult`).

Note: See the [purely-syntactic](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/2_imp/lesson_4/exercises/purely-syntactic) exercise in the nightly built for details and test programs.

***Exercise 4 (10 points):*** Define a variant of callcc, say callCC, which never returns to the current continuation unless a value is specifically passed to that continuation. Can you define them in terms of each other? Pick one of the substitution versus the environment-based definitions (get extra-credit if you do both).

Note: See the [callCC (substitution)](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B/lesson_1/exercises/callCC), 
[from-call-CC-to-callcc (substitution)](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B/lesson_1/exercises/from-call-CC-to-callcc), [from-callcc-to-call-CC(substitution)](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B/lesson_1/exercises/from-callcc-to-call-CC), 
[callCC (environment)](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B/lesson_6/exercises/callCC), 
[from-call-CC-to-callcc (environment)](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B/lesson_6/exercises/from-call-CC-to-callcc), and [from-callcc-to-call-CC (environment)](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/3_lambda%2B%2B/lesson_6/exercises/from-callcc-to-call-CC) exercises in the nightly built for details and test programs.

***Exercise 5 (10 points):*** The current `halt;` statement of IMP++ only halts the current thread.  Define an `abort;` statement which halts the entire program.
