---
layout: page_project
hide_hero: true
title: Parallel paradigms for NWP
date: 2017-08-10 08:24 +0200
navbar: Projects
subnavbar: pintnwp
logo: nerc_logo.png
project_url: http://gotw.nerc.ac.uk/list_full.asp?pcode=NE%2FR008795%2F1
short_desc: Parallel Paradigms for Numerical Weather Prediction
members:
  - name: Colin Cotter (Imperial College London)
  - name: Daniel Ruprecht (University of Leeds)
  - name: Beth Wingate (University of Exeter)
  - name: David Ham (Imperial College London)
  - name: Martin Schreiber (University of Exeter)
  - name: David Acreman (University of Exeter)
  - name: Jemma Shipton (Imperial College London)
---

Weather forecasts and climate simulations require dedicated high performance supercomputers to run. Advances in the power of supercomputers bring the possibility of simulating the atmosphere at higher resolution (i.e. with more detail) without having to wait longer for the answer. It has been consistently shown that increasing the resolution of atmosphere models results in more accurate weather forecasts and climate simulations.

However, getting models that can make full use of state-of-the-art supercomputers is very challenging. The Met Office is in the process of installing a new Cray XC40 supercomputer which which will deliver 16 petaflops (16 quadrillion arithmetic operations per second) peak processing power by using 4800000 individual processors computing together at the same time (in parallel). In the next few decades supercomputers are expected to deliver more and more computing power, by using more and more processors. The main thing that slows down computations on these massively parallel supercomputers is communicating data between processors. Unfortunately, the physics of the atmosphere means that the weather in one location is intrinsically linked with the weather at all other locations on the globe; this means that a lot of data communication between processors is required.

Scientists who develop atmosphere models are currently grappling with the fact that we are close to the limit of what is possible in terms of resolution and simulation speed, due to the communication requirements of the mathematical algorithms that are used to solve the equations that predict how the weather evolves in time. At the moment, these algorithms use geographic parallelism: the globe is divided up into overlapping pieces and each piece is given to a different processor, which must communicate data to processors that share geographic locations on the overlaps. To speed up a model, we need to use more and more processors on smaller and smaller regions. The speed-up is eventually limited when there are so many overlapping regions that all of the globe is covered by overlaps, and the model spends all of the time communicating.

This means that it is time to invent new mathematical algorithms that can make better use of the parallel computer. In this project we will develop algorithms that are time-parallel as well as geographic-parallel. Instead of advancing the forecast of the model forwards step by step in time, these methods produce several different estimates of the weather at the next step, before combining them together to make a more accurate solution. Each of these different estimates can be independently calculated, which introduces additional parallel computation into the model.

This project is in close partnership with the Met Office. If successful, these algorithms will lead to faster and higher resolution weather forecast and climate prediction models at the Met Office, leading to more accurate forecasts for government, industry and the general public. The Met Office provides forecasts for customers across the transport sector, particularly for aviation planning (so that aeroplanes can avoid headwinds and make use of tailwinds) and predictions of the motion of volcanic ash clouds. It also provides forecasts for retail and leisure, insurers, the Ministry of Defence, and the Environment Agency (including flood forecasting). More accurate forecasts will allow all of these business organisations to plan further into the future, avoiding risks and unnecessary costs.

{% bibliography --cited %}
