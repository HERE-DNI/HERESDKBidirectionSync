---
title: "ChargingStop Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-chargingstop"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ChargingStop.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/ChargingStop"></a>
<a title="ChargingStop Structure Reference"></a>
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
        ChargingStop Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct ChargingStop : Hashable</code></pre>
</div>
</div>
<p>The options to specify a user-planned charging stop.
<strong>Note:</strong>
In order to specify this <code>ChargingStop</code>, it is also required to set
[sdk.routing.BatterySpecifications.total_capacity_in_kilowatt_hours], [sdk.routing.BatterySpecifications.initial_charge_in_kilowatt_hours],
and [sdk.routing.BatterySpecifications.charging_curve].
Without all of them, the route calculation will fail as an invalid parameter error.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV16powerInKilowattsSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/powerInKilowatts"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV16powerInKilowattsSdvp">powerInKilowatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of rated power of the connector (in kW).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var powerInKilowatts: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV16currentInAmperesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentInAmperes"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV16currentInAmperesSdvp">currentInAmperes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of rated current of the connector (in A).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var currentInAmperes: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV14voltageInVoltsSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/voltageInVolts"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV14voltageInVoltsSdvp">voltageInVolts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of rated voltage of the connector (in V).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var voltageInVolts: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV10supplyTypeAA0b6SupplyE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/supplyType"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV10supplyTypeAA0b6SupplyE0OSgvp">supplyType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Supply type of the suggested connector.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var supplyType: ChargingSupplyType?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV11minDurationSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minDuration"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV11minDurationSdSgvp">minDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The minimum duration the user expects to charge at the station,
including <code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp">BatterySpecifications.chargingSetupDuration</a></code>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var minDuration: TimeInterval?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV11maxDurationSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxDuration"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV11maxDurationSdSgvp">maxDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum duration the user plans to charge at the station,
including <code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV21chargingSetupDurationSdvp">BatterySpecifications.chargingSetupDuration</a></code>.
<strong>Note:</strong>
At least one of <code>min_duration</code> and <code>max_duration</code> is required for a user-planned charging stop.
For most use cases, providing at least <code>min_duration</code> is recommended.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxDuration: TimeInterval?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12ChargingStopV16powerInKilowatts07currentE7Amperes07voltageE5Volts10supplyType11minDuration03maxN0ACSd_S2dAA0b6SupplyL0OSgSdSgAMtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(powerInKilowatts:currentInAmperes:voltageInVolts:supplyType:minDuration:maxDuration:)"></a>
<a class="token" href="#/s:7heresdk12ChargingStopV16powerInKilowatts07currentE7Amperes07voltageE5Volts10supplyType11minDuration03maxN0ACSd_S2dAA0b6SupplyL0OSgSdSgAMtcfc">init(powerInKilowatts:<wbr/>currentInAmperes:<wbr/>voltageInVolts:<wbr/>supplyType:<wbr/>minDuration:<wbr/>maxDuration:<wbr/>)</a>
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
<pre><code>public init(powerInKilowatts: Double = 0.0, currentInAmperes: Double = 0.0, voltageInVolts: Double = 0.0, supplyType: ChargingSupplyType? = nil, minDuration: TimeInterval? = nil, maxDuration: TimeInterval? = nil)</code></pre>
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
