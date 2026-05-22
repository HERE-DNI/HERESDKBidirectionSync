---
title: "Untitled"
slug: "sdk-for-flutter-explore-routing-routeoptions-optimizewaypointsorder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- optimizeWaypointsOrder.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routeoptions-class</li>
<li class="self-crumb">optimizeWaypointsOrder property</li>
</ol>
<div class="self-name">optimizeWaypointsOrder</div>
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
<h1>optimizeWaypointsOrder property</h1></div>
<section class="multi-line-signature">
        
        bool
        optimizeWaypointsOrder
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. /sdk-for-flutter-explore-routing-optimizationmode.
The starting and destination /sdk-for-flutter-explore-routing-waypoint-class are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see /sdk-for-flutter-explore-routing-route-sections, /sdk-for-flutter-explore-routing-section-departureplace, /sdk-for-flutter-explore-routing-section-arrivalplace, /sdk-for-flutter-explore-routing-routeplace-waypointindex).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool optimizeWaypointsOrder;</code></pre>
</section>
</div> 
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">

<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routeoptions-class</li>
<li class="self-crumb">optimizeWaypointsOrder property</li>
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



</div>
`
}</HTMLBlock>
