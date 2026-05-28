---
title: "ViolatedRestriction / Details"
slug: "sdk-for-ios-explore-api-reference-structs-violatedrestriction-details"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/Details"></a>
<a title="Details Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-routing">Routing</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-structs-violatedrestriction">ViolatedRestriction</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        Details Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Details</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">Details</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Optional restriction details, contains additional information depending on the specific violation, zero or more member might be set.
For example, if the vehicle violates the maximum allowed height during the trip, then the member <code>max_height_in_centimeters</code> will
be set with the maximum allowed height value.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxWeightPerAxleInKilograms"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilogramss5Int32VSgvp">maxWeightPerAxleInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted weight per axle during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxWeightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV32maxWeightPerAxleGroupInKilogramsAA03MaxhiF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxWeightPerAxleGroupInKilograms"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV32maxWeightPerAxleGroupInKilogramsAA03MaxhiF0VSgvp">maxWeightPerAxleGroupInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted weight per axle group during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxWeightPerAxleGroupInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-maxaxlegroupweight">MaxAxleGroupWeight</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV22maxHeightInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxHeightInCentimeters"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV22maxHeightInCentimeterss5Int32VSgvp">maxHeightInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted height during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">VehicleSpecification.heightInCentimeters</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxHeightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV21maxWidthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxWidthInCentimeters"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV21maxWidthInCentimeterss5Int32VSgvp">maxWidthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted width during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">VehicleSpecification.widthInCentimeters</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxWidthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV22maxLengthInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxLengthInCentimeters"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV22maxLengthInCentimeterss5Int32VSgvp">maxLengthInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted length during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">VehicleSpecification.lengthInCentimeters</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxLengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenAxleCountAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/forbiddenAxleCount"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenAxleCountAA12IntegerRangeVSgvp">forbiddenAxleCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The restriction to trucks with axles number within specified range during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>
is within this range.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">forbiddenAxleCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-integerrange">IntegerRange</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV21forbiddenTrailerCountAA12IntegerRangeVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/forbiddenTrailerCount"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV21forbiddenTrailerCountAA12IntegerRangeVSgvp">forbiddenTrailerCount</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constrains the restriction to trucks with number of trailer within specified range during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code>
is within this range.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">forbiddenTrailerCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-integerrange">IntegerRange</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenHazardousGoodsSayAA0F8MaterialOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/forbiddenHazardousGoods"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenHazardousGoodsSayAA0F8MaterialOGvp">forbiddenHazardousGoods</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">VehicleSpecification.hazardousMaterials</a></code> from
<code><a href="../../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code><a href="../../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>.
This property is the intersection of the two lists.</p>
<p><strong>Note</strong> <code>RoadSignWarning</code> events and <code>RouteViolations</code> are only given for violations that are
indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">forbiddenHazardousGoods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV17maxTunnelCategoryAA0fG0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxTunnelCategory"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV17maxTunnelCategoryAA0fG0OSgvp">maxTunnelCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tunnel category to restrict transport of specific goods during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">VehicleSpecification.tunnelCategory</a></code> from
<code><a href="../../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code><a href="../../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxTunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenTruckTypeAA0fG0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/forbiddenTruckType"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV18forbiddenTruckTypeAA0fG0OSgvp">forbiddenTruckType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This property will be set if a restriction applies to the value of <code><a href="sdk-for-ios-explore-api-reference-..-..-enums-trucktype">TruckType</a></code>
parameter used for route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use <code>forbidden_truck_category</code> instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">forbiddenTruckType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-trucktype">TruckType</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV22forbiddenTruckCategoryAA0fG0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/forbiddenTruckCategory"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV22forbiddenTruckCategoryAA0fG0OSgvp">forbiddenTruckCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This property will be set if a restriction applies to the value of <code><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckcategory">TruckCategory</a></code>
parameter used for route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">forbiddenTruckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckcategory">TruckCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenTruckRoadTypesSayAA0fG4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/forbiddenTruckRoadTypes"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV23forbiddenTruckRoadTypesSayAA0fG4TypeOGvp">forbiddenTruckRoadTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains violated restrictions for truck road types.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">forbiddenTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV20routingZoneReferenceSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routingZoneReference"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV20routingZoneReferenceSSSgvp">routingZoneReference</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the restricted routing zone reference
This property will be set if the <code><a href="../../Structs/AvoidanceOptions.html#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">AvoidanceOptions.zoneCategories</a></code> is not empty</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routingZoneReference</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV29maxPayloadCapacityInKilogramss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxPayloadCapacityInKilograms"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV29maxPayloadCapacityInKilogramss5Int32VSgvp">maxPayloadCapacityInKilograms</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted payload capacity during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">VehicleSpecification.payloadCapacityInKilograms</a></code>
exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxPayloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV8timeRuleAA04TimeF0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/timeRule"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV8timeRuleAA04TimeF0CSgvp">timeRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Time intervals during which restrictions are enforced.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-timerule">TimeRule</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV9maxWeightAA07Vehiclec3MaxF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxWeight"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV9maxWeightAA07Vehiclec3MaxF0VSgvp">maxWeight</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>
parameter used for route calculation exceeds this value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxWeight</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV16maxNumberOfTiress5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxNumberOfTires"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV16maxNumberOfTiress5Int32VSgvp">maxNumberOfTires</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the maximum permitted number of tires.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">VehicleSpecification.tiresCount</a></code> exceeds the specified value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxNumberOfTires</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV41maxKingpinToRearAxleDistanceInCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxKingpinToRearAxleDistanceInCentimeters"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV41maxKingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">maxKingpinToRearAxleDistanceInCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
This property will be set if the
<code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">VehicleSpecification.kingpinToRearAxleDistanceInCentimeters</a></code>
exceeds the specified value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxKingpinToRearAxleDistanceInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilograms0efgh5GroupiJ00e6HeightI11Centimeters0e5WidthiM00e6LengthiM009forbiddenH5Count0p7TrailerQ00P14HazardousGoods0E14TunnelCategory0p5TruckV00pW9RoadTypes20routingZoneReference0e15PayloadCapacityiJ08timeRule0eF00E13NumberOfTires0e13KingpinToRearh8DistanceiM0AEs5Int32VSg_AA03MaxhkF0VSgA3yA12IntegerRangeVSgA3_SayAA0S8MaterialOGAA0uV0OSgAA0wV0OSgSayAA0wX4TypeOGSSSgAyA8TimeRuleCSgAA07Vehiclec3MaxF0VSgA2Ytcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maxWeightPerAxleInKilograms:maxWeightPerAxleGroupInKilograms:maxHeightInCentimeters:maxWidthInCentimeters:maxLengthInCentimeters:forbiddenAxleCount:forbiddenTrailerCount:forbiddenHazardousGoods:maxTunnelCategory:forbiddenTruckCategory:forbiddenTruckRoadTypes:routingZoneReference:maxPayloadCapacityInKilograms:timeRule:maxWeight:maxNumberOfTires:maxKingpinToRearAxleDistanceInCentimeters:)"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilograms0efgh5GroupiJ00e6HeightI11Centimeters0e5WidthiM00e6LengthiM009forbiddenH5Count0p7TrailerQ00P14HazardousGoods0E14TunnelCategory0p5TruckV00pW9RoadTypes20routingZoneReference0e15PayloadCapacityiJ08timeRule0eF00E13NumberOfTires0e13KingpinToRearh8DistanceiM0AEs5Int32VSg_AA03MaxhkF0VSgA3yA12IntegerRangeVSgA3_SayAA0S8MaterialOGAA0uV0OSgAA0wV0OSgSayAA0wX4TypeOGSSSgAyA8TimeRuleCSgAA07Vehiclec3MaxF0VSgA2Ytcfc">init(maxWeightPerAxleInKilograms:<wbr/>maxWeightPerAxleGroupInKilograms:<wbr/>maxHeightInCentimeters:<wbr/>maxWidthInCentimeters:<wbr/>maxLengthInCentimeters:<wbr/>forbiddenAxleCount:<wbr/>forbiddenTrailerCount:<wbr/>forbiddenHazardousGoods:<wbr/>maxTunnelCategory:<wbr/>forbiddenTruckCategory:<wbr/>forbiddenTruckRoadTypes:<wbr/>routingZoneReference:<wbr/>maxPayloadCapacityInKilograms:<wbr/>timeRule:<wbr/>maxWeight:<wbr/>maxNumberOfTires:<wbr/>maxKingpinToRearAxleDistanceInCentimeters:<wbr/>)</a>
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
<li>maxWeightPerAxleInKilograms: Max permitted weight per axle during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code>
exceeds this value.</li>
<li>maxWeightPerAxleGroupInKilograms: Max permitted weight per axle group during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code>
exceeds this value.</li>
<li>maxHeightInCentimeters: Max permitted height during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">VehicleSpecification.heightInCentimeters</a></code>
exceeds this value.</li>
<li>maxWidthInCentimeters: Max permitted width during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">VehicleSpecification.widthInCentimeters</a></code>
exceeds this value.</li>
<li>maxLengthInCentimeters: Max permitted length during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">VehicleSpecification.lengthInCentimeters</a></code>
exceeds this value.</li>
<li>forbiddenAxleCount: The restriction to trucks with axles number within specified range during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>
is within this range.</li>
<li>forbiddenTrailerCount: Constrains the restriction to trucks with number of trailer within specified range during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code>
is within this range.</li>
<li>forbiddenHazardousGoods: There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">VehicleSpecification.hazardousMaterials</a></code> from
<code><a href="../../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code><a href="../../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>.
This property is the intersection of the two lists.</li>
</ul>
<p><strong>Note</strong> <code>RoadSignWarning</code> events and <code>RouteViolations</code> are only given for violations that are
  indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.</p>
