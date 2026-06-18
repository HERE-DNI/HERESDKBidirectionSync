---
title: "BatterySpecifications (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-batteryspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- BatterySpecifications.html -->









<main role="main">
<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-routing-package-summary">com.here.sdk.routing</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance">com.here.sdk.routing.BatterySpecifications</div>
</div>
<section class="class-description" id="class-description">
<hr/>
<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">BatterySpecifications</span>
<span class="extends-implements">extends <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></span></div>
<div class="block"><p>Parameters related to the electric vehicle's battery.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- =========== FIELD SUMMARY =========== -->
<li>
<section class="field-summary" id="field-summary">

<div class="caption"><span>Fields</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Field</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#chargingCurve">chargingCurve</a></code></div>
<div class="col-last even-row-color">
<div class="block">Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).</div>
</div>
<div class="col-first odd-row-color"><code><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#chargingSetupDuration">chargingSetupDuration</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Time in seconds spent after arriving at a charging station, but before actually charging,
 e.g., time spent for payment processing.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt;</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#connectorTypes">connectorTypes</a></code></div>
<div class="col-last even-row-color">
<div class="block">List of available charging connector types.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#initialChargeInKilowattHours">initialChargeInKilowattHours</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Charge level of the vehicle's battery at the start of the route (in kWh).</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#maxChargingCurrentInAmperes">maxChargingCurrentInAmperes</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum charging current supported by the vehicle's battery in Amperes.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#maxChargingVoltageInVolts">maxChargingVoltageInVolts</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Maximum charging voltage supported by the vehicle's battery in Volts.</div>
</div>
<div class="col-first even-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#maxPowerAtLowVoltageInKilowatts">maxPowerAtLowVoltageInKilowatts</a></code></div>
<div class="col-last even-row-color">
<div class="block">The maximum power in kilowatts at which a vehicle can charge under given these conditions:
 
 The charging station connector's maximum supply voltage is less than 800 V.
 <a href="sdk-for-android-explore-index#maxChargingVoltageInVolts"><code>maxChargingVoltageInVolts</code></a> is greater than or equal to 800 V.</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours">minChargeAtChargingStationInKilowattHours</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Minimum charge when arriving at a charging station in kWh.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#minChargeAtDestinationInKilowattHours">minChargeAtDestinationInKilowattHours</a></code></div>
<div class="col-last even-row-color">
<div class="block">Minimum charge at the final route destination in kWh.</div>
</div>
<div class="col-first odd-row-color"><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#minChargeAtFirstChargingStationInKilowattHours">minChargeAtFirstChargingStationInKilowattHours</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Minimum charge when arriving at first charging station in kWh.</div>
</div>
<div class="col-first even-row-color"><code>double</code></div>
<div class="col-second even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#targetChargeInKilowattHours">targetChargeInKilowattHours</a></code></div>
<div class="col-last even-row-color">
<div class="block">Maximum charge to which the battery should be charged at a charging station (in kWh).</div>
</div>
<div class="col-first odd-row-color"><code>double</code></div>
<div class="col-second odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#totalCapacityInKilowattHours">totalCapacityInKilowattHours</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Total capacity of the vehicle's battery (in kWh).</div>
</div>
</div>
</section>
</li>
<!-- ======== CONSTRUCTOR SUMMARY ======== -->
<li>
<section class="constructor-summary" id="constructor-summary">

<div class="caption"><span>Constructors</span></div>
<div class="summary-table two-column-summary">
<div class="table-header col-first">Constructor</div>
<div class="table-header col-last">Description</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E()">BatterySpecifications</a>()</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name odd-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes,
 <a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> chargingSetupDuration)</code></div>
