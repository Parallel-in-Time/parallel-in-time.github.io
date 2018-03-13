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
[Jülich Supercomputing Centre](http://www.fz-juelich.de/ias/jsc)
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

Details on the application procedure will be posted for each workshop separately on the respective local websites.

## Previous Grantees

### [6th Conference on Parallel-in-Time Integration, Ascona, Switzerland](/events/6th-pint-workshop/)

**Ben S. Southworth**, University of Colorado at Boulder, USA

Talk: "Solving Space-time Discretizations of the Wave Equation with Algebraic Multigrid"

Algebraic multigrid (AMG) is an iterative solver for large sparse linear systems
that, for many applications, scales linearly in complexity with the number of
degrees of freedom. It also scales in parallel to hundreds of thousands of cores,
making it a key component of many high-performance simulation codes. For the
symmetric positive definite case, often resulting from the discretization of elliptic
partial differential equations (PDEs), convergence of AMG is well motivated and
AMG is among the fastest numerical solvers available. However, highly nonsymmetric
matrices pose difficulties for AMG in theory and in practice. Although a number of efforts have been made to develop AMG for nonsymmetric linear systems, few have considered highly nonsymmetric cases, and those that have demonstrated success on nonsymmetric systems typically use a multilevel
strategy that does not scale well in parallel (K-cycles or W-cycles). Each of these
issues are likely part of the reason that AMG has yet to be demonstrated as an
effective parallel-in-time solver. Although a number of works have looked at
geometric multigrid and parabolic PDEs, there is a large gap in the parallel-intime
literature in terms of algebraic solvers and/or space-time discretizations of
hyperbolic PDEs.

Although hyperbolic PDEs arise frequently in physical simulation, their
solution is often constrained to sequential, explicit time stepping schemes, or
implicit schemes with relatively slow (not O(n)) linear solvers. Recently, we
developed a reduction-based algebraic multigrid (AMG) solver, AMGir, and its
generalization LAIR, to solve upwind discretizations of the steady- state
transport equation. AMGir/LAIR proved to be a fast and robust solver for the
steady-state transport equation, even on unstructured meshes and with high-order
finite elements. Due to the success of AMGir/LAIR applied to upwind
discretizations of gradients, a natural research direction to consider is further
developing the method with a focus on parallel-in-time applications. Full spacetime
discretizations often use some form of upwind or semi-upwind discretization
in time, which leads to a global space-time matrix amenable to AMGir/LAIR. 

Here, we consider a discretization of the 2d-space, 1d-time, wave equation written
in first-order form, corresponding to a system with two variables. A modification
of AMGir/LAIR is developed to account for the system structure, and the method
proves very effective. In particular, the reduction aspect of AMGir/LAIR applied
to the wave equation is striking – initial iterations appear to diverge, but
convergence factors then plummet to ρ ~ 1E−10. AMGir/LAIR is able to seamlessly
handle the system structure and solve the space-time wave equation, a well-known
challenging parallel-in-time problem, showing promise as a robust framework for
parallel-in-time.

**Federico Danieli**, Mathematical Institute, University of Oxford, UK

Title: "An Alternative to the Coarse Solver for the Parareal Algorithm"

The Parareal algorithm is one of the simplest and most widely spread techniques
to achieve parallelisation in the computation of the solution of ODEs and PDEs
by splitting their time domain. However, ensuring its stability can be a challenging
task, which for the largest part revolves around the choice of the most apt pair of
fine and coarse solvers for the problem at hand. Stability is also an issue in the
case of advection-dominated equations, where the algorithm has often been shown
to perform poorly. In the attempt to overcome these problems, an alternative
formulation of Parareal is presented. Starting from an interpretation of the
algorithm as a Newton method, we notice how the sensitivity of the solution from
the application of the fine solver, with respect to variations on the initial
conditions, appears in the update formula. Rather than resorting to the application
of a coarse solver in order to approximate this term and consequently propagate
the update along the time domain, we aim to estimate this sensitivity in a direct
manner. The approach chosen is suitable for systems of ODEs of small size and
some simple PDEs, and extensions to general cases are not trivial and still remain
object of further work. However, the first experiments on model problems show the
potential of this method to overcome some of the limitations of Parareal, as well
as to boost its convergence speed.

**Marc Olm**, Technical University of Catalonia & CIMNE, Spain

Title: "Nonlinear parallel-in-time multilevel Schur complement solvers for ordinary differential equations"

In this work, we propose a parallel-in-time solver for linear and nonlinear ordinary
differential equations. The approach is based on an efficient multilevel solver of the
Schur complement related to a multilevel time partition. For linear problems, the
scheme leads to a fast direct method. Next, two different strategies for solving
nonlinear ODEs are proposed. First, we consider a Newton method over the global
nonlinear ODE, using the multilevel Schur complement solver at every nonlinear
iteration. Second, we state the global nonlinear problem in terms of the nonlinear
Schur complement (at an arbitrary level), and perform nonlinear iterations over it.
Numerical experiments show that the proposed schemes are weakly scalable, i.e.,
we can efficiently exploit increasing computational resources to solve for more time
steps the same problem. 

### [5th PinT Workshop, Banff, Canada](/events/5th-pint-workshop/)

**Thibaut Lunet**, ISAE-Supaero & CERFACS, Toulouse, France

Talk: "[On the time-parallelization of the solution of Navier-Stokes equations using Parareal](http://www.birs.ca/events/2016/5-day-workshops/16w5030/videos/watch/201611290945-Lunet.html)"

Unsteady turbulent flow simulations using the Navier Stokes equations require larger and larger problem sizes. On an other side, new supercomputer architectures will be available in the next decade, with computational power based on a larger number of cores rather than significantly increased CPU frequency. Hence most of the current generation CFD software will face critical efficiency issues if bounded to massive spatial parallelization and we consider time parallelization as an attractive alternative to enhance efficiency on multi-cores architectures. Several algorithms developed in the last decades (Parareal, PFASST) may be straightforwardly applied to the Navier-Stokes equations, but the Parareal algorithm remains one of the simplest solutions in the case of explicit time stepping, compressible flow Based on an optimized implementation of Parareal we modelize the speed-up obtained when combining both space and time parallelizations. This modelization takes into account the speedup of an actual structured, massively parallel CFD solver and the cost of time communications, both measured on two different supercomputers. Some preliminary requirements for a worthy time-parallel integration will be then derived, in terms of both Parareal iteration count and size of the time subdomain window. We then study within this framework, possible enhancements of the well-known convergence difficulties for Parareal encountered for advection dominated problems. The proposed approach is based on the representation of Parareal as an algebraic system of nonlinear equations solved by a preconditioned Newton’s method. The new formulation targets the reduction of the degree of non-normality of its Jacobian by slightly modifying the Parareal iteration. Performance on examples related to canonical linear problems, like the Dahlquist and the one-dimensional advection equation, is analysed. To conclude we comment on the extension of this method to nonlinear problems.

**Stephanie Günther**, TU Kaiserslautern, AG Scientific Computing, Kaiserslautern, Germany

Talk: "[Adjoint Sensitivity Computation for the Parallel Multigrid Reduction in Time Software Library XBraid](http://www.birs.ca/events/2016/5-day-workshops/16w5030/videos/watch/201611300832-Gunther.html)"

In this paper we present an adjoint solver for the multigrid in time software library XBraid. XBraid provides a non-intrusive approach for simulating unsteady dynamics on multiple processors while parallelizing not only in space but also in the time domain. It applies an iterative multigrid reduction in time algorithm to existing spatially parallel classical time propagators and computes the unsteady solution parallel in time. However, in many engineering applications not only the primal unsteady flow computation is of interest but also the ability to compute sensitivities that determine the influence of design changes to some output quantity. In recent years, adjoint solvers have widely been developed which propagate sensitivity information backwards through the time domain. We develop an adjoint solver for XBraid that enhances the primal iterations by an iteration for computing adjoint sensitivities. In each iteration, the adjoint code runs backwards through the primal XBraid actions and computes the consistent discrete adjoint sensitivities parallel in time. It is highly non-intrusive as existing adjoint time propagators can easily be integrated through the adjoint interface. We validate the adjoint code by applying it to an unsteady partial differential equation that mimics the behavior of separated flows past bluff bodies. In our 1D model, the near wake is mimicked by a nonlinear ODE, namely the Lorenz attractor which exhibits self-excited oscillations. The far wake is modeled by an advection - diffusion equation whose upstream boundary condition is determined by the ODE mimicking the near wake. We demonstrate the integration of a serial time stepping algorithm, that solves the PDE forward in time, into the parallel-in-time XBraid framework as well as the development of the corresponding adjoint interface. The resulting sensitivities are in good agreement with those computed from finite differences. Nevertheless, there is still great potential for optimizing the performance of the adjoint code using advanced algorithmic differentiation techniques such as reverse accumulation and checkpointing. Due to the iterative nature of the primal and the adjoint flow computation, the method is very well suited for simultaneous optimization algorithms like the One-shot method which solve the optimization problem in the full space. They have proven to be very efficient for optimization with steady-state PDE constraints while its application to unsteady PDE is still under development. The non-intrusive adjoint XBraid solver is therefore highly desirable and will extend its application range from pure simulation to optimization.
