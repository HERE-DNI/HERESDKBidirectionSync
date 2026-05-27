---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-transitroutingengine-calculateroute"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- calculateRoute.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/TransitRoutingEngine-class.html">/sdk-for-flutter-explore-routing-transitroutingengine-class</a></li>
<li class="self-crumb">calculateRoute abstract method</li>
</ol>
<div class="self-name">calculateRoute</div>
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
<div class="main-content" data-above-sidebar="routing/TransitRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateRoute abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
calculateRoute(<wbr/><ol class="parameter-list"> <li><a href="../../routing/TransitWaypoint-class.html">/sdk-for-flutter-explore-routing-transitwaypoint-class</a> startingPoint, </li>
<li><a href="../../routing/TransitWaypoint-class.html">/sdk-for-flutter-explore-routing-transitwaypoint-class</a> destination, </li>
<li><a href="../../routing/TransitRouteOptions-class.html">/sdk-for-flutter-explore-routing-transitrouteoptions-class</a> routeOptions, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates a public transit route from the origin to the destination.</p>
<ul>
<li>
<p><code>startingPoint</code> Position of starting point.</p>
</li>
<li>
<p><code>destination</code> Position of destination.</p>
</li>
<li>
<p><code>routeOptions</code> Options for public transit route calculation.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns <a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle calculateRoute(TransitWaypoint startingPoint, TransitWaypoint destination, TransitRouteOptions routeOptions, CalculateRouteCallback callback);</code></pre>
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
<li><a href="../../routing/TransitRoutingEngine-class.html">/sdk-for-flutter-explore-routing-transitroutingengine-class</a></li>
<li class="self-crumb">calculateRoute abstract method</li>
</ol>
<h5>TransitRoutingEngine class</h5>
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
