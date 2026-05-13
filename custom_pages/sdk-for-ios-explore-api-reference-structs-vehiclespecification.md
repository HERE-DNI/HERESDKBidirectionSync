---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-vehiclespecification"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VehicleSpecification.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleSpecification"></a>
<a title="VehicleSpecification Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VehicleSpecification Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VehicleSpecification</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Contains vehicle related attributes. Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/heightInCentimeters"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">heightInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/widthInCentimeters"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">widthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInCentimeters"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">lengthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCount"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">axleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
Rendering: When set, truck restriction icons for an axle count greater than <code>VehicleSpecification.axleCount</code> will not be displayed.
When specifying <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>, then <code>VehicleSpecification.axleCount</code> is required and must be greater than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerCount"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">trailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines number of trailers attached to the vehicle. The provided value must be in the range [0, 255].
By default, it is not set.
When specifying <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>, then <code>VehicleSpecification.trailerCount</code> is required and must be greater than 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV9truckTypeAA05TruckE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckType"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV9truckTypeAA05TruckE0Ovp">truckType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Will be replaced with <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">truckCategory</a></code> when the <code>TruckSpecification</code> will be replaced by <code>VehicleSpecification</code>.
Defines the type of truck.
Defaults to <code><a href="../Enums/TruckType.html#/s:7heresdk9TruckTypeO8straightyA2CmF">TruckType.straight</a></code>.
Rendering <code>sdk.mapview.TruckProfile</code>: <code>VehicleSpecification.truckType</code> is ignored and has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use <code>VehicleSpecification.truckCategory</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">truckType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-trucktype">TruckType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckCategory"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">truckCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the truck category.
By default, it is not set.
Rendering: <code>VehicleSpecification.truckCategory</code> is ignored and has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-truckcategory">TruckCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV12isTruckLightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTruckLight"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV12isTruckLightSbvp">isTruckLight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan.
Defaults to <code>false</code>.</p>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
the vehicle can access, which access restrictions apply, and which speed limits are applicable.
Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to <code>true</code>,
you will get, for example, the same speed limits as for cars. Make sure to set the flag only to <code>true</code>, when
a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When on <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontentsettings">MapContentSettings</a></code>, then this flag will be ignored and has no effect.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.</li>
</ul><div class="aside aside-note">
<p class="aside-title">Note</p>
    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.

