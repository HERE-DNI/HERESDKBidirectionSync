---
title: "Implementation"
slug: "sdk-for-flutter-explore-routing-routeoptions-routeoptions"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RouteOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li><a href="../../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a></li>
<li class="self-crumb">RouteOptions constructor</li>
</ol>
<div class="self-name">RouteOptions</div>
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
<h1>RouteOptions constructor</h1></div>
<section class="multi-line-signature">
RouteOptions(<wbr/>[<ol class="parameter-list"> <li><a href="../../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a> optimizationMode = OptimizationMode.fastest, </li>
<li>int alternatives = 0, </li>
<li>DateTime? departureTime = null, </li>
<li>DateTime? arrivalTime = null, </li>
<li>double? speedCapInMetersPerSecond = null, </li>
<li>bool enableRouteHandle = false, </li>
<li><a href="../../routing/TrafficOptimizationMode.html">/sdk-for-flutter-explore-routing-trafficoptimizationmode</a> trafficOptimizationMode = TrafficOptimizationMode.timeDependent, </li>
<li>bool enableTolls = false, </li>
<li>bool optimizeWaypointsOrder = false, </li>
<li>bool enableRouteLabels = false, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>optimizationMode</code> The optimization mode to be used for route calculation. By default, it is <a href="../../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>.</li>
<li><code>alternatives</code> Maximum number of alternative routes that will be calculated, in addition
to the best one. The provided value must be in the range [0, 6].
Alternative routes can be unavailable, thus they are not guaranteed to be returned.
The order of routes is from the best to the worst, as evaluated by the route calculation
algorithm and according to the given input parameters.
Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
Must be 0 for isoline calculation.</li>
<li><code>departureTime</code> Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="../../routing/RouteOptions/trafficOptimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.</li>
</ul>
<p><strong>Note</strong>:</p>
<ul>
<li>Both departure time and <a href="../../routing/RouteOptions/arrivalTime.html">/sdk-for-flutter-explore-routing-routeoptions-arrivaltime</a> cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
<ul>
<li><code>arrivalTime</code> Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="../../routing/RouteOptions/trafficOptimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.</li>
</ul>
<p><strong>Note</strong>:</p>
<ul>
<li>Both <a href="../../routing/RouteOptions/departureTime.html">/sdk-for-flutter-explore-routing-routeoptions-departuretime</a> and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
<ul>
<li><code>speedCapInMetersPerSecond</code> Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>,
<a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> and <a href="../../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> transport modes.
For car, truck and scooter transport modes, it will affect <a href="../../routing/Route/duration.html">/sdk-for-flutter-explore-routing-route-duration</a> of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
which means that no speed cap is set.</li>
<li><code>enableRouteHandle</code> A flag that indicates whether the resulting route should contain a <a href="../../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>.
Defaults to <code>false</code>.
Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</li>
<li><code>trafficOptimizationMode</code> The traffic optimization mode to be used for route calculation. By default, it is <a href="../../routing/TrafficOptimizationMode.html">/sdk-for-flutter-explore-routing-trafficoptimizationmode</a>, which enables traffic-aware routing.</li>
<li><code>enableTolls</code> A flag that indicates whether the resulting route <a href="../../routing/Section/tolls.html">/sdk-for-flutter-explore-routing-section-tolls</a> properties should contain
tolls data. Defaults to <code>false</code>.</li>
</ul>
<p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
Consult your HERE representative to get more information on the related pricing schemes.</p>
<p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p>
<ul>
<li><code>optimizeWaypointsOrder</code> A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="../../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>.
The starting and destination <a href="../../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <a href="../../routing/Route/sections.html">/sdk-for-flutter-explore-routing-route-sections</a>, <a href="../../routing/Section/departurePlace.html">/sdk-for-flutter-explore-routing-section-departureplace</a>, <a href="../../routing/Section/arrivalPlace.html">/sdk-for-flutter-explore-routing-section-arrivalplace</a>, <a href="../../routing/RoutePlace/waypointIndex.html">/sdk-for-flutter-explore-routing-routeplace-waypointindex</a>).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.</li>
<li><code>enableRouteLabels</code> Specifies whether route labels should be included in the route response.
Route labels identify major highways or road names along the route.
By default, this is set to <code>false</code>.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">RouteOptions([OptimizationMode optimizationMode = OptimizationMode.fastest, int alternatives = 0, DateTime? departureTime = null, DateTime? arrivalTime = null, double? speedCapInMetersPerSecond = null, bool enableRouteHandle = false, TrafficOptimizationMode trafficOptimizationMode = TrafficOptimizationMode.timeDependent, bool enableTolls = false, bool optimizeWaypointsOrder = false, bool enableRouteLabels = false])
  : optimizationMode = optimizationMode, alternatives = alternatives, departureTime = departureTime, arrivalTime = arrivalTime, speedCapInMetersPerSecond = speedCapInMetersPerSecond, enableRouteHandle = enableRouteHandle, trafficOptimizationMode = trafficOptimizationMode, enableTolls = enableTolls, optimizeWaypointsOrder = optimizeWaypointsOrder, enableRouteLabels = enableRouteLabels;</code></pre>
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
<li><a href="../../routing/RouteOptions-class.html">/sdk-for-flutter-explore-routing-routeoptions-class</a></li>
<li class="self-crumb">RouteOptions constructor</li>
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
</div></div>
</div>
</HTMLBlock>
