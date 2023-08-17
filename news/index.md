---
layout: page
navbar: News
subnavbar: Overview
footer: false
hide_hero: true
---

<div class="blog-index">
  {% assign index = true %}
  {% for post in site.posts %}
  <article class="post on-index {% if forloop.last %}last{% endif %}">
    {% include article.html %}
  </article>
  <hr>
  {% endfor %}
</div>

<ul class="pager">
  {% if paginator.next_page %}
  <li class="previous"><a href="{{ paginator.next_page }}">&larr;&nbsp;Older</a></li>
  {% else %}
  <li class="previous disabled"><a href="#">&larr;&nbsp;Older</a></li>
  {% endif %}
  <li><a href="/news/archive.html">News Archive</a></li>
  {% if paginator.previous_page %}
  <li class="next"><a href="{{ paginator.previous_page }}">Newer&nbsp;&rarr;</a></li>
  {% else %}
  <li class="next disabled"><a href="#">Newer&nbsp;&rarr;</a></li>
  {% endif %}
</ul>