<div class="col-last odd-row-color">
<div class="block">Creates a new instance.</div>
</div>
<div class="col-constructor-name even-row-color"><code><a class="member-name-link" href="sdk-for-android-explore-index#%3Cinit%3E(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration,java.lang.Double)">BatterySpecifications</a><wbr/>(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes,
 <a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> chargingSetupDuration,
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxPowerAtLowVoltageInKilowatts)</code></div>
<div class="col-last even-row-color">
<div class="block">Creates a new instance.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>boolean</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#equals(java.lang.Object)">equals</a><wbr/>(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>int</code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-index#hashCode()">hashCode</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ FIELD DETAIL =========== -->
<li>
<section class="field-details" id="field-detail">

<ul class="member-list">
<li>
<section class="detail" id="totalCapacityInKilowattHours">
<h3>totalCapacityInKilowattHours</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">totalCapacityInKilowattHours</span></div>
<div class="block"><p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></div>
</section>
</li>
<li>
<section class="detail" id="initialChargeInKilowattHours">
<h3>initialChargeInKilowattHours</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">initialChargeInKilowattHours</span></div>
<div class="block"><p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></div>
</section>
</li>
<li>
<section class="detail" id="targetChargeInKilowattHours">
<h3>targetChargeInKilowattHours</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">targetChargeInKilowattHours</span></div>
<div class="block"><p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargingCurve">
<h3>chargingCurve</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt;</span> <span class="element-name">chargingCurve</span></div>
<div class="block"><p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></div>
</section>
</li>
<li>
<section class="detail" id="connectorTypes">
<h3>connectorTypes</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt;</span> <span class="element-name">connectorTypes</span></div>
<div class="block"><p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></div>
</section>
</li>
<li>
<section class="detail" id="minChargeAtChargingStationInKilowattHours">
<h3>minChargeAtChargingStationInKilowattHours</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">minChargeAtChargingStationInKilowattHours</span></div>
<div class="block"><p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="minChargeAtFirstChargingStationInKilowattHours">
<h3>minChargeAtFirstChargingStationInKilowattHours</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">minChargeAtFirstChargingStationInKilowattHours</span></div>
<div class="block"><p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></div>
</section>
</li>
<li>
<section class="detail" id="minChargeAtDestinationInKilowattHours">
<h3>minChargeAtDestinationInKilowattHours</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">minChargeAtDestinationInKilowattHours</span></div>
<div class="block"><p>Minimum charge at the final route destination in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxChargingVoltageInVolts">
<h3>maxChargingVoltageInVolts</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxChargingVoltageInVolts</span></div>
<div class="block"><p>Maximum charging voltage supported by the vehicle's battery in Volts.
 It must be positive.
 When omitted, the voltage is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxChargingCurrentInAmperes">
<h3>maxChargingCurrentInAmperes</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxChargingCurrentInAmperes</span></div>
<div class="block"><p>Maximum charging current supported by the vehicle's battery in Amperes.
 It must be positive.
 When omitted, the charging current is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></div>
</section>
</li>
<li>
<section class="detail" id="chargingSetupDuration">
<h3>chargingSetupDuration</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a></span> <span class="element-name">chargingSetupDuration</span></div>
<div class="block"><p>Time in seconds spent after arriving at a charging station, but before actually charging,
 e.g., time spent for payment processing.
 Defaults to 0 seconds.</p></div>
</section>
</li>
<li>
<section class="detail" id="maxPowerAtLowVoltageInKilowatts">
<h3>maxPowerAtLowVoltageInKilowatts</h3>
<div class="member-signature"><span class="annotations">@Nullable
</span><span class="modifiers">public</span> <span class="return-type"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a></span> <span class="element-name">maxPowerAtLowVoltageInKilowatts</span></div>
<div class="block"><p>The maximum power in kilowatts at which a vehicle can charge under given these conditions:
 <ul>
<li>The charging station connector's maximum supply voltage is less than 800 V.</li>
<li><a href="sdk-for-android-explore-index#maxChargingVoltageInVolts"><code>maxChargingVoltageInVolts</code></a> is greater than or equal to 800 V.
 The provided value must be greater than or equal to 0. By default, it is not set.
 <strong>Note:</strong> The feature is not supported by the <code>OfflineRoutingEngine</code>.</li>
