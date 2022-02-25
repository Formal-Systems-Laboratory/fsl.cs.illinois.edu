---
layout: default
title: CS422 - Programming Language Design (Spring 2022)
---

# CS422 - Programming Language Design (Spring 2022)

Students enrolled in this class are expected to check this web page regularly. 
Complete lecture notes will be posted here.

## Zoom Link

[https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)

### Lecture Recordings

[Feb 25](https://illinois.zoom.us/rec/share/Hw2pkOjLs1tvIReSrk50oxOTlqUH81uBsVhhivE8l7PdddVyElnXiRo5zAN3Mw6B.2VJnoEYQ628XIruC?startTime=1645819308000)
[Feb 23](https://illinois.zoom.us/rec/share/um40ZMuLx6EXr2hvGQD_BpXvGvXBM-Mc8uvHpRE2AildDju32LpUSO2aTd_uflrt.Dk5StW4ylnD3VZ6d?startTime=1645646501000)
[Feb 18](https://illinois.zoom.us/rec/share/Z79h57mfB1zYJDxawDsotUqL6OB19AKbpu0aeshvl9EZLpO1UTY0UmUzi15OIqy-.3lxHmMeDHljehvV8?startTime=1645214483000)
[Feb 16](https://illinois.zoom.us/rec/share/hH_qwfpkDm9fBFJpc880JB2m440UrDdWrVbj_WZERet8SVmQXTJroa-9einL1wkC.XIrdpnGnUpcbT6k_?startTime=1645041500000)
[Feb 11](https://illinois.zoom.us/rec/share/GHHfvQr3q0l57KdI8x9OUCrp6kzt_Etil-M8-6Y9xw34_QkCWFL676tEtQlsomqX.kdKSTh2omuotBDs7?startTime=1644610038000)
[Feb 9](https://illinois.zoom.us/rec/share/LaB7CflkvxQ4Zs-VoRTZ91QwYZHKB8k356PFqK36QrCeLfE-y9uAvFnfyjkthiO5.mrm_EPx0tNDfaenF?startTime=1644437009000)
[Feb 9 whiteboard]({{site.baseurl}}/assets/CS422-Feb_9_whiteboard.jpg)
[Feb 4](https://illinois.zoom.us/rec/share/d7_AFFnzp3z_GWk3cdRXmOi0lyb_HPW2EkUFSaH8G-XmE6BINyzbpnbVAIlHjITL.XsF2F1FzfukbxAOs?startTime=1644004900000)
[Feb 2](https://illinois.zoom.us/rec/share/ZJwUdLcg3sTkIiylhyXLvQ3qPYWXbidXuDA5Yd25cRmM6wIBBrL_qWOxGY7e8S_X.aOSgYOrqlH8yHRUs?startTime=1643832156000) 
[Jan 28](https://illinois.zoom.us/rec/share/lz0ZOwGfDYLrDznX9UDFn53DeJuRRpCpGYlZ6dToT6yA1o9Q5inYGHwR1DqTtz5g.J7yUhEo7UOnlrd0u?startTime=1643400843000)
[Jan 26](https://illinois.zoom.us/rec/share/vqMewycqFFYZEMTyhDrxhS7aSGWDjubQokNj6CX2UE58l2LXGU7UYSqUuSm7n4Y-.gnOeZEjFPRqJOM9T?startTime=1643227356000)
[Jan 21](https://illinois.zoom.us/rec/share/BCUSRktliCEpiO4dkzLpdX3p9e4uh_VOcdK4vt3Y4_p4Zbr5riAbPXU_v1wIppjQ.fbfEnD9QzhwO9Mj9?startTime=1642795353000)
[Jan 19](https://illinois.zoom.us/rec/share/fiOmld9qHJ1W7HM6yHhYNe6PyHJ0k45blppXEkJJWG2Oi9RENx8lusN71dC-UmHc.CDCzsRL5XHuqFKom?startTime=1642622875000)

## Course Description

CS422 is an advanced course on principles of programming language design. Major semantic approaches to programming languages will be discussed, such as structural operational semantics (various kinds), denotational semantics, and rewriting-based semantics. Programming language paradigms will be investigated and rigorously defined, including: imperative, functional, object-oriented, and logic programming languages; parameter binding and evaluation strategies; type checking and type inference; concurrency. Since the definitional framework used in this class will be executable, interpreters for the designed languages will be obtained for free. Software analysis tools reasoning about programs in these languages will also arise naturally. Major theoretical models will be discussed.

- Meetings: W/F 14:00-15:15, hybrid --- Sidney Lu Mech Engr Bldg 1043 and also [Online](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)
- Credit: 3 or 4 credits
- Professor: [Grigore Rosu]({{site.baseurl}}/people/grigore-rosu/index.html) (Office: SC 2110)
- Office hours: Held by Grigore Rosu on Zoom or in SC 2110; by appointment.

## Lecture Notes, Useful Material

The links below provide you with useful material for this class, including complete lecture notes. These materials will be added by need.

- ***Introduction.*** [Slides]({{site.baseurl}}/assets/CS422-Spring-2020-01.pdf)
- ***Structural Operational Semantics.*** [Slides]({{site.baseurl}}/assets/CS422-Spring-2020-02-Conventional-Executable-Semantics.pdf)
  - Book lecture notes on the IMP language, big-step SOS, and small-step SOS (you can skip the rewriting logic and Maude parts; comments welcome!): [IMP-BigStep-SmallStep]({{site.baseurl}}/assets/CS422-Spring-2020-02a-IMP-BigStep-SmallStep.pdf)


---
<b><em><span style="color:red">HW1 (due date: Friday Feb 4, AoE)</span></em></b>

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
<b><em><span style="color:red">HW2 (due date: Friday February 18, AoE)</span></em></b>

***Exercise 1 (10 points):*** The current K LAMBDA semantics of mu (in Lesson 8) is based on substitution, and then letrec is defined as a derived operation using mu. Give mu a different semantics, as a derived construct by translation into other LAMBDA constructs, like we defined letrec in Lesson 7. To test it, use the same definition of letrec in terms of mu (from Lesson 8) and write 3 recursive programs, like the provided factorial-letrec.lambda.

Note: See the [mu-derived](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/1_lambda/lesson_8/exercises/mu-derived) exercise in the nightly built for details and test programs.

***Exercise 2 (10 points):*** Modify the K definition of IMP to not automatically initialize variables to 0. Instead, declared variables should stay uninitialized until assigned a value, and the execution should get stuck when an uninitialized variable is looked up.

Note: See the [uninitialized-variables](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/2_imp/lesson_4/exercises/uninitialized-variables) exercise in the nightly built for details and test programs.

***Exercise 3 (10 points):*** Mofify IMP so that the K "followed by" arrow, `~>`, does not explicitly occur in the definition (it currently occurs in the semantics of sequential composition). Hint: make sequential composition `strict(1)` or `seqstrict`, and have statements reduce to "{}" instead of ".", ... and don't forget to make "{}" a KResult (you may need a new syntactic category for that, which only includes "{}" and is included in KResult).

Note: See the [purely-syntactic](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/2_imp/lesson_4/exercises/purely-syntactic) exercise in the nightly built for details and test programs.

---
<b><em><span style="color:red">HW3 (due date: Friday March 4, AoE)</span></em></b>

***Exercise 1 (10 points):*** Define a variant of callcc, say callCC, which never returns to the current continuation unless a value is specifically passed to that continuation. Can you define them in terms of each other? Do these in both the substitution and the environment-based definitions.

Note: See the [callCC (substitution)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_1/exercises/callCC), 
[from-call-CC-to-callcc (substitution)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_1/exercises/from-call-CC-to-callcc), [from-callcc-to-call-CC(substitution)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_1/exercises/from-callcc-to-call-CC), 
[callCC (environment)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_6/exercises/callCC), 
[from-call-CC-to-callcc (environment)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_6/exercises/from-call-CC-to-callcc), and [from-callcc-to-call-CC (environment)](https://github.com/kframework/k/tree/master/k-distribution/pl-tutorial/1_k/3_lambda%2B%2B/lesson_6/exercises/from-callcc-to-call-CC) exercises in the nightly built for details and test programs.

***Exercise 2 (10 points):*** The current "halt;" statement of IMP++ only halts the current thread.  Define an "abort;" statement which halts the entire program.

Note: See the [abort](https://github.com/runtimeverification/k/tree/master/k-distribution/pl-tutorial/1_k/4_imp%2B%2B/lesson_7/exercises/abort) exercise in the nightly built for details and test programs.
