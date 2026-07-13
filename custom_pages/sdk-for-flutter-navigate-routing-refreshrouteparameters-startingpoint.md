---
title: "startingPoint property - RefreshRouteParameters class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-refreshrouteparameters-startingpoint"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RefreshRouteParameters-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">startingPoint</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a>? <span class="name">startingPoint</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Identify the new starting point of the route. It should be of type <a href="sdk-for-flutter-navigate-routing-waypointtype">WaypointType.stopover</a>. Otherwise, an <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.invalidParameter</a> error is generated. Moreover, it should be very close to the original route specified with the <a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a>. The location of this waypoint may by provided, for example, by a `RouteProgress` event. Since the new starting point is expected to be along the original route, the original route geometry is used to reach the remaining waypoints. The new route will not include the <a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a> items that lie behind the new starting point (i.e. the path that was already traveled). Plus, <a href="sdk-for-flutter-navigate-routing-route-lengthinmeters">Route.lengthInMeters</a>, <a href="sdk-for-flutter-navigate-routing-route-duration">Route.duration</a>, and similar values are from the new starting point to the destination. If the new waypoint is too far off the original route, the route refresh may fail and an <a href="sdk-for-flutter-navigate-routing-routingerror">RoutingError.couldNotMatchOrigin</a> error is triggered. In that case, an application may decide to calculate a new route from scratch.

</div>

## Implementation

``` dart
Waypoint? startingPoint;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

