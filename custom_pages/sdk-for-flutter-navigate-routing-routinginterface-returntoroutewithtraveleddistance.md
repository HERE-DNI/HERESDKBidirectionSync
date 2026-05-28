---
title: "returnToRouteWithTraveledDistance abstract method"
slug: "sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- returnToRouteWithTraveledDistance.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routinginterface-class</li>
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
/sdk-for-flutter-navigate-core-threading-taskhandle-class
returnToRouteWithTraveledDistance(<wbr/><ol class="parameter-list"> <li>/sdk-for-flutter-navigate-routing-route-class route, </li>
<li>/sdk-for-flutter-navigate-routing-waypoint-class startingPoint, </li>
<li>int lastTraveledSectionIndex, </li>
<li>int traveledDistanceOnLastSectionInMeters, </li>
<li>/sdk-for-flutter-navigate-routing-calculateroutecallback callback, </li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Asynchronously calculates a new route that leads back to the original route.</p>
<p>The part of
the original route which was already traveled by the user is ignored.</p>
<p><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
be ignored.
Additionally, the following route options are ignored:
/sdk-for-flutter-navigate-routing-routeoptions-alternatives, /sdk-for-flutter-navigate-routing-routeoptions-arrivaltime, and
/sdk-for-flutter-navigate-routing-routeoptions-optimizationmode.
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
<p><code>route</code> A /sdk-for-flutter-navigate-routing-route-class calculated using the online or offline route engine. For the offline case, It
should not contain an indoor /sdk-for-flutter-navigate-routing-section-class as such routes will fail. For the online case, it
should have /sdk-for-flutter-navigate-routing-routehandle-class.</p>
</li>
<li>
<p><code>startingPoint</code> The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
type /sdk-for-flutter-navigate-routing-waypointtype. Otherwise, an /sdk-for-flutter-navigate-routing-routingerror
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
<p>Returns /sdk-for-flutter-navigate-core-threading-taskhandle-class. Handle that will be used to manipulate the execution of the task.</p>
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-routing-routinginterface-class</li>
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
`
}</HTMLBlock>