</div><ul>
<li>Supported only in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code> transport mode.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTruckLight</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/payloadCapacityInKilograms"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">payloadCapacityInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0.
By default, it is not set.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta)
transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">payloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerAxleCount"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">trailerAxleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>, hence <code>VehicleSpecification.trailerAxleCount</code> must be less than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>
and greater than or equal to 1. <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code> are required to specify <code>VehicleSpecification.trailerAxleCount</code>.
By default, it is not set.</p>
<p><strong>Note:</strong>: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/kingpinToRearAxleDistanceInCentimeters"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">kingpinToRearAxleDistanceInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the kingpin to rear axle distance, in centimeters.</p>
<p><strong>NOTE:</strong> Currently, the KPRA restrictions are only present in California and Idaho.
<strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">kingpinToRearAxleDistanceInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV22emptyWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/emptyWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV22emptyWeightInKilogramss5Int32VSgvp">emptyWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.
The provided value must be greater than or equal to 0.
By default, it is not set.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">emptyWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/grossWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">grossWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code>.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 4250 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 7550 kg.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">currentWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 5000 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 8500 kg.</li>
<li>A route request with <code>VehicleSpecification.currentWeightInKilograms</code> above <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code> may result in
non-compliant or invalid routes.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">currentWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weightPerAxleInKilograms"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">weightPerAxleInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li><code>VehicleSpecification.weightPerAxleInKilograms</code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code> are incompatible.
When available for your edition, if both attributes are set, during online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> an <code>RoutingError.INVALID_PARAMETER</code>
error is generated. Otherwise, when offline <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> is in place, both parameters are evaluated and the
maximum value between them will be used.</li>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weightPerAxleGroup"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">weightPerAxleGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allows specification of axle weights in a more fine-grained way than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code>.
This is relevant in countries with signs and regulations that specify different limits for different axle
groups, like the USA and Sweden.
By default is not set.</p>
<p><strong>Notes:</strong></p>
<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code> and <code>VehicleSpecification.weightPerAxleGroup</code> are incompatible.
When available for your edition, if both attributes are set, during online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> an <code>RoutingError.INVALID_PARAMETER</code>
error is generated. Otherwise, when offline <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> is in place, both parameters are evaluated and
the maximum value between them will be used.</li>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weightPerAxleGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-weightperaxlegroup">WeightPerAxleGroup</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV12isCommercialSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isCommercial"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV12isCommercialSbvp">isCommercial</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies whether the vehicle is a commercial or a non-commercial vehicle.
Defaults to <code>false</code>.</p>
<p><strong>Notes</strong></p>
<ul>
<li>Only supported for online routing.</li>
<li>This parameter is currently used only for the calculation of tolls in regions where it is applicable.</li>
<li>Not used for offline calculations.</li>
<li>Supported for <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code> and <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isCommercial</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV27lastCharacterOfLicensePlateSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastCharacterOfLicensePlate"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV27lastCharacterOfLicensePlateSSSgvp">lastCharacterOfLicensePlate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Last character of license plate in String format. This value can be used to
evaluate restrictions in environmental zones.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV28engineSizeInCubicCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/engineSizeInCubicCentimeters"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV28engineSizeInCubicCentimeterss5Int32VSgvp">engineSizeInCubicCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535.
Default value is <code>nil</code>, which means the scooter route calculation ignores all engine size limits on the
road.</p>
<p><strong>Notes</strong></p>
<ul>
<li>For now, this option is only relevant in Japan and will be ignored for other countries. Currently,
map data for this option is only available for Japan.</li>
<li>Supported only in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO7scooteryA2CmF">TransportMode.scooter</a></code> (Alpha) transport mode.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">engineSizeInCubicCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tiresCount"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">tiresCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.
By default, it is not set.
Otherwise it is guaranteed to be in the range [1, 255].</p>
<p><strong>Note</strong>: This parameter is not supported in isoline routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tiresCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tunnelCategory"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">tunnelCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <code><a href="sdk-for-ios-explore-api-reference-..-enums-tunnelcategory">TunnelCategory</a></code> for the available options.
By default, it is not set.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousMaterials"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">hazardousMaterials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a list of hazardous materials shipped in the vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-..-enums-hazardousmaterial">HazardousMaterial</a></code> for the available options.
By default, it is an empty list.</p>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
<code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV9occupancys5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/occupancy"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV9occupancys5Int32VSgvp">occupancy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle’s ability to use HOV/carpool restricted lanes.
Should not be less than 1 or greater than 255.
By default, it is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">occupancy</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV19heightInCentimeters05widtheF006lengtheF09axleCount07trailerJ013truckCategory12isTruckLight015payloadCapacityE9Kilograms0k4AxleJ0013kingpinToReart8DistanceeF0011emptyWeighteS005grosszeS007currentzeS009weightPerteS009weightPerT5Group0N10Commercial27lastCharacterOfLicensePlate010engineSizee5CubicF005tiresJ006tunnelM018hazardousMaterials9occupancyACs5Int32VSg_A0_A0_A0_A0_AA0oM0OSgSbA0_A0_A0_A0_A0_A0_A0_AA0z3PerT5GroupVSgSbSSSgA0_A0_AA06TunnelM0OSgSayAA17HazardousMaterialOGA0_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(heightInCentimeters:widthInCentimeters:lengthInCentimeters:axleCount:trailerCount:truckCategory:isTruckLight:payloadCapacityInKilograms:trailerAxleCount:kingpinToRearAxleDistanceInCentimeters:emptyWeightInKilograms:grossWeightInKilograms:currentWeightInKilograms:weightPerAxleInKilograms:weightPerAxleGroup:isCommercial:lastCharacterOfLicensePlate:engineSizeInCubicCentimeters:tiresCount:tunnelCategory:hazardousMaterials:occupancy:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV19heightInCentimeters05widtheF006lengtheF09axleCount07trailerJ013truckCategory12isTruckLight015payloadCapacityE9Kilograms0k4AxleJ0013kingpinToReart8DistanceeF0011emptyWeighteS005grosszeS007currentzeS009weightPerteS009weightPerT5Group0N10Commercial27lastCharacterOfLicensePlate010engineSizee5CubicF005tiresJ006tunnelM018hazardousMaterials9occupancyACs5Int32VSg_A0_A0_A0_A0_AA0oM0OSgSbA0_A0_A0_A0_A0_A0_A0_AA0z3PerT5GroupVSgSbSSSgA0_A0_AA06TunnelM0OSgSayAA17HazardousMaterialOGA0_tcfc">init(heightInCentimeters:<wbr/>widthInCentimeters:<wbr/>lengthInCentimeters:<wbr/>axleCount:<wbr/>trailerCount:<wbr/>truckCategory:<wbr/>isTruckLight:<wbr/>payloadCapacityInKilograms:<wbr/>trailerAxleCount:<wbr/>kingpinToRearAxleDistanceInCentimeters:<wbr/>emptyWeightInKilograms:<wbr/>grossWeightInKilograms:<wbr/>currentWeightInKilograms:<wbr/>weightPerAxleInKilograms:<wbr/>weightPerAxleGroup:<wbr/>isCommercial:<wbr/>lastCharacterOfLicensePlate:<wbr/>engineSizeInCubicCentimeters:<wbr/>tiresCount:<wbr/>tunnelCategory:<wbr/>hazardousMaterials:<wbr/>occupancy:<wbr/>)</a>
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
<li>heightInCentimeters: Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>widthInCentimeters: Vehicle width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>lengthInCentimeters: Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>axleCount: Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
Rendering: When set, truck restriction icons for an axle count greater than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> will not be displayed.
When specifying <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>, then <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> is required and must be greater than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>trailerCount: Defines number of trailers attached to the vehicle. The provided value must be in the range [0, 255].
By default, it is not set.
When specifying <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>, then <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code> is required and must be greater than 0.</li>
<li>truckCategory: Defines the truck category.
By default, it is not set.
Rendering: <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">VehicleSpecification.truckCategory</a></code> is ignored and has no effect.</li>
<li>isTruckLight: A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan.
Defaults to <code>false</code>.</li>
</ul>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
  the vehicle can access, which access restrictions apply, and which speed limits are applicable.
  Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
  not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to <code>true</code>,
  you will get, for example, the same speed limits as for cars. Make sure to set the flag only to <code>true</code>, when
  a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When on <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontentsettings">MapContentSettings</a></code>, then this flag will be ignored and has no effect.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
  experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.</li>
