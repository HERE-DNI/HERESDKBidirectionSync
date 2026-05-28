---
title: "refreshRouteWithTraveledDistanceAndRoutingOptions abstract method"
slug: "sdk-for-flutter-explore-routing-routingengine-refreshroutewithtraveleddistanceandroutingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- refreshRouteWithTraveledDistanceAndRoutingOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routingengine-class</li>
<li class="self-crumb">refreshRouteWithTraveledDistanceAndRoutingOptions abstract method</li>
</ol>
<div class="self-name">refreshRouteWithTraveledDistanceAndRoutingOptions</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>refreshRouteWithTraveledDistanceAndRoutingOptions abstract method</h1></div>
<section class="multi-line-signature">
<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.28.0. Use the refresh_route() methods with RefreshRouteParameters parameter instead.")</li>
</ol>
</div>
/sdk-for-flutter-explore-core-threading-taskhandle-class
refreshRouteWithTraveledDistanceAndRoutingOptions(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-explore-routing-routehandle-class routeHandle, </li>
<li>/sdk-for-flutter-explore-routing-waypoint-class? startingPoint, </li>
<li>int? lastTraveledSectionIndex, </li>
<li>int? traveledDistanceOnLastSectionInMeters, </li>
<li>/sdk-for-flutter-explore-routing-routingoptions-class options, </li>
<li>/sdk-for-flutter-explore-routing-calculateroutecallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously refreshes a previously calculated route from the provided /sdk-for-flutter-explore-routing-routehandle-class, updating
the starting point and route metadata based on /sdk-for-flutter-explore-routing-routingoptions-class.</p>
<p>The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated. If you only want to refresh the contained traffic information, consider to use
/sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge instead.</p>
<p>Calling this method will trigger a new "HERE Routing" transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
<ul>
<li>
<p><code>routeHandle</code> The route handle holding the route to be refreshed.</p>
</li>
<li>
<p><code>startingPoint</code> Updates the starting point of the route. It should be of type /sdk-for-flutter-explore-routing-waypointtype. Otherwise,
an /sdk-for-flutter-explore-routing-routingerror error is generated. Moreover, it should be very close to the
original route specified with the /sdk-for-flutter-explore-routing-routehandle-class. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the /sdk-for-flutter-explore-routing-waypoint-class items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, /sdk-for-flutter-explore-routing-route-lengthinmeters and /sdk-for-flutter-explore-routing-route-duration
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an /sdk-for-flutter-explore-routing-routingerror error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
</li>
<li>
<p><code>options</code> The options define the vehicle and route options to calculate the route.</p>
</li>
<li>
<p><code>callback</code> Callback object that will be invoked after refreshing the route.
It is always invoked on the main thread.</p>
</li>
</ul>
<p>Returns /sdk-for-flutter-explore-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.28.0. Use the refresh_route() methods with RefreshRouteParameters parameter instead.")

TaskHandle refreshRouteWithTraveledDistanceAndRoutingOptions(RouteHandle routeHandle, Waypoint? startingPoint, int? lastTraveledSectionIndex, int? traveledDistanceOnLastSectionInMeters, RoutingOptions options, CalculateRouteCallback callback);</code></pre>
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
<li>/sdk-for-flutter-explore-routing-routingengine-class</li>
<li class="self-crumb">refreshRouteWithTraveledDistanceAndRoutingOptions abstract method</li>
</ol>
<h5>RoutingEngine class</h5>
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
