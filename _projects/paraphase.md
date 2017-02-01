---
layout: page_project
title: "ParaPhase"
date: 2014-06-15 16:24 +0200
updated: 2015-06-03 19:30:00 +0200
navbar: Projects
subnavbar: ParaPhase
logo: paraphase-logo.png
project_url: http://www.paraphase.de 
short_desc: space-time parallel adaptive simulation of phase-field models on HPC architectures
members:
  - name: Heike Emmerich (Univ. Bayreuth)
  - name: Carsten Gräser (FU Berlin)
  - name: Marc-Andre Keip (Univ. Stuttgart)
  - name: Jiri Kraus (NVIDIA)
  - name: Oliver Sander (TU Dresden)
  - name: Robert Speck (Forschungszentrum Jülich)
---

Phase-field models are an important class of mathematical techniques for the description of a multitude of physical and technical processes. Examples are the modelling of cracks and fracture propagation in solid media like ceramics or dry soil, the representation of liquid phase epitaxy for solar cells, semi-conductors or LEDs as well as melting and solidification processes of alloys. The price for the broad applicability and mathematical elegance of this approach is the significant computing cost required for the simulation of phase-field equations at large scales, demanding the use of modern HPC architectures. 

The goal of the project “ParaPhase -- space-time parallel adaptive simulation of phase-field models on HPC architectures” funded by the German Federal Ministry of Education and Research (FKZ 01IH15005A, BMBF program “[IKT 2020 -  Forschung für Innovation](https://www.bmbf.de/de/ikt-2020-forschung-fuer-innovation-854.html)") is the development of algorithms and methods that allow for highly efficient space-time parallel and adaptive simulations of phase-field problems. Three key aspects are addressed in the course of the project:

1. **Heterogeneous parallelization in space**. The adaptive phase-field multigrid algorithm TNNMG will be parallelized using load-balanced decomposition techniques and GPU-based acceleration of the smoother.
1. **Innovative parallelization in time**. For optimal parallel performance even on extreme scale platforms, novel approaches like Parareal and the “parallel full approximation scheme in space and time” for the parallelization in the temporal direction will be used, exploiting the hierarchical structures of spatial discretization and solver.
1. **High-order methods in space and time**. To increase the arithmetic intensity, i.e., the ratio between computation and memory access, flexible high-order methods in space (using the Discontinuous Galerkin approach) and time (using spectral deferred corrections) will be implemented and combined.

The interdisciplinary consortium consists of two partners with a long-standing experience in the particular field of applications (the groups of [Heike Emmerich](http://www.mps.uni-bayreuth.de/de/team/Emmerich_Heike/) at Universität Bayreuth and [Marc-Andre Keip](http://www.mechbau.uni-stuttgart.de/ls1/members/profs/keip/) at Universität Stuttgart) as well as four partners with a strong background in methods, algorithms and HPC (the groups of [Carsten Gräser](http://page.mi.fu-berlin.de/graeser/) at FU Berlin, [Oliver Sander](http://www.math.tu-dresden.de/~osander/) at TU Dresden, [Robert Speck](http://www.fz-juelich.de/ias/jsc/speck_r) at JSC and Jiri Kraus from the [NVIDIA Application Lab](http://www.fz-juelich.de/ias/jsc/EN/Research/HPCTechnology/ExaScaleLabs/NVLAB/_node.html)). While the algorithms developed in this project will be primarily used for studying fracture propagation and liquid phase epitaxy, these problem classes already represent a wide range of challenges in industrial applications. Based on the open source software [DUNE](https://dune-project.org/), the “Distributed and Unified Numerics Environment”, the resulting algorithms will help to make large-scale HPC simulations accessible for researchers in these fields.