</ul><div class="aside aside-note">
<p class="aside-title">Note</p>
    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.

</div><ul>
<li>Supported only in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code> transport mode.

<ul>
<li>payloadCapacityInKilograms: Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0.
By default, it is not set.</li>
</ul></li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta)
  transport modes.</p>
<ul>
<li>trailerAxleCount: Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>, hence <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code> must be less than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>
and greater than or equal to 1. <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code> are required to specify <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>.
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong>: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p>
<ul>
<li>kingpinToRearAxleDistanceInCentimeters: Defines the kingpin to rear axle distance, in centimeters.</li>
</ul>
<p><strong>NOTE:</strong> Currently, the KPRA restrictions are only present in California and Idaho.
  <strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>emptyWeightInKilograms: Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.
The provided value must be greater than or equal to 0.
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>grossWeightInKilograms: Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code>.
By default, it is not set.</li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 4250 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 7550 kg.

<ul>
<li>currentWeightInKilograms: Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>.
By default, it is not set.</li>
</ul></li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 5000 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 8500 kg.</li>
<li>A route request with <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code> above <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code> may result in
  non-compliant or invalid routes.

<ul>
<li>weightPerAxleInKilograms: Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.</li>
</ul></li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code> are incompatible.
  When available for your edition, if both attributes are set, during online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> an <code>RoutingError.INVALID_PARAMETER</code>
  error is generated. Otherwise, when offline <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> is in place, both parameters are evaluated and the
  maximum value between them will be used.</li>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.

<ul>
<li>weightPerAxleGroup: Allows specification of axle weights in a more fine-grained way than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code>.
This is relevant in countries with signs and regulations that specify different limits for different axle
groups, like the USA and Sweden.
By default is not set.</li>
</ul></li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code> are incompatible.
  When available for your edition, if both attributes are set, during online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> an <code>RoutingError.INVALID_PARAMETER</code>
  error is generated. Otherwise, when offline <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> is in place, both parameters are evaluated and
  the maximum value between them will be used.</li>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.

<ul>
<li>isCommercial: Specifies whether the vehicle is a commercial or a non-commercial vehicle.
Defaults to <code>false</code>.</li>
</ul></li>
</ul>
<p><strong>Notes</strong></p>
<ul>
<li>Only supported for online routing.</li>
<li>This parameter is currently used only for the calculation of tolls in regions where it is applicable.</li>
<li>Not used for offline calculations.</li>
<li>Supported for <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code> and <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>.

