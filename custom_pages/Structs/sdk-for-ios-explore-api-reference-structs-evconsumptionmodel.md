---
title: "EVConsumptionModel Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-evconsumptionmodel"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- EVConsumptionModel.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/EVConsumptionModel"></a>
<a title="EVConsumptionModel Structure Reference"></a>
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
        EVConsumptionModel Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct EVConsumptionModel : Hashable</code></pre>
</div>
</div>
<p>Parameters specific for the electric vehicle, which are then used to calculate
energy consumption on a given route.
At minimum, you must provide <code><a href="../Structs/EVConsumptionModel.html#/s:7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp">EVConsumptionModel.ascentConsumptionInWattHoursPerMeter</a></code>,
<code><a href="../Structs/EVConsumptionModel.html#/s:7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp">EVConsumptionModel.descentRecoveryInWattHoursPerMeter</a></code> and a
<code><a href="../Structs/EVConsumptionModel.html#/s:7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">EVConsumptionModel.freeFlowSpeedTable</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ascentConsumptionInWattHoursPerMeter"></a>
<a class="token" href="#/s:7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeterSdvp">ascentConsumptionInWattHoursPerMeter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Rate of energy consumed per meter rise in elevation (in Wh/m, i.e., Watt-hours per meter).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var ascentConsumptionInWattHoursPerMeter: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/descentRecoveryInWattHoursPerMeter"></a>
<a class="token" href="#/s:7heresdk18EVConsumptionModelV34descentRecoveryInWattHoursPerMeterSdvp">descentRecoveryInWattHoursPerMeter</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Rate of energy recovered per meter fall in elevation (in Wh/m, i.e., Watt-hours per meter).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var descentRecoveryInWattHoursPerMeter: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/freeFlowSpeedTable"></a>
<a class="token" href="#/s:7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">freeFlowSpeedTable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Free flow speed table describes energy consumption when traveling at constant speed.
It defines a function curve specifying consumption rate at a given free flow speed
on a flat stretch of road.
Map keys represent speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
At minimum, one key/value pair must be set. In this case the consumption value is
used for all possible speed keys.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var freeFlowSpeedTable: [Int32 : Double]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVConsumptionModelV17trafficSpeedTableSDys5Int32VSdGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSpeedTable"></a>
<a class="token" href="#/s:7heresdk18EVConsumptionModelV17trafficSpeedTableSDys5Int32VSdGvp">trafficSpeedTable</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic speed table describes energy consumption when traveling under heavy traffic
conditions, i.e. when the vehicle is expected to often change the travel speed.
It defines a function curve specifying consumption rate at a given speed under traffic
conditions on a flat stretch of road.
Map keys represent traffic speed values that are non-negative integers in units of (km/h).
Map values represent consumption values that are non-negative floating point values
in units of (Wh/m).
The function is linearly interpolated between each successive pair of data points:
For values below the first list value, the first value is used.
For values after the last list value, the last list value is used.
If only one key/value pair is set, the consumption value is
used for all possible traffic speed keys.
If <code>EVConsumptionModel.trafficSpeedTable</code> is empty then only
<code><a href="../Structs/EVConsumptionModel.html#/s:7heresdk18EVConsumptionModelV18freeFlowSpeedTableSDys5Int32VSdGvp">EVConsumptionModel.freeFlowSpeedTable</a></code> is used for calculating speed-related
energy consumption.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var trafficSpeedTable: [Int32 : Double]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVConsumptionModelV40auxiliaryConsumptionInWattHoursPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/auxiliaryConsumptionInWattHoursPerSecond"></a>
<a class="token" href="#/s:7heresdk18EVConsumptionModelV40auxiliaryConsumptionInWattHoursPerSecondSdvp">auxiliaryConsumptionInWattHoursPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Rate of energy (in Wh/s) consumed by the vehicle’s auxiliary systems
(e.g., air conditioning, lights) per second of travel.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var auxiliaryConsumptionInWattHoursPerSecond: Double</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeter015descentRecoveryfghiJ018freeFlowSpeedTable07trafficoP009auxiliaryefghI6SecondACSd_SdSDys5Int32VSdGAKSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(ascentConsumptionInWattHoursPerMeter:descentRecoveryInWattHoursPerMeter:freeFlowSpeedTable:trafficSpeedTable:auxiliaryConsumptionInWattHoursPerSecond:)"></a>
<a class="token" href="#/s:7heresdk18EVConsumptionModelV36ascentConsumptionInWattHoursPerMeter015descentRecoveryfghiJ018freeFlowSpeedTable07trafficoP009auxiliaryefghI6SecondACSd_SdSDys5Int32VSdGAKSdtcfc">init(ascentConsumptionInWattHoursPerMeter:<wbr/>descentRecoveryInWattHoursPerMeter:<wbr/>freeFlowSpeedTable:<wbr/>trafficSpeedTable:<wbr/>auxiliaryConsumptionInWattHoursPerSecond:<wbr/>)</a>
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
<pre><code>public init(ascentConsumptionInWattHoursPerMeter: Double = 0.0, descentRecoveryInWattHoursPerMeter: Double = 0.0, freeFlowSpeedTable: [Int32 : Double] = [:], trafficSpeedTable: [Int32 : Double] = [:], auxiliaryConsumptionInWattHoursPerSecond: Double = 0.0)</code></pre>
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
