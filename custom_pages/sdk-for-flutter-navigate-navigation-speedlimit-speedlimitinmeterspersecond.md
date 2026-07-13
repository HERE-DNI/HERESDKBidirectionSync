---
title: "speedLimitInMetersPerSecond property - SpeedLimit class - navigation library - Dart API"
slug: "sdk-for-flutter-navigate-navigation-speedlimit-speedlimitinmeterspersecond"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- speedLimitInMetersPerSecond.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="navigation/SpeedLimit-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">speedLimitInMetersPerSecond</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">speedLimitInMetersPerSecond</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Regular speed limit if available. In case of unbounded speed limit, the value is zero.

**Note:** When following a route, then this value will depend on the selected transport mode. For other speed limits, like weather-dependent speed limits only the value as shown on the local road sign is provided. It may not be applicable to all transport modes. For tracking mode (without following a route), the VehicleProfile is ignored and only the speed limit from the local road sign is provided or the regular speed limit for a particular type of road or area like regular inner-city speed limits.

</div>

## Implementation

``` dart
double? speedLimitInMetersPerSecond;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
