---
title: "RouteOptions constructor"
slug: "sdk-for-flutter-explore-routing-routeoptions-routeoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOptions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routeoptions-class</li>
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
RouteOptions(<wbr/>[<ol class="parameter-list"> <li>/sdk-for-flutter-explore-routing-optimizationmode optimizationMode = OptimizationMode.fastest, </li>
<li>int alternatives = 0, </li>
<li>DateTime? departureTime = null, </li>
<li>DateTime? arrivalTime = null, </li>
<li>double? speedCapInMetersPerSecond = null, </li>
<li>bool enableRouteHandle = false, </li>
<li>/sdk-for-flutter-explore-routing-trafficoptimizationmode trafficOptimizationMode = TrafficOptimizationMode.timeDependent, </li>
<li>bool enableTolls = false, </li>
<li>bool optimizeWaypointsOrder = false, </li>
<li>bool enableRouteLabels = false, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>optimizationMode</code> The optimization mode to be used for route calculation. By default, it is /sdk-for-flutter-explore-routing-optimizationmode.</li>
<li><code>alternatives</code> Maximum number of alternative routes that will be calculated, in addition
to the best one. The provided value must be in the range [0, 6].
Alternative routes can be unavailable, thus they are not guaranteed to be returned.
The order of routes is from the best to the worst, as evaluated by the route calculation
algorithm and according to the given input parameters.
Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
Must be 0 for isoline calculation.</li>
<li><code>departureTime</code> Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per /sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.</li>
</ul>
<p><strong>Note</strong>:</p>
<ul>
<li>Both departure time and /sdk-for-flutter-explore-routing-routeoptions-arrivaltime cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
<ul>
<li><code>arrivalTime</code> Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per /sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.</li>
</ul>
<p><strong>Note</strong>:</p>
<ul>
<li>Both /sdk-for-flutter-explore-routing-routeoptions-departuretime and arrival time cannot be set at the same time.</li>
<li>This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset
when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00</li>
</ul>
<ul>
<li><code>speedCapInMetersPerSecond</code> Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for /sdk-for-flutter-explore-transport-transportmode,
/sdk-for-flutter-explore-transport-transportmode and /sdk-for-flutter-explore-transport-transportmode transport modes.
For car, truck and scooter transport modes, it will affect /sdk-for-flutter-explore-routing-route-duration of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
which means that no speed cap is set.</li>
<li><code>enableRouteHandle</code> A flag that indicates whether the resulting route should contain a /sdk-for-flutter-explore-routing-routehandle-class.
Defaults to <code>false</code>.
Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.</li>
<li><code>trafficOptimizationMode</code> The traffic optimization mode to be used for route calculation. By default, it is /sdk-for-flutter-explore-routing-trafficoptimizationmode, which enables traffic-aware routing.</li>
<li><code>enableTolls</code> A flag that indicates whether the resulting route /sdk-for-flutter-explore-routing-section-tolls properties should contain
tolls data. Defaults to <code>false</code>.</li>
</ul>
<p><strong>Note:</strong> When a route calculation request asks tolls, a pricing scheme with higher rates might be applied.
Consult your HERE representative to get more information on the related pricing schemes.</p>
<p><strong>Note:</strong> For users of the <code>OfflineRoutingEngine</code> this is a beta release of this feature,
so there could be a few bugs and unexpected behaviors. The <code>OfflineRoutingEngine</code> is only available for the Navigate license. For users of the <code>RoutingEngine</code> the feature is stable.</p>
<ul>
<li><code>optimizeWaypointsOrder</code> A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. /sdk-for-flutter-explore-routing-optimizationmode.
The starting and destination /sdk-for-flutter-explore-routing-waypoint-class are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see /sdk-for-flutter-explore-routing-route-sections, /sdk-for-flutter-explore-routing-section-departureplace, /sdk-for-flutter-explore-routing-section-arrivalplace, /sdk-for-flutter-explore-routing-routeplace-waypointindex).
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
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-routeoptions-class</li>
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
`
}</HTMLBlock>
