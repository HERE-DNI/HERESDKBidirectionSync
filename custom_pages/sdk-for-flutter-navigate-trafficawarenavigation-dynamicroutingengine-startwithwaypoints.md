---
title: "startWithWaypoints abstract method"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-startwithwaypoints"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startWithWaypoints.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class</li>
<li class="self-crumb">startWithWaypoints abstract method</li>
</ol>
<div class="self-name">startWithWaypoints</div>
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
<div class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startWithWaypoints abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the start() method with RoutingOptions parameter instead.")</li>
</ol>
</div>
void
startWithWaypoints(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-routing-routehandle-class routeHandle, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-navigate-routing-waypoint-class&gt; waypoints, </li>
<li>/sdk-for-flutter-navigate-routing-refreshrouteoptions-class refreshRouteOptions, </li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutinglistener-class listener, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Starts polling the HERE backend services to find a better route,
as defined by the /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-class.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle from the HERE routing backend.</p>
</li>
<li>
<p><code>waypoints</code> Allows to specify detailed information on the waypoints of the route.
This parameter can be useful, when additional information needs to be
specified besides the coordinates - as the coordinates can be retrieved
from the contained /sdk-for-flutter-navigate-routing-routeplace-class that are already contained in
the /sdk-for-flutter-navigate-routing-routehandle-class parameter.</p>
</li>
<li>
<p><code>refreshRouteOptions</code> The options for the route calculation.</p>
</li>
<li>
<p><code>listener</code> The listener to receive the events.</p>
</li>
</ul>
<p>Throws /sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingenginestartexception-class. when the passed parameter are invalid.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the start() method with RoutingOptions parameter instead.")

void startWithWaypoints(RouteHandle routeHandle, List&lt;Waypoint&gt; waypoints, RefreshRouteOptions refreshRouteOptions, DynamicRoutingListener listener);</code></pre>
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
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengine-class</li>
<li class="self-crumb">startWithWaypoints abstract method</li>
</ol>
<h5>DynamicRoutingEngine class</h5>
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
