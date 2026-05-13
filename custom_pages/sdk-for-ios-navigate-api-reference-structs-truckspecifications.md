---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-structs-truckspecifications"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TruckSpecifications.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TruckSpecifications"></a>
<a title="TruckSpecifications Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TruckSpecifications Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TruckSpecifications</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TruckSpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Truck specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/grossWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp">grossWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp">TruckSpecifications.currentWeightInKilograms</a></code>. By default, it is not set.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/currentWeightInKilograms"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp">currentWeightInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp">TruckSpecifications.grossWeightInKilograms</a></code>. By default, it is not set.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV24weightPerAxleInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weightPerAxleInKilograms"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV24weightPerAxleInKilogramss5Int32VSgvp">weightPerAxleInKilograms</a>
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
By default, it is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV18weightPerAxleGroupAA06WeightefG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/weightPerAxleGroup"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV18weightPerAxleGroupAA06WeightefG0VSgvp">weightPerAxleGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
By default is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">weightPerAxleGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-weightperaxlegroup">WeightPerAxleGroup</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TruckSpecificationsV19heightInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/heightInCentimeters"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV19heightInCentimeterss5Int32VSgvp">heightInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV18widthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/widthInCentimeters"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV18widthInCentimeterss5Int32VSgvp">widthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV19lengthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInCentimeters"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV19lengthInCentimeterss5Int32VSgvp">lengthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Truck length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/axleCount"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">axleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
greater than <code>TruckSpecifications.axleCount</code> will not be displayed.
When specifying <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>, then <code>TruckSpecifications.axleCount</code> is required and must be greater than <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerCount"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">trailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 255]. By default, it is not set.
When specifying <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>, then <code>TruckSpecifications.trailerCount</code> is required and must be greater than 0.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV9truckTypeAA0bE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckType"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV9truckTypeAA0bE0Ovp">truckType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the type of truck. By default, it is <code><a href="../Enums/TruckType.html#/s:7heresdk9TruckTypeO8straightyA2CmF">TruckType.straight</a></code>.
Rendering <code>sdk.mapview.TruckProfile</code>: <code>TruckSpecifications.truckType</code> is ignored and has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trucktype">TruckType</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TruckSpecificationsV02isB5LightSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTruckLight"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV02isB5LightSbvp">isTruckLight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.</p>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
the vehicle can access, which access restrictions apply, and which speed limits are applicable.
Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true,
you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when
a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When <code>TruckSpecifications</code> are set as part of <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapcontentsettings">MapContentSettings</a></code>, then this flag will be ignored and
has no effect.</p>
<p><strong>Note:</strong>
This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases with a deprecation process.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV26payloadCapacityInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/payloadCapacityInKilograms"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV26payloadCapacityInKilogramss5Int32VSgvp">payloadCapacityInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0. By default, it is not set.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trailerAxleCount"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">trailerAxleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code>, hence <code>TruckSpecifications.trailerAxleCount</code> must be less than <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code>
and greater than or equal to 1. <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code> and <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">TruckSpecifications.trailerCount</a></code> are required to specify <code>TruckSpecifications.trailerAxleCount</code>.
By default, it is not set.
Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</p>
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
<a name="/s:7heresdk19TruckSpecificationsV22grossWeightInKilograms07currentefG0013weightPerAxlefG00ijK5Group06heightF11Centimeters05widthfN006lengthfN09axleCount07trailerR09truckType02isB5Light015payloadCapacityfG00skR0ACs5Int32VSg_A2sA0ejkL0VSgA5sA0bU0OSbA2Stcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(grossWeightInKilograms:currentWeightInKilograms:weightPerAxleInKilograms:weightPerAxleGroup:heightInCentimeters:widthInCentimeters:lengthInCentimeters:axleCount:trailerCount:truckType:isTruckLight:payloadCapacityInKilograms:trailerAxleCount:)"></a>
<a class="token" href="#/s:7heresdk19TruckSpecificationsV22grossWeightInKilograms07currentefG0013weightPerAxlefG00ijK5Group06heightF11Centimeters05widthfN006lengthfN09axleCount07trailerR09truckType02isB5Light015payloadCapacityfG00skR0ACs5Int32VSg_A2sA0ejkL0VSgA5sA0bU0OSbA2Stcfc">init(grossWeightInKilograms:<wbr/>currentWeightInKilograms:<wbr/>weightPerAxleInKilograms:<wbr/>weightPerAxleGroup:<wbr/>heightInCentimeters:<wbr/>widthInCentimeters:<wbr/>lengthInCentimeters:<wbr/>axleCount:<wbr/>trailerCount:<wbr/>truckType:<wbr/>isTruckLight:<wbr/>payloadCapacityInKilograms:<wbr/>trailerAxleCount:<wbr/>)</a>
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
<li>grossWeightInKilograms: Gross truck weight, including trailers and shipped goods when loaded at capacity, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV24currentWeightInKilogramss5Int32VSgvp">TruckSpecifications.currentWeightInKilograms</a></code>. By default, it is not set.</li>
<li>currentWeightInKilograms: Current truck weight, including trailers and shipped goods currently loaded, specified in
kilograms. The provided value must be greater than or equal to 0. If unspecified,
it will default to <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV22grossWeightInKilogramss5Int32VSgvp">TruckSpecifications.grossWeightInKilograms</a></code>. By default, it is not set.</li>
<li>weightPerAxleInKilograms: Heaviest weight per axle, regardless of axle type or axle group.
It is evaluated against all axle weight restrictions, including single axle and tandem axle weight restrictions.
The provided value must be greater or equal to 0.
By default, it is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</li>
<li>weightPerAxleGroup: Allows specification of axle weights in a more fine-grained way than <code>weight_per_axle_in_kilograms</code>.
This is relevant in countries with signs and regulations that specify different limits for different axle groups, like the USA and Sweden.
By default is not set.
<strong>Note:</strong> <code>weight_per_axle_in_kilograms</code> and <code>weight_per_axle_group</code> are incompatible.
When available for your edition, if both attributes are set, during online RoutingEngine an [sdk.routing.RoutingError.INVALID_PARAMETER] error is generated.
Otherwise, when offline RoutingEngine is in place, both parameters are evaluated and the maximum value between them will be used.</li>
<li>heightInCentimeters: Truck height in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li>widthInCentimeters: Truck width in centimeters. The provided value must be in the range [0, 5000].
By default, it is not set.</li>
<li>lengthInCentimeters: Truck length in centimeters. The provided value must be in the range [0, 30000].
By default, it is not set.</li>
<li>axleCount: Defines total number of axles in the vehicle. The provided value must be greater than or
equal to 2. By default, it is not set.
Route calculation: When not set, possible axle count restrictions will not be
taken into consideration.
Rendering <code>sdk.mapview.TruckProfile</code>: When set, truck restriction icons for an axle count
greater than <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code> will not be displayed.
When specifying <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>, then <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code> is required and must be greater than <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>.</li>
<li>trailerCount: Defines number of trailers attached to the vehicle. The provided value must be in the range
[0, 255]. By default, it is not set.
When specifying <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>, then <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">TruckSpecifications.trailerCount</a></code> is required and must be greater than 0.</li>
<li>truckType: Defines the type of truck. By default, it is <code><a href="../Enums/TruckType.html#/s:7heresdk9TruckTypeO8straightyA2CmF">TruckType.straight</a></code>.
Rendering <code>sdk.mapview.TruckProfile</code>: <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9truckTypeAA0bE0Ovp">TruckSpecifications.truckType</a></code> is ignored and has no effect.</li>
<li>isTruckLight: A flag indicating whether the truck is light enough to be classified more as a car than a truck in Japan.
The flag should not be set to <code>true</code> in other countries than Japan. The flag defaults to <code>false</code>.</li>
</ul>
<p>A light truck exempts from many legal restrictions for normal trucks in Japan, for example, which streets
  the vehicle can access, which access restrictions apply, and which speed limits are applicable.
  Restrictions related to the dimensions of the truck, or its cargo may still apply and setting this flag will
  not always overwrite these settings: Make sure to not exceed the specifications that classify a truck as light.</p>
