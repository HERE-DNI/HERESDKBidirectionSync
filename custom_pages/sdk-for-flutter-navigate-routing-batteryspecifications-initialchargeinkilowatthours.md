---
title: "initialChargeInKilowattHours property - BatterySpecifications class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-batteryspecifications-initialchargeinkilowatthours"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- initialChargeInKilowattHours.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">initialChargeInKilowattHours</span> property

</div>

<div class="section multi-line-signature">

double <span class="name">initialChargeInKilowattHours</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-flutter-navigate-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

</div>

## Implementation

``` dart
double initialChargeInKilowattHours;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
