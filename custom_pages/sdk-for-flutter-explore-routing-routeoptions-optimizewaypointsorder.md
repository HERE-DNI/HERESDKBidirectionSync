---
title: "optimizeWaypointsOrder property - RouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routeoptions-optimizewaypointsorder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- optimizeWaypointsOrder.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">optimizeWaypointsOrder</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">optimizeWaypointsOrder</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A flag that indicates whether the order of waypoints that is passed to

    calculateRoute()

should be optimized in the best order. The best order is calculated by the same metrics that are used during regular calculation, e.g. <a href="sdk-for-flutter-explore-routing-optimizationmode">OptimizationMode</a>. The starting and destination <a href="sdk-for-flutter-explore-routing-waypoint-class">Waypoint</a> are not reordered. If the whole number of waypoints is fewer than 4 - the flag doesn't affect the resulting route (nothing to optimize). The resulting order of waypoints can be identified by their waypoint indices in the route sections (see <a href="sdk-for-flutter-explore-routing-route-sections">Route.sections</a>, <a href="sdk-for-flutter-explore-routing-section-departureplace">Section.departurePlace</a>, <a href="sdk-for-flutter-explore-routing-section-arrivalplace">Section.arrivalPlace</a>, <a href="sdk-for-flutter-explore-routing-routeplace-waypointindex">RoutePlace.waypointIndex</a>). Currently, the waypoints order optimization is available only when using the `OfflineRoutingEngine` (only available for the Navigate license). Defaults to `false`.
</p>

</div>

## Implementation

``` dart
bool optimizeWaypointsOrder;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
