---
layout: default
title: Matching Logic
---


## What is Matching Logic? {#what_is_matching_logic}

### For programming language semanticists: {#for_programming_language_semanticists}

Matching logic is a unifying foundational logic for programming
languages, specification, verification. It serves as the foundation of
the [K framework](http://k-framework.org): a formal language framework
where all programming languages must have a formal semantics and all
language tools are automatically generated by the framework from the
semantics at no additional costs, in a correct-by-construction manner.

Traditionally, concrete behaviors of programs are defined by
[operational
semantics](https://en.wikipedia.org/wiki/Operational_semantics), while
the properties of them are specified and proved using [axiomatic
semantics](https://en.wikipedia.org/wiki/Axiomatic_semantics), such as
[Hoare logic](https://en.wikipedia.org/wiki/Hoare_logic). Unfortunately,
axiomatic semantics of real languages are rather complex, so correctness
proofs are necessary in order to trust the proven properties. Moreover,
such proofs have to be maintained as the language changes, which is
generally perceived as a burden. Ideally, we would like to have only
*one* reference language semantics, which are used for both deriving
program behaviors and verifying programs.

Matching logic allows us to regard a programming language through both
operational and axiomatic lenses at the same time, making no distinction
between the two. The semantics of a programming language is given in
matching logic as a set of rewrite rules. Both operational behaviors and
formal properties of a program are derived using the
*language-independent* proof system of matching logic. That is, we use
the same proof system to reason about all programming languages, which
is different from the classic axiomatic semantics approach where
different languages require their own set of proof rules (see, e.g.,
[Hoare logic rules](https://en.wikipedia.org/wiki/Hoare_logic#Rules) for
a set of proof rules that were designed specifically for a simple
imperative language). In conclusion, one matching logic semantics
fulfills the roles of both operational and axiomatic semantics in a
uniform manner.

One of the key observations made by matching logic is that program
states can be represented as algebraic datatypes called
*configurations*. A configuration contains all information of the
program state, such as its current computation (i.e. the program/code),
its computing context (e.g., environments, heaps, etc.), input and
output buffer, and many others. Program configurations can be *matched*
by (configuration) *patterns*, which are matching logic formulas with
variables and constraints. A rewrite rule of a matching logic semantics
has the form lhs =\> rhs where lhs and rhs are patterns. It specifies
that all configurations matching lhs should rewrite to the
configurations matching rhs, in one computation step. In this way,
matching logic defines the formal semantics of a programming language by
defining the set of all its configurations and then defining a
[transition system](https://en.wikipedia.org/wiki/Transition_system)
over the configurations using rewrite rules.

### For logicians: {#for_logicians}

Matching logic is a powerful extension of the [normal modal
logic](https://en.wikipedia.org/wiki/Normal_modal_logic) with
many-sorted universes, many-sorted modalities, first-order logic (FOL)
quantifiers ∀ and ∃, and the least fixpoint μ-binder. Many
logics/calculi/models, especially those important in the study of
programming languages, can be defined as theories in matching logic.
Here is a non-exhaustive list of the logics/calculi/models that are
definable in matching
logic:![](Logics.png "fig:Logics.png"){width="700"}

-   First-order logic (FOL) and its extension with least fixpoints;
-   Modal logic variants and extensions, in particular, modal μ-logic
    and hybrid logic;
-   Temporal logics such as linear temporal logic (LTL) and computation
    tree logic (CTL);
-   Dynamic logic;
-   Hoare logic, which is the foundation of most existing
    state-of-the-art program verifiers;
-   Reachability logic, which is the foundation of language-independent
    program verification that is implemented by the K framework;
-   Separation logic and its extension with recursive definitions;
-   Equational and rewriting logic;
-   Many-sorted and order-sorted algebras;
-   Complex type structures such as polymorphic types, function types,
    and dependent types;
-   λ-calculus;
-   Pure type systems;

The diagram above on the right depicts the relationship among these
logics/calculi/models, where arrows mean \"is subsumed by\" or \"can be
defined in\". The box labeled \"Matching Logic\" denotes ML (without
fixpoints); the one labeled \"Matching μ-logic\" denotes MmL; the one
labeled \"Applicative Matching Logic\" denotes AML. The node labeled
\"K\" denotes the current implementation of K, which builds upon ML and
automates a fragment of RL reasoning. The big bidirectional dotted arrow
between K and AML means our ultimate goal to leverage K to the same
level as MmL.

## Getting Started {#getting_started}

Matching logic is the result of a continuous 20-year effort in finding a
foundation logic for formal language frameworks, such as K, and has led
to dozens of research papers, listed in
[Publications](Matching_Logic_Publications "wikilink"). Here, we select
some milestone papers for starters, discuss the ongoing projects and
open problems, and review some earlier papers that compare matching
logic with the classic Hoare-style program verification.

### Core publications {#core_publications}

-   A comprehensive in-depth survey paper of the mathematical
    foundations of matching logic. The paper discusses the motivation of
    matching logic and its usage in K, defines its syntax and semantics,
    shows that many logics can be defined as theories, including FOL,
    modal logic S5, and separation logic, and proposes a sound and
    complete proof system. Note that the paper only considers the
    fragment without the least fixpoint μ-binder, which we denote as ML
    to avoid confusion with the full matching logic with fixpoints.

    {% include paper.html id="rosu-2017-lmcs" %}

-   The canonical paper that proposes matching logic in its full
    generality that includes fixpoints, called matching μ-logic and
    denoted as MmL. The paper extends ML with the μ-binder, and shows
    that more logics can be defined in it as theories, including FOL
    with least fixpoints, modal μ-logic and its temporal/dynamic logic
    fragments, separation logic with recursive definitions (see the
    technical report version), and reachability logic. The paper also
    proposes a more general proof system for MmL.

    {% include paper.html id="chen-rosu-2019-lics" %}

-   An alternative presentation of MmL, but with a lot of
    simplification. This new presentation is called applicative matching
    logic, denoted as AML. AML eliminates the many-sorted universes and
    infrastructures from MmL, keeping only one binary symbol called
    application that applies its first argument to its second. AML is
    the result of our attempt in making the foundational logic of K
    *minimal*, without losing any expressive and reasoning power of MmL.
    The paper proposes an elegant way to deal with multiple sort
    universes and additionally shows that many-sorted and order-sorted
    algebras, λ-calculus, pure type systems, and K are all definable as
    theories.

    {% include paper.html id="chen-rosu-2019-trb" %}

### Open problems {#open_problems}

See [Open Problems](Open_Problems "wikilink").

## Publications that compare with Hoare-style verification {#publications_that_compare_with_hoare_style_verification}

The following set of papers discusses how the classic Hoare logic for
program verification is subsumed by reachability logic (shortened RL)
for language-independent verification. Since RL is proved to be subsumed
in matching logic in the MmL paper, Hore-style verification is just a
special instance of matching logic reasoning.

-   A summary of the RL-style language-independent program verification
    and its use in practice.

    {% include paper.html id="chen-rosu-2018-isola" %}

-   A language-independent proof system for all-path reachability, with
    soundness and relative completeness proofs

    {% include paper.html id="stefanescu-ciobaca-mereuta-moore-serbanuta-rosu-2014-rta" %}

-   A language-independent proof system for one-path reachability which
    supports semantics given with conditional rules (big-step and
    small-step), with soundness and relative completeness proofs

    {% include paper.html id="rosu-stefanescu-ciobaca-moore-2013-lics" %}

-   A language-independent program verification framework, including the
    MatchC verifier:

    {% include paper.html id="rosu-stefanescu-2012-oopsla" %}

-   The relationship to Hoare logic, including a mechanical translation
    of Hoare logic proofs into matching logic proofs:

    {% include paper.html id="rosu-stefanescu-2012-fm" %}

See also the [K and Matching Logic](fsl:K_and_Matching_Logic "wikilink")
webpage at UIUC, which contains slides and an interview.

## Related Links {#related_links}

-   The [K framework](http://k-framework.org) webpage