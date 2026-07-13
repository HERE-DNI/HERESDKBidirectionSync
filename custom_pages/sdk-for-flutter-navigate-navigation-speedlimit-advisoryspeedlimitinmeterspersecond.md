---
title: "advisorySpeedLimitInMetersPerSecond property - SpeedLimit class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedlimit-advisoryspeedlimitinmeterspersecond"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- advisorySpeedLimitInMetersPerSecond.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpeedLimit-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">advisorySpeedLimitInMetersPerSecond</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">advisorySpeedLimitInMetersPerSecond</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

A recommended speed limit that may not be indicated on the local road signs, but that serves to warn a driver that the road conditions may indicate a lower speed. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road.

- Advisory speed signs due to construction are not included.
- A speed value is published for advisory signs.

A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

</div>

## Implementation

``` dart
double? advisorySpeedLimitInMetersPerSecond;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
