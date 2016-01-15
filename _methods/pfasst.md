---
layout: page_method
title: PFASST
subtitle: Parallel Full Approximation Scheme in Space and Time
date: 2014-06-16 00:00:00 +0000
navbar: Methods
subnavbar: pfasst
short_desc: PFASST is a time-parallel expansion of spectral deferred corrections methods.
---

PFASST has been proposed by {% cite EmmettMinion2012 %}.
It is based on spectral deferred corrections [(SDC)](http://dx.doi.org/10.1023/A:1022338906936) and
contains multi-level spectral deferred corrections {% cite SpeckEtAl2014_BIT %} as special case when 
running on a single processor in time.
PFASST's performance has been studied in massively parallel simulation using tens and hundreds of
thousands of cores {% cite SpeckEtAl2012 RuprechtEtAl2013_SC %}.

A C++ library implementing SDC, MLSDC and PFASST is [available](https://github.com/Parallel-in-Time)
under a BSD license.

{% bibliography --cited %}