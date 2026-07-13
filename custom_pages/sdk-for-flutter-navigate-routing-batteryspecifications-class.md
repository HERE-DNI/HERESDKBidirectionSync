---
title: "BatterySpecifications class - routing library - Dart API"
slug: "sdk-for-flutter-navigate-routing-batteryspecifications-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="routing/routing-library-sidebar.html" data-below-sidebar="routing/BatterySpecifications-class-sidebar.html">

<div>

# <span class="kind-class">BatterySpecifications</span> class

</div>

<div class="section desc markdown">

Parameters related to the electric vehicle's battery.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-batteryspecifications">BatterySpecifications</a></span><span class="signature">(\<a href="sdk-for-flutter-navigate-routing-chargingconnectortype"><span id="sdk-for-flutter-navigate-param-totalCapacityInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">totalCapacityInKilowattHours</span> = <span class="default-value">0.0</span>, </span><span id="sdk-for-flutter-navigate-param-initialChargeInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">initialChargeInKilowattHours</span> = <span class="default-value">0.0</span>, </span><span id="sdk-for-flutter-navigate-param-targetChargeInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">targetChargeInKilowattHours</span> = <span class="default-value">0.0</span>, </span><span id="sdk-for-flutter-navigate-param-chargingCurve" class="parameter"><span class="type-annotation">Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span></span> <span class="parameter-name">chargingCurve</span> = <span class="default-value">const {}</span>, </span><span id="sdk-for-flutter-navigate-param-connectorTypes" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter">[ChargingConnectorType</a></span>\></span></span> <span class="parameter-name">connectorTypes</span> = <span class="default-value">const \[\]</span>, </span><span id="sdk-for-flutter-navigate-param-minChargeAtChargingStationInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minChargeAtChargingStationInKilowattHours</span> = <span class="default-value">0.0</span>, </span><span id="sdk-for-flutter-navigate-param-minChargeAtFirstChargingStationInKilowattHours" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">minChargeAtFirstChargingStationInKilowattHours</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-minChargeAtDestinationInKilowattHours" class="parameter"><span class="type-annotation">double</span> <span class="parameter-name">minChargeAtDestinationInKilowattHours</span> = <span class="default-value">0.0</span>, </span><span id="sdk-for-flutter-navigate-param-maxChargingVoltageInVolts" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">maxChargingVoltageInVolts</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-maxChargingCurrentInAmperes" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">maxChargingCurrentInAmperes</span> = <span class="default-value">null</span>, </span><span id="sdk-for-flutter-navigate-param-chargingSetupDuration" class="parameter"><span class="type-annotation">Duration</span> <span class="parameter-name">chargingSetupDuration</span> = <span class="default-value">const Duration(seconds: 0)</span>, </span><span id="sdk-for-flutter-navigate-param-maxPowerAtLowVoltageInKilowatts" class="parameter"><span class="type-annotation">double?</span> <span class="parameter-name">maxPowerAtLowVoltageInKilowatts</span> = <span class="default-value">null</span></span>\])</span>  
Creates a new instance.

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-batteryspecifications-withdefaults">BatterySpecifications.withDefaults</a></span><span class="signature">()</span>  
Creates a new instance.

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-chargingcurve">chargingCurve</a></span> <span class="signature">↔ Map<span class="signature">\<<wbr></wbr><span class="type-parameter">double</span>, <span class="type-parameter">double</span>\></span></span>  
Function curve describing the maximum battery charging rate (in kW) at a given charge level (in kWh). Map keys represent charge levels that are non-negative floating point values in units of (kWh). Map values represent charging rate values that are positive floating point values in units of (kW). Given charge levels must cover the entire range of \<a href="sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">0, [BatterySpecifications.targetChargeInKilowattHours</a>\], otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. The charging curve is considered piecewise constant instead of being interpolated. Defaults to an empty container. **Note:** For a user-planned <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If one or more values are not set, the route calculation will fail as an invalid parameter error.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-chargingsetupduration">chargingSetupDuration</a></span> <span class="signature">↔ Duration</span>  
Time in seconds spent after arriving at a charging station, but before actually charging, e.g., time spent for payment processing. Defaults to 0 seconds.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-connectortypes">connectorTypes</a></span> <span class="signature">↔ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-routing-chargingconnectortype">ChargingConnectorType</a></span>\></span></span>  
List of available charging connector types. It must be at least one charging connector type added, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to an empty container.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-initialchargeinkilowatthours">initialChargeInKilowattHours</a></span> <span class="signature">↔ double</span>  
Charge level of the vehicle's battery at the start of the route (in kWh). It must be non-negative and less than or equal to the value of <a href="sdk-for-flutter-navigate-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an an invalid parameter error.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-maxchargingcurrentinamperes">maxChargingCurrentInAmperes</a></span> <span class="signature">↔ double?</span>  
Maximum charging current supported by the vehicle's battery in Amperes. It must be positive. When omitted, the charging current is determined by the charging station attributes. Defaults to `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-maxchargingvoltageinvolts">maxChargingVoltageInVolts</a></span> <span class="signature">↔ double?</span>  
Maximum charging voltage supported by the vehicle's battery in Volts. It must be positive. When omitted, the voltage is determined by the charging station attributes. Defaults to `null`.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-maxpoweratlowvoltageinkilowatts">maxPowerAtLowVoltageInKilowatts</a></span> <span class="signature">↔ double?</span>  
The maximum power in kilowatts at which a vehicle can charge under given these conditions:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">minChargeAtChargingStationInKilowattHours</a></span> <span class="signature">↔ double</span>  
Minimum charge when arriving at a charging station in kWh. It must be non-negative and less than the value of <a href="sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatdestinationinkilowatthours">minChargeAtDestinationInKilowattHours</a></span> <span class="signature">↔ double</span>  
Minimum charge at the final route destination in kWh. It must be non-negative and less than the value of <a href="sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatfirstchargingstationinkilowatthours">minChargeAtFirstChargingStationInKilowattHours</a></span> <span class="signature">↔ double?</span>  
Minimum charge when arriving at first charging station in kWh. This overrides <a href="sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> for the first charging station. If not specified, <a href="sdk-for-flutter-navigate-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> will be used for all charging stations, including the first one. Defaults to `null`. When initialized, it must be non-negative and less than the value of <a href="sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. This is usually used when the current charge is too low to reach a charging station within `minChargeAtChargingStation` limits.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-targetchargeinkilowatthours">targetChargeInKilowattHours</a></span> <span class="signature">↔ double</span>  
Maximum charge to which the battery should be charged at a charging station (in kWh). It must be positive and less than or equal to the value of <a href="sdk-for-flutter-navigate-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>, otherwise the <a href="sdk-for-flutter-navigate-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid. Defaults to 0.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-totalcapacityinkilowatthours">totalCapacityInKilowattHours</a></span> <span class="signature">↔ double</span>  
Total capacity of the vehicle's battery (in kWh). It must be positive. Defaults to 0. **Note:** For a user-planned <a href="sdk-for-flutter-navigate-routing-chargingstop-class">ChargingStop</a>, this parameter is also required. If not set greater than 0, the route calculation will fail as an invalid parameter error.

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-routing-batteryspecifications-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

