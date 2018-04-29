---
layout: page_code
title: SWEET
date: 2018-04-29 11:45 +0200
navbar: Codes
subnavbar: sweet
logo: 
code_url: https://schreiberx.github.io/sweetsite/
language: C++
developers:
  - name: Martin Schreiber
    lead_developer: true
  - name: Pedro Peixoto
  - name: Andreas Schmitt
  - name: Francois Hamon


---

Development written in C++ which allows to study PinT time integration and compare it to other time integration methods using global spectral methods in space.

This C++ development supports the development of simulations using global spectral methods.
The main reason for using spectral methods is to reduce or fully avoid discretization errors in space and focus purely on time-integration issues for ODEs and PDEs.
The PinT methods Parareal, rational approximation of exponential integrators (REXI), ML-SDC (based on libPFASST), PFASST were studied so far using ODEs, the Burgers, advection and shallow-water equations. 