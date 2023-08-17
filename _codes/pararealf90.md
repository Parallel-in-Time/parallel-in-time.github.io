---
layout: page_code
hide_hero: true
title: "PararealF90"
date: 2015-09-24 16:45 +0200
navbar: Codes
subnavbar: pararealf90
logo:
code_url: https://github.com/Parallel-in-Time/PararealF90
language: F90
github_repo: "Parallel-in-Time/PararealF90"
license: BSD 2-clause
releases:
  - version: 1.0
    date: 2015-09-23
    link: https://github.com/Parallel-in-Time/PararealF90/releases/tag/v1.0
    download: https://github.com/Parallel-in-Time/PararealF90/releases/tag/v1.0
developers:
  - name: Daniel Ruprecht
    email: d.ruprecht@leeds.ac.uk
short_desc: Fortran90 special-purpose Parareal code.
---

A lightweight special-purpose Fortran90 implementation of Parareal.

Provides implementations of [Parareal](/methods/parareal.html) in both MPI and OpenMP to allow for a comparison of the
effect of different parallelisation strategies on runtime, memory footprint and energy consumption.
{% cite Ruprecht2017_lncs %}

{% bibliography --cited %}
