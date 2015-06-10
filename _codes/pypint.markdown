---
layout: page_code
title: "PyPinT"
date: 2014-06-15 16:45 +0200
updated: 2014-06-18 09:50 +0200
navbar: Codes
subnavbar: pypint
footer: true
logo: 
code_url: http://parallel-in-time.github.io/PyPinT
language: Python
github_repo: "Parallel-in-Time/PyPinT"
license: MIT
developers:
  - name: Torbjörn Klatt
    email: t.klatt@fz-juelich.de
    lead_developer: true
  - name: Dieter Moser
    email: d.moser@fz-juelich.de
    lead_developer: true
  - name: Dr. Robert Speck
    email: r.speck@fz-juelich.de
short_desc: <em>DEPRECATED</em> A Python3 framework for Parallel-in-Time integration routines.
---

With growing interest in parallel-in-time methods many different and new solvers for ordinary 
differential equations have gained the attention of researchers from various fields.
In order to clearly estimate the potential and limitations of these mostly iterative solvers, a 
modular prototyping framework not only helps to understand their properties and various facets but 
also allows to easily implement and test new ideas.

As an example, the _Parallel Full Approximation Scheme in Space and Time_ (_PFASST_ {% cite EmmettMinion2012 %})
and its serial counterpart, multi-level spectral deferred corrections (_MLSDC_ {% cite SpeckEtAl2014_BIT %}) are composed of 
multiple levels and even types of spectral deferred correction sweeps which are coupled by 
space-time restriction and interpolation operators.
These modular and interchangeable combinations of different techniques already generate a vast 
amount of variations with different effects on solvability and efficiency towards a diverse set of 
problems.

For a thorough and systematic analysis of methods like _PFASST_ or _Parareal_ we take the path of 
a well-planned and fully modular implementation of these algorithms.
By following the object-oriented programming paradigm we create an abstract decomposition of the 
methods’ functional components combined in a framework for parallel-in-time algorithms.
Different methods implemented in a single framework using a unified base functionality enables 
detailed qualitative and quantitative analysis without paying too much attention to underlying 
implementation details.

Due to its flexibility, extensibility and rather comfortable learning curve Python has an ever 
growing world-wide community within science, academia and industry.
For _PyPinT_, it provides the building block for a flexible and unified framework, allowing fast 
prototyping of iterative parallel-in-time algorithms.
Well-maintained and open-source third party modules such as [_NumPy_][NumPy] and [_SciPy_][SciPy] 
offer high-level interfaces to performant low-level functionalities for matrix and vector 
arithmetics, common mathematical methods and plotting capabilities.
In addition, current efforts leave the door open for enabling _PyPinT_ to be applied on HPC clusters.

## Goals

Accompanying the development of parallel-in-time algorithms, new ideas can be implemented in 
_PyPinT_ immediately.
Utilizing the framework’s analysis tools such as calculation and plotting of stability regions, 
runtime and characteristic values (e.g. residuals), new algorithms can easily be studied in detail.
Clearly defined interfaces, a strictly modular concept and different levels of abstraction enable 
the user to exchange certain parts of the algorithms and add his or her own methods to enrich the 
whole framework. 

Students, undergraduate and graduate, with a basic knowledge of iterative solvers and some 
programming skills will be able to use and extend _PyPinT_ and discover, learn and understand the 
mechanics of parallel-in-time methods.
_PyPinT_ is open-source licensed and available on GitHub, thus fostering collaboration and ease 
contribution of amplifications by interested people.  
Ultimately, _PyPinT_ should not only represent a package for applying and studying parallel-in-time 
methods but also provide a development environment for enhancing existing and inventing new methods.
Finally, _PyPinT_ can also provide valuable insight and guidance for future, performance-oriented 
implementations in other programming languages.

[numPy]: http://www.numpy.org/
[sciPy]: http://scipy.org/scipylib/index.html

{% bibliography --cited %}
