---
title: "Constructors"
slug: "sdk-for-flutter-explore-routing-routeoptions-class"
---

<HTMLBlock>
<div class="sdk-for-flutter">
<!-- RouteOptions-class.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="routing/RouteOptions-class.html#constructors">Constructors</a></li>
<li><a href="routing/RouteOptions/RouteOptions.html">RouteOptions</a></li>
<li><a href="routing/RouteOptions/RouteOptions.withDefaults.html">withDefaults</a></li>
<li class="section-title">
<a href="routing/RouteOptions-class.html#instance-properties">Properties</a>
</li>
<li><a href="routing/RouteOptions/alternatives.html">alternatives</a></li>
<li><a href="routing/RouteOptions/arrivalTime.html">arrivalTime</a></li>
<li><a href="routing/RouteOptions/departureTime.html">departureTime</a></li>
<li><a href="routing/RouteOptions/enableRouteHandle.html">enableRouteHandle</a></li>
<li><a href="routing/RouteOptions/enableRouteLabels.html">enableRouteLabels</a></li>
<li><a href="routing/RouteOptions/enableTolls.html">enableTolls</a></li>
<li><a href="routing/RouteOptions/hashCode.html">hashCode</a></li>
<li><a href="routing/RouteOptions/optimizationMode.html">optimizationMode</a></li>
<li><a href="routing/RouteOptions/optimizeWaypointsOrder.html">optimizeWaypointsOrder</a></li>
<li class="inherited"><a href="routing/RouteOptions/runtimeType.html">runtimeType</a></li>
<li><a href="routing/RouteOptions/speedCapInMetersPerSecond.html">speedCapInMetersPerSecond</a></li>
<li><a href="routing/RouteOptions/trafficOptimizationMode.html">trafficOptimizationMode</a></li>
<li class="section-title inherited"><a href="routing/RouteOptions-class.html#instance-methods">Methods</a></li>
<li class="inherited"><a href="routing/RouteOptions/noSuchMethod.html">noSuchMethod</a></li>
<li class="inherited"><a href="routing/RouteOptions/toString.html">toString</a></li>
<li class="section-title"><a href="routing/RouteOptions-class.html#operators">Operators</a></li>
<li><a href="routing/RouteOptions/operator_equals.html">operator ==</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RouteOptions class</li>
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
<div class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RouteOptions-class-sidebar.html" id="dartdoc-main-content">
<div>
<h1>RouteOptions class</h1></div>
<section class="desc markdown">
<p>The options to specify how the route will be calculated.</p>
</section>
<section class="summary offset-anchor" id="constructors">
<h2>Constructors</h2>
<dl class="constructor-summary-list">
<dt class="callable" id="RouteOptions">
<a href="../routing/RouteOptions/RouteOptions.html">/sdk-for-flutter-explore-routing-routeoptions-routeoptions</a>([<a href="../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a> optimizationMode = OptimizationMode.fastest, int alternatives = 0, DateTime? departureTime = null, DateTime? arrivalTime = null, double? speedCapInMetersPerSecond = null, bool enableRouteHandle = false, <a href="../routing/TrafficOptimizationMode.html">/sdk-for-flutter-explore-routing-trafficoptimizationmode</a> trafficOptimizationMode = TrafficOptimizationMode.timeDependent, bool enableTolls = false, bool optimizeWaypointsOrder = false, bool enableRouteLabels = false])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="RouteOptions.withDefaults">
<a href="../routing/RouteOptions/RouteOptions.withDefaults.html">/sdk-for-flutter-explore-routing-routeoptions-routeoptions-withdefaults</a>()
</dt>
<dd>
          Creates a new instance.
        </dd>
</dl>
</section>
<section class="summary offset-anchor" id="instance-properties">
<h2>Properties</h2>
<dl class="properties">
<dt class="property" id="alternatives">
<a href="../routing/RouteOptions/alternatives.html">/sdk-for-flutter-explore-routing-routeoptions-alternatives</a>
↔ int
</dt>
<dd>
  Maximum number of alternative routes that will be calculated, in addition
to the best one. The provided value must be in the range [0, 6].
Alternative routes can be unavailable, thus they are not guaranteed to be returned.
The order of routes is from the best to the worst, as evaluated by the route calculation
algorithm and according to the given input parameters.
Defaults to 0, which means there are no alternatives, i.e. only the best route is returned.
Must be 0 for isoline calculation.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="arrivalTime">
<a href="../routing/RouteOptions/arrivalTime.html">/sdk-for-flutter-explore-routing-routeoptions-arrivaltime</a>
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="../routing/RouteOptions/trafficOptimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="departureTime">
<a href="../routing/RouteOptions/departureTime.html">/sdk-for-flutter-explore-routing-routeoptions-departuretime</a>
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per <a href="../routing/RouteOptions/trafficOptimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode</a>.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableRouteHandle">
<a href="../routing/RouteOptions/enableRouteHandle.html">/sdk-for-flutter-explore-routing-routeoptions-enableroutehandle</a>
↔ bool
</dt>
<dd>
  A flag that indicates whether the resulting route should contain a <a href="../routing/RouteHandle-class.html">/sdk-for-flutter-explore-routing-routehandle-class</a>.
Defaults to <code>false</code>.
Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableRouteLabels">
<a href="../routing/RouteOptions/enableRouteLabels.html">/sdk-for-flutter-explore-routing-routeoptions-enableroutelabels</a>
↔ bool
</dt>
<dd>
  Specifies whether route labels should be included in the route response.
Route labels identify major highways or road names along the route.
By default, this is set to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableTolls">
<a href="../routing/RouteOptions/enableTolls.html">/sdk-for-flutter-explore-routing-routeoptions-enabletolls</a>
↔ bool
</dt>
<dd>
  A flag that indicates whether the resulting route <a href="../routing/Section/tolls.html">/sdk-for-flutter-explore-routing-section-tolls</a> properties should contain
tolls data. Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
<a href="../routing/RouteOptions/hashCode.html">/sdk-for-flutter-explore-routing-routeoptions-hashcode</a>
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="optimizationMode">
<a href="../routing/RouteOptions/optimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-optimizationmode</a>
↔ <a href="../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>
</dt>
<dd>
  The optimization mode to be used for route calculation. By default, it is <a href="../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="optimizeWaypointsOrder">
<a href="../routing/RouteOptions/optimizeWaypointsOrder.html">/sdk-for-flutter-explore-routing-routeoptions-optimizewaypointsorder</a>
↔ bool
</dt>
<dd>
  A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="../routing/OptimizationMode.html">/sdk-for-flutter-explore-routing-optimizationmode</a>.
The starting and destination <a href="../routing/Waypoint-class.html">/sdk-for-flutter-explore-routing-waypoint-class</a> are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see <a href="../routing/Route/sections.html">/sdk-for-flutter-explore-routing-route-sections</a>, <a href="../routing/Section/departurePlace.html">/sdk-for-flutter-explore-routing-section-departureplace</a>, <a href="../routing/Section/arrivalPlace.html">/sdk-for-flutter-explore-routing-section-arrivalplace</a>, <a href="../routing/RoutePlace/waypointIndex.html">/sdk-for-flutter-explore-routing-routeplace-waypointindex</a>).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
<a href="../routing/RouteOptions/runtimeType.html">/sdk-for-flutter-explore-routing-routeoptions-runtimetype</a>
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="speedCapInMetersPerSecond">
<a href="../routing/RouteOptions/speedCapInMetersPerSecond.html">/sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond</a>
↔ double?
</dt>
<dd>
  Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for <a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a>,
<a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> and <a href="../transport/TransportMode.html">/sdk-for-flutter-explore-transport-transportmode</a> transport modes.
For car, truck and scooter transport modes, it will affect <a href="../routing/Route/duration.html">/sdk-for-flutter-explore-routing-route-duration</a> of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
which means that no speed cap is set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficOptimizationMode">
<a href="../routing/RouteOptions/trafficOptimizationMode.html">/sdk-for-flutter-explore-routing-routeoptions-trafficoptimizationmode</a>
↔ <a href="../routing/TrafficOptimizationMode.html">/sdk-for-flutter-explore-routing-trafficoptimizationmode</a>
</dt>
<dd>
  The traffic optimization mode to be used for route calculation. By default, it is <a href="../routing/TrafficOptimizationMode.html">/sdk-for-flutter-explore-routing-trafficoptimizationmode</a>, which enables traffic-aware routing.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
<a href="../routing/RouteOptions/noSuchMethod.html">/sdk-for-flutter-explore-routing-routeoptions-nosuchmethod</a>(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
<a href="../routing/RouteOptions/toString.html">/sdk-for-flutter-explore-routing-routeoptions-tostring</a>(<wbr/>)
    → String

</dt>
<dd class="inherited">
  A string representation of this object.
  <div class="features">inherited</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="operators">
<h2>Operators</h2>
<dl class="callables">
<dt class="callable" id="operator ==">
<a href="../routing/RouteOptions/operator_equals.html">/sdk-for-flutter-explore-routing-routeoptions-operator-equals</a>(<wbr/>Object other)
    → bool

</dt>
<dd>
  The equality operator.
  

</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li><a href="../index.html">/sdk-for-flutter-explore</a></li>
<li><a href="../routing/routing-library.html">/sdk-for-flutter-explore-routing-routing-library</a></li>
<li class="self-crumb">RouteOptions class</li>
</ol>
<h5>routing library</h5>
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
