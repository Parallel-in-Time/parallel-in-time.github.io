---
layout: page_code
hide_hero: true
title: "LibPFASST"
date: 2026-07-15 12:20 +0200
updated: 2026-07-15 12:20 +0200
navbar: Codes
subnavbar: libPFASST
logo:
code_url: https://github.com/libpfasst/LibPFASST
language: Fortran 90
github_repo: "libpfasst/LibPFASST"
releases:
  - version: 1.1
    date: 2017-03-21
    link: https://github.com/libpfasst/LibPFASST/releases/tag/v1.1
  - version: 1.0
    date: 2017-03-20
    link: https://github.com/libpfasst/LibPFASST/releases/tag/v1.0
developers:
  - name: Michael Minion
    email: michael.l.minion@gmail.com
  - name: Sebastian Götschel
    email: sebastian.goetschel@tuhh.de
  - name: Matthew Emmett
    email: matthew@emmett.ca

short_desc: lightweight implementation of the PFASST algorithm
---

LibPFASST is a lightweight implementation of the Parallel Full Approximation Scheme in Space and Time (PFASST {% cite EmmettMinion2012 %}) algorithm.
It is written in Fortran (mostly F90, with some F03), but can be interfaced with C and C++ fairly easily.

{% bibliography --cited %}
