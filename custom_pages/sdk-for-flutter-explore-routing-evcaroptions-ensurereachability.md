---
title: "ensureReachability property - EVCarOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-evcaroptions-ensurereachability"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ensureReachability.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/EVCarOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">ensureReachability</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">ensureReachability</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Ensure that the vehicle does not run out of energy along the way. Requires valid <a href="sdk-for-flutter-explore-routing-evcaroptions-batteryspecifications">EVCarOptions.batterySpecifications</a>. It also requires that <a href="sdk-for-flutter-explore-routing-routeoptions-optimizationmode">RouteOptions.optimizationMode</a> = <a href="sdk-for-flutter-explore-routing-optimizationmode">OptimizationMode.fastest</a>, <a href="sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond">RouteOptions.speedCapInMetersPerSecond</a> is not set, and <a href="sdk-for-flutter-explore-routing-avoidanceoptions-class">AvoidanceOptions</a> is empty. Otherwise, this object is considered invalid. Setting this flag enables calculation of a route optimized for electric vehicles. Charging stations may be added along the route to ensure that the vehicle does not run out of energy along the way. It is especially useful for longer routes, because after all, charging stations are much less common than petrol stations. **Note** An `sdk.routing.RoutingError.INVALID_PARAMETER` is generated when the `sdk.routing.EVCarOptions.ensure_reachability` is set to `true` in case `sdk.routing.RoutingEngine.import_route` is called. Defaults to `false`.

</div>

## Implementation

``` dart
bool ensureReachability;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
