---
layout: page_method
title: PFASST
subtitle: Parallel Full Approximation Scheme in Space and Time
date: 2014-06-16 00:00:00 +0000
navbar: Methods
subnavbar: pfasst
footer: true
---

PFASST has been proposed by [Matt Emmett and Michael Minion in 2012.](http://dx.doi.org/10.2140/camcos.2012.7.105)
It is based on spectral deferred corrections [(SDC)](http://dx.doi.org/10.1023/A:1022338906936) and contains multi-level spectral deferred corrections [(MLSDC)](http://arxiv.org/abs/1307.1312) as special case when running on a single processor in time. PFASST's performance has been studied in massively parallel simulation using tens and hundreds of thousands of cores [[1]](http://conferences.computer.org/sc/2012/papers/1000a083.pdf), [[2]](http://sc13.supercomputing.org/sites/default/files/PostersArchive/tech_posters/post148s2-file3.pdf).

A C++ library implementing SDC, MLSDC and PFASST is [available](https://github.com/Parallel-in-Time) under a BSD license.