---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routeoptions-departuretime"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- departureTime.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a></li>
<li class="self-crumb">departureTime property</li>
</ol>
<div class="self-name">departureTime</div>
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
<div class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>departureTime property</h1></div>
<section class="multi-line-signature">
        
        DateTime?
        departureTime
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="../../routing/RouteOptions/trafficOptimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.</p>
<p><strong>Note</strong>:</p>
<ul>
<li>Both departure time and <a href="../../routing/RouteOptions/arrivalTime.html">/sdk-for-flutter-explore-routing-routeoptions-arrivaltime</a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">DateTime? departureTime;</code></pre>
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
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a></li>
<li class="self-crumb">departureTime property</li>
</ol>
<h5>RouteOptions class</h5>
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
