---
title: "maxPowerAtLowVoltageInKilowatts property - BatterySpecifications class - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-maxpoweratlowvoltageinkilowatts"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-property">maxPowerAtLowVoltageInKilowatts</span> property

</div>

<div class="section multi-line-signature">

double? <span class="name">maxPowerAtLowVoltageInKilowatts</span>

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

</div>

<div class="section desc markdown">

The maximum power in kilowatts at which a vehicle can charge under given these conditions:

- The charging station connector's maximum supply voltage is less than 800 V.
- <a href="sdk-for-flutter-explore-routing-batteryspecifications-maxchargingvoltageinvolts">BatterySpecifications.maxChargingVoltageInVolts</a> is greater than or equal to 800 V. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** The feature is not supported by the `OfflineRoutingEngine`.

</div>

## Implementation

``` dart
double? maxPowerAtLowVoltageInKilowatts;
```

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

