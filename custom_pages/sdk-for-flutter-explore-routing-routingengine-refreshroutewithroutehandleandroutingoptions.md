---
title: "refreshRouteWithRouteHandleAndRoutingOptions method - RoutingEngine class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routingengine-refreshroutewithroutehandleandroutingoptions"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingEngine-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">refreshRouteWithRouteHandleAndRoutingOptions</span> abstract method

</div>

<div class="section multi-line-signature">

<div>

1.  @Deprecated("Will be removed in v4.28.0. Use the \`refresh_route()\` methods with RefreshRouteParameters parameter instead.")

</div>

<span class="returntype"><a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name deprecated">refreshRouteWithRouteHandleAndRoutingOptions</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-refreshRouteWithRouteHandleAndRoutingOptions-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span>
2.  <span id="sdk-for-flutter-explore-refreshRouteWithRouteHandleAndRoutingOptions-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">startingPoint</span>, </span>
3.  <span id="sdk-for-flutter-explore-refreshRouteWithRouteHandleAndRoutingOptions-param-options" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a></span> <span class="parameter-name">options</span>, </span>
4.  <span id="sdk-for-flutter-explore-refreshRouteWithRouteHandleAndRoutingOptions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously refreshes a previously calculated route from the provided <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>, updating the starting point and route metadata based on <a href="sdk-for-flutter-explore-routing-routingoptions-class">RoutingOptions</a>.

The route shape from the new starting point to the destination remains unchanged, and only metadata such as arrival time and traffic delays are updated. If you only want to refresh the contained traffic information, consider to use <a href="sdk-for-flutter-explore-routing-routingengine-calculatetrafficonroutewithcurrentcharge">RoutingEngine.calculateTrafficOnRouteWithCurrentCharge</a> instead.

Calling this method will trigger a new "HERE Routing" transaction, for example, if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.

- `routeHandle` The route handle holding the route to be refreshed.

- `startingPoint` Updates the starting point of the route. It should be of type <a href="sdk-for-flutter-explore-routing-waypointtype">WaypointType.stopover</a>. Otherwise, an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.invalidParameter</a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-flutter-explore-routing-routehandle-class">RouteHandle</a>. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a> items that lie behind the new starting point (i.e. the path that was already traveled). Plus, <a href="sdk-for-flutter-explore-routing-route-lengthinmeters">Route.lengthInMeters</a> and <a href="sdk-for-flutter-explore-routing-route-duration">Route.duration</a> values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-flutter-explore-routing-routingerror">RoutingError.couldNotMatchOrigin</a> error is triggered. In that case, an application may decide to calculate a new route from scratch.

- `options` The options define the vehicle and route options to calculate the route.

- `callback` Callback object that will be invoked after refreshing the route. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
@Deprecated("Will be removed in v4.28.0. Use the `refresh_route()` methods with RefreshRouteParameters parameter instead.")

TaskHandle refreshRouteWithRouteHandleAndRoutingOptions(RouteHandle routeHandle, Waypoint startingPoint, RoutingOptions options, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

