---
title: "RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition constructor - RefreshRouteParameters - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-refreshrouteparameters-refreshrouteparameters-withroutehandleandwaypointandsectionposition"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RefreshRouteParameters-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-withRouteHandleAndWaypointAndSectionPosition-param-routeHandle" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-routehandle-class">RouteHandle</a></span> <span class="parameter-name">routeHandle</span>, </span>
2.  <span id="sdk-for-flutter-navigate-withRouteHandleAndWaypointAndSectionPosition-param-startingPoint" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-routing-waypoint-class">Waypoint</a></span> <span class="parameter-name">startingPoint</span>, </span>
3.  <span id="sdk-for-flutter-navigate-withRouteHandleAndWaypointAndSectionPosition-param-startingSectionIndex" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">startingSectionIndex</span>, </span>
4.  <span id="sdk-for-flutter-navigate-withRouteHandleAndWaypointAndSectionPosition-param-traveledDistanceOnStartingSectionInMeters" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">traveledDistanceOnStartingSectionInMeters</span>, </span>

)

</div>

<div class="section desc markdown">

Create a new instance of <a href="sdk-for-flutter-navigate-routing-refreshrouteparameters-class">RefreshRouteParameters</a> with the new starting point and the section position on the route.

- `routeHandle` The route handle holding the route to be refreshed.

- `startingPoint` Identify the new starting point of the route.

- `startingSectionIndex` Indicates the index of the last traveled route section.

- `traveledDistanceOnStartingSectionInMeters` Provides an indication on how much of the starting section is already traveled.

</div>

## Implementation

``` dart
factory RefreshRouteParameters.withRouteHandleAndWaypointAndSectionPosition(RouteHandle routeHandle, Waypoint startingPoint, int startingSectionIndex, int traveledDistanceOnStartingSectionInMeters) => $prototype.withRouteHandleAndWaypointAndSectionPosition(routeHandle, startingPoint, startingSectionIndex, traveledDistanceOnStartingSectionInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

