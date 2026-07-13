---
title: "calculatePedestrianRoute method - RoutingInterface class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routinginterface-calculatepedestrianroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculatePedestrianRoute.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculatePedestrianRoute</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the \`calculate_route()\` methods with RoutingOptions parameter instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name deprecated">calculatePedestrianRoute</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-calculatePedestrianRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span>
2.  <span id="sdk-for-flutter-navigate-calculatePedestrianRoute-param-pedestrianOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-pedestrianoptions-class" class="deprecated">PedestrianOptions</a></span> <span class="parameter-name">pedestrianOptions</span>, </span>
3.  <span id="sdk-for-flutter-navigate-calculatePedestrianRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates a pedestrian route from one point to another, passing through the given waypoints in the given order.

- `waypoints` The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

An <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType.stopover</a>.

- `pedestrianOptions` Options specific for pedestrian route calculation, along with common route options. Note that <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.shortest</a> is is not supported for pedestrians and converted to <a href="sdk-for-flutter-navigate-routing-optimizationmode">OptimizationMode.fastest</a> automatically.

- `callback` Callback object that will be invoked after route calculation. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.")

TaskHandle calculatePedestrianRoute(List<Waypoint> waypoints, PedestrianOptions pedestrianOptions, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
