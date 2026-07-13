---
title: "BatterySpecifications constructor - BatterySpecifications - routing library - Dart API"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications"
---

<div id="sdk-for-flutter-explore-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-explore-dartdoc-main-content" class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-constructor">BatterySpecifications</span> constructor

</div>

<div class="section multi-line-signature">

<span class="name">BatterySpecifications</span>(<wbr></wbr>\<a href="sdk-for-flutter-explore-routing-chargingconnectortype">

1.  <span id="sdk-for-flutter-explore-param-totalCapacityInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">totalCapacityInKilowattHours</span> = <span class="default-value">0.0</span>, </span>
2.  <span id="sdk-for-flutter-explore-param-initialChargeInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">initialChargeInKilowattHours</span> = <span class="default-value">0.0</span>, </span>
3.  <span id="sdk-for-flutter-explore-param-targetChargeInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">targetChargeInKilowattHours</span> = <span class="default-value">0.0</span>, </span>
4.  <span id="sdk-for-flutter-explore-param-chargingCurve" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span></span> <span class="parameter-name">chargingCurve</span> = <span class="default-value">const {}</span>, </span>
5.  <span id="sdk-for-flutter-explore-param-connectorTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">[ChargingConnectorType</a></span>\></span></span> <span class="parameter-name">connectorTypes</span> = <span class="default-value">const \[\]</span>, </span>
6.  <span id="sdk-for-flutter-explore-param-minChargeAtChargingStationInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minChargeAtChargingStationInKilowattHours</span> = <span class="default-value">0.0</span>, </span>
7.  <span id="sdk-for-flutter-explore-param-minChargeAtFirstChargingStationInKilowattHours" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">minChargeAtFirstChargingStationInKilowattHours</span> = <span class="default-value">null</span>, </span>
8.  <span id="sdk-for-flutter-explore-param-minChargeAtDestinationInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minChargeAtDestinationInKilowattHours</span> = <span class="default-value">0.0</span>, </span>
9.  <span id="sdk-for-flutter-explore-param-maxChargingVoltageInVolts" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">maxChargingVoltageInVolts</span> = <span class="default-value">null</span>, </span>
10. <span id="sdk-for-flutter-explore-param-maxChargingCurrentInAmperes" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">maxChargingCurrentInAmperes</span> = <span class="default-value">null</span>, </span>
11. <span id="sdk-for-flutter-explore-param-chargingSetupDuration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">chargingSetupDuration</span> = <span class="default-value">const Duration(seconds: 0)</span>, </span>
12. <span id="sdk-for-flutter-explore-param-maxPowerAtLowVoltageInKilowatts" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">maxPowerAtLowVoltageInKilowatts</span> = <span class="default-value">null</span>, </span>

\])

</div>

<div class="section desc markdown">

Creates a new instance.

- `totalCapacityInKilowattHours` Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.
- `initialChargeInKilowattHours` Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.
- `targetChargeInKilowattHours` Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0.
- `chargingCurve` Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \<a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">0, [BatterySpecifications.targetChargeInKilowattHours</a>\], otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned <a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.
- `connectorTypes` List of available charging connector types. It must be at least one charging connector type added, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to an empty container.
- `minChargeAtChargingStationInKilowattHours` Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0.
- `minChargeAtFirstChargingStationInKilowattHours` Minimum charge when arriving at first charging station in kWh. This overrides <a href="sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> for the first charging station. If not specified, <a href="sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.
- `minChargeAtDestinationInKilowattHours` Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of <a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0.
- `maxChargingVoltageInVolts` Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.
- `maxChargingCurrentInAmperes` Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `null`.
- `chargingSetupDuration` Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.
- `maxPowerAtLowVoltageInKilowatts` The maximum power in kilowatts at which a vehicle can charge under given these conditions:

<!-- -->

- The charging station connector's maximum supply voltage is less than 800 V.
- <a href="sdk-for-flutter-explore-routing-batteryspecifications-maxchargingvoltageinvolts">BatterySpecifications.maxChargingVoltageInVolts</a> is greater than or equal to 800 V. The provided value must be greater than or equal to 0. By default, it is not set. **Note:** The feature is not supported by the `OfflineRoutingEngine`.

</div>

## Implementation

``` dart
BatterySpecifications([double totalCapacityInKilowattHours = 0.0, double initialChargeInKilowattHours = 0.0, double targetChargeInKilowattHours = 0.0, Map<double, double> chargingCurve = const {}, List<ChargingConnectorType> connectorTypes = const [], double minChargeAtChargingStationInKilowattHours = 0.0, double? minChargeAtFirstChargingStationInKilowattHours = null, double minChargeAtDestinationInKilowattHours = 0.0, double? maxChargingVoltageInVolts = null, double? maxChargingCurrentInAmperes = null, Duration chargingSetupDuration = const Duration(seconds: 0), double? maxPowerAtLowVoltageInKilowatts = null])
  : totalCapacityInKilowattHours = totalCapacityInKilowattHours, initialChargeInKilowattHours = initialChargeInKilowattHours, targetChargeInKilowattHours = targetChargeInKilowattHours, chargingCurve = chargingCurve, connectorTypes = connectorTypes, minChargeAtChargingStationInKilowattHours = minChargeAtChargingStationInKilowattHours, minChargeAtFirstChargingStationInKilowattHours = minChargeAtFirstChargingStationInKilowattHours, minChargeAtDestinationInKilowattHours = minChargeAtDestinationInKilowattHours, maxChargingVoltageInVolts = maxChargingVoltageInVolts, maxChargingCurrentInAmperes = maxChargingCurrentInAmperes, chargingSetupDuration = chargingSetupDuration, maxPowerAtLowVoltageInKilowatts = maxPowerAtLowVoltageInKilowatts;
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas-left--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

