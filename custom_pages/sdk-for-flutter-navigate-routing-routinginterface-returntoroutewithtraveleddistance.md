---
title: "returnToRouteWithTraveledDistance method - RoutingInterface class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-routinginterface-returntoroutewithtraveleddistance"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- returnToRouteWithTraveledDistance.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RoutingInterface-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">returnToRouteWithTraveledDistance</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> <span class="name">returnToRouteWithTraveledDistance</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-route" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-route-class">Route</a></span> <span class="parameter-name">route</span>, </span>
2.  <span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">startingPoint</span>, </span>
3.  <span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-lastTraveledSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">lastTraveledSectionIndex</span>, </span>
4.  <span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-traveledDistanceOnLastSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnLastSectionInMeters</span>, </span>
5.  <span id="sdk-for-flutter-navigate-returnToRouteWithTraveledDistance-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-calculateroutecallback">CalculateRouteCallback</a></span> <span class="parameter-name">callback</span>, </span>

)

</div>

<div class="section desc markdown">

Asynchronously calculates a new route that leads back to the original route.

The part of the original route which was already traveled by the user is ignored.

**Note:** Stopover waypoints are guaranteed to be visited. Pass-through waypoints will be ignored. Additionally, the following route options are ignored: <a href="sdk-for-flutter-navigate-routing-routeoptions-alternatives">RouteOptions.alternatives</a>, <a href="sdk-for-flutter-navigate-routing-routeoptions-arrivaltime">RouteOptions.arrivalTime</a>, and <a href="sdk-for-flutter-navigate-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a>. Most route options are only applied to the newly calculated part back to the route.

An application may use this method to submit a new starting point for a previously calculated route. This method tries to avoid a costly route re-calculation as much as possible. In case returning to the route without re-calculation is not possible, a new route is calculated, while trying to salvage the previous route as much as possible. However, a completely new route containing no part of the previous route is possible, too.

Note that this function uses only a limited amount of map data around the new origin. Therefore, it may also work fine with temporarily cached map data. It may also copy some of the original route data into the new route.

A typical use case is to await at least 3 `RouteDeviation` events before calling this method.

- Or alternatively, wait at least 10 seconds after getting the first deviation event.
- On top, the user experience can be improved by checking if the vehicle has moved at least 50 meters since calling this method for the last time.
- Optionally, it may make sense to verify if the vehicle was ever following the route by checking if `RouteDeviation.lastLocationOnRoute` is set.

Note that deviation events are sent each time a deviation is detected, i.e. for each new location update, regardless if the location has changed or not. More information can be found in the Developer Guide in the "Handle route deviations" section.

- `route` A <a href="sdk-for-flutter-navigate-routing-route-class">Route</a> calculated using the online or offline route engine. For the offline case, It should not contain an indoor <a href="sdk-for-flutter-navigate-routing-section-class">Section</a> as such routes will fail. For the online case, it should have <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>.

- `startingPoint` The current location, for example, provided by a `RouteDeviation` event. The waypoint needs to be of type <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType.stopover</a>. Otherwise, an <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.invalidParameter</a> error is generated.

- `lastTraveledSectionIndex` Indicates the index of the last traveled route section. Traveled part of the route won't be reused.

- `traveledDistanceOnLastSectionInMeters` Offset in meter to the last visited position on the route section defined by the last traveled section index.

- `callback` Callback object that will be invoked after route calculation. It is always invoked on the main thread.

Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.

</div>

## Implementation

``` dart
TaskHandle returnToRouteWithTraveledDistance(Route route, Waypoint startingPoint, int lastTraveledSectionIndex, int traveledDistanceOnLastSectionInMeters, CalculateRouteCallback callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
