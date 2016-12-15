---
layout: page
title: "Travel Grants"
created: 2016-03-22 10:00:00 +0200
navbar: Events
subnavbar: Travel Grants
comments: false
sharing: false
footer: true
---

## Description
For the next three workshops, [Jülich Supercomputing Centre](http://www.fz-juelich.de/ias/jsc)
is providing travel support for PhD students working in the field of parallel-in-time integration methods.

With this commitment, JSC is emphasizing the importance of regular community meetings, in particular for
young scientists working on their PhD thesis. Up to three students per workshop will receive up to EUR 1.500 each
for covering parts of their travel expenses.

The Scientific Committee of the PinT Workshop Series will select the students based on applications.
These should include:

  - a description of their thesis topic, stating the connection to parallel-in-time methods ("This is what I'm working on", 1-2 pages)
  - a letter of motivation, containing a short CV ("This is why I should receive the grant", 1-2 pages)
  - a short description of the group and institute they are affiliated to ("This is where I work", up to 1 page)

Also, students traveling to one of the meetings via this grant are expected to present their work either
on a poster or during a talk.

This offer is starting with the [5th PinT Workshop](/events/5th-pint-workshop/) at BIRS. Students who would like to apply should write to r.speck@fz-juelich.de as soon as possible.

For future events, a deadline will be announced together with the workshop.

## Previous Grantees

### [5th PinT Workshop, Banff, Canada](/events/5th-pint-workshop/)

**Thibaut Lunet**, ISAE-Supaero & CERFACS, Toulouse, France

Talk: "[On the time-parallelization of the solution of Navier-Stokes equations using Parareal](http://www.birs.ca/events/2016/5-day-workshops/16w5030/videos/watch/201611290945-Lunet.html)"

Unsteady turbulent flow simulations using the Navier Stokes equations require larger and larger problem sizes. On an other side, new supercomputer architectures will be available in the next decade, with computational power based on a larger number of cores rather than significantly increased CPU frequency. Hence most of the current generation CFD software will face critical efficiency issues if bounded to massive spatial parallelization and we consider time parallelization as an attractive alternative to enhance efficiency on multi-cores architectures. Several algorithms developed in the last decades (Parareal, PFASST) may be straightforwardly applied to the Navier-Stokes equations, but the Parareal algorithm remains one of the simplest solutions in the case of explicit time stepping, compressible flow Based on an optimized implementation of Parareal we modelize the speed-up obtained when combining both space and time parallelizations. This modelization takes into account the speedup of an actual structured, massively parallel CFD solver and the cost of time communications, both measured on two different supercomputers. Some preliminary requirements for a worthy time-parallel integration will be then derived, in terms of both Parareal iteration count and size of the time subdomain window. We then study within this framework, possible enhancements of the well-known convergence difficulties for Parareal encountered for advection dominated problems. The proposed approach is based on the representation of Parareal as an algebraic system of nonlinear equations solved by a preconditioned Newton’s method. The new formulation targets the reduction of the degree of non-normality of its Jacobian by slightly modifying the Parareal iteration. Performance on examples related to canonical linear problems, like the Dahlquist and the one-dimensional advection equation, is analysed. To conclude we comment on the extension of this method to nonlinear problems.

**Stephanie Günther**, TU Kaiserslautern, AG Scientific Computing, Kaiserslautern, Germany

Talk: "[Adjoint Sensitivity Computation for the Parallel Multigrid Reduction in Time Software Library XBraid](http://www.birs.ca/events/2016/5-day-workshops/16w5030/videos/watch/201611300832-Gunther.html)"

In this paper we present an adjoint solver for the multigrid in time software library XBraid. XBraid provides a non-intrusive approach for simulating unsteady dynamics on multiple processors while parallelizing not only in space but also in the time domain. It applies an iterative multigrid reduction in time algorithm to existing spatially parallel classical time propagators and computes the unsteady solution parallel in time. However, in many engineering applications not only the primal unsteady flow computation is of interest but also the ability to compute sensitivities that determine the influence of design changes to some output quantity. In recent years, adjoint solvers have widely been developed which propagate sensitivity information backwards through the time domain. We develop an adjoint solver for XBraid that enhances the primal iterations by an iteration for computing adjoint sensitivities. In each iteration, the adjoint code runs backwards through the primal XBraid actions and computes the consistent discrete adjoint sensitivities parallel in time. It is highly non-intrusive as existing adjoint time propagators can easily be integrated through the adjoint interface. We validate the adjoint code by applying it to an unsteady partial differential equation that mimics the behavior of separated flows past bluff bodies. In our 1D model, the near wake is mimicked by a nonlinear ODE, namely the Lorenz attractor which exhibits self-excited oscillations. The far wake is modeled by an advection - diffusion equation whose upstream boundary condition is determined by the ODE mimicking the near wake. We demonstrate the integration of a serial time stepping algorithm, that solves the PDE forward in time, into the parallel-in-time XBraid framework as well as the development of the corresponding adjoint interface. The resulting sensitivities are in good agreement with those computed from finite differences. Nevertheless, there is still great potential for optimizing the performance of the adjoint code using advanced algorithmic differentiation techniques such as reverse accumulation and checkpointing. Due to the iterative nature of the primal and the adjoint flow computation, the method is very well suited for simultaneous optimization algorithms like the One-shot method which solve the optimization problem in the full space. They have proven to be very efficient for optimization with steady-state PDE constraints while its application to unsteady PDE is still under development. The non-intrusive adjoint XBraid solver is therefore highly desirable and will extend its application range from pure simulation to optimization.
