---
title: "sdk-for-ios-explore-api-reference-structs-batteryspecifications"
slug: "sdk-for-ios-explore-api-reference-structs-batteryspecifications"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BatterySpecifications"></a>
<a title="BatterySpecifications Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        BatterySpecifications Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>BatterySpecifications</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BatterySpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
For a user-planned <code><a href="sdk-for-ios-explore-api-reference-structs-chargingstop">ChargingStop</a></code>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an invalid parameter error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">totalCapacityInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
For a user-planned <code><a href="sdk-for-ios-explore-api-reference-structs-chargingstop">ChargingStop</a></code>, this parameter is also required.
If not set greater than 0, the route calculation will fail as an an invalid parameter error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">initialChargeInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">targetChargeInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
For a user-planned <code><a href="sdk-for-ios-explore-api-reference-structs-chargingstop">ChargingStop</a></code>, this parameter is also required.
If one or more values are not set, the route calculation will fail as an invalid parameter error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargingCurve</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">connectorTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingconnectortype">ChargingConnectorType</a></span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minChargeAtChargingStationInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minChargeAtFirstChargingStationInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minChargeAtDestinationInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxChargingVoltageInVolts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxChargingCurrentInAmperes</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">chargingSetupDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxPowerAtLowVoltageInKilowatts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">totalCapacityInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">initialChargeInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">targetChargeInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">chargingCurve</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span> <span class="o">=</span> <span class="p">[:],</span> <span class="nv">connectorTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingconnectortype">ChargingConnectorType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">minChargeAtChargingStationInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">minChargeAtFirstChargingStationInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">minChargeAtDestinationInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">maxChargingVoltageInVolts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxChargingCurrentInAmperes</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">chargingSetupDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">maxPowerAtLowVoltageInKilowatts</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
</body>
</html>

`
}</HTMLBlock>
