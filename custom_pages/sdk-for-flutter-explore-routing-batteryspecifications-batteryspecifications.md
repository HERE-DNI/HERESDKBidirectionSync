---
title: "BatterySpecifications constructor"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BatterySpecifications.html -->


<div>
<h1>BatterySpecifications constructor</h1></div>

BatterySpecifications([<ol class="parameter-list"> <li>double totalCapacityInKilowattHours = 0.0, </li>
<li>double initialChargeInKilowattHours = 0.0, </li>
<li>double targetChargeInKilowattHours = 0.0, </li>
<li>Map&lt;double, double&gt; chargingCurve = const {}, </li>
<li>List&lt;<a href="sdk-for-flutter-explore-routing-chargingconnectortype">ChargingConnectorType</a>&gt; connectorTypes = const [], </li>
<li>double minChargeAtChargingStationInKilowattHours = 0.0, </li>
<li>double? minChargeAtFirstChargingStationInKilowattHours = null, </li>
<li>double minChargeAtDestinationInKilowattHours = 0.0, </li>
<li>double? maxChargingVoltageInVolts = null, </li>
<li>double? maxChargingCurrentInAmperes = null, </li>
<li>Duration chargingSetupDuration = const Duration(seconds: 0), </li>
<li>double? maxPowerAtLowVoltageInKilowatts = null, </li>
</ol>])
    

<p>Creates a new instance.</p>
<ul>
<li><code>totalCapacityInKilowattHours</code> Total capacity of the vehicle's battery (in kWh).
It must be positive.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an invalid parameter error.</li>
<li><code>initialChargeInKilowattHours</code> Charge level of the vehicle's battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
<a href="sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>,
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.</li>
<li><code>targetChargeInKilowattHours</code> Maximum charge to which the battery should be charged at a charging station (in kWh).
It must be positive and less than or equal to the value of
<a href="sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours">BatterySpecifications.totalCapacityInKilowattHours</a>,
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Defaults to 0.</li>
<li><code>chargingCurve</code> Function curve describing the maximum battery charging rate (in kW) at a given charge
level (in kWh).
Map keys represent charge levels that are non-negative floating point values
in units of (kWh).
Map values represent charging rate values that are positive floating point values
in units of (kW).
Given charge levels must cover the entire range of
[0, <a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>],
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
The charging curve is considered piecewise constant instead of being interpolated.
Defaults to an empty container.
<strong>Note:</strong>
For a user-planned <a href="sdk-for-flutter-explore-routing-chargingstop-class">ChargingStop</a>, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.</li>
<li><code>connectorTypes</code> List of available charging connector types.
It must be at least one charging connector type added, otherwise
the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Defaults to an empty container.</li>
<li><code>minChargeAtChargingStationInKilowattHours</code> Minimum charge when arriving at a charging station in kWh.
It must be non-negative and less than the value of
<a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>,
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Defaults to 0.</li>
<li><code>minChargeAtFirstChargingStationInKilowattHours</code> Minimum charge when arriving at first charging station in kWh.
This overrides <a href="sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> for the first charging station.
If not specified, <a href="sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a> will be used
for all charging stations, including the first one.
Defaults to <code>null</code>.
When initialized, it must be non-negative and less than the value of
<a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>,
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</li>
<li><code>minChargeAtDestinationInKilowattHours</code> Minimum charge at the final route destination in kWh.
It must be non-negative and less than the value of
<a href="sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours">BatterySpecifications.targetChargeInKilowattHours</a>,
otherwise the <a href="sdk-for-flutter-explore-routing-batteryspecifications-class">BatterySpecifications</a> instance is considered invalid.
Defaults to 0.</li>
<li><code>maxChargingVoltageInVolts</code> Maximum charging voltage supported by the vehicle's battery in Volts.
It must be positive.
When omitted, the voltage is determined by the charging station attributes.
Defaults to <code>null</code>.</li>
<li><code>maxChargingCurrentInAmperes</code> Maximum charging current supported by the vehicle's battery in Amperes.
It must be positive.
When omitted, the charging current is determined by the charging station attributes.
Defaults to <code>null</code>.</li>
<li><code>chargingSetupDuration</code> Time in seconds spent after arriving at a charging station, but before actually charging,
e.g., time spent for payment processing.
Defaults to 0 seconds.</li>
<li><code>maxPowerAtLowVoltageInKilowatts</code> The maximum power in kilowatts at which a vehicle can charge under given these conditions:</li>
</ul>
<ul>
<li>The charging station connector's maximum supply voltage is less than 800 V.</li>
<li><a href="sdk-for-flutter-explore-routing-batteryspecifications-maxchargingvoltageinvolts">BatterySpecifications.maxChargingVoltageInVolts</a> is greater than or equal to 800 V.
The provided value must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong> The feature is not supported by the <code>OfflineRoutingEngine</code>.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">BatterySpecifications([double totalCapacityInKilowattHours = 0.0, double initialChargeInKilowattHours = 0.0, double targetChargeInKilowattHours = 0.0, Map&lt;double, double&gt; chargingCurve = const {}, List&lt;ChargingConnectorType&gt; connectorTypes = const [], double minChargeAtChargingStationInKilowattHours = 0.0, double? minChargeAtFirstChargingStationInKilowattHours = null, double minChargeAtDestinationInKilowattHours = 0.0, double? maxChargingVoltageInVolts = null, double? maxChargingCurrentInAmperes = null, Duration chargingSetupDuration = const Duration(seconds: 0), double? maxPowerAtLowVoltageInKilowatts = null])
  : totalCapacityInKilowattHours = totalCapacityInKilowattHours, initialChargeInKilowattHours = initialChargeInKilowattHours, targetChargeInKilowattHours = targetChargeInKilowattHours, chargingCurve = chargingCurve, connectorTypes = connectorTypes, minChargeAtChargingStationInKilowattHours = minChargeAtChargingStationInKilowattHours, minChargeAtFirstChargingStationInKilowattHours = minChargeAtFirstChargingStationInKilowattHours, minChargeAtDestinationInKilowattHours = minChargeAtDestinationInKilowattHours, maxChargingVoltageInVolts = maxChargingVoltageInVolts, maxChargingCurrentInAmperes = maxChargingCurrentInAmperes, chargingSetupDuration = chargingSetupDuration, maxPowerAtLowVoltageInKilowatts = maxPowerAtLowVoltageInKilowatts;</code></pre>

 



</div>
`
}</HTMLBlock>
