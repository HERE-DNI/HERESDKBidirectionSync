---
title: "TaxiBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-structs-vehiclespecification-taxibuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TaxiBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/TaxiBuilder"></a>
<a title="TaxiBuilder Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Routing.html">Routing</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Structs/VehicleSpecification.html">VehicleSpecification</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        TaxiBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class TaxiBuilder</code></pre>
<pre><code>extension VehicleSpecification.TaxiBuilder: NativeBase</code></pre>
<pre><code>extension VehicleSpecification.TaxiBuilder: Hashable</code></pre>
</div>
</div>
<p>This class constructs a <code><a href="../../Structs/VehicleSpecification.html">VehicleSpecification</a></code> for a taxi.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderCAEycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderCAEycfc">init()</a>
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
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC23withHeightInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withHeightInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC23withHeightInCentimetersyAEs5Int32VF">withHeightInCentimeters(_:<wbr/>)</a>
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
<pre><code>public func withHeightInCentimeters(_ heightInCentimeters: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the vehicle height set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC22withWidthInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withWidthInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC22withWidthInCentimetersyAEs5Int32VF">withWidthInCentimeters(_:<wbr/>)</a>
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
<pre><code>public func withWidthInCentimeters(_ widthInCentimeters: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the vehicle width set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC23withLengthInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withLengthInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC23withLengthInCentimetersyAEs5Int32VF">withLengthInCentimeters(_:<wbr/>)</a>
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
<pre><code>public func withLengthInCentimeters(_ lengthInCentimeters: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the vehicle length set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC13withAxleCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withAxleCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC13withAxleCountyAEs5Int32VF">withAxleCount(_:<wbr/>)</a>
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
<pre><code>public func withAxleCount(_ axleCount: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the axle count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC42withKingpinToRearAxleDistanceInCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withKingpinToRearAxleDistanceInCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC42withKingpinToRearAxleDistanceInCentimetersyAEs5Int32VF">withKingpinToRearAxleDistanceInCentimeters(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle kingpin to rear axle distance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withKingpinToRearAxleDistanceInCentimeters(_ length: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>length</em>
</code>
</td>
<td>
<div>
<p>The distance from kingpin to the rear axle.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the kingpin to rear axle set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC16withTrailerCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTrailerCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC16withTrailerCountyAEs5Int32VF">withTrailerCount(_:<wbr/>)</a>
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
<pre><code>public func withTrailerCount(_ trailerCount: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the trailer count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC30withPayloadCapacityInKilograms07payloadhiJ0AEs5Int32V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withPayloadCapacityInKilograms(payloadCapacityInKilograms:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC30withPayloadCapacityInKilograms07payloadhiJ0AEs5Int32V_tF">withPayloadCapacityInKilograms(payloadCapacityInKilograms:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the vehicle payload capacity in kilograms.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withPayloadCapacityInKilograms(payloadCapacityInKilograms: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>payloadCapacityInKilograms</em>
</code>
</td>
<td>
<div>
<p>The vehicle payload capacity in kilograms.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the payload capacity set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC20withTrailerAxleCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTrailerAxleCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC20withTrailerAxleCountyAEs5Int32VF">withTrailerAxleCount(_:<wbr/>)</a>
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
<pre><code>public func withTrailerAxleCount(_ trailerAxleCount: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the trailer axle count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC26withGrossWeightInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withGrossWeightInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC26withGrossWeightInKilogramsyAEs5Int32VF">withGrossWeightInKilograms(_:<wbr/>)</a>
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
<pre><code>public func withGrossWeightInKilograms(_ grossWeightInKilograms: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the gross weight set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC28withCurrentWeightInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withCurrentWeightInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC28withCurrentWeightInKilogramsyAEs5Int32VF">withCurrentWeightInKilograms(_:<wbr/>)</a>
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
<pre><code>public func withCurrentWeightInKilograms(_ currentWeightInKilograms: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the current weight set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC26withEmptyWeightInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withEmptyWeightInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC26withEmptyWeightInKilogramsyAEs5Int32VF">withEmptyWeightInKilograms(_:<wbr/>)</a>
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
<pre><code>public func withEmptyWeightInKilograms(_ emptyWeightInKilograms: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the empty weight set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC28withWeightPerAxleInKilogramsyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withWeightPerAxleInKilograms(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC28withWeightPerAxleInKilogramsyAEs5Int32VF">withWeightPerAxleInKilograms(_:<wbr/>)</a>
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
<pre><code>public func withWeightPerAxleInKilograms(_ weightPerAxleInKilograms: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the current weight per axle set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC16withIsCommercialyAESbF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withIsCommercial(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC16withIsCommercialyAESbF">withIsCommercial(_:<wbr/>)</a>
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
<pre><code>public func withIsCommercial(_ isCommercial: Bool) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the is commercial flag set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC31withLastCharacterOfLicensePlateyAESSF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withLastCharacterOfLicensePlate(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC31withLastCharacterOfLicensePlateyAESSF">withLastCharacterOfLicensePlate(_:<wbr/>)</a>
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
<pre><code>public func withLastCharacterOfLicensePlate(_ lastCharacterOfLicensePlate: String) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the last character of the licence plate set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC32withEngineSizeInCubicCentimetersyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withEngineSizeInCubicCentimeters(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC32withEngineSizeInCubicCentimetersyAEs5Int32VF">withEngineSizeInCubicCentimeters(_:<wbr/>)</a>
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
<pre><code>public func withEngineSizeInCubicCentimeters(_ engineSizeInCubicCentimeters: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the engine size set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC14withTiresCountyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTiresCount(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC14withTiresCountyAEs5Int32VF">withTiresCount(_:<wbr/>)</a>
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
<pre><code>public func withTiresCount(_ tiresCount: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the vehicle tires count set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC18withTunnelCategoryyAeA0gH0OF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withTunnelCategory(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC18withTunnelCategoryyAeA0gH0OF">withTunnelCategory(_:<wbr/>)</a>
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
<pre><code>public func withTunnelCategory(_ tunnelCategory: TunnelCategory) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the vehicle tunnel category set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC13withOccupancyyAEs5Int32VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withOccupancy(_:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC13withOccupancyyAEs5Int32VF">withOccupancy(_:<wbr/>)</a>
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
<pre><code>public func withOccupancy(_ occupancy: Int32) -&gt; VehicleSpecification.TaxiBuilder</code></pre>
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
<p>The <code>VehicleSpecification.TaxiBuilder</code> object with the vehicle occupants number set to the new value.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC5buildACyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC5buildACyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds the <code><a href="../../Structs/VehicleSpecification.html">VehicleSpecification</a></code> object for <code><a href="../../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> with the specifications taken
from the <code>VehicleSpecification.TaxiBuilder</code> object.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; VehicleSpecification</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code><a href="../../Structs/VehicleSpecification.html">VehicleSpecification</a></code> object created from the <code>VehicleSpecification.TaxiBuilder</code> object.</p>
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
