---
title: "setDistanceToTarget method - MapCamera class - mapview library - Dart API"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-setdistancetotarget"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="mapview/MapCamera-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">setDistanceToTarget</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype">void</span> <span class="name">setDistanceToTarget</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-setDistanceToTarget-param-distanceInMeters" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">distanceInMeters</span></span>

)

</div>

<div class="section desc markdown">

Makes the camera look at current target from certain distance

This function neither modifies target coordinates nor target orientation.

- `distanceInMeters` Distance in meters to the target point. Minimal distance value is clamped to 100 meters.

</div>

## Implementation

``` dart
void setDistanceToTarget(double distanceInMeters);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

