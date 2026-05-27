---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routinginterface-returntoroutewithtraveleddistance"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- returnToRouteWithTraveledDistance.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RoutingInterface-class.html">/sdk-for-flutter-explore-routing-routinginterface-class</a></li>
<li class="self-crumb">returnToRouteWithTraveledDistance abstract method</li>
</ol>
<div class="self-name">returnToRouteWithTraveledDistance</div>
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
<div class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>returnToRouteWithTraveledDistance abstract method</h1></div>
<section class="multi-line-signature">
<a href="../../core.threading/TaskHandle-class.html">/sdk-for-flutter-explore-core-threading-taskhandle-class</a>
returnToRouteWithTraveledDistance(<wbr/><ol class="parameter-list"> <li><a href="../../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a> route, </li>
<li><a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> startingPoint, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li><a href="../../routing/CalculateRouteCallback.html">/sdk-for-flutter-explore-routing-calculateroutecallback</a> callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates a new route that leads back to the original route.</p>
<p>The part of
the original route which was already traveled by the user is ignored.</p>
<p><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
be ignored.
Additionally, the following route options are ignored:
<a href="../../routing/RouteOptions/alternatives.html">/sdk-for-flutter-explore-routing-routeoptions-alternatives</a>, <a href="../../routing/RouteOptions/arrivalTime.html">/sdk-for-flutter-explore-routing-routeoptions-arrivaltime</a>, and
<a href="../../routing/RouteOptions/optimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-optimizationmode</a>.
Most route options are only applied to the newly calculated part back to the route.</p>
<p>An application may use this method to submit a new
starting point for a previously calculated route. This method tries to avoid a costly
route re-calculation as much as possible. In case returning to the route without
re-calculation is not possible, a new route is calculated, while trying to salvage
the previous route as much as possible. However, a completely new route
containing no part of the previous route is possible, too.</p>
<p>Note that this function uses only a limited amount of map data around the new origin.
Therefore, it may also work fine with temporarily cached map data. It may also copy some of the
original route data into the new route.</p>
<p>A typical use case is to await at least 3 <code>RouteDeviation</code> events before calling this method.</p>
<ul>
<li>Or alternatively, wait at least 10 seconds after getting the first deviation event.</li>
<li>On top, the user experience can be improved by checking if the vehicle has moved at least
50 meters since calling this method for the last time.</li>
<li>Optionally, it may make sense to verify if the vehicle was ever following the route by checking if
<code>RouteDeviation.lastLocationOnRoute</code> is set.</li>
</ul>
<p>Note that deviation events are sent each time a deviation is detected, i.e. for each new location
update, regardless if the location has changed or not.
More information can be found in the Developer Guide in the "Handle route deviations" section.</p>
<ul>
<li>
<p><code>route</code> A <a href="../../routing/Route-class.html">/sdk-for-flutter-explore-routing-route-class</a> calculated using the online or offline route engine. For the offline case, It
should not contain an indoor <a href="../../routing/Section-class.html">/sdk-for-flutter-explore-routing-section-class</a> as such routes will fail. For the online case, it
should have <a href="../../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>.</p>
</li>
<li>
<p><code>startingPoint</code> The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
type <a href="../../routing/WaypointType.html">/sdk-for-flutter-explore-routing-waypointtype</a>. Otherwise, an <a href="../../routing/RoutingError.html">/sdk-for-flutter-explore-routing-routingerror</a>
error is generated.</p>
</li>
<li>
<p><code>lastTraveledSectionIndex</code> Indicates the index of the last traveled route section. Traveled part of the route won't be reused.</p>
</li>
<li>
<p><code>traveledDistanceOnLastSectionInMeters</code> Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle returnToRouteWithTraveledDistance(Route route, Waypoint startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, CalculateRouteCallback callback);</code></pre>
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
<li><a href="../../routing/RoutingInterface-class.html">/sdk-for-flutter-explore-routing-routinginterface-class</a></li>
<li class="self-crumb">returnToRouteWithTraveledDistance abstract method</li>
</ol>
<h5>RoutingInterface class</h5>
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
