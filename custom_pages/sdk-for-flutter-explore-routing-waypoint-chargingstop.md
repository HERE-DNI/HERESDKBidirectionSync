---
title: "chargingStop property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-waypoint-chargingstop"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- chargingStop.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">chargingStop</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>? <span class="name">chargingStop</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies of a user-planned charging stop. The resulting `Route` may contain this waypoint as a `RoutePlace` with a non-null `ChargingStation` member when the provided specifications indicate that a stop is required to charge the EV battery. **Note:** If `EVCarOptions.ensure_reachability` is not set as `true` and `ChargingStop.min_duration` is not provided, route calculation may suggest a better charging stop instead of this stop.

</div>

## Implementation

``` dart
ChargingStop? chargingStop;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