<ul>
<li>maxTunnelCategory: Tunnel category to restrict transport of specific goods during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">VehicleSpecification.tunnelCategory</a></code> from
<code><a href="../../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code><a href="../../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>
exceeds this value.</li>
<li>forbiddenTruckCategory: This property will be set if a restriction applies to the value of <code><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckcategory">TruckCategory</a></code>
parameter used for route calculation.</li>
<li>forbiddenTruckRoadTypes: Contains violated restrictions for truck road types.</li>
<li>routingZoneReference: Contains the restricted routing zone reference
This property will be set if the <code><a href="../../Structs/AvoidanceOptions.html#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">AvoidanceOptions.zoneCategories</a></code> is not empty</li>
<li>maxPayloadCapacityInKilograms: Max permitted payload capacity during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">VehicleSpecification.payloadCapacityInKilograms</a></code>
exceeds this value.</li>
<li>timeRule: Time intervals during which restrictions are enforced.</li>
<li>maxWeight: Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>
parameter used for route calculation exceeds this value.</li>
<li>maxNumberOfTires: Contains the maximum permitted number of tires.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">VehicleSpecification.tiresCount</a></code> exceeds the specified value.</li>
<li>maxKingpinToRearAxleDistanceInCentimeters: Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
This property will be set if the
<code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">VehicleSpecification.kingpinToRearAxleDistanceInCentimeters</a></code>
exceeds the specified value.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maxWeightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxWeightPerAxleGroupInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-maxaxlegroupweight">MaxAxleGroupWeight</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxHeightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxWidthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxLengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenAxleCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTrailerCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenHazardousGoods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">maxTunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTruckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckcategory">TruckCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">routingZoneReference</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxPayloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxWeight</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxNumberOfTires</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxKingpinToRearAxleDistanceInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilograms0efgh5GroupiJ00e6HeightI11Centimeters0e5WidthiM00e6LengthiM009forbiddenH5Count0p7TrailerQ00P14HazardousGoods0E14TunnelCategory0P9TruckType0pwV00pW9RoadTypes20routingZoneReference0e15PayloadCapacityiJ08timeRule0eF00E13NumberOfTires0e13KingpinToRearh8DistanceiM0AEs5Int32VSg_AA03MaxhkF0VSgA3zA12IntegerRangeVSgA4_SayAA0S8MaterialOGAA0uV0OSgAA0wX0OSgAA0wV0OSgSayAA0wyX0OGSSSgAzA8TimeRuleCSgAA07Vehiclec3MaxF0VSgA2Ztcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maxWeightPerAxleInKilograms:maxWeightPerAxleGroupInKilograms:maxHeightInCentimeters:maxWidthInCentimeters:maxLengthInCentimeters:forbiddenAxleCount:forbiddenTrailerCount:forbiddenHazardousGoods:maxTunnelCategory:forbiddenTruckType:forbiddenTruckCategory:forbiddenTruckRoadTypes:routingZoneReference:maxPayloadCapacityInKilograms:timeRule:maxWeight:maxNumberOfTires:maxKingpinToRearAxleDistanceInCentimeters:)"></a>
<a class="token" href="#/s:7heresdk19ViolatedRestrictionV7DetailsV27maxWeightPerAxleInKilograms0efgh5GroupiJ00e6HeightI11Centimeters0e5WidthiM00e6LengthiM009forbiddenH5Count0p7TrailerQ00P14HazardousGoods0E14TunnelCategory0P9TruckType0pwV00pW9RoadTypes20routingZoneReference0e15PayloadCapacityiJ08timeRule0eF00E13NumberOfTires0e13KingpinToRearh8DistanceiM0AEs5Int32VSg_AA03MaxhkF0VSgA3zA12IntegerRangeVSgA4_SayAA0S8MaterialOGAA0uV0OSgAA0wX0OSgAA0wV0OSgSayAA0wyX0OGSSSgAzA8TimeRuleCSgAA07Vehiclec3MaxF0VSgA2Ztcfc">init(maxWeightPerAxleInKilograms:<wbr/>maxWeightPerAxleGroupInKilograms:<wbr/>maxHeightInCentimeters:<wbr/>maxWidthInCentimeters:<wbr/>maxLengthInCentimeters:<wbr/>forbiddenAxleCount:<wbr/>forbiddenTrailerCount:<wbr/>forbiddenHazardousGoods:<wbr/>maxTunnelCategory:<wbr/>forbiddenTruckType:<wbr/>forbiddenTruckCategory:<wbr/>forbiddenTruckRoadTypes:<wbr/>routingZoneReference:<wbr/>maxPayloadCapacityInKilograms:<wbr/>timeRule:<wbr/>maxWeight:<wbr/>maxNumberOfTires:<wbr/>maxKingpinToRearAxleDistanceInCentimeters:<wbr/>)</a>
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
<li>maxWeightPerAxleInKilograms: Max permitted weight per axle during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24weightPerAxleInKilogramss5Int32VSgvp">VehicleSpecification.weightPerAxleInKilograms</a></code>
exceeds this value.</li>
<li>maxWeightPerAxleGroupInKilograms: Max permitted weight per axle group during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18weightPerAxleGroupAA06WeightefG0VSgvp">VehicleSpecification.weightPerAxleGroup</a></code>
exceeds this value.</li>
<li>maxHeightInCentimeters: Max permitted height during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19heightInCentimeterss5Int32VSgvp">VehicleSpecification.heightInCentimeters</a></code>
exceeds this value.</li>
<li>maxWidthInCentimeters: Max permitted width during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18widthInCentimeterss5Int32VSgvp">VehicleSpecification.widthInCentimeters</a></code>
exceeds this value.</li>
<li>maxLengthInCentimeters: Max permitted length during the trip, in centimeters.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV19lengthInCentimeterss5Int32VSgvp">VehicleSpecification.lengthInCentimeters</a></code>
exceeds this value.</li>
<li>forbiddenAxleCount: The restriction to trucks with axles number within specified range during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9axleCounts5Int32VSgvp">VehicleSpecification.axleCount</a></code>
is within this range.</li>
<li>forbiddenTrailerCount: Constrains the restriction to trucks with number of trailer within specified range during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV12trailerCounts5Int32VSgvp">VehicleSpecification.trailerCount</a></code>
is within this range.</li>
<li>forbiddenHazardousGoods: There are two lists for our trip: Hazardous goods restrictions applied during the trip, and the list used
for the route calculation provided using <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV18hazardousMaterialsSayAA17HazardousMaterialOGvp">VehicleSpecification.hazardousMaterials</a></code> from
<code><a href="../../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code><a href="../../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>.
This property is the intersection of the two lists.</li>
</ul>
<p><strong>Note</strong> <code>RoadSignWarning</code> events and <code>RouteViolations</code> are only given for violations that are
  indicated on a road sign. Additional legal restrictions might apply when transporting hazardous materials.</p>
