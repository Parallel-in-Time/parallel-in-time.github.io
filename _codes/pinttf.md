---
layout: page_code
title: "PinT-TF"
date: 2018-03-09 13:02 +0900
updated: 2018-03-09 13:02 +0900 
navbar: Codes
subnavbar: pinttf 
logo: 
code_url: https://github.com/xjtju/PinT
language: C++,F90  
license: MIT 
github_repo: "xjtju/PinT"
developers:
  - name: Jian Xiao 
    email: xiaojian@tju.edu.cn 
    lead_developer: true
  - name:  Mikio Iizuka 
    email: iizuka.mikio.903@m.kyushu-u.ac.jp 
  - name: Kenji Ono 
    email: keno@cc.kyushu-u.ac.jp 
short_desc: A performance and convergency testing framework for Parallel-in-Time methods, currently only for Parareal. 
---
In order to quickly explore the applicability of the [Parareal](/methods/parareal.html) algorithm, we have built the very light-weighted framework. As a path finder of applying the parareal algorithm to real-world computing problems, it provides a basic space-time parallel and performance profiling functionalities. 

The framework implemented the Parareal skeleton on an uniform mesh(1D/2D/3D), and some common linear solvers and time integrators, including SOR, BiCGStab, Newton-Raphson etc. For running a test, You only need to provide problem-specific stencil code, and then choose a proper combination of solvers. All the parameters controlling the space-time domain division, convergence check, coarsening factor etc. can be predefined through an .INI file, easily be changed and tuned. If some default function cannot be able to support some specific problem, it can be easily be extended by writting a new implementation in problem-specific sub classes.

The framework is mainly written by C++ for good template and extension, most BLAS related calculations is performed by Fortran for performance reason and easy matrix manipulation. It is very light-weighted, the only necessary third library is [inih](https://github.com/benhoyt/inih), a small but excellent .INI file parser. HDF5 output and performance monitoring are also optionally supported by [HDF5](https://www.hdfgroup.org/HDF5) library and [PMLlib](https://github.com/avr-aics-riken/PMlib) respectively.      

At current release, the code has provided two examples for heat equation and Allen-Cahn equation. We will continue to improve the generality and adaptability of it.  
