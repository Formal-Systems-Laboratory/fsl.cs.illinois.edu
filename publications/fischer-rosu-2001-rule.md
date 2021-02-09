---
abstract: We present a logical framework in which abstract interpretations can be
  naturally specified and then verified. Our approach is based on membership equational
  logic which extends equational logics by membership axioms, asserting that a term
  has a certain sort. We represent an abstract interpretation as a membership equational
  logic specification, usually as an overloaded order-sorted signature with membership
  axioms. It turns out that, for any term, its least sort over this specification
  corresponds to its most concrete abstract value. Maude implements membership equational
  logic and provides mechanisms to calculate the least sort of a term efficiently.
  We first show how Maude can be used to get prototyping of abstract interpretations
  for free. Building on the meta-logic facilities of Maude, we further develop a tool
  that automatically checks an abstract interpretation against a set of user-defined
  properties. This can be used to select an appropriate abstract interpretation, to
  characterize the specific loss of information during abstraction, and to compare
  different abstractions with each other.
authors: [Bernd Fischer, Grigore Rosu]
categories: [automated_reasoning, program_verification, executable_semantics, programming_languages,
  semantics, rewrite_logic]
date: 2001-06-01
id: fischer-rosu-2001-rule
title: Interpreting Abstract Interpretations in Membership Equational Logic
---
