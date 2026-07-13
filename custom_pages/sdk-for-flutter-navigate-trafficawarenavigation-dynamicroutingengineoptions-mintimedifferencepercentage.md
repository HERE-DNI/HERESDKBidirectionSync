---
title: "minTimeDifferencePercentage property - DynamicRoutingEngineOptions class - trafficawarenavigation library - Dart API"
slug: "sdk-for-flutter-navigate-trafficawarenavigation-dynamicroutingengineoptions-mintimedifferencepercentage"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="trafficawarenavigation/DynamicRoutingEngineOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">minTimeDifferencePercentage</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">minTimeDifferencePercentage</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The value is in the range of \[0, 1\] over the remaining (current position to next waypoint) To get notified, the following check must be true: oldEstimatedTimeOfArrival - newEstimatedTimeOfArrival \>= newRouteDuration \* `min_time_difference_percentage`. A value of 0 will be treated as `null` meaning no event will be sent. In order to receive events the difference needs to be greater than 0. Defaults to `null`.

</div>

## Implementation

``` dart
double? minTimeDifferencePercentage;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

