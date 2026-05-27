---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-avoidboundingboxareaoptions-avoidboundingboxarea"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- avoidBoundingBoxArea.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/AvoidBoundingBoxAreaOptions-class.html">/sdk-for-flutter-explore-routing-avoidboundingboxareaoptions-class</a></li>
<li class="self-crumb">avoidBoundingBoxArea property</li>
</ol>
<div class="self-name">avoidBoundingBoxArea</div>
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
<div class="main-content" data-above-sidebar="routing/AvoidBoundingBoxAreaOptions-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>avoidBoundingBoxArea property</h1></div>
<section class="multi-line-signature">
<a href="../../core/GeoBox-class.html">/sdk-for-flutter-explore-core-geobox-class</a>
avoidBoundingBoxArea
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Area of rectangular shape which routes must not cross. Strictly enforced.
<strong>Note:</strong>
Violations are reported as <code>sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD</code>.
This avoidance option is not supported for <code>IsolineOptions</code>. If it is defined for isoline calculation then an <code>sdk.routing.RoutingError.INVALID_PARAMETER</code> error is generated.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">GeoBox avoidBoundingBoxArea;</code></pre>
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
<li><a href="../../routing/AvoidBoundingBoxAreaOptions-class.html">/sdk-for-flutter-explore-routing-avoidboundingboxareaoptions-class</a></li>
<li class="self-crumb">avoidBoundingBoxArea property</li>
</ol>
<h5>AvoidBoundingBoxAreaOptions class</h5>
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