<ul>
<li>lastCharacterOfLicensePlate: Last character of license plate in String format. This value can be used to
evaluate restrictions in environmental zones.
By default, it is not set.</li>
<li>engineSizeInCubicCentimeters: Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535.
Default value is <code>nil</code>, which means the scooter route calculation ignores all engine size limits on the
road.</li>
</ul></li>
</ul>
<p><strong>Notes</strong></p>
<ul>
<li>For now, this option is only relevant in Japan and will be ignored for other countries. Currently,
  map data for this option is only available for Japan.</li>
<li>Supported only in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO7scooteryA2CmF">TransportMode.scooter</a></code> (Alpha) transport mode.

<ul>
<li>tiresCount: The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.
By default, it is not set.
Otherwise it is guaranteed to be in the range [1, 255].</li>
</ul></li>
</ul>
<p><strong>Note</strong>: This parameter is not supported in isoline routing.</p>
<ul>
<li>tunnelCategory: Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <code><a href="sdk-for-ios-explore-api-reference-..-enums-tunnelcategory">TunnelCategory</a></code> for the available options.
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>hazardousMaterials: Specifies a list of hazardous materials shipped in the vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-..-enums-hazardousmaterial">HazardousMaterial</a></code> for the available options.
By default, it is an empty list.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>occupancy: Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle’s ability to use HOV/carpool restricted lanes.
Should not be less than 1 or greater than 255.
By default, it is not set.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-truckcategory">TruckCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isTruckLight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">payloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">kingpinToRearAxleDistanceInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">emptyWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">currentWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-weightperaxlegroup">WeightPerAxleGroup</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isCommercial</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">engineSizeInCubicCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">tiresCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">occupancy</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV19heightInCentimeters05widtheF006lengtheF09axleCount07trailerJ09truckType0L8Category12isTruckLight015payloadCapacityE9Kilograms0k4AxleJ0013kingpinToRearu8DistanceeF0011emptyWeighteT0011grossWeighteT0013currentWeighteT009weightPerueT009weightPerU5Group0O10Commercial27lastCharacterOfLicensePlate010engineSizee5CubicF005tiresJ006tunnelN018hazardousMaterials9occupancyACs5Int32VSg_A1_A1_A1_A1_AA0pM0OAA0pN0OSgSbA1_A1_A1_A1_A1_A1_A1_AA09WeightPerU5GroupVSgSbSSSgA1_A1_AA06TunnelN0OSgSayAA17HazardousMaterialOGA1_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(heightInCentimeters:widthInCentimeters:lengthInCentimeters:axleCount:trailerCount:truckType:truckCategory:isTruckLight:payloadCapacityInKilograms:trailerAxleCount:kingpinToRearAxleDistanceInCentimeters:emptyWeightInKilograms:grossWeightInKilograms:currentWeightInKilograms:weightPerAxleInKilograms:weightPerAxleGroup:isCommercial:lastCharacterOfLicensePlate:engineSizeInCubicCentimeters:tiresCount:tunnelCategory:hazardousMaterials:occupancy:)"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV19heightInCentimeters05widtheF006lengtheF09axleCount07trailerJ09truckType0L8Category12isTruckLight015payloadCapacityE9Kilograms0k4AxleJ0013kingpinToRearu8DistanceeF0011emptyWeighteT0011grossWeighteT0013currentWeighteT009weightPerueT009weightPerU5Group0O10Commercial27lastCharacterOfLicensePlate010engineSizee5CubicF005tiresJ006tunnelN018hazardousMaterials9occupancyACs5Int32VSg_A1_A1_A1_A1_AA0pM0OAA0pN0OSgSbA1_A1_A1_A1_A1_A1_A1_AA09WeightPerU5GroupVSgSbSSSgA1_A1_AA06TunnelN0OSgSayAA17HazardousMaterialOGA1_tcfc">init(heightInCentimeters:<wbr/>widthInCentimeters:<wbr/>lengthInCentimeters:<wbr/>axleCount:<wbr/>trailerCount:<wbr/>truckType:<wbr/>truckCategory:<wbr/>isTruckLight:<wbr/>payloadCapacityInKilograms:<wbr/>trailerAxleCount:<wbr/>kingpinToRearAxleDistanceInCentimeters:<wbr/>emptyWeightInKilograms:<wbr/>grossWeightInKilograms:<wbr/>currentWeightInKilograms:<wbr/>weightPerAxleInKilograms:<wbr/>weightPerAxleGroup:<wbr/>isCommercial:<wbr/>lastCharacterOfLicensePlate:<wbr/>engineSizeInCubicCentimeters:<wbr/>tiresCount:<wbr/>tunnelCategory:<wbr/>hazardousMaterials:<wbr/>occupancy:<wbr/>)</a>
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
<li>heightInCentimeters: Vehicle height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>widthInCentimeters: Vehicle width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>lengthInCentimeters: Vehicle length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>axleCount: Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2.
By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be taken into consideration.
Rendering: When set, truck restriction icons for an axle count greater than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> will not be displayed.
When specifying <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>, then <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> is required and must be greater than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>trailerCount: Defines number of trailers attached to the vehicle. The provided value must be in the range [0, 255].
By default, it is not set.
When specifying <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>, then <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code> is required and must be greater than 0.</li>
<li>truckType: Will be replaced with <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">truckCategory</a></code> when the <code>TruckSpecification</code> will be replaced by <code>VehicleSpecification</code>.
Defines the type of truck.
Defaults to <code><a href="../Enums/TruckType.html#/s:7heresdk9TruckTypeO8straightyA2CmF">TruckType.straight</a></code>.
Rendering <code>sdk.mapview.TruckProfile</code>: <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9truckTypeAA05TruckE0Ovp">VehicleSpecification.truckType</a></code> is ignored and has no effect.</li>
<li>truckCategory: Defines the truck category.
By default, it is not set.
Rendering: <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">VehicleSpecification.truckCategory</a></code> is ignored and has no effect.</li>
<li>isTruckLight: A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan.
Defaults to <code>false</code>.</li>
</ul>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
  the vehicle can access, which access restrictions apply, and which speed limits are applicable.
  Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
  not always overwrite these settings. Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to <code>true</code>,
  you will get, for example, the same speed limits as for cars. Make sure to set the flag only to <code>true</code>, when
  a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When on <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcontentsettings">MapContentSettings</a></code>, then this flag will be ignored and has no effect.</p>
