---
layout: page
title: "References"
date: 2015-06-01 00:00:00 +0000
comments: false
sharing: false
footer: true
---

## Statistics

{% raw %}
<div class="row" id="statistics">
  <div class="col-md-4">
    <div id="total-num-pubs"></div>
    <div id="chart-raw-data" class="collapse"></div>
  </div>
  <div class="col-md-8">
    <canvas id="pint-pubs-chart" class="img-responsive hidden-xs hidden-sm" width="800" height="400"></canvas>
  </div>
  <noscript>
    <div class="col-md-12">
      <div class="alert alert-warning" role="alert">
        You need to activate JavaScript to see the awesome statistics and beautify below listings.
      </div>
    </div>
  </noscript>
</div>
{% endraw %}

## 2015

{% bibliography --file pint -q @*[year=2015] %}

## 2014

{% bibliography --file pint -q @*[year=2014] %}

## 2013

{% bibliography --file pint -q @*[year=2013] %}

## 2012

{% bibliography --file pint -q @*[year=2012] %}

## 2011

{% bibliography --file pint -q @*[year=2011] %}

## 2010

{% bibliography --file pint -q @*[year=2010] %}

## 2009

{% bibliography --file pint -q @*[year=2009] %}

## 2008

{% bibliography --file pint -q @*[year=2008] %}

## 2007

{% bibliography --file pint -q @*[year=2007] %}

## 2006

{% bibliography --file pint -q @*[year=2006] %}

## 2005

{% bibliography --file pint -q @*[year=2005] %}

## 2000 - 2004

{% bibliography --file pint -q @*[year>=2000 && year<=2004] %}

## 1995 - 1999

{% bibliography --file pint -q @*[year>=1995 && year<=1999] %}

## 1990 - 1994

{% bibliography --file pint -q @*[year>=1990 && year<=1994] %}

## Pre 1990

{% bibliography --file pint -q @*[year<=1989] %}

{% raw %}
<script src="//cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js" type="text/javascript"></script>
<script src="/js/bib_stats.min.js" type="text/javascript"></script>
{% endraw %}
