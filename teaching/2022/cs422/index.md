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

[Jan 28](https://illinois.zoom.us/rec/share/lz0ZOwGfDYLrDznX9UDFn53DeJuRRpCpGYlZ6dToT6yA1o9Q5inYGHwR1DqTtz5g.J7yUhEo7UOnlrd0u?startTime=1643400843000)
[Jan 26](https://illinois.zoom.us/rec/share/vqMewycqFFYZEMTyhDrxhS7aSGWDjubQokNj6CX2UE58l2LXGU7UYSqUuSm7n4Y-.gnOeZEjFPRqJOM9T?startTime=1643227356000)
[Jan 21](https://illinois.zoom.us/rec/share/BCUSRktliCEpiO4dkzLpdX3p9e4uh_VOcdK4vt3Y4_p4Zbr5riAbPXU_v1wIppjQ.fbfEnD9QzhwO9Mj9?startTime=1642795353000)
[Jan 19](https://illinois.zoom.us/rec/share/fiOmld9qHJ1W7HM6yHhYNe6PyHJ0k45blppXEkJJWG2Oi9RENx8lusN71dC-UmHc.CDCzsRL5XHuqFKom?startTime=1642622875000)

## Course Description

CS422 is an advanced course on principles of programming language design. Major semantic approaches to programming languages will be discussed, such as structural operational semantics (various kinds), denotational semantics, and rewriting-based semantics. Programming language paradigms will be investigated and rigorously defined, including: imperative, functional, object-oriented, and logic programming languages; parameter binding and evaluation strategies; type checking and type inference; concurrency. Since the definitional framework used in this class will be executable, interpreters for the designed languages will be obtained for free. Software analysis tools reasoning about programs in these languages will also arise naturally. Major theoretical models will be discussed.

- Meetings: W/F 14:00-15:15, Online
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