<p><strong>Notes:</strong></p>
<ul>
<li>This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
  experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.</li>
</ul><div class="aside aside-note">
<p class="aside-title">Note</p>
    Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases without a deprecation process.

</div><ul>
<li>Supported only in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code> transport mode.

<ul>
<li>payloadCapacityInKilograms: Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0.
By default, it is not set.</li>
</ul></li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta)
  transport modes.</p>
<ul>
<li>trailerAxleCount: Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>, hence <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code> must be less than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>
and greater than or equal to 1. <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code> are required to specify <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV16trailerAxleCounts5Int32VSgvp">VehicleSpecification.trailerAxleCount</a></code>.
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong>: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p>
<ul>
<li>kingpinToRearAxleDistanceInCentimeters: Defines the kingpin to rear axle distance, in centimeters.</li>
</ul>
<p><strong>NOTE:</strong> Currently, the KPRA restrictions are only present in California and Idaho.
  <strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>emptyWeightInKilograms: Empty weight of the vehicle without any load, excluding trailers, specified in kilograms.
The provided value must be greater than or equal to 0.
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>grossWeightInKilograms: Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code>.
By default, it is not set.</li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 4250 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 7550 kg.

<ul>
<li>currentWeightInKilograms: Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>.
By default, it is not set.</li>
</ul></li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</li>
<li>Maximum weight for a car or taxi <em>without</em> a trailer is 5000 kg.</li>
<li>Maximum weight for a car or taxi <em>with</em> a trailer is 8500 kg.</li>
<li>A route request with <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code> above <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code> may result in
  non-compliant or invalid routes.

<ul>
<li>weightPerAxleInKilograms: Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.</li>
</ul></li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code> are incompatible.
  When available for your edition, if both attributes are set, during online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> an <code>RoutingError.INVALID_PARAMETER</code>
  error is generated. Otherwise, when offline <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> is in place, both parameters are evaluated and the
  maximum value between them will be used.</li>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.

