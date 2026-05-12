---
title: "BatterySpecifications Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-batteryspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- BatterySpecifications.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/BatterySpecifications"></a>
<a title="BatterySpecifications Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        BatterySpecifications Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct BatterySpecifications : Hashable</code></pre>
</div>
</div>
<p>Parameters related to the electric vehicle’s battery.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/totalCapacityInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp">totalCapacityInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Total capacity of the vehicle’s battery (in kWh).
It must be positive.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <code><a href="../Structs/ChargingStop.html">ChargingStop</a></code>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an invalid parameter error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var totalCapacityInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/initialChargeInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp">initialChargeInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Charge level of the vehicle’s battery at the start of the route (in kWh).
It must be non-negative and less than or equal to the value of
<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp">BatterySpecifications.totalCapacityInKilowattHours</a></code>,
otherwise the <code>BatterySpecifications</code> instance is considered invalid.
Defaults to 0.
<strong>Note:</strong>
For a user-planned <code><a href="../Structs/ChargingStop.html">ChargingStop</a></code>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var initialChargeInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/targetChargeInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">targetChargeInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum charge to which the battery should be charged at a charging station (in kWh).
It must be positive and less than or equal to the value of
<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp">BatterySpecifications.totalCapacityInKilowattHours</a></code>,
otherwise the <code>BatterySpecifications</code> instance is considered invalid.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var targetChargeInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV13chargingCurveSDyS2dGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingCurve"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV13chargingCurveSDyS2dGvp">chargingCurve</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Function curve describing the maximum battery charging rate (in kW) at a given charge
level (in kWh).
Map keys represent charge levels that are non-negative floating point values
in units of (kWh).
Map values represent charging rate values that are positive floating point values
in units of (kW).
Given charge levels must cover the entire range of
[0, <code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">BatterySpecifications.targetChargeInKilowattHours</a></code>],
otherwise the <code>BatterySpecifications</code> instance is considered invalid.
The charging curve is considered piecewise constant instead of being interpolated.
Defaults to an empty container.
<strong>Note:</strong>
For a user-planned <code><a href="../Structs/ChargingStop.html">ChargingStop</a></code>, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var chargingCurve: [Double : Double]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV14connectorTypesSayAA21ChargingConnectorTypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/connectorTypes"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV14connectorTypesSayAA21ChargingConnectorTypeOGvp">connectorTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of available charging connector types.
It must be at least one charging connector type added, otherwise
the <code>BatterySpecifications</code> instance is considered invalid.
Defaults to an empty container.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var connectorTypes: [ChargingConnectorType]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minChargeAtChargingStationInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp">minChargeAtChargingStationInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum charge when arriving at a charging station in kWh.
It must be non-negative and less than the value of
<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">BatterySpecifications.targetChargeInKilowattHours</a></code>,
otherwise the <code>BatterySpecifications</code> instance is considered invalid.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var minChargeAtChargingStationInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV46minChargeAtFirstChargingStationInKilowattHoursSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minChargeAtFirstChargingStationInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV46minChargeAtFirstChargingStationInKilowattHoursSdSgvp">minChargeAtFirstChargingStationInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum charge when arriving at first charging station in kWh.
This overrides <code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a></code> for the first charging station.
If not specified, <code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV41minChargeAtChargingStationInKilowattHoursSdvp">BatterySpecifications.minChargeAtChargingStationInKilowattHours</a></code> will be used
for all charging stations, including the first one.
Defaults to <code>nil</code>.
When initialized, it must be non-negative and less than the value of
<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">BatterySpecifications.targetChargeInKilowattHours</a></code>,
otherwise the <code>BatterySpecifications</code> instance is considered invalid.
This is usually used when the current charge is too low to reach a charging station within <code>minChargeAtChargingStation</code> limits.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var minChargeAtFirstChargingStationInKilowattHours: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV37minChargeAtDestinationInKilowattHoursSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minChargeAtDestinationInKilowattHours"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV37minChargeAtDestinationInKilowattHoursSdvp">minChargeAtDestinationInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum charge at the final route destination in kWh.
It must be non-negative and less than the value of
<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV27targetChargeInKilowattHoursSdvp">BatterySpecifications.targetChargeInKilowattHours</a></code>,
otherwise the <code>BatterySpecifications</code> instance is considered invalid.
Defaults to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var minChargeAtDestinationInKilowattHours: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV25maxChargingVoltageInVoltsSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxChargingVoltageInVolts"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV25maxChargingVoltageInVoltsSdSgvp">maxChargingVoltageInVolts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum charging voltage supported by the vehicle’s battery in Volts.
It must be positive.
When omitted, the voltage is determined by the charging station attributes.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxChargingVoltageInVolts: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV27maxChargingCurrentInAmperesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxChargingCurrentInAmperes"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV27maxChargingCurrentInAmperesSdSgvp">maxChargingCurrentInAmperes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum charging current supported by the vehicle’s battery in Amperes.
It must be positive.
When omitted, the charging current is determined by the charging station attributes.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxChargingCurrentInAmperes: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/chargingSetupDuration"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp">chargingSetupDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time in seconds spent after arriving at a charging station, but before actually charging,
e.g., time spent for payment processing.
Defaults to 0 seconds.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var chargingSetupDuration: TimeInterval</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV31maxPowerAtLowVoltageInKilowattsSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPowerAtLowVoltageInKilowatts"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV31maxPowerAtLowVoltageInKilowattsSdSgvp">maxPowerAtLowVoltageInKilowatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum power in kilowatts at which a vehicle can charge under given these conditions:</p>
<ul>
<li>The charging station connector’s maximum supply voltage is less than 800 V.</li>
<li><code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV25maxChargingVoltageInVoltsSdSgvp">BatterySpecifications.maxChargingVoltageInVolts</a></code> is greater than or equal to 800 V.
The provided value must be greater than or equal to 0. By default, it is not set.
<strong>Note:</strong> The feature is not supported by the <code>OfflineRoutingEngine</code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxPowerAtLowVoltageInKilowatts: Double?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHours013initialChargefgH006targetjfgH013chargingCurve14connectorTypes03minj17AtChargingStationfgH00pjq5FirstrsfgH00pjq11DestinationfgH003maxr7VoltageF5Volts0vr7CurrentF7Amperes0L13SetupDuration0v5Powerq3LowwF9KilowattsACSd_S2dSDyS2dGSayAA0R13ConnectorTypeOGS2dSgSdA2TSdATtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(totalCapacityInKilowattHours:initialChargeInKilowattHours:targetChargeInKilowattHours:chargingCurve:connectorTypes:minChargeAtChargingStationInKilowattHours:minChargeAtFirstChargingStationInKilowattHours:minChargeAtDestinationInKilowattHours:maxChargingVoltageInVolts:maxChargingCurrentInAmperes:chargingSetupDuration:maxPowerAtLowVoltageInKilowatts:)"></a>
<a class="token" href="#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHours013initialChargefgH006targetjfgH013chargingCurve14connectorTypes03minj17AtChargingStationfgH00pjq5FirstrsfgH00pjq11DestinationfgH003maxr7VoltageF5Volts0vr7CurrentF7Amperes0L13SetupDuration0v5Powerq3LowwF9KilowattsACSd_S2dSDyS2dGSayAA0R13ConnectorTypeOGS2dSgSdA2TSdATtcfc">init(totalCapacityInKilowattHours:<wbr/>initialChargeInKilowattHours:<wbr/>targetChargeInKilowattHours:<wbr/>chargingCurve:<wbr/>connectorTypes:<wbr/>minChargeAtChargingStationInKilowattHours:<wbr/>minChargeAtFirstChargingStationInKilowattHours:<wbr/>minChargeAtDestinationInKilowattHours:<wbr/>maxChargingVoltageInVolts:<wbr/>maxChargingCurrentInAmperes:<wbr/>chargingSetupDuration:<wbr/>maxPowerAtLowVoltageInKilowatts:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(totalCapacityInKilowattHours: Double = 0.0, initialChargeInKilowattHours: Double = 0.0, targetChargeInKilowattHours: Double = 0.0, chargingCurve: [Double : Double] = [:], connectorTypes: [ChargingConnectorType] = [], minChargeAtChargingStationInKilowattHours: Double = 0.0, minChargeAtFirstChargingStationInKilowattHours: Double? = nil, minChargeAtDestinationInKilowattHours: Double = 0.0, maxChargingVoltageInVolts: Double? = nil, maxChargingCurrentInAmperes: Double? = nil, chargingSetupDuration: TimeInterval = 0, maxPowerAtLowVoltageInKilowatts: Double? = nil)</code></pre>
</div>
</div>
</section>
</div>
</li>
</ul>
</div>
</section>
</section>
<section id="footer">
<p>© 2026 <a class="link" href="" rel="external noopener" target="_blank"></a>. All rights reserved. (Last updated: 2026-04-14)</p>
<p>Generated by <a class="link" href="https://github.com/realm/jazzy" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a class="link" href="https://realm.io" rel="external noopener" target="_blank">Realm</a> project.</p>
</section>
</article>
</div>



</div>
`
}</HTMLBlock>
