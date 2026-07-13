---
title: "chargingCurve property - BatterySpecifications class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-batteryspecifications-chargingcurve"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- chargingCurve.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">chargingCurve</span> property

</div>

<div class="section multi-line-signature">

Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span> <span class="name">chargingCurve</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \<a href="sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">0, [BatterySpecifications.targetChargeInKilowattHours</a>\], otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

</div>

## Implementation

``` dart
Map<double, double> chargingCurve;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
