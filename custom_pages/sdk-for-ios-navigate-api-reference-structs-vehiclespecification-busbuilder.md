---
title: "BusBuilder"
slug: "sdk-for-ios-navigate-api-reference-structs-vehiclespecification-busbuilder"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/BusBuilder"></a>
<a title="BusBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

<a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a>

        BusBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>BusBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">BusBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class constructs a <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></code> for a bus.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderCAEycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderCAEycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC23withHeightInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withHeightInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC23withHeightInCentimetersyAEs5Int32VF">withHeightInCentimeters(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle height in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withHeightInCentimeters</span><span class="p">(</span><span class="n">_</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>heightInCentimeters</em>
</code>
</td>
<td>
<div>
<p>The vehicle height in centimeters.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the vehicle height set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC22withWidthInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withWidthInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC22withWidthInCentimetersyAEs5Int32VF">withWidthInCentimeters(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle width in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withWidthInCentimeters</span><span class="p">(</span><span class="n">_</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>widthInCentimeters</em>
</code>
</td>
<td>
<div>
<p>The vehicle width in centimeters.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the vehicle width set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC23withLengthInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withLengthInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC23withLengthInCentimetersyAEs5Int32VF">withLengthInCentimeters(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle length in centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withLengthInCentimeters</span><span class="p">(</span><span class="n">_</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lengthInCentimeters</em>
</code>
</td>
<td>
<div>
<p>The vehicle length in centimeters.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the vehicle length set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC13withAxleCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withAxleCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC13withAxleCountyAEs5Int32VF">withAxleCount(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle axle count.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withAxleCount</span><span class="p">(</span><span class="n">_</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>axleCount</em>
</code>
</td>
<td>
<div>
<p>The vehicle axle count.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the axle count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC16withTrailerCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTrailerCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC16withTrailerCountyAEs5Int32VF">withTrailerCount(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle trailer count.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withTrailerCount</span><span class="p">(</span><span class="n">_</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>trailerCount</em>
</code>
</td>
<td>
<div>
<p>The vehicle trailer count.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the trailer count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC20withTrailerAxleCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTrailerAxleCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC20withTrailerAxleCountyAEs5Int32VF">withTrailerAxleCount(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle trailer axle count.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withTrailerAxleCount</span><span class="p">(</span><span class="n">_</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>trailerAxleCount</em>
</code>
</td>
<td>
<div>
<p>The vehicle trailer axle count.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the trailer axle count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC26withGrossWeightInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withGrossWeightInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC26withGrossWeightInKilogramsyAEs5Int32VF">withGrossWeightInKilograms(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle gross weight in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withGrossWeightInKilograms</span><span class="p">(</span><span class="n">_</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>grossWeightInKilograms</em>
</code>
</td>
<td>
<div>
<p>The vehicle gross weight in kilograms.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the gross weight set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC28withCurrentWeightInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withCurrentWeightInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC28withCurrentWeightInKilogramsyAEs5Int32VF">withCurrentWeightInKilograms(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle current weight in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withCurrentWeightInKilograms</span><span class="p">(</span><span class="n">_</span> <span class="nv">currentWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>currentWeightInKilograms</em>
</code>
</td>
<td>
<div>
<p>The vehicle current weight in kilograms.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the current weight set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC26withEmptyWeightInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withEmptyWeightInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC26withEmptyWeightInKilogramsyAEs5Int32VF">withEmptyWeightInKilograms(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle empty weight in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withEmptyWeightInKilograms</span><span class="p">(</span><span class="n">_</span> <span class="nv">emptyWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>emptyWeightInKilograms</em>
</code>
</td>
<td>
<div>
<p>The vehicle empty weight in kilograms.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the empty weight set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC28withWeightPerAxleInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withWeightPerAxleInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC28withWeightPerAxleInKilogramsyAEs5Int32VF">withWeightPerAxleInKilograms(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle weight per axle in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withWeightPerAxleInKilograms</span><span class="p">(</span><span class="n">_</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>weightPerAxleInKilograms</em>
</code>
</td>
<td>
<div>
<p>The vehicle weight per axle in kilograms.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the current weight per axle set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC22withWeightPerAxleGroupyAeA0ghiJ0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withWeightPerAxleGroup(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC22withWeightPerAxleGroupyAeA0ghiJ0VF">withWeightPerAxleGroup(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle weight per axle group.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withWeightPerAxleGroup</span><span class="p">(</span><span class="n">_</span> <span class="nv">weightPerAxleGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-weightperaxlegroup">WeightPerAxleGroup</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>weightPerAxleGroup</em>
</code>
</td>
<td>
<div>
<p>The vehicle weight per axle group.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the current weight per axle group set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC16withIsCommercialyAESbF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withIsCommercial(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC16withIsCommercialyAESbF">withIsCommercial(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle is commercial flag.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withIsCommercial</span><span class="p">(</span><span class="n">_</span> <span class="nv">isCommercial</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>isCommercial</em>
</code>
</td>
<td>
<div>
<p>The vehicle is commercial flag.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the is commercial flag set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC31withLastCharacterOfLicensePlateyAESSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withLastCharacterOfLicensePlate(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC31withLastCharacterOfLicensePlateyAESSF">withLastCharacterOfLicensePlate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle last character of the license plate.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withLastCharacterOfLicensePlate</span><span class="p">(</span><span class="n">_</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lastCharacterOfLicensePlate</em>
</code>
</td>
<td>
<div>
<p>The vehicle last character of the license plate.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the last character of the licence plate set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC32withEngineSizeInCubicCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withEngineSizeInCubicCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC32withEngineSizeInCubicCentimetersyAEs5Int32VF">withEngineSizeInCubicCentimeters(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle engine size in cubic centimeters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withEngineSizeInCubicCentimeters</span><span class="p">(</span><span class="n">_</span> <span class="nv">engineSizeInCubicCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>engineSizeInCubicCentimeters</em>
</code>
</td>
<td>
<div>
<p>The vehicle engine size in cubic centimeters.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the engine size set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC14withTiresCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTiresCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC14withTiresCountyAEs5Int32VF">withTiresCount(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle tires count.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withTiresCount</span><span class="p">(</span><span class="n">_</span> <span class="nv">tiresCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tiresCount</em>
</code>
</td>
<td>
<div>
<p>The vehicle tires count.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the vehicle tires count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC18withTunnelCategoryyAeA0gH0OF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTunnelCategory(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC18withTunnelCategoryyAeA0gH0OF">withTunnelCategory(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle tunnel category.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withTunnelCategory</span><span class="p">(</span><span class="n">_</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-tunnelcategory">TunnelCategory</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tunnelCategory</em>
</code>
</td>
<td>
<div>
<p>The vehicle tunnel category.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the vehicle tunnel category set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC13withOccupancyyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withOccupancy(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC13withOccupancyyAEs5Int32VF">withOccupancy(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle occupants number.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withOccupancy</span><span class="p">(</span><span class="n">_</span> <span class="nv">occupancy</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>occupancy</em>
</code>
</td>
<td>
<div>
<p>The vehicle occupants number.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.BusBuilder</code> object with the vehicle occupants number set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC5buildACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC5buildACyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds the <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></code> object for <code><a href="../../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code> with the specifications taken
from the <code>VehicleSpecification.BusBuilder</code> object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclespecification">VehicleSpecification</a></code> object created from the <code>VehicleSpecification.BusBuilder</code> object.</p>
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
