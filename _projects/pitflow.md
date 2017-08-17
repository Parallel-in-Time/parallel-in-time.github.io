---
layout: page_project
title: "PiT Flow"
date: 2017-08-10 08:24 +0200
navbar: Projects
subnavbar: PiTFlow
logo: pit_flow.png
project_url: https://www.archer.ac.uk/community/eCSE/eCSE-projects.php
short_desc: Accelerating simulations of cerebrovascular blood flow through parallelization in time
members:
  - name: Derek Groen (Brunel University London)
  - name: Daniel Ruprecht (University of Leeds)
  - name: Rupert Nash (EPCC, University of Edinburgh)
  - name: David Scott (EPCC, University of Edinburgh)
---

*This project is funded through [ARCHER's Embedded CSE (eCSE)](https://www.archer.ac.uk/community/eCSE/eCSE-projects.php) support*

[HemeLB](http://www.2020science.net/software/hemelb.html) {% cite GroenEtAl2013 --file other/hemelb %} is code designed to simulate blood flow in arteries using Lattice-Boltzmann methods (LBM). For complex geometries like the [Circle of Willis](https://en.wikipedia.org/wiki/Circle_of_Willis), it scales up to 25k cores on the Cray XC30 supercomputer [ARCHER](http://www.archer.ac.uk/about-archer/hardware/) but simulations still take several days to complete. Building on the work by Randles and Kaxiras {% cite Randles2014 %}, this project will integrate parallel-in-time integration capacities into HemeLB to extend scaling and reduce wall-clock times.

The aims of the project are:

 1. Implement the [Parareal](https://en.wikipedia.org/wiki/Parareal) {% cite LionsEtAl2001 %} algorithm into HemeLB to provide parallel-in-time integration capacities.
 2. Optimise communication and scheduling in time to minimise overheads and improve efficiency and resource utilisation of Parareal.
 3. Demonstrate speedup of five or better using the Circle of Willis simulation model, thus bringing simulations times down to a day or less.
 4. Simplify and automate the Parallel-In-Time implementation, allowing others in the community to perform these runs with a single-line command using FabSim.
 5. Continuously provide information about the employed parallel-in-time approach to the ARCHER community to facilitate adoption for other codes.

{% bibliography --file other/hemelb %}
{% bibliography --cited %}