<ul>
<li>weightPerAxleGroup: Allows specification of axle weights in a more fine-grained way than <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code>.
This is relevant in countries with signs and regulations that specify different limits for different axle
groups, like the USA and Sweden.
By default is not set.</li>
</ul></li>
</ul>
<p><strong>Notes:</strong></p>
<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code> and <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code> are incompatible.
  When available for your edition, if both attributes are set, during online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> an <code>RoutingError.INVALID_PARAMETER</code>
  error is generated. Otherwise, when offline <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code> is in place, both parameters are evaluated and
  the maximum value between them will be used.</li>
<li>Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.

<ul>
<li>isCommercial: Specifies whether the vehicle is a commercial or a non-commercial vehicle.
Defaults to <code>false</code>.</li>
</ul></li>
</ul>
<p><strong>Notes</strong></p>
<ul>
<li>Only supported for online routing.</li>
<li>This parameter is currently used only for the calculation of tolls in regions where it is applicable.</li>
<li>Not used for offline calculations.</li>
<li>Supported for <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code> and <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>.

<ul>
<li>lastCharacterOfLicensePlate: Last character of license plate in String format. This value can be used to
evaluate restrictions in environmental zones.
By default, it is not set.</li>
<li>engineSizeInCubicCentimeters: Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535.
Default value is <code>nil</code>, which means the scooter route calculation ignores all engine size limits on the
road.</li>
</ul></li>
</ul>
<p><strong>Notes</strong></p>
<ul>
<li>For now, this option is only relevant in Japan and will be ignored for other countries. Currently,
  map data for this option is only available for Japan.</li>
<li>Supported only in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO7scooteryA2CmF">TransportMode.scooter</a></code> (Alpha) transport mode.

<ul>
<li>tiresCount: The total number of tires the vehicle has, i.e., the tires on the base vehicle and any attached trailers.
By default, it is not set.
Otherwise it is guaranteed to be in the range [1, 255].</li>
</ul></li>
</ul>
<p><strong>Note</strong>: This parameter is not supported in isoline routing.</p>
<ul>
<li>tunnelCategory: Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <code><a href="sdk-for-ios-explore-api-reference-..-enums-tunnelcategory">TunnelCategory</a></code> for the available options.
By default, it is not set.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>hazardousMaterials: Specifies a list of hazardous materials shipped in the vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-..-enums-hazardousmaterial">HazardousMaterial</a></code> for the available options.
By default, it is an empty list.</li>
</ul>
<p><strong>Note:</strong> Supported in <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3busyA2CmF">TransportMode.bus</a></code>, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO10privateBusyA2CmF">TransportMode.privateBus</a></code>,
  <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code> (Beta), <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code> (Beta) transport modes.</p>
<ul>
<li>occupancy: Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle’s ability to use HOV/carpool restricted lanes.
Should not be less than 1 or greater than 255.
By default, it is not set.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated)</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">truckType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-trucktype">TruckType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-trucktype">TruckType</a></span><span class="o">.</span><span class="n">straight</span><span class="p">,</span> <span class="nv">truckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-truckcategory">TruckCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isTruckLight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">payloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">kingpinToRearAxleDistanceInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">emptyWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">currentWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-weightperaxlegroup">WeightPerAxleGroup</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">isCommercial</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">engineSizeInCubicCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">tiresCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">tunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">occupancy</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10CarBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/CarBuilder"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10CarBuilderC">CarBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></code> for a car.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification-carbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">CarBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">CarBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV12TruckBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TruckBuilder"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV12TruckBuilderC">TruckBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></code> for a truck.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification-truckbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TruckBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">TruckBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">TruckBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV14ScooterBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ScooterBuilder"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV14ScooterBuilderC">ScooterBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></code> for a scooter.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification-scooterbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ScooterBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">ScooterBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">ScooterBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV11TaxiBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TaxiBuilder"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV11TaxiBuilderC">TaxiBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></code> for a taxi.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification-taxibuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TaxiBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">TaxiBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">TaxiBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV10BusBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/BusBuilder"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV10BusBuilderC">BusBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></code> for a bus.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification-busbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">BusBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">BusBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20VehicleSpecificationV17PrivateBusBuilderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/PrivateBusBuilder"></a>
<a class="token" href="#/s:7heresdk20VehicleSpecificationV17PrivateBusBuilderC">PrivateBusBuilder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class constructs a <code><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></code> for a private bus.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification-privatebusbuilder">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PrivateBusBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">PrivateBusBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-vehiclespecification">VehicleSpecification</a></span><span class="o">.</span><span class="kt">PrivateBusBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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

</div>
`
}</HTMLBlock>
