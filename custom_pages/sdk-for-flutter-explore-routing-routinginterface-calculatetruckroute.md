---
title: "calculateTruckRoute method - RoutingInterface class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routinginterface-calculatetruckroute"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- calculateTruckRoute.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">calculateTruckRoute</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the \`calculate_route()\` methods with RoutingOptions parameter instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name deprecated">calculateTruckRoute</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-calculateTruckRoute-param-waypoints" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a></span>\></span></span> <span class="parameter-name">waypoints</span>, </span>
2.  <span id="sdk-for-flutter-explore-calculateTruckRoute-param-truckOptions" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-truckoptions-class" class="deprecated">TruckOptions</a></span> <span class="parameter-name">truckOptions</span>, </span>
3.  <span id="sdk-for-flutter-explore-calculateTruckRoute-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates a truck route from one point to another, passing through the given waypoints in the given order.

- `waypoints` The list of waypoints used to calculate the route. The first element marks the starting position, the last marks the destination. Waypoints in between are interpreted as intermediate.

An <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated when the waypoint list contains less than two elements or when the first and the last waypoints are not of type <a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>.

- `truckOptions` Options specific for truck route calculation, along with common route options.

- `callback` Callback object that will be invoked after route calculation. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the `calculate_route()` methods with RoutingOptions parameter instead.")

TaskHandle calculateTruckRoute(List<Waypoint> waypoints, TruckOptions truckOptions, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
