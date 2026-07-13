---
title: "transitRadiusInMeters property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-waypoint-transitradiusinmeters"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- transitRadiusInMeters.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">transitRadiusInMeters</span> property

</div>

<div class="section multi-line-signature">

int <span class="name">transitRadiusInMeters</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The maximum allowed distance from the waypoint that the calculated route may pass through. For example, to drive past a city without necessarily going into the city center, you can specify the coordinates of the center and a transit radius of 5000m. The default transit radius is zero. If the route should pass the waypoint as close as possible, the default value should be kept. Note that the waypoint will be map-matched to a road. Non-zero values allow a greater tolerance. Note that <a href="sdk-for-flutter-navigate-routing-waypoint-sideofstreethint">Waypoint.sideOfStreetHint</a> option is ignored if the user sets this option with a value greater than zero.

</div>

## Implementation

``` dart
int transitRadiusInMeters;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
