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

---
<b><em><span style="color:red">HW3 (due date: Tuesday, October 14, AoE)</span></em></b>

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

---

- ***SIMPLE: Designing Imperative Programming Languages***
  - [SIMPLE untyped, statically typed, and dynamically typed](https://github.com/runtimeverification/pl-tutorial/tree/master/2_languages/1_simple).
  - [K Tutorial, Part 5: Defining type systems](https://github.com/runtimeverification/pl-tutorial/tree/master/1_k/5_types) (this is optional at this stage, but instructive for better understanding the static semantics; read at least Lesson 1, and skim Lesson 6).
  - [K Overview]({{site.baseurl}}/assets/CS422-K-Overview.pdf) paper, which also defines and explains SIMPLE. Sections 3 and 4 (the other sections were covered above)

---
<b><em><span style="color:red">HW4 (due date: Thursday, Nov 6st, AoE</span></em></b>

***Exercise 1 (10 points):*** Add `break;` and `continue;` to untyped SIMPLE. Just take the semantics of these from C/C++/Java, if uncertain. Do only the simple, unlabeled ones, which only break/continue the innermost loop. One thing to think about: do you still want to desugar the for-loop into a while-loop as we do it now?

Note: See the [break-continue](https://github.com/runtimeverification/pl-tutorial/tree/master/2_languages/1_simple/1_untyped/exercises/break-continue) exercise for untyped SIMPLE in the nightly built for details and test programs.

***Exercise 2 (10 points):*** Our current exceptions in SIMPLE are quite simplistic: the thrown exceptional value is caught by the innermost try-catch statement, and you get a runtime error (stuck) if the type of the thrown value is not the same as the type of the exception's parameter. They work fine if you restrict them to only throw and catch integer values, like we did in the static semantics, but modern languages do not like this limitation. Change the existing dynamic semantics of typed SIMPLE to propagate a thrown exception to the outer try-catch statement when the inner one cannot handle the exception due to a type mismatch. For example, `try { try { throw 7; } catch(bool x) {print(1};} } catch{int x) {print(2);}` should print 2, not get stuck as it currently happens.

Note: See the [typed-exceptions](https://github.com/runtimeverification/pl-tutorial/tree/master/2_languages/1_simple/2_typed/2_dynamic/exercises/typed-exceptions) exercise for dynamically typed SIMPLE in the nightly built for details and test programs.

***Exercise 3 (10 points):*** Same as Pb2, but for the static semantics of the typed SIMPLE. For this exercise (but not for the previous one), modify also the syntax of SIMPLE to allow functions to declare what exceptions they can throw.

Note: See the [functions-with-throws](https://github.com/runtimeverification/pl-tutorial/tree/master/2_languages/1_simple/2_typed/1_static/exercises/functions-with-throws) exercise for statically typed SIMPLE in the nightly built for details and test programs.

***Exercise 4 (10 points):*** Compilers typically collect all the variables declared in a block and move them all in one place, renaming them appropriately everywhere to avoid name conflicts. Consequently, they do not like you to declare a variable twice in the same block. Modify the static semantics of SIMPLE to reject programs which declare the same variable twice in a block. Your resulting type system should get stuck when a variable is declared the second time.

Note: See the [no-duplicate-declarations](https://github.com/runtimeverification/pl-tutorial/tree/master/2_languages/1_simple/2_typed/1_static/exercises/no-duplicate-declarations) exercise for statically typed SIMPLE in the nightly built for details and test programs.

For each of the problems, also provide one test program which should succeed and one which should fail. You will get two extra-points if any of your tests break everybody's definition (except potentially yours). If you handle more than one succeeding and one failing test, then I will randomly choose one of each.

---
- ***KOOL: Designing Object-Oriented Programming Languages***
  - [KOOL untyped, statically typed, and dynamically typed](https://github.com/runtimeverification/pl-tutorial/tree/master/2_languages/2_kool).