<ul>
<li>maxTunnelCategory: Tunnel category to restrict transport of specific goods during the trip.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV14tunnelCategoryAA06TunnelE0OSgvp">VehicleSpecification.tunnelCategory</a></code> from
<code><a href="../../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code><a href="../../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code>
exceeds this value.</li>
<li>forbiddenTruckType: This property will be set if a restriction applies to the value of <code><a href="sdk-for-ios-explore-api-reference-..-..-enums-trucktype">TruckType</a></code>
parameter used for route calculation.</li>
<li>forbiddenTruckCategory: This property will be set if a restriction applies to the value of <code><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckcategory">TruckCategory</a></code>
parameter used for route calculation.</li>
<li>forbiddenTruckRoadTypes: Contains violated restrictions for truck road types.</li>
<li>routingZoneReference: Contains the restricted routing zone reference
This property will be set if the <code><a href="../../Structs/AvoidanceOptions.html#/s:7heresdk16AvoidanceOptionsV14zoneCategoriesSayAA12ZoneCategoryOGvp">AvoidanceOptions.zoneCategories</a></code> is not empty</li>
<li>maxPayloadCapacityInKilograms: Max permitted payload capacity during the trip, in kilograms.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV26payloadCapacityInKilogramss5Int32VSgvp">VehicleSpecification.payloadCapacityInKilograms</a></code>
exceeds this value.</li>
<li>timeRule: Time intervals during which restrictions are enforced.</li>
<li>maxWeight: Max permitted weight during the trip, in kilograms, along with the specific type of maximum permitted weight restriction.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV22grossWeightInKilogramss5Int32VSgvp">VehicleSpecification.grossWeightInKilograms</a></code>
parameter used for route calculation exceeds this value.</li>
<li>maxNumberOfTires: Contains the maximum permitted number of tires.
This property will be set if the <code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV10tiresCounts5Int32VSgvp">VehicleSpecification.tiresCount</a></code> exceeds the specified value.</li>
<li>maxKingpinToRearAxleDistanceInCentimeters: Contains the maximum permitted distance from kingpin to the rear axle in centimeters.
This property will be set if the
<code><a href="../../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV38kingpinToRearAxleDistanceInCentimeterss5Int32VSgvp">VehicleSpecification.kingpinToRearAxleDistanceInCentimeters</a></code>
exceeds the specified value.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated)</span>
<span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maxWeightPerAxleInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxWeightPerAxleGroupInKilograms</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-maxaxlegroupweight">MaxAxleGroupWeight</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxHeightInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxWidthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxLengthInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenAxleCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTrailerCount</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-integerrange">IntegerRange</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenHazardousGoods</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">maxTunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTruckType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-trucktype">TruckType</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTruckCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckcategory">TruckCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">forbiddenTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">routingZoneReference</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxPayloadCapacityInKilograms</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">timeRule</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-timerule">TimeRule</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxWeight</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-vehiclerestrictionmaxweight">VehicleRestrictionMaxWeight</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxNumberOfTires</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxKingpinToRearAxleDistanceInCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
