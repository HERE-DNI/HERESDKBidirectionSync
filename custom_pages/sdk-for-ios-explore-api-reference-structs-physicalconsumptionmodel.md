---
title: "PhysicalConsumptionModel"
slug: "sdk-for-ios-explore-api-reference-structs-physicalconsumptionmodel"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PhysicalConsumptionModel"></a>
<a title="PhysicalConsumptionModel Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        PhysicalConsumptionModel Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PhysicalConsumptionModel</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PhysicalConsumptionModel</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Defines the physical consumption model for electric vehicles,
using vehicle-specific parameters to calculate energy consumption along a route.
<strong>Note:</strong> [sdk.transport.VehicleSpecification.current_weight_in_kilograms] must be set.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV20driveTrainEfficiencySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/driveTrainEfficiency"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV20driveTrainEfficiencySdvp">driveTrainEfficiency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The proportion of the energy drawn from the battery that is used to move the vehicle.
(This is to factor in energy losses through heat in the motors, for example.)
Supported range from 0 to 1</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">driveTrainEfficiency</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV22recuperationEfficiencySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/recuperationEfficiency"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV22recuperationEfficiencySdvp">recuperationEfficiency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.</p>
<p>Supported range from 0 to 1</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">recuperationEfficiency</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV014auxiliaryPowerC7InWattsSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/auxiliaryPowerConsumptionInWatts"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV014auxiliaryPowerC7InWattsSdvp">auxiliaryPowerConsumptionInWatts</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Power (in W) consumed by the vehicle’s auxiliary systems (for example, air conditioning, lights).</p>
<p>The provided value must be greater than or equal to 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">auxiliaryPowerConsumptionInWatts</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV25frontalAreaInSquareMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/frontalAreaInSquareMeters"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV25frontalAreaInSquareMetersSdvp">frontalAreaInSquareMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.
Physical consumption model is using this value in combination with <code><a href="../Structs/PhysicalConsumptionModel.html#/s:7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp">airDragCoefficient</a></code> to calculate the consumption caused by air resistance.
As fallback <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">VehicleSpecification.widthInCentimeters</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">VehicleSpecification.heightInCentimeters</a></code> are used.</p>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>In the range from 0.5 to 50</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">frontalAreaInSquareMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV28rollingResistanceCoefficientSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rollingResistanceCoefficient"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV28rollingResistanceCoefficientSdvp">rollingResistanceCoefficient</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.
The main causes of this resistance are tire deformation, wing drag, and friction with the ground.
The coefficient of rolling resistance is a numerical value indicating the severity of this factor.</p>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>Supported range from 0 to 1</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">rollingResistanceCoefficient</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/airDragCoefficient"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp">airDragCoefficient</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.
More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.</p>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>Supported range from 0 to 1</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">airDragCoefficient</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24PhysicalConsumptionModelV20driveTrainEfficiency012recuperationG0014auxiliaryPowerC7InWatts011frontalAreaK12SquareMeters28rollingResistanceCoefficient07airDragS0ACSd_S5dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(driveTrainEfficiency:recuperationEfficiency:auxiliaryPowerConsumptionInWatts:frontalAreaInSquareMeters:rollingResistanceCoefficient:airDragCoefficient:)"></a>
<a class="token" href="#/s:7heresdk24PhysicalConsumptionModelV20driveTrainEfficiency012recuperationG0014auxiliaryPowerC7InWatts011frontalAreaK12SquareMeters28rollingResistanceCoefficient07airDragS0ACSd_S5dtcfc">init(driveTrainEfficiency:<wbr/>recuperationEfficiency:<wbr/>auxiliaryPowerConsumptionInWatts:<wbr/>frontalAreaInSquareMeters:<wbr/>rollingResistanceCoefficient:<wbr/>airDragCoefficient:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>driveTrainEfficiency: The proportion of the energy drawn from the battery that is used to move the vehicle.
(This is to factor in energy losses through heat in the motors, for example.)
Supported range from 0 to 1</li>
<li>recuperationEfficiency: The proportion of the energy gained when braking or going downhill that can be recuperated and restored as battery charge.</li>
</ul>
<p>Supported range from 0 to 1</p>
<ul>
<li>auxiliaryPowerConsumptionInWatts: Power (in W) consumed by the vehicle’s auxiliary systems (for example, air conditioning, lights).</li>
</ul>
<p>The provided value must be greater than or equal to 0.</p>
<ul>
<li>frontalAreaInSquareMeters: Frontal area represents the total cross section area of the vehicle as viewed from the front, specified in square meters.
Physical consumption model is using this value in combination with <code><a href="../Structs/PhysicalConsumptionModel.html#/s:7heresdk24PhysicalConsumptionModelV18airDragCoefficientSdvp">airDragCoefficient</a></code> to calculate the consumption caused by air resistance.
As fallback <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">VehicleSpecification.widthInCentimeters</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">VehicleSpecification.heightInCentimeters</a></code> are used.</li>
</ul>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>In the range from 0.5 to 50</p>
<ul>
<li>rollingResistanceCoefficient: Rolling resistance refers to the resistance experienced by your vehicle tire as it rolls over a surface.
The main causes of this resistance are tire deformation, wing drag, and friction with the ground.
The coefficient of rolling resistance is a numerical value indicating the severity of this factor.</li>
</ul>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>Supported range from 0 to 1</p>
<ul>
<li>airDragCoefficient: The drag coefficient of an vehicle defines the way the vehicle is expected to pass through the surrounding air.
More streamlined vehicles are more aerodynamic and therefore have smaller drag coefficient.</li>
</ul>
<p>This parameter is used to provide a more accurate consumption prediction for electric vehicles.</p>
<p>Supported range from 0 to 1</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">driveTrainEfficiency</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span> <span class="nv">recuperationEfficiency</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span> <span class="nv">auxiliaryPowerConsumptionInWatts</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span> <span class="nv">frontalAreaInSquareMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.5</span><span class="p">,</span> <span class="nv">rollingResistanceCoefficient</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">,</span> <span class="nv">airDragCoefficient</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.1</span><span class="p">)</span></code></pre>
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
