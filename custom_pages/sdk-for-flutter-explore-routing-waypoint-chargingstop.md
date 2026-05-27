---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-waypoint-chargingstop"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- chargingStop.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a></li>
<li class="self-crumb">chargingStop property</li>
</ol>
<div class="self-name">chargingStop</div>
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
<div class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>chargingStop property</h1></div>
<section class="multi-line-signature">
<a href="../../routing/ChargingStop-class.html">/sdk-for-flutter-explore-routing-chargingstop-class</a>?
        chargingStop
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Specifies of a user-planned charging stop.
The resulting <code>Route</code> may contain this waypoint as a <code>RoutePlace</code> with a non-null <code>ChargingStation</code> member
when the provided specifications indicate that a stop is required to charge the EV battery.
<strong>Note:</strong>
If <code>EVCarOptions.ensure_reachability</code> is not set as <code>true</code> and <code>ChargingStop.min_duration</code> is not provided,
route calculation may suggest a better charging stop instead of this stop.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ChargingStop? chargingStop;</code></pre>
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
<li><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a></li>
<li class="self-crumb">chargingStop property</li>
</ol>
<h5>Waypoint class</h5>
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
