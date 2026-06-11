---
title: "sdk-for-ios-explore-api-reference-structs-chargingstop"
slug: "sdk-for-ios-explore-api-reference-structs-chargingstop"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ChargingStop"></a>
<a title="ChargingStop Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        ChargingStop Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ChargingStop</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ChargingStop</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">powerInKilowatts</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currentInAmperes</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">voltageInVolts</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">supplyType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingsupplytype">ChargingSupplyType</a></span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">powerInKilowatts</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">currentInAmperes</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">voltageInVolts</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">supplyType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-chargingsupplytype">ChargingSupplyType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">minDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
