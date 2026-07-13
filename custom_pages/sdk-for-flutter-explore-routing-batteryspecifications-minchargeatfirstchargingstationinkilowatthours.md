---
title: "minChargeAtFirstChargingStationInKilowattHours property - BatterySpecifications class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-minchargeatfirstchargingstationinkilowatthours"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">minChargeAtFirstChargingStationInKilowattHours</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">minChargeAtFirstChargingStationInKilowattHours</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

Minimum charge when arriving at first charging station in kWh. This overrides <a href="sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> for the first charging station. If not specified, <a href="sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

</div>

## Implementation

``` dart
double? minChargeAtFirstChargingStationInKilowattHours;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

