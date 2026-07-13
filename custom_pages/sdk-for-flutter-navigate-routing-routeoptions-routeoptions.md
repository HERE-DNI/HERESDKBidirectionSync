---
title: "RouteOptions constructor - RouteOptions - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routeoptions-routeoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RouteOptions.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RouteOptions</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RouteOptions</span>(<wbr></wbr>\<a href="sdk-for-flutter-navigate-routing-optimizationmode">

1.  <span id="sdk-for-flutter-navigate-param-optimizationMode" class="parameter"><span class="type-annotation">[OptimizationMode</a></span> <span class="parameter-name">optimizationMode</span> = <span class="default-value">OptimizationMode.fastest</span>, </span>
2.  <span id="sdk-for-flutter-navigate-param-alternatives" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">alternatives</span> = <span class="default-value">0</span>, </span>
3.  <span id="sdk-for-flutter-navigate-param-departureTime" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">departureTime</span> = <span class="default-value">null</span>, </span>
4.  <span id="sdk-for-flutter-navigate-param-arrivalTime" class="parameter"><span class="type-annotation">DateTime?</span> <span class="parameter-name">arrivalTime</span> = <span class="default-value">null</span>, </span>
5.  <span id="sdk-for-flutter-navigate-param-speedCapInMetersPerSecond" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">speedCapInMetersPerSecond</span> = <span class="default-value">null</span>, </span>
6.  <span id="sdk-for-flutter-navigate-param-enableRouteHandle" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableRouteHandle</span> = <span class="default-value">false</span>, </span>
7.  <span id="sdk-for-flutter-navigate-param-trafficOptimizationMode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode</a></span> <span class="parameter-name">trafficOptimizationMode</span> = <span class="default-value">TrafficOptimizationMode.timeDependent</span>, </span>
8.  <span id="sdk-for-flutter-navigate-param-enableTolls" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableTolls</span> = <span class="default-value">false</span>, </span>
9.  <span id="sdk-for-flutter-navigate-param-optimizeWaypointsOrder" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">optimizeWaypointsOrder</span> = <span class="default-value">false</span>, </span>
10. <span id="sdk-for-flutter-navigate-param-enableRouteLabels" class="parameter"><span class="type-annotation">bool</span> <span class="parameter-name">enableRouteLabels</span> = <span class="default-value">false</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `optimizationMode` The optimization mode to be used for route calculation. By default, it is <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.fastest</a>.
- `alternatives` Maximum number of alternative routes that will be calculated, in addition to the best one. The provided value must be in the range \[0, 6\]. Alternative routes can be unavailable, thus they are not guaranteed to be returned. The order of routes is from the best to the worst, as evaluated by the route calculation algorithm and according to the given input parameters. Defaults to 0, which means there are no alternatives, i.e. only the best route is returned. Must be 0 for isoline calculation.
- `departureTime` Optional time when travel is expected to start. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, i.e. now. Therefore, by default, a time-aware route request is initiated including traffic.

**Note**:

- Both departure time and <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a> cannot be set at the same time.
- This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

<!-- -->

- `arrivalTime` Optional time when travel is expected to end. Traffic speed and incidents shall be taken into account in the calculation of the route, per <a href="sdk-for-flutter-navigate-routing-routeoptions-trafficoptimizationmode">RouteOptions.trafficOptimizationMode</a>. By default, the time is not set. If the time is not set, the current time will be used internally, to predict the arrival time. Therefore, by default, a time-aware route request is initiated including traffic.

**Note**:

- Both <a href="sdk-for-flutter-navigate-routing-routeoptions-departuretime">RouteOptions.departureTime</a> and arrival time cannot be set at the same time.
- This parameter is handled as local time. Therefore, it is necessary to specify the time zone offset when setting the time in areas with different time zones, i.e. 2025-02-04T08:00:00+07:00

<!-- -->

- `speedCapInMetersPerSecond` Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a> and <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.scooter</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="sdk-for-flutter-navigate-routing-route-duration">Route.duration</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.
- `enableRouteHandle` A flag that indicates whether the resulting route should contain a <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>. Defaults to `false`. Note that a `RouteHandle` generated by the online `RoutingEngine` is not compatible with the `OfflineRoutingEngine` and vice versa.
- `trafficOptimizationMode` The traffic optimization mode to be used for route calculation. By default, it is <a href="sdk-for-flutter-navigate-routing-trafficoptimizationmode">TrafficOptimizationMode.timeDependent</a>, which enables traffic-aware routing.
- `enableTolls` A flag that indicates whether the resulting route <a href="sdk-for-flutter-navigate-routing-section-tolls">Section.tolls</a> properties should contain tolls data. Defaults to `false`.

**Note:** When a route calculation request asks tolls, a pricing scheme with higher rates might be applied. Consult your HERE representative to get more information on the related pricing schemes.

**Note:** For users of the `OfflineRoutingEngine` this is a beta release of this feature, so there could be a few bugs and unexpected behaviors. The `OfflineRoutingEngine` is only available for the Navigate license. For users of the `RoutingEngine` the feature is stable.

- `optimizeWaypointsOrder` A flag that indicates whether the order of waypoints that is passed to

      calculateRoute()

  should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode</a>. The starting and destination <a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="sdk-for-flutter-navigate-routing-route-sections">Route.sections</a>, <a href="sdk-for-flutter-navigate-routing-section-departureplace">Section.departurePlace</a>, <a href="sdk-for-flutter-navigate-routing-section-arrivalplace">Section.arrivalPlace</a>, <a href="sdk-for-flutter-navigate-routing-routeplace-waypointindex">RoutePlace.waypointIndex</a>). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.

- `enableRouteLabels` Specifies whether route labels should be included in the route response. Route labels identify major highways or road names along the route. By default, this is set to `false`.

</div>

## Implementation

``` dart
RouteOptions([OptimizationMode optimizationMode = OptimizationMode.fastest, int alternatives = 0, DateTime? departureTime = null, DateTime? arrivalTime = null, double? speedCapInMetersPerSecond = null, bool enableRouteHandle = false, TrafficOptimizationMode trafficOptimizationMode = TrafficOptimizationMode.timeDependent, bool enableTolls = false, bool optimizeWaypointsOrder = false, bool enableRouteLabels = false])
  : optimizationMode = optimizationMode, alternatives = alternatives, departureTime = departureTime, arrivalTime = arrivalTime, speedCapInMetersPerSecond = speedCapInMetersPerSecond, enableRouteHandle = enableRouteHandle, trafficOptimizationMode = trafficOptimizationMode, enableTolls = enableTolls, optimizeWaypointsOrder = optimizeWaypointsOrder, enableRouteLabels = enableRouteLabels;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