<p>In Japan, for light trucks the same restrictions apply as for cars. Therefore, when the flag is set to true,
  you will get, for example, the same speed limits as for cars. Make sure to set the flag only to true, when
  a vehicle matches the classification for light trucks according to the vehicle regulations in Japan.</p>
<p>When <code>TruckSpecifications</code> are set as part of <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapcontentsettings">MapContentSettings</a></code>, then this flag will be ignored and
  has no effect.</p>
<p><strong>Note:</strong>
  This flag and the concept of light trucks are supported only in Japan as beta and are considered to be
  experimental in other regions. Therefore, for now, it is recommended to use this flag only in Japan.
  Note that this is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
  Related APIs may change for new releases with a deprecation process.</p>
<ul>
<li>payloadCapacityInKilograms: Allowed payload capacity, including trailers, specified in kilograms. The provided value
must be greater then or equal to 0. By default, it is not set.</li>
<li>trailerAxleCount: Defines total number of axles across all the trailers attached to the vehicle.
This number is included in <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code>, hence <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code> must be less than <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code>
and greater than or equal to 1. <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV9axleCounts5Int32VSgvp">TruckSpecifications.axleCount</a></code> and <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV12trailerCounts5Int32VSgvp">TruckSpecifications.trailerCount</a></code> are required to specify <code><a href="../Structs/TruckSpecifications.html#/s:7heresdk19TruckSpecificationsV16trailerAxleCounts5Int32VSgvp">TruckSpecifications.trailerAxleCount</a></code>.
By default, it is not set.
Note: This parameter is currently used only for the calculation of tolls in regions where it is applicable.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">grossWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">currentWeightInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">weightPerAxleGroup</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-weightperaxlegroup">WeightPerAxleGroup</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">heightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">widthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">lengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">axleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">truckType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trucktype">TruckType</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-trucktype">TruckType</a></span><span class="o">.</span><span class="n">straight</span><span class="p">,</span> <span class="nv">isTruckLight</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">payloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">trailerAxleCount</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
