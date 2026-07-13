---
title: "sideOfStreetHint property - Waypoint class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-waypoint-sideofstreethint"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- sideOfStreetHint.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/Waypoint-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">sideOfStreetHint</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a>? <span class="name">sideOfStreetHint</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Optional coordinates to indicate which side of the street should be used to reach the waypoint. For example, if the location is to the left of the street, the router will prefer using that side in case the street has dividers. Note that this option is ignored if the user sets <a href="sdk-for-flutter-navigate-routing-waypoint-transitradiusinmeters">Waypoint.transitRadiusInMeters</a> option with a value greater than zero.

</div>

## Implementation

``` dart
GeoCoordinates? sideOfStreetHint;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
