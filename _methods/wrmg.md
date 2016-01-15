---
layout: page_method
title: Space-time concurrent multigrid waveform relaxation (WRMG)
subtitle: WRMG
date: 2015-07-01 17:00:00 +0000
updated: 2015-07-01 17:00:00 +0000
navbar: Methods
subnavbar: wrmg
short_desc: WRMG is normally only a space-concurrent method; time parallelism is possible using cyclic reduction.
---

Multigrid waveform relaxation {% cite LubichOstermann1987 %} is an algorithm for solving parabolic partial differential equations on multicomputers. The method is based on applying standard iterative methods to systems of ordinary differential equations and using multigrid techniques for accelerating this process. Some time parallelism was introduced in the method described in {% cite VandewalleVandeVelde1994 %} by using pipelining or the partition method. However, a small sequential component remained. In {% cite HortonEtAl1995 %}, it was shown that when using cyclic reduction instead of the partition method major classes of parabolic problems can be solved in polylog parallel time without giving up linear serial complexity. In {% cite VandewalleHorton1995 %}, the method was analyzed bz means of local Fourier analysis and compared to similar results for a time-parallel multigrid method.

{% bibliography --cited %}
