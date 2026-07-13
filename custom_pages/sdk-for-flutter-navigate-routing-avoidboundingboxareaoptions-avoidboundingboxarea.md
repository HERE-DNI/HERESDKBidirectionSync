---
title: "avoidBoundingBoxArea property - AvoidBoundingBoxAreaOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-avoidboundingboxareaoptions-avoidboundingboxarea"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/AvoidBoundingBoxAreaOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">avoidBoundingBoxArea</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-geobox-class">GeoBox</a> <span class="name">avoidBoundingBoxArea</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Area of rectangular shape which routes must not cross. Strictly enforced. **Note:** Violations are reported as `sdk.routing.SectionNoticeCode.VIOLATED_BLOCKED_ROAD`. This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated.

</div>

## Implementation

``` dart
GeoBox avoidBoundingBoxArea;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

