---
title: CS 522 -- Spring 2024
layout: default
---

# CS522 - Programming Language Semantics

Students enrolled in this class are expected to check this web page
regularly. Lecture notes and important other material will be posted
here.

## Zoom link

To be used rarely, only when not available (traveling or sick).  Or for office hours:

[https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09](https://illinois.zoom.us/j/2172447431?pwd=dEtxWmdJR0FYOElUa1ZLL2RJRzdZUT09)

### Lecture Recordings

[Jan 23](https://illinois.zoom.us/rec/share/Qb0Bwcu7Ow04XuUKsHti894PgwRmQhZcC5e-FP5y05NdKHVMJU9irvQw0UfNeSfT.RONFV3eANEMYo4dq)
[Feb 20](https://illinois.zoom.us/rec/share/3adC_b6gC4o6-kdR3etwJO3dVKwmhzdN5v-5bHvM9AE1CXm5weZhp9buSK6L-m5a.m2CzO5XoOJjfKtzo)
[Mar 21](https://illinois.zoom.us/rec/share/TiVMBw7KesFPXSTNU5RCr57A8uXsNc7-0w70iZJYclRFZdxcgD7P7eNqQlBPiwHs.Zq-oGtFewgq8kvos)

## Course Description {#course_description}

CS522 is an advanced course on semantics of programming languages.
Various semantic approaches and related aspects will be defined and
investigated. Executable semantics of various programming languages and
paradigms will be discussed, together with major theoretical models.

-   *Meetings*: Tu/Th 11:00 - 12:15
-   *Location*: Campus Instructional Facility 2018
-   *Professor*: Grigore Rosu (Office: SC 2110, WWW: <http://fsl.cs.illinois.edu/grosu>, Email: grosu@illinois.edu)
-   *Office hours*: By appointment, very flexible (held by Grigore Rosu either in SC 2110 or on Zoom at the same link as above)

## Lecture Notes, Useful Material {#lecture_notes_useful_material}

The links below provide you with useful material for this class,
including complete lecture notes. These materials will be added *by
need* and more topics will be added.

-   [Introduction](01-Introduction.pdf)

-   Conventional Semantic Approaches

    -   [Slides (PDF)](02-Conventional-Executable-Semantics.pdf),
        [Slides (PPTX)](02-Conventional-Executable-Semantics.pptx)
        <font color=red>(incomplete)</font>
    -   [Book material on IMP, Big-Step SOS, Small-Step SOS, and Denotational
        Semantics](CS522-Spring-2024-basic-semantics.pdf)

-   Rewriting Logic and Maude

    -   [slides](CS522-Spring-2024-Maude.pdf) - recommended only for a quick look
    -   [Book material](CS522-Spring-2024-Maude-book.pdf) - recommended
 
-   ### HW1 (due Thursday, February 1st, AoE) {#hw1}

    The following exercises are from the book material above. Do them only in
    Maude (that is, *not* on paper) by modifying [the provided Maude code for
    HW1](CS522-Spring-2024-Maude-HW1.zip): Exercise 56 (page 137); Exercise 70
    (page 155).

    In case you are not familiar with Maude, you are encouraged to do the
    following exercises to warm-up (but please do not include them as part of
    your HW1 submission): Exercise 30; Exercise 32; Exercise 33; Exercise 35;
    Exercise 36. All at pages 80/81.

-   ### HW2 (due Thursday, February 15, AoE) {#hw2}

    The following exercises related to denotational semantics are from the book
    material above: Exercises 80, 81, 82 (page 168; write these up on paper, or
    in a PDF); Exercise 83 (page 169; do it only in Maude, that is, *not* on
    paper, by modifying [the provided Maude code for
    HW2](CS522-Spring-2024-Maude-HW2.zip)).

-   [Book material on IMP++: Challenging Big-Step SOS, Small-Step SOS, and
    Denotational Semantics](CS522-Spring-2024-IMP++.pdf)

-   ### HW3 (due Tuesday, March 5)

    Combine all the individual extensions of IMP in [the provided Maude code for
    HW3 (similar to that provided for HW2)](CS522-Spring-2024-Maude-HW3.zip) into the IMP++ language. Read the book
    material above for all the technical details. You should create a subfolder
    of imp called 6-imp++, and that should have four subfolders, one for each
    semantic style. Provide also three IMP++ programs.  Note: Big-step and Denotational will be the most tedious, because they are the least modular.  Pick only one of them, and do the other for fun and extra-credit (if you want it).

-  [Book material on Modular SOS, Evaluation Contexts, and the CHAM](CS522-Spring-2024-MSOS-RSEC-CHAM.pdf)

-   ### HW4 (due Thursday, March 21 - extended deadline)

    Same as HW3 but for the three additional semantic approaches discussed in the
    lecture notes above: MSOS, RSEC, and CHAM. Use
    [this provided Maude code for HW4](CS522-Spring-2024-Maude-HW4.zip).
    Handle also a short essay discussing the advantages and limitations of each of
    the semantic approaches discussed so far in class, assigning a (justified) score
    between 1 and 10 to each of them.

-   Category theory: definition, diagrams, cones and limits, exponentials

    -   [Slides](CS522-Spring-2024-Category-Theory-slides.pdf)

    -   [Hand written notes on category theory properties](CS522-Spring-2024-HandWritten-Category-Theory.zip)

-   Lambda Calculus and Combinatory Logic

    - [Slides](CS522-Spring-2024-Lambda-slides.pdf)

    - [Book material on Lambda Calculus and Combinatory Logic](CS522-Spring-2024-Lambda.pdf)

-   ### HW5 (due Tuesday, April 09, AoE)

    This is a theoretical HW, requiring you to do two proofs using category
    theory. You are strongly encouraged to do \*all\* the exercises in the
    slides, especially if you did not have prior experience with category
    theory. If you do the two exercises perfectly, then anything else you
    do will count for extra-credit.
    - (1, easy) Exercise 8 on slide 20 in the
    [category theory slides](CS522-Spring-2024-Category-Theory-slides.pdf).
    - (2, harder) Property 1 on "category theory - 3.png" in the
    [hand written notes on category theory properties](CS522-Spring-2024-HandWritten-Category-Theory.zip); redraw the diagram with the correct objects and morphisms where they are deleted (figuring out the problem/diagram is 50% of a category theory proof).

-   Simply-Typed Lambda Calculus
    * Basic notions: type system, equational semantics, models, completeness.  [Slides](CS522-Spring-2024-Simply-Typed-Lambda-Calculus.pdf)
    * Cartesian Closed Categories as models for simply-typed lambda-calculus.  [Slides](CS522-Spring-2024-PL-CCC.pdf)

-   ### HW6 (due Thursday, April 25, AoE)
       
       Complete this [LAMBDA code snippet](CS522-Spring-2024-Lambda-Maude.zip).
       This covers knowledge about untyped lambda-calculus, fixed-points,
       combinatory logic, and de Bruijn nameless representations.

- Recursion, Types, Polymorphism
    * Recursion and Types. [Slides](CS522-Spring-2024-Recursion.pdf)
    * Polymorphism. [Slides](CS522-Spring-2024-Polymorphism.pdf)

-   ### Extra-Credit (due Friday, May 03, AoE)

    This can be regarded as "Final exam", but it only counts as HW
    (and not project) extra-credit and has the same weight as any of the
    previous HWs. If you got a good score so far for the 6 HWs above,
    then you do not need to do this extra-credit. Choose one, and only
    one, of the following and do it well (you will get either 10 or 0
    for this extra-credit problem!):
    
    1. Proposition 8 from the slides on simply-typed lambda calculus. Exercises 5 and 6 from the slides on CCCs.

    2. Consider the PCF language with call-by-value (note that the
       slides above define the call-by-name variant). Give it a small-step,
       a big-step, and a denotational semantics in Maude, using the
       representations of these semantic approaches discussed in the first
       part of the class. Provide also 5 (five) PCF programs that can be
       used to test all three of your semantics. You can use the builtins
       provided as part of the previous HWs (you should only need the
       generic substitution from there).
    
    3. This has two problems. The first is to define a type checker for
       the parametric polymorphic lambda-calculus (or System F). The second
       is to define a type checker for the subtype polymorphic
       lambda-calculus. In both cases, make sure that you also include the
       conditional and a few examples showing that your definition works.
       Feel free to pick whatever syntax you want for the various
       constructs (both for terms and for types).
       
