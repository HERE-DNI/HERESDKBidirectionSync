---
title: "corridorExceptionAreas property - AvoidCorridorAreaOptions class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-avoidcorridorareaoptions-corridorexceptionareas"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- corridorExceptionAreas.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/AvoidCorridorAreaOptions-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">corridorExceptionAreas</span> property

</div>

<div class="section multi-line-signature">

List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a></span>\></span> <span class="name">corridorExceptionAreas</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Areas of corridor shape to exclude from avoidance. **Note:** Even though `GeoCorridor.half_width_in_meters` is an optional property in case of exception areas it is mandatory. Otherwise route calculation will fail with an `sdk.routing.RoutingError.INVALID_PARAMETER` error.

</div>

## Implementation

``` dart
List<GeoCorridor> corridorExceptionAreas;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
