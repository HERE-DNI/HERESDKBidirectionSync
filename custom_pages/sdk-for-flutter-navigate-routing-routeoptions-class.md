---
title: "RouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routeoptions-class"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOptions-class.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/RouteOptions-class-sidebar.html">

<div>

# <span class="kind-class">RouteOptions</span> class

</div>

<div class="section desc markdown">

The options to specify how the route will be calculated.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-routeoptions">RouteOptions</a></span><span class="signature">(\<a href="sdk-for-flutter-navigate-routing-optimizationmode"><span id="sdk-for-flutter-navigate-param-optimizationMode" class="parameter"><span class="type-annotation">[OptimizationMode</a></span> <span class="parameter-name">optimizationMode</span> = <span class="default-value">OptimizationMode.fastest</span>, </span><span id="sdk-for-flutter-navigate-param-alternatives" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">alternatives</span> = <span class="default-value">0</span>, </span><span id="sdk-for-flutter-navigate-param-departureTime" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">departureTime</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-arrivalTime" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">arrivalTime</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-speedCapInMetersPerSecond" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">speedCapInMetersPerSecond</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-enableRouteHandle" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableRouteHandle</span> = <span class="default-value">false</span>, </span><span id="sdk-for-flutter-navigate-param-trafficOptimizationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span> <span class="parameter-name">trafficOptimizationMode</span> = <span class="default-value">TrafficOptimizationMode.timeDependent</span>, </span><span id="sdk-for-flutter-navigate-param-enableTolls" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableTolls</span> = <span class="default-value">false</span>, </span><span id="sdk-for-flutter-navigate-param-optimizeWaypointsOrder" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">optimizeWaypointsOrder</span> = <span class="default-value">false</span>, </span><span id="sdk-for-flutter-navigate-param-enableRouteLabels" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableRouteLabels</span> = <span class="default-value">false</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-routeoptions-withdefaults">RouteOptions.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-alternatives">alternatives</a></span> <span class="signature">↔ int</span>  
Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">arrivalTime</a></span> <span class="signature">↔ DateTime?</span>  
Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">departureTime</a></span> <span class="signature">↔ DateTime?</span>  
Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-enableroutehandle">enableRouteHandle</a></span> <span class="signature">↔ bool</span>  
A flag that indicates whether the resulting route should contain a <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-enableroutelabels">enableRouteLabels</a></span> <span class="signature">↔ bool</span>  
Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-enabletolls">enableTolls</a></span> <span class="signature">↔ bool</span>  
A flag that indicates whether the resulting route <a href="sdk-for-flutter-navigate-routing-section-tolls">Section.tolls</a> properties should contain tolls data. Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-optimizationmode">optimizationMode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a></span>  
The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.fastest</a>.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-optimizewaypointsorder">optimizeWaypointsOrder</a></span> <span class="signature">↔ bool</span>  
A flag that indicates whether the order of waypoints that is passed to

    calculateRoute()

should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a>. The starting and destination <a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="sdk-for-flutter-navigate-routing-route-sections">Route.sections</a>, <a href="sdk-for-flutter-navigate-routing-section-departureplace">Section.departurePlace</a>, <a href="sdk-for-flutter-navigate-routing-section-arrivalplace">Section.arrivalPlace</a>, <a href="sdk-for-flutter-navigate-routing-routeplace-waypointindex">RoutePlace.waypointIndex</a>). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-speedcapinmeterspersecond">speedCapInMetersPerSecond</a></span> <span class="signature">↔ double?</span>  
Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a> and <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.scooter</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="sdk-for-flutter-navigate-routing-route-duration">Route.duration</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">trafficOptimizationMode</a></span> <span class="signature">↔ <a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span>  
The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode.timeDependent</a>, which enables traffic-aware routing.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-routeoptions-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
