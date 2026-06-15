---
title: "EVConsumptionModel"
slug: "sdk-for-ios-navigate-api-reference-structs-evconsumptionmodel"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVConsumptionModel"></a>
<a title="EVConsumptionModel Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        EVConsumptionModel Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVConsumptionModel</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVConsumptionModel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ascentConsumptionInWattHoursPerMeter</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">descentRecoveryInWattHoursPerMeter</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">freeFlowSpeedTable</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficSpeedTable</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">auxiliaryConsumptionInWattHoursPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">ascentConsumptionInWattHoursPerMeter</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">descentRecoveryInWattHoursPerMeter</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">freeFlowSpeedTable</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span> <span class="o">=</span> <span class="p">[:],</span> <span class="nv">trafficSpeedTable</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span> <span class="p">:</span> <span class="kt">Double</span><span class="p">]</span> <span class="o">=</span> <span class="p">[:],</span> <span class="nv">auxiliaryConsumptionInWattHoursPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">)</span></code></pre>
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
} </HTMLBlock>
