---
title: "BatterySpecifications constructor"
slug: "sdk-for-flutter-explore-routing-batteryspecifications-batteryspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- BatterySpecifications.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-batteryspecifications-class</li>
<li class="self-crumb">BatterySpecifications constructor</li>
</ol>
<div class="self-name">BatterySpecifications</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="routing/BatterySpecifications-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>BatterySpecifications constructor</h1></div>
<section class="multi-line-signature">
BatterySpecifications(<wbr/>[<ol class="parameter-list"> <li>double totalCapacityInKilowattHours = 0.0, </li>
<li>double initialChargeInKilowattHours = 0.0, </li>
<li>double targetChargeInKilowattHours = 0.0, </li>
<li>Map&lt;<wbr/>double, double&gt; chargingCurve = const {}, </li>
<li>List&lt;<wbr/>/sdk-for-flutter-explore-routing-chargingconnectortype&gt; connectorTypes = const [], </li>
<li>double minChargeAtChargingStationInKilowattHours = 0.0, </li>
<li>double? minChargeAtFirstChargingStationInKilowattHours = null, </li>
<li>double minChargeAtDestinationInKilowattHours = 0.0, </li>
<li>double? maxChargingVoltageInVolts = null, </li>
<li>double? maxChargingCurrentInAmperes = null, </li>
<li>Duration chargingSetupDuration = const Duration(seconds: 0), </li>
<li>double? maxPowerAtLowVoltageInKilowatts = null, </li>
</ol>])
    </section>
<section class="desc markdown">
<p>Creates a new instance.</p>
<ul>
<li><code>totalCapacityInKilowattHours</code> Total capacity of the vehicle's battery (in kWh).
It must be positive.
Defaults to 0.
<strong>Note:</strong>
For a user-planned /sdk-for-flutter-explore-routing-chargingstop-class, this parameter is also required.
If not set greater than 0, the route calculation will fail as an invalid parameter error.</li>
<li><code>initialChargeInKilowattHours</code> Charge level of the vehicle's battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned /sdk-for-flutter-explore-routing-chargingstop-class, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.</li>
<li><code>targetChargeInKilowattHours</code> Maximum charge to which the battery should be charged at a charging station (in kWh).
It must be positive and less than or equal to the value of
/sdk-for-flutter-explore-routing-batteryspecifications-totalcapacityinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.</li>
<li><code>chargingCurve</code> Function curve describing the maximum battery charging rate (in kW) at a given charge
level (in kWh).
Map keys represent charge levels that are non-negative floating point values
in units of (kWh).
Map values represent charging rate values that are positive floating point values
in units of (kW).
Given charge levels must cover the entire range of
[0, /sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours],
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
The charging curve is considered piecewise constant instead of being interpolated.
Defaults to an empty container.
<strong>Note:</strong>
For a user-planned /sdk-for-flutter-explore-routing-chargingstop-class, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.</li>
<li><code>connectorTypes</code> List of available charging connector types.
It must be at least one charging connector type added, otherwise
the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to an empty container.</li>
<li><code>minChargeAtChargingStationInKilowattHours</code> Minimum charge when arriving at a charging station in kWh.
It must be non-negative and less than the value of
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
Defaults to 0.</li>
<li><code>minChargeAtFirstChargingStationInKilowattHours</code> Minimum charge when arriving at first charging station in kWh.
This overrides /sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours for the first charging station.
If not specified, /sdk-for-flutter-explore-routing-batteryspecifications-minchargeatchargingstationinkilowatthours will be used
for all charging stations, including the first one.
Defaults to <code>null</code>.
When initialized, it must be non-negative and less than the value of
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</li>
<li><code>minChargeAtDestinationInKilowattHours</code> Minimum charge at the final route destination in kWh.
It must be non-negative and less than the value of
/sdk-for-flutter-explore-routing-batteryspecifications-targetchargeinkilowatthours,
otherwise the /sdk-for-flutter-explore-routing-batteryspecifications-class instance is considered invalid.
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
<li>/sdk-for-flutter-explore-routing-batteryspecifications-maxchargingvoltageinvolts is greater than or equal to 800 V.
The provided value must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong> The feature is not supported by the <code>OfflineRoutingEngine</code>.</li>
</ul>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">BatterySpecifications([double totalCapacityInKilowattHours = 0.0, double initialChargeInKilowattHours = 0.0, double targetChargeInKilowattHours = 0.0, Map&lt;double, double&gt; chargingCurve = const {}, List&lt;ChargingConnectorType&gt; connectorTypes = const [], double minChargeAtChargingStationInKilowattHours = 0.0, double? minChargeAtFirstChargingStationInKilowattHours = null, double minChargeAtDestinationInKilowattHours = 0.0, double? maxChargingVoltageInVolts = null, double? maxChargingCurrentInAmperes = null, Duration chargingSetupDuration = const Duration(seconds: 0), double? maxPowerAtLowVoltageInKilowatts = null])
  : totalCapacityInKilowattHours = totalCapacityInKilowattHours, initialChargeInKilowattHours = initialChargeInKilowattHours, targetChargeInKilowattHours = targetChargeInKilowattHours, chargingCurve = chargingCurve, connectorTypes = connectorTypes, minChargeAtChargingStationInKilowattHours = minChargeAtChargingStationInKilowattHours, minChargeAtFirstChargingStationInKilowattHours = minChargeAtFirstChargingStationInKilowattHours, minChargeAtDestinationInKilowattHours = minChargeAtDestinationInKilowattHours, maxChargingVoltageInVolts = maxChargingVoltageInVolts, maxChargingCurrentInAmperes = maxChargingCurrentInAmperes, chargingSetupDuration = chargingSetupDuration, maxPowerAtLowVoltageInKilowatts = maxPowerAtLowVoltageInKilowatts;</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-explore</li>
<li>/sdk-for-flutter-explore-routing-routing-library</li>
<li>/sdk-for-flutter-explore-routing-batteryspecifications-class</li>
<li class="self-crumb">BatterySpecifications constructor</li>
</ol>
<h5>BatterySpecifications class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
