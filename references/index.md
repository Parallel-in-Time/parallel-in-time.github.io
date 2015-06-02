---
layout: page
title: "References"
date: 2015-06-01 00:00:00 +0000
comments: false
sharing: false
footer: true
---

This list of publications closely related to parallel-in-time integration is probably not complete.
Please feel free to add any missing publications through a [pull request on GitHub](https://github.com/Parallel-in-Time/parallel-in-time.github.io/wiki).

## Statistics

{% raw %}
<div class="row" id="statistics">
  <div class="col-md-4">
    <div id="total-num-pubs"></div>
    <div id="stats-buttons" class="btn-group btn-group-xs btn-group-justified" role="group">
      <a class="btn btn-xs btn-default" role="button" target="_blank" title="download BibTeX file"
         href="https://raw.githubusercontent.com/Parallel-in-Time/parallel-in-time.github.io/source/_bibliography/pint.bib">
         <i class="fa fa-fw fa-download"></i> BibTeX
      </a>
    </div>
    <p id="image-download-docu" class="text-muted"></p>
    <div id="chart-raw-data" class="collapse"></div>
  </div>
  <div class="col-md-8">
    <canvas id="pint-pubs-chart" class="img-responsive" width="800" height="400"></canvas>
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

{% raw %}
<h2>2015 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2015] %}

{% raw %}
<h2>2014 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2014] %}

{% raw %}
<h2>2013 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2013] %}

{% raw %}
<h2>2012 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2012] %}

{% raw %}
<h2>2011 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2011] %}

{% raw %}
<h2>2010 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2010] %}

{% raw %}
<h2>2009 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2009] %}

{% raw %}
<h2>2008 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2008] %}

{% raw %}
<h2>2007 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2007] %}

{% raw %}
<h2>2006 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2006] %}

{% raw %}
<h2>2005 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year=2005] %}

{% raw %}
<h2>2000 - 2004 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year>=2000 && year<=2004] %}

{% raw %}
<h2>1995 - 1999 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year>=1995 && year<=1999] %}

{% raw %}
<h2>1990 - 1994 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year>=1990 && year<=1994] %}

{% raw %}
<h2>Pre 1990 <span class="count-stat"></span></h2>
{% endraw %}

{% bibliography --file pint -q @*[year<=1989] %}

{% raw %}
<script src="//cdnjs.cloudflare.com/ajax/libs/Chart.js/1.0.2/Chart.min.js" type="text/javascript"></script>
<script src="/js/bib_stats.min.js" type="text/javascript"></script>
{% endraw %}
