---
title: "startingPoint property"
slug: "sdk-for-flutter-navigate-routing-refreshrouteparameters-startingpoint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startingPoint.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-refreshrouteparameters-class</li>
<li class="self-crumb">startingPoint property</li>
</ol>
<div class="self-name">startingPoint</div>
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
<div class="main-content" data-above-sidebar="routing/RefreshRouteParameters-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>startingPoint property</h1></div>
<section class="multi-line-signature">
/sdk-for-flutter-navigate-routing-waypoint-class?
        startingPoint
<div class="features">getter/setter pair</div>
</section>
<section class="desc markdown">
<p>Identify the new starting point of the route. It should be of type /sdk-for-flutter-navigate-routing-waypointtype.
Otherwise, an /sdk-for-flutter-navigate-routing-routingerror error is generated. Moreover, it should be very close to the
original route specified with the /sdk-for-flutter-navigate-routing-routehandle-class. The location of this waypoint may by provided,
for example, by a <code>RouteProgress</code> event. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the /sdk-for-flutter-navigate-routing-waypoint-class items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, /sdk-for-flutter-navigate-routing-route-lengthinmeters, /sdk-for-flutter-navigate-routing-route-duration, and similar
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an /sdk-for-flutter-navigate-routing-routingerror error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">Waypoint? startingPoint;</code></pre>
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
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-refreshrouteparameters-class</li>
<li class="self-crumb">startingPoint property</li>
</ol>
<h5>RefreshRouteParameters class</h5>
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
