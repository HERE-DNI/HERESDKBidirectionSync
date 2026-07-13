---
title: "isCommercial property - VehicleSpecification class - transport library - Dart API"
slug: "sdk-for-flutter-navigate-transport-vehiclespecification-iscommercial"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- isCommercial.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="transport/VehicleSpecification-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">isCommercial</span> property

</div>

<div class="section multi-line-signature">

bool <span class="name">isCommercial</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Specifies whether the vehicle is a commercial or a non-commercial vehicle. Defaults to `false`.

**Notes**

- Only supported for online routing.
- This parameter is currently used only for the calculation of tolls in regions where it is applicable.
- Not used for offline calculations.
- Supported for <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.car</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.truck</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.bus</a>, <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.privateBus</a> and <a href="sdk-for-flutter-navigate-transport-transportmode">TransportMode.taxi</a>.

</div>

## Implementation

``` dart
bool isCommercial;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
