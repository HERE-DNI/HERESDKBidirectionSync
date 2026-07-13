---
title: "ChargingStop constructor - ChargingStop - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-chargingstop-chargingstop"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/ChargingStop-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">ChargingStop</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">ChargingStop</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-explore-param-powerInKilowatts" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">powerInKilowatts</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-currentInAmperes" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">currentInAmperes</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-voltageInVolts" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">voltageInVolts</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-supplyType" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-explore-routing-chargingsupplytype">ChargingSupplyType</a>?</span> <span class="parameter-name">supplyType</span>, </span>
5.  <span id="sdk-for-flutter-explore-param-minDuration" class="parameter"><span class="type-annotation">Duration?</span> <span class="parameter-name">minDuration</span>, </span>
6.  <span id="sdk-for-flutter-explore-param-maxDuration" class="parameter"><span class="type-annotation">Duration?</span> <span class="parameter-name">maxDuration</span>, </span>

)

</div>

<div class="section desc markdown">

Creates a new instance.

- `powerInKilowatts` The value of rated power of the connector (in kW).
- `currentInAmperes` The value of rated current of the connector (in A).
- `voltageInVolts` The value of rated voltage of the connector (in V).
- `supplyType` Supply type of the suggested connector.
- `minDuration` The minimum duration the user expects to charge at the station, including <a href="sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration">BatterySpecifications.chargingSetupDuration</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.
- `maxDuration` The maximum duration the user plans to charge at the station, including <a href="sdk-for-flutter-explore-routing-batteryspecifications-chargingsetupduration">BatterySpecifications.chargingSetupDuration</a>. **Note:** At least one of `min_duration` and `max_duration` is required for a user-planned charging stop. For most use cases, providing at least `min_duration` is recommended.

</div>

## Implementation

``` dart
ChargingStop(this.powerInKilowatts, this.currentInAmperes, this.voltageInVolts, this.supplyType, this.minDuration, this.maxDuration);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

