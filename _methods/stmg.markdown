---
layout: page_method
title: Space-time Multigrid (STMG)
subtitle: STMG
date: 2015-07-01 17:00:00 +0000
updated: 2015-07-01 17:00:00 +0000
navbar: Methods
subnavbar: STMG
short_desc: STMG is a time-parallel method for parabolic PDEs.
footer: true
---

The _space-time multigrid_ method {% cite HortonVandewalle1995 %} treats the whole of the space-time problem simultaneously. The multigrid approach uses point smoothers and employs a parameter-dependent coarsening strategy that chooses either semicoarsening in space or in time on each level of the multigrid hierarchy. 

{% bibliography --cited %}
