---
layout: page_code
title: "ParaDdiag"
date: 2020-06-12 21:00:00 +0000
updated: 2020-06-12 21:00:00 +0000
navbar: Codes
subnavbar: ParaDiag
logo: 
code_url: https://github.com/wushulin/ParaDIAG
language: MATLAB & Fortran
github_repo: 
license: MIT
releases:
  - version: 1.0
    date: 2020-06-12
    link: https://github.com/wushulin/ParaDIAG
    download: https://github.com/wushulin/ParaDIAG
developers: 
  - link:
      name: See ParaDiag github page
      url: https://github.com/wushulin/ParaDIAG
short_desc:  ParaDiag includes diagonalization-based Parallel-in-Time (PinT) algorithms, which can handle both both dissipative and hyperbolic equations.
---
ParaDiag is a collection of {\em diagonalization-based} parallel-in-time (PinT) algorithms and 
  can be categorized into two classes: 
\begin{itemize}
\item Direct ParaDiag algorithms
\item Iterative ParaDiag algorithms
\end{itemize}
The general idea for all the ParaDiag algorithms is to form the difference equations arising from some time discretization (e.g., the backward Euler method or the trapezoidal rule) into an {\em all-at-once} system and then solve such a system  directly or  iteratively. Maday and R{\o}nquist first introduced this idea in {% cite MadayRonquist2008 %}.

For direct ParaDiag algorithms, we diagonalize  the time discretization matrix and decouple the all-at-once system into a series of sub-systems, which can be solved in parallel across all time levels.   The research for direct ParaDiag algorithms focuses on making the time discretization matrix be diagonalizable and making  the condition number of the eigenvector matrix as small as possible.    For the iterative ParaDiag algorithms, we precondition the all-at-once system by a block $\alpha$-circulant matrix and solve the preconditioning step for each iteration via a  block  Fourier spectral factorization.    
 
ParaDiag algorithms can handle both dissipative and hyperbolic equations (such as acoustic equations  and the Schr$\ddot{\rm o}$dinger equations).  An introductory  document in this field is {% cite GanderEtAl2020 %}, where the reader can find   variants,   applications and some representative theoretical results of ParaDiag. This document will be updated regularly when new interesting progress appears.  

{% bibliography --cited %}
