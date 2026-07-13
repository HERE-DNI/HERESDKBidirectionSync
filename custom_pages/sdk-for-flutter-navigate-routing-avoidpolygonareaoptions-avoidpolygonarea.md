---
title: "avoidPolygonArea property - AvoidPolygonAreaOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-avoidpolygonareaoptions-avoidpolygonarea"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/AvoidPolygonAreaOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">avoidPolygonArea</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a> <span class="name">avoidPolygonArea</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Area of polygon shape which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-flutter-navigate-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>. **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated.

</div>

## Implementation

``` dart
GeoPolygon avoidPolygonArea;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

