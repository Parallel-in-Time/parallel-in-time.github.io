---
layout: page_project
title: "BorisSDC"
date: 2017-08-10 08:24 +0200
navbar: Projects
subnavbar: BorisSDC
logo: epsrc.png
project_url: http://gow.epsrc.ac.uk/NGBOViewGrant.aspx?GrantRef=EP/P02372X/1
short_desc: A new algorithm to track fast ions in fusion reactors
members:
  - name: Daniel Ruprecht (University of Leeds)
  - name: Krasymyr Tretiak (University of Leeds)
  - name: Debasmita Samaddar (Culham Centre for Fusion Energy)
  - name: Rob Akers (Culham Centre for Fusion Energy)
  - name: James Buchanan (Culham Centre for Fusion Energy)
---

Fusion reactors could some day provide a clean and nearly inexhaustible source of energy, but their development has proven to be challenging. Nevertheless, great progress has been made in recent decades and fusion research is now at a critical stage: ITER, the first test reactor anticipated to generate a surplus of energy, is being built and operation is planned to start around 2025. It will serve as a testbed for DEMO, a prototype for a commercially viable fusion power plant to be completed by 2050. The Culham Centre for Fusion Energy (CCFE) is a key contributor to this development: it operates the Joint European Torus (JET) which is currently the world's largest fusion test reactor. JET is important for experimental results and validation of simulation software, both of which are used to inform the design of the much larger ITER

Computer simulations complementing experiments with test reactors are critical for the design and operation of ITER but also to explore alternative reactor designs. The immense complexity of the physics involved translates into complex mathematical models which take a long time to solve numerically, even on modern computer architectures. As reactors grow in size and complexity, so do the employed models and therefore solution times. LOCUST, for example, is a state-of-the-art particle tracker used operationally at CCFE and optimised heavily to exploit graphical processing unit (GPU) accelerators. However, one simulation of the trajectories of fast ions generated from neutral beam injection in the JET test reactor still takes around 10 hours to complete. Because of the higher energies, a similar simulation for ITER already takes 4 to 7 days. Therefore, at the moment, design choices can be informed only by a small number of simulations with carefully selected parameters. However, systematic exploration of a wide range of design parameters in computer simulations is not yet possible.

The project will develop a new and more efficient algorithm {% cite WinkelEtAl2015 --file other/sdc %} and deploy it as a particle tracker in CCFE's operational simulation software. This will help to significantly reduce solution times and contribute toward the order of magnitude reduction of runtimes needed for effective in-silico design of components for ITER. While the new algorithm will be deployed for a specific application, the mathematical ideas developed during the project can help to improve the efficiency of computer simulations in other applications such as manufacturing processes involving plasmas, for example for flat panel displays or solar panels.

{% bibliography --file other/sdc --cited %}