</ul></p></div>
</section>
</li>
</ul>
</section>
</li>
<!-- ========= CONSTRUCTOR DETAIL ======== -->
<li>
<section class="constructor-details" id="constructor-detail">

<ul class="member-list">
<li>
<section class="detail" id="&lt;init&gt;()">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span>()</div>
<div class="block"><p>Creates a new instance.</p></div>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double,java.lang.Double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>minChargeAtFirstChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>minChargeAtFirstChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></dd>
<dd><code>minChargeAtDestinationInKilowattHours</code> - <p>Minimum charge at the final route destination in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>minChargeAtFirstChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></dd>
<dd><code>minChargeAtDestinationInKilowattHours</code> - <p>Minimum charge at the final route destination in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>maxChargingVoltageInVolts</code> - <p>Maximum charging voltage supported by the vehicle's battery in Volts.
 It must be positive.
 When omitted, the voltage is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>minChargeAtFirstChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></dd>
<dd><code>minChargeAtDestinationInKilowattHours</code> - <p>Minimum charge at the final route destination in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>maxChargingVoltageInVolts</code> - <p>Maximum charging voltage supported by the vehicle's battery in Volts.
 It must be positive.
 When omitted, the voltage is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
<dd><code>maxChargingCurrentInAmperes</code> - <p>Maximum charging current supported by the vehicle's battery in Amperes.
 It must be positive.
 When omitted, the charging current is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes,
 @NonNull
 <a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> chargingSetupDuration)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>minChargeAtFirstChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></dd>
<dd><code>minChargeAtDestinationInKilowattHours</code> - <p>Minimum charge at the final route destination in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>maxChargingVoltageInVolts</code> - <p>Maximum charging voltage supported by the vehicle's battery in Volts.
 It must be positive.
 When omitted, the voltage is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
<dd><code>maxChargingCurrentInAmperes</code> - <p>Maximum charging current supported by the vehicle's battery in Amperes.
 It must be positive.
 When omitted, the charging current is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
<dd><code>chargingSetupDuration</code> - <p>Time in seconds spent after arriving at a charging station, but before actually charging,
 e.g., time spent for payment processing.
 Defaults to 0 seconds.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="&lt;init&gt;(double,double,double,java.util.Map,java.util.List,double,java.lang.Double,double,java.lang.Double,java.lang.Double,com.here.time.Duration,java.lang.Double)">
