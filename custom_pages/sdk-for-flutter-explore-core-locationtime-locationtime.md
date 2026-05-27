---
title: "Implementation"
slug: "sdk-for-flutter-explore-core-locationtime-locationtime"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- LocationTime.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/LocationTime-class.html">/sdk-for-flutter-explore-core-locationtime-class</a></li>
<li class="self-crumb">LocationTime const constructor</li>
</ol>
<div class="self-name">LocationTime</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="core/LocationTime-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>LocationTime constructor</h1></div>
<section class="multi-line-signature">
      const
      LocationTime(<wbr/><ol class="parameter-list single-line"> <li>DateTime localTime, </li>
<li>DateTime utcTime, </li>
<li>Duration utcOffset</li>
</ol>)
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>localTime</code> The time as observed in the tied location. For example, if a route is requested in Cracow,
Poland, the local time is "2022-03-23T16:07:31" in CET, i.e. one hour ahead of the UTC time.</li>
<li><code>utcTime</code> The time as Coordinated Universal Time (UTC). For example, if a route is requested in Poland,
the UTC time is "2022-03-23T15:07:31", i.e. one hour behind the local time.</li>
<li><code>utcOffset</code> The UTC offset is the difference between the local time and the Coordinated Universal Time (UTC)
in seconds. For example, if the local time is UTC+01:00, it is +3600 and if the local time is
UTC-05:00, it is -18000.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">const LocationTime(this.localTime, this.utcTime, this.utcOffset);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../core/core-library.html">/sdk-for-flutter-explore-core-core-library</a></li>
<li><a href="../../core/LocationTime-class.html">/sdk-for-flutter-explore-core-locationtime-class</a></li>
<li class="self-crumb">LocationTime const constructor</li>
</ol>
<h5>LocationTime class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
</HTMLBlock>
