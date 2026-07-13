---
title: "speedCapInMetersPerSecond property - RouteOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-routeoptions-speedcapinmeterspersecond"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/RouteOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">speedCapInMetersPerSecond</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">speedCapInMetersPerSecond</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies the maximum speed in meters per second, which the user wishes not to exceed. The valid range is \[1, 70\] meters per second. Note that it is valid only for <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.car</a>, <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.truck</a> and <a href="sdk-for-flutter-explore-transport-transportmode">TransportMode.scooter</a> transport modes. For car, truck and scooter transport modes, it will affect <a href="sdk-for-flutter-explore-routing-route-duration">Route.duration</a> of the route. Only for scooter transport mode, it may affect the route geometry. Defaults to `null`, which means that no speed cap is set.

</div>

## Implementation

``` dart
double? speedCapInMetersPerSecond;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

