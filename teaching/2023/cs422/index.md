---
layout: default
title: CS422 - Programming Language Design (Fall 2023)
---

# CS422 - Programming Language Design (Fall 2023)

Students enrolled in this class are expected to check this web page regularly. 
Complete lecture notes will be posted here.

## Zoom Link

[https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)

### Lecture Recordings

[Aug 29](https://illinois.zoom.us/rec/share/YF_yxlwPFwEt0ycyGhHNtc8lqLBm3aGQUWGBnBGjyaVncjTHPlzEKPBxk_41fGVk.5o6SUHkt8dpyv7RF)
[Sept 5](https://illinois.zoom.us/rec/share/0Zs4EKFBAIYZlhPFYfJE11oUYIuELzV20AJKbt3gkVaGQJiS-__5cqQKpLDP9yG4.eLre3mydJ7zjS6Fg)
[Oct 17](https://illinois.zoom.us/rec/share/lFqYsOz4GO4rwBFhEE3W2c7-vUjbqE6MF3B3_sHudixoR8VgvKn1Fnl81UukZwYW.CSH2BkBIuslILSHX)
[Oct 19](https://illinois.zoom.us/rec/share/GLv8EfgUmVn0dAufBntk-GGc37Zzm7kio_do7-ZlUcLVTCh7NvkWixfyyDRYs1wo.hWPyBh0bdoOf9-IK)
[Nov 14](https://illinois.zoom.us/rec/share/yk1AL52ZS3Lv8vUlGXNNt6jm3RbM1-hN5bX_JrfOseULf7BBA-uTDFGc-p-me2ee.Uf6ZV4Bf3JMgLvsn)
[Nov 16](https://illinois.zoom.us/rec/share/0lpzLqlhvgpjVp9oD2ogSpo8wl5HXqaB_243iLcpWIdk48Z1Y-KP1vyWZ-6pDRY_.lNY_yvUDjdxgOZAt)


## Course Description

CS422 is an advanced course on principles of programming language design. Major semantic approaches to programming languages will be discussed, such as structural operational semantics (various kinds), denotational semantics, and rewriting-based semantics. Programming language paradigms will be investigated and rigorously defined, including: imperative, functional, object-oriented, and logic programming languages; parameter binding and evaluation strategies; type checking and type inference; concurrency. Since the definitional framework used in this class will be executable, interpreters for the designed languages will be obtained for free. Software analysis tools reasoning about programs in these languages will also arise naturally. Major theoretical models will be discussed.

- Meetings: Tu/Th 12:30-13:45, hybrid --- Siebel 1214 and also [Online](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)
- Credit: 3 or 4 credits
- Professor: [Grigore Rosu]({{site.baseurl}}/people/grigore-rosu/index.html) (Office: SC 2110)
- Office hours: Held by Grigore Rosu on Zoom or in SC 2110; by appointment.

## Lecture Notes, Useful Material

The links below provide you with useful material for this class, including complete lecture notes. These materials will be added by need.

- ***Introduction.*** [Slides]({{site.baseurl}}/assets/CS422-Spring-2020-01.pdf)
- ***Structural Operational Semantics.*** [Slides]({{site.baseurl}}/assets/CS422-Spring-2020-02-Conventional-Executable-Semantics.pdf)
  - Book lecture notes on the IMP language, big-step SOS, and small-step SOS (you can skip the rewriting logic and Maude parts; comments welcome!): [IMP-BigStep-SmallStep]({{site.baseurl}}/assets/CS422-Spring-2020-02a-IMP-BigStep-SmallStep.pdf)


---
<b><em><span style="color:red">HW1 (due date: Thursday, Sept 7th, AoE)</span></em></b>

***Exercise 1 (10 points):*** Modify IMP (its Big-Step and its Small-Step SOS) to halt when a division-by-zero takes place, returning a configuration holding the state in which the division by zero took place.

***Exercise 2 (10 points):*** Add a variable increment construct, `++x` (increment `x` and return the incremented value), to IMP: first add it to the formal BNF syntax, then to the Big-Step SOS, then to the type-system, and then to the Small-Step SOS.

***Exercise 3 (10 points):*** Add I/O constructs, `read()` and `print(AExp)` to IMP: first add these to the formal BNF syntax (`read()` is an `AExp` construct and `print(AExp)` is a `Stmt` construct), then to the Big-Step SOS, then to the type-system, and then to the Small-Step SOS.

***Exercise 4 (10 points):*** Combine the three above: add division-by-zero halting, an increment construct, and the two I/O constructs to IMP. Feel free to comment on what's going on, particularly on how inconvenient it is to do certain things in SOS (one of the points of this HW is to understand the limitations of SOS, so you will appreciate K).

---

- ***K Framework*** (Official website: [http://kframework.org](http://kframework.org); all generated from [Github repo](https://github.com/runtimeverification/k/tree/master/k-distribution/pl-tutorial))
  - [K Tutorial, Part 1: Defining LAMBDA](https://kframework.org/k-distribution/pl-tutorial/) (see the provided video and textual documentation); Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/1_lambda) to see the code on GitHub. 
  - [K Tutorial, Part 2: Defining IMP](https://kframework.org/k-distribution/pl-tutorial/) (see the provided video and textual documentation); Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/2_imp) to see the code on GitHub. 
  - [K Tutorial, Part 3: Defining LAMBDA++](https://kframework.org/k-distribution/pl-tutorial/) (see the provided video and textual documentation); Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B) to see the code on GitHub. 
  - [K Tutorial, Part 4: Defining IMP++](https://kframework.org/k-distribution/pl-tutorial/) (see the provided video and textual documentation); Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/4_imp%2B%2B) to see the code on GitHub. 
  - [K Overview]({{site.baseurl}}/assets/CS422-K-Overview.pdf) paper to learn more about K. Sections 1 and 2 (the other sections are optional now; they are covered below)

---
<b><em><span style="color:red">HW2 (due date: Tuesday, September 26, AoE)</span></em></b>

***Exercise 1 (10 points):*** The current K LAMBDA semantics of mu (in Lesson 8) is based on substitution, and then letrec is defined as a derived operation using mu. Give mu a different semantics, as a derived construct by translation into other LAMBDA constructs, like we defined letrec in Lesson 7. To test it, use the same definition of letrec in terms of mu (from Lesson 8) and write 3 recursive programs, like the provided factorial-letrec.lambda.

Note: See the [mu-derived](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/1_lambda/lesson_8/exercises/mu-derived) exercise in the nightly built for details and test programs.

***Exercise 2 (10 points):*** Modify the K definition of IMP to not automatically initialize variables to 0. Instead, declared variables should stay uninitialized until assigned a value, and the execution should get stuck when an uninitialized variable is looked up.

Note: See the [uninitialized-variables](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/2_imp/lesson_4/exercises/uninitialized-variables) exercise in the nightly built for details and test programs.

***Exercise 3 (10 points):*** Mofify IMP so that the K "followed by" arrow, `~>`, does not explicitly occur in the definition (it currently occurs in the semantics of sequential composition). Hint: make sequential composition `strict(1)` or `seqstrict`, and have statements reduce to "{}" instead of ".", ... and don't forget to make "{}" a KResult (you may need a new syntactic category for that, which only includes "{}" and is included in KResult).

Note: See the [purely-syntactic](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/2_imp/lesson_4/exercises/purely-syntactic) exercise in the nightly built for details and test programs.

---
<b><em><span style="color:red">HW3 (due date: Thursday October 5, AoE)</span></em></b>

***Exercise 1 (10 points):*** Define a variant of callcc, say callCC, which never returns to the current continuation unless a value is specifically passed to that continuation. Can you define them in terms of each other? Do these in both the substitution and the environment-based definitions.

Note: See the [callCC (substitution)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_1/exercises/callCC), 
[from-call-CC-to-callcc (substitution)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_1/exercises/from-call-CC-to-callcc), [from-callcc-to-call-CC(substitution)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_1/exercises/from-callcc-to-call-CC), 
[callCC (environment)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_6/exercises/callCC), 
[from-call-CC-to-callcc (environment)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_6/exercises/from-call-CC-to-callcc), and [from-callcc-to-call-CC (environment)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_6/exercises/from-callcc-to-call-CC) exercises in the nightly built for details and test programs.

***Exercise 2 (10 points):*** The current `halt;` statement of IMP++ only halts the current thread.  Define an `abort;` statement which halts the entire program.

Note: See the [abort](https://github.com/runtimeverification/k/tree/master/k-distribution/pl-tutorial/1_k/4_imp%2B%2B/lesson_7/exercises/abort) exercise in the nightly built for details and test programs.

---

- ***Matching Logic - A Minimal Foundation for Programming Languages***
  - Optional, but informative.  Matching logic is the logic underlying K.
  - http://matching-logic.org
  - [Marktoberdorf Lecture Notes](https://events.model.in.tum.de/mod23/lectures.html)

---

- ***SIMPLE: Designing Imperative Programming Languages***
  - [SIMPLE untyped, statically typed, and dynamically typed](https://kframework.org/k-distribution/pl-tutorial/) (Part 7 of the K Tutorial). Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/1_simple) to see the code on GitHub.
  - [K Tutorial, Part 5: Defining type systems](https://kframework.org/k-distribution/pl-tutorial/) (this is optional at this stage, but instructive for better understanding the static semantics; read at least Lesson 1, and skim Lesson 6). Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/5_types) to see the code on GitHub. 
  - [K Overview]({{site.baseurl}}/assets/CS422-K-Overview.pdf) paper, which also defines and explains SIMPLE. Sections 3 and 4 (the other sections were covered above)

---
<b><em><span style="color:red">HW4 (due date: Tuesday, Oct 31st, AoE</span></em></b>

***Exercise 1 (10 points):*** Add `break;` and `continue;` to untyped SIMPLE. Just take the semantics of these from C/C++/Java, if uncertain. Do only the simple, unlabeled ones, which only break/continue the innermost loop. One thing to think about: do you still want to desugar the for-loop into a while-loop as we do it now?

Note: See the [break-continue](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/1_simple/1_untyped/exercises/break-continue) exercise for untyped SIMPLE in the nightly built for details and test programs.

***Exercise 2 (10 points):*** Our current exceptions in SIMPLE are quite simplistic: the thrown exceptional value is caught by the innermost try-catch statement, and you get a runtime error (stuck) if the type of the thrown value is not the same as the type of the exception's parameter. They work fine if you restrict them to only throw and catch integer values, like we did in the static semantics, but modern languages do not like this limitation. Change the existing dynamic semantics of typed SIMPLE to propagate a thrown exception to the outer try-catch statement when the inner one cannot handle the exception due to a type mismatch. For example, `try { try { throw 7; } catch(bool x) {print(1};} } catch{int x) {print(2);}` should print 2, not get stuck as it currently happens.

Note: See the [typed-exceptions](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/1_simple/2_typed/2_dynamic/exercises/typed-exceptions) exercise for dynamically typed SIMPLE in the nightly built for details and test programs.

***Exercise 3 (10 points):*** Same as Pb2, but for the static semantics of the typed SIMPLE. For this exercise (but not for the previous one), modify also the syntax of SIMPLE to allow functions to declare what exceptions they can throw.

Note: See the [functions-with-throws](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/1_simple/2_typed/1_static/exercises/functions-with-throws) exercise for statically typed SIMPLE in the nightly built for details and test programs.

***Exercise 4 (10 points):*** Compilers typically collect all the variables declared in a block and move them all in one place, renaming them appropriately everywhere to avoid name conflicts. Consequently, they do not like you to declare a variable twice in the same block. Modify the static semantics of SIMPLE to reject programs which declare the same variable twice in a block. Your resulting type system should get stuck when a variable is declared the second time.

Note: See the [no-duplicate-declarations](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/1_simple/2_typed/1_static/exercises/no-duplicate-declarations) exercise for statically typed SIMPLE in the nightly built for details and test programs.

For each of the problems, also provide one test program which should succeed and one which should fail. You will get two extra-points if any of your tests break everybody's definition (except potentially yours). If you handle more than one succeeding and one failing test, then I will randomly choose one of each.

---
- ***KOOL: Designing Object-Oriented Programming Languages***
  - [KOOL untyped, statically typed, and dynamically typed](https://kframework.org/k-distribution/pl-tutorial) (Part 8 of the K Tutorial). Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/2_kool) to see the code on GitHub. 

---
<b><em><span style="color:red">HW5 (due date: Tuesday, November 28, AoE)</span></em></b>

***Exercise 1 (10 points):*** Currently, all class members (fields and/or methods) are public in KOOL. Sometimes we want to keep members of a class private, in the sense that subclasses do not have direct access to those members. This exercise asks you to add private members to untyped KOOL. Syntactically, you should allow a new keyword, "private", to optionally prepend member declarations. For example, `private var x=10, y=10;` or `private method f(x,y) {...}`.

Note: See the [private-members](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/2_kool/1_untyped/exercises/private-members) exercise for untyped KOOL in the nightly built for details and test programs.

***Exercise 2 (10 points):*** Same as Exercise 1, but for dynamically typed KOOL.

Note: See the [private-members](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/2_kool/2_typed/1_dynamic/exercises/private-members) exercise for dynamically typed KOOL in the nightly built for details and test programs.

***Exercise 3 (10 points):*** Same as Eercises 1 and 2, but for statically typed KOOL.

Note: See the [private-members](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/2_kool/2_typed/2_static/exercises/private-members) exercise for statically typed KOOL in the nightly built for details and test programs.

---

- ***FUN: Designing Functional Programming Languages***
  - [FUN untyped](https://kframework.org/k-distribution/pl-tutorial/) (Part 9 of the K Tutorial, without the type inferencer). Click [here](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/2_languages/3_fun) to see the code on GitHub. 

---
---
... more to come ...
---