<h3>BatterySpecifications</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="element-name">BatterySpecifications</span><wbr/><span class="parameters">(double totalCapacityInKilowattHours,
 double initialChargeInKilowattHours,
 double targetChargeInKilowattHours,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html" title="class or interface in java.util">Map</a>&lt;<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>,<wbr/><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a>&gt; chargingCurve,
 @NonNull
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" title="class or interface in java.util">List</a>&lt;<a href="sdk-for-android-explore-chargingconnectortype" title="enum class in com.here.sdk.routing">ChargingConnectorType</a>&gt; connectorTypes,
 double minChargeAtChargingStationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> minChargeAtFirstChargingStationInKilowattHours,
 double minChargeAtDestinationInKilowattHours,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingVoltageInVolts,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxChargingCurrentInAmperes,
 @NonNull
 <a href="sdk-for-android-explore-duration" title="class in com.here.time">Duration</a> chargingSetupDuration,
 @Nullable
 <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" title="class or interface in java.lang">Double</a> maxPowerAtLowVoltageInKilowatts)</span></div>
<div class="block"><p>Creates a new instance.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>totalCapacityInKilowattHours</code> - <p>Total capacity of the vehicle's battery (in kWh).
 It must be positive.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>initialChargeInKilowattHours</code> - <p>Charge level of the vehicle's battery at the start of the route (in kWh).
 It must be non-negative and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p></dd>
<dd><code>targetChargeInKilowattHours</code> - <p>Maximum charge to which the battery should be charged at a charging station (in kWh).
 It must be positive and less than or equal to the value of
 <a href="sdk-for-android-explore-index#totalCapacityInKilowattHours"><code>totalCapacityInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>chargingCurve</code> - <p>Function curve describing the maximum battery charging rate (in kW) at a given charge
 level (in kWh).
 Map keys represent charge levels that are non-negative floating point values
 in units of (kWh).
 Map values represent charging rate values that are positive floating point values
 in units of (kW).
 Given charge levels must cover the entire range of
 [0, <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>],
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 The charging curve is considered piecewise constant instead of being interpolated.
 Defaults to an empty container.
 <strong>Note:</strong>
 For a user-planned <a href="sdk-for-android-explore-chargingstop" title="class in com.here.sdk.routing"><code>ChargingStop</code></a>, this parameter is also required.
 If one or more values are not set, the route calculation will fail as an invalid parameter error.</p></dd>
<dd><code>connectorTypes</code> - <p>List of available charging connector types.
 It must be at least one charging connector type added, otherwise
 the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to an empty container.</p></dd>
<dd><code>minChargeAtChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at a charging station in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>minChargeAtFirstChargingStationInKilowattHours</code> - <p>Minimum charge when arriving at first charging station in kWh.
 This overrides <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> for the first charging station.
 If not specified, <a href="sdk-for-android-explore-index#minChargeAtChargingStationInKilowattHours"><code>minChargeAtChargingStationInKilowattHours</code></a> will be used
 for all charging stations, including the first one.
 Defaults to <code>null</code>.
 When initialized, it must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p></dd>
<dd><code>minChargeAtDestinationInKilowattHours</code> - <p>Minimum charge at the final route destination in kWh.
 It must be non-negative and less than the value of
 <a href="sdk-for-android-explore-index#targetChargeInKilowattHours"><code>targetChargeInKilowattHours</code></a>,
 otherwise the <a href="sdk-for-android-explore-batteryspecifications" title="class in com.here.sdk.routing"><code>BatterySpecifications</code></a> instance is considered invalid.
 Defaults to 0.</p></dd>
<dd><code>maxChargingVoltageInVolts</code> - <p>Maximum charging voltage supported by the vehicle's battery in Volts.
 It must be positive.
 When omitted, the voltage is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
<dd><code>maxChargingCurrentInAmperes</code> - <p>Maximum charging current supported by the vehicle's battery in Amperes.
 It must be positive.
 When omitted, the charging current is determined by the charging station attributes.
 Defaults to <code>null</code>.</p></dd>
<dd><code>chargingSetupDuration</code> - <p>Time in seconds spent after arriving at a charging station, but before actually charging,
 e.g., time spent for payment processing.
 Defaults to 0 seconds.</p></dd>
<dd><code>maxPowerAtLowVoltageInKilowatts</code> - <p>The maximum power in kilowatts at which a vehicle can charge under given these conditions:
 <ul>
<li>The charging station connector's maximum supply voltage is less than 800 V.</li>
<li><a href="sdk-for-android-explore-index#maxChargingVoltageInVolts"><code>maxChargingVoltageInVolts</code></a> is greater than or equal to 800 V.
 The provided value must be greater than or equal to 0. By default, it is not set.
 <strong>Note:</strong> The feature is not supported by the <code>OfflineRoutingEngine</code>.</li>
</ul></p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="equals(java.lang.Object)">
<h3>equals</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr/><span class="parameters">(<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a> obj)</span></div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="hashCode()">
<h3>hashCode</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()</div>
<dl class="notes">
<dt>Overrides:</dt>
<dd><code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a></code> in class <code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></code></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->
</main>





</div>
`
}</HTMLBlock>
