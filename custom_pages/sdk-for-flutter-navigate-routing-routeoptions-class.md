---
title: "RouteOptions class"
slug: "sdk-for-flutter-navigate-routing-routeoptions-class"
---

<HTMLBlock>{
`
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
/sdk-for-flutter-navigate-routing-routeoptions-routeoptions([/sdk-for-flutter-navigate-routing-optimizationmode optimizationMode = OptimizationMode.fastest, int alternatives = 0, DateTime? departureTime = null, DateTime? arrivalTime = null, double? speedCapInMetersPerSecond = null, bool enableRouteHandle = false, /sdk-for-flutter-navigate-routing-trafficoptimizationmode trafficOptimizationMode = TrafficOptimizationMode.timeDependent, bool enableTolls = false, bool optimizeWaypointsOrder = false, bool enableRouteLabels = false])
</dt>
<dd>
          Creates a new instance.
        </dd>
<dt class="callable" id="RouteOptions.withDefaults">
/sdk-for-flutter-navigate-routing-routeoptions-routeoptions-withdefaults()
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
/sdk-for-flutter-navigate-routing-routeoptions-alternatives
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
/sdk-for-flutter-navigate-routing-routeoptions-arrivaltime
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to end. Traffic speed and
incidents shall be taken into account in the calculation of the route, per /sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode.
By default, the time is not set.
If the time is not set, the current time will be used internally, to predict the arrival time.
Therefore, by default, a time-aware route request is initiated including traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="departureTime">
/sdk-for-flutter-navigate-routing-routeoptions-departuretime
↔ DateTime?
</dt>
<dd>
  Optional time when travel is expected to start. Traffic speed and
incidents shall be taken into account in the calculation of the route, per /sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode.
By default, the time is not set.
If the time is not set, the current time will be used internally, i.e. now.
Therefore, by default, a time-aware route request is initiated including traffic.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableRouteHandle">
/sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle
↔ bool
</dt>
<dd>
  A flag that indicates whether the resulting route should contain a /sdk-for-flutter-navigate-routing-routehandle-class.
Defaults to <code>false</code>.
Note that a <code>RouteHandle</code> generated by the online <code>RoutingEngine</code> is not compatible with the <code>OfflineRoutingEngine</code> and vice versa.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableRouteLabels">
/sdk-for-flutter-navigate-routing-routeoptions-enableroutelabels
↔ bool
</dt>
<dd>
  Specifies whether route labels should be included in the route response.
Route labels identify major highways or road names along the route.
By default, this is set to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="enableTolls">
/sdk-for-flutter-navigate-routing-routeoptions-enabletolls
↔ bool
</dt>
<dd>
  A flag that indicates whether the resulting route /sdk-for-flutter-navigate-routing-section-tolls properties should contain
tolls data. Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="hashCode">
/sdk-for-flutter-navigate-routing-routeoptions-hashcode
→ int
</dt>
<dd>
  The hash code for this object.
  <div class="features">no setter</div>
</dd>
<dt class="property" id="optimizationMode">
/sdk-for-flutter-navigate-routing-routeoptions-optimizationmode
↔ /sdk-for-flutter-navigate-routing-optimizationmode
</dt>
<dd>
  The optimization mode to be used for route calculation. By default, it is /sdk-for-flutter-navigate-routing-optimizationmode.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="optimizeWaypointsOrder">
/sdk-for-flutter-navigate-routing-routeoptions-optimizewaypointsorder
↔ bool
</dt>
<dd>
  A flag that indicates whether the order of waypoints that is passed to <code>calculateRoute()</code> should be optimized in the best order.
The best order is calculated by the same metrics that are used during regular calculation, e.g. /sdk-for-flutter-navigate-routing-optimizationmode.
The starting and destination /sdk-for-flutter-navigate-routing-waypoint-class are not reordered.
If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize).
The resulting order of waypoints can be identified by their waypoint indices in the route sections
(see /sdk-for-flutter-navigate-routing-route-sections, /sdk-for-flutter-navigate-routing-section-departureplace, /sdk-for-flutter-navigate-routing-section-arrivalplace, /sdk-for-flutter-navigate-routing-routeplace-waypointindex).
Currently, the waypoints order optimization is available only when using the <code>OfflineRoutingEngine</code> (only available for the Navigate license).
Defaults to <code>false</code>.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property inherited" id="runtimeType">
/sdk-for-flutter-navigate-routing-routeoptions-runtimetype
→ Type
</dt>
<dd class="inherited">
  A representation of the runtime type of the object.
  <div class="features">no setterinherited</div>
</dd>
<dt class="property" id="speedCapInMetersPerSecond">
/sdk-for-flutter-navigate-routing-routeoptions-speedcapinmeterspersecond
↔ double?
</dt>
<dd>
  Specifies the maximum speed in meters per second, which the user wishes not to exceed.
The valid range is [1, 70] meters per second. Note that it is valid only for /sdk-for-flutter-navigate-transport-transportmode,
/sdk-for-flutter-navigate-transport-transportmode and /sdk-for-flutter-navigate-transport-transportmode transport modes.
For car, truck and scooter transport modes, it will affect /sdk-for-flutter-navigate-routing-route-duration of
the route. Only for scooter transport mode, it may affect the route geometry. Defaults to <code>null</code>,
which means that no speed cap is set.
  <div class="features">getter/setter pair</div>
</dd>
<dt class="property" id="trafficOptimizationMode">
/sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode
↔ /sdk-for-flutter-navigate-routing-trafficoptimizationmode
</dt>
<dd>
  The traffic optimization mode to be used for route calculation. By default, it is /sdk-for-flutter-navigate-routing-trafficoptimizationmode, which enables traffic-aware routing.
  <div class="features">getter/setter pair</div>
</dd>
</dl>
</section>
<section class="summary offset-anchor inherited" id="instance-methods">
<h2>Methods</h2>
<dl class="callables">
<dt class="callable inherited" id="noSuchMethod">
/sdk-for-flutter-navigate-routing-routeoptions-nosuchmethod(<wbr/>Invocation invocation)
    → dynamic

</dt>
<dd class="inherited">
  Invoked when a nonexistent method or property is accessed.
  <div class="features">inherited</div>
</dd>
<dt class="callable inherited" id="toString">
/sdk-for-flutter-navigate-routing-routeoptions-tostring(<wbr/>)
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
/sdk-for-flutter-navigate-routing-routeoptions-operator-equals(<wbr/>Object other)
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
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
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
`
}</HTMLBlock>
