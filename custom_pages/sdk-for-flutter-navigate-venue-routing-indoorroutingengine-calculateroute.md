---
title: "calculateRoute abstract method"
slug: "sdk-for-flutter-navigate-venue-routing-indoorroutingengine-calculateroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateRoute.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-class</li>
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
<div class="main-content" data-above-sidebar="venue.routing/IndoorRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>calculateRoute abstract method</h1></div>
<section class="multi-line-signature">
void
calculateRoute(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class from, </li>
<li>/sdk-for-flutter-navigate-venue-routing-indoorwaypoint-class to, </li>
<li>/sdk-for-flutter-navigate-venue-routing-indoorrouteoptions-class routeOptions, </li>
<li>/sdk-for-flutter-navigate-venue-routing-calculateindoorroutecallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates a route inside a venue.</p>
<ul>
<li>
<p><code>from</code> A starting position of the route to calculate.</p>
</li>
<li>
<p><code>to</code> A destination position of the route to calculate.</p>
</li>
<li>
<p><code>routeOptions</code> Options specific for indoor route calculation, along with
common route options.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void calculateRoute(IndoorWaypoint from, IndoorWaypoint to, IndoorRouteOptions routeOptions, CalculateIndoorRouteCallback callback);</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-indoorroutingengine-class</li>
<li class="self-crumb">calculateRoute abstract method</li>
</ol>
<h5>IndoorRoutingEngine class</h5>
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
`
}</HTMLBlock>
