---
title: "avoidCorridorArea property - AvoidCorridorAreaOptions class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-avoidcorridorareaoptions-avoidcorridorarea"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- avoidCorridorArea.html -->
<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/AvoidCorridorAreaOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">avoidCorridorArea</span> property

</div>

<div class="section multi-line-signature">

<a href="sdk-for-flutter-explore-core-geocorridor-class">GeoCorridor</a> <span class="name">avoidCorridorArea</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Area of corridor shape which routes must not cross. Strictly enforced. Violations are reported as <a href="sdk-for-flutter-explore-routing-sectionnoticecode">SectionNoticeCode.violatedBlockedRoad</a>. **Note:** This avoidance option is not supported for `IsolineOptions`. If it is defined for isoline calculation then an `sdk.routing.RoutingError.INVALID_PARAMETER` error is generated. Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an `sdk.routing.RoutingError.INVALID_PARAMETER` error.

</div>

## Implementation

``` dart
GeoCorridor avoidCorridorArea;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
