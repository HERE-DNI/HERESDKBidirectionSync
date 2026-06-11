---
title: "sdk-for-ios-navigate-api-reference-transport"
slug: "sdk-for-ios-navigate-api-reference-transport"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/Transport"></a>
<a title="Transport  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
        Transport  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Transport</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17BusSpecificationsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/BusSpecifications"></a>
<a class="token" href="#/s:7heresdk17BusSpecificationsV">BusSpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Bus specifications contain vehicle related attributes. Examples: height, weight, width.
Only the fields that are set are considered for restriction handling.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-busspecifications">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use TransportSpecification instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">BusSpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17CarSpecificationsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/CarSpecifications"></a>
<a class="token" href="#/s:7heresdk17CarSpecificationsV">CarSpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count.
Only the fields that are set are considered for restriction handling.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-carspecifications">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use TransportSpecification instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">CarSpecifications</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25GeneralVehicleSpeedLimitsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeneralVehicleSpeedLimits"></a>
<a class="token" href="#/s:7heresdk25GeneralVehicleSpeedLimitsV">GeneralVehicleSpeedLimits</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains the speed limits for vehicles in a country / state.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-generalvehiclespeedlimits">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeneralVehicleSpeedLimits</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28HazardousMaterialRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/HazardousMaterialRestriction"></a>
<a class="token" href="#/s:7heresdk28HazardousMaterialRestrictionV">HazardousMaterialRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents restriction on transport of hazardous materials.
A generic restriction, applying to any hazardous material, is encoded with empty member
variables.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-hazardousmaterialrestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">HazardousMaterialRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23PedestrianSpecificationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PedestrianSpecification"></a>
<a class="token" href="#/s:7heresdk23PedestrianSpecificationV">PedestrianSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Pedestrian specific settings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-pedestrianspecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PedestrianSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RestrictionTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/RestrictionType"></a>
<a class="token" href="#/s:7heresdk15RestrictionTypeO">RestrictionType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Type of vehicle restriction.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-restrictiontype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">RestrictionType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20ScooterSpecificationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ScooterSpecification"></a>
<a class="token" href="#/s:7heresdk20ScooterSpecificationV">ScooterSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Scooter specific settings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-scooterspecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScooterSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19SpecificRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpecificRestriction"></a>
<a class="token" href="#/s:7heresdk19SpecificRestrictionV">SpecificRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a specific vehicle restriction.
A <code>SpecificRestriction</code> defines what type of restriction applies (weight, height, etc.)
and the range of allowed values. It is always used as part of a <code><a href="sdk-for-ios-navigate-api-reference-structs-vehiclerestriction">VehicleRestriction</a></code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-specificrestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpecificRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TaxiSpecificationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TaxiSpecification"></a>
<a class="token" href="#/s:7heresdk17TaxiSpecificationV">TaxiSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Taxi specific settings.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-taxispecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TaxiSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TimeRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TimeRestriction"></a>
<a class="token" href="#/s:7heresdk15TimeRestrictionV">TimeRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents restriction based on time.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-timerestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TimeRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportModeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TransportMode"></a>
<a class="token" href="#/s:7heresdk13TransportModeO">TransportMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the mode of transport used for route calculalation.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-transportmode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransportMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TransportSpecificationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TransportSpecification"></a>
<a class="token" href="#/s:7heresdk22TransportSpecificationV">TransportSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Contains transport attributes details related to the transport mode.
<strong>Notes</strong></p>
<ul>
<li>By default all vehicle specifications from <code>RoutingOptions.transport_specification</code> are set to
<code>nil</code> and the <code>RoutingOptions.transport_specification.transport_mode</code> is set to <code><a href="Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>.</li>
<li>A route can be calculated with only the <code>RoutingOptions.transport_specification.transport_mode</code> set.</li>
</ul>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-transportspecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TransportSpecification</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TransportTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TransportType"></a>
<a class="token" href="#/s:7heresdk13TransportTypeO">TransportType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies types of transportation for which access/restriction rules apply.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-transporttype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TransportType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TruckCategoryO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TruckCategory"></a>
<a class="token" href="#/s:7heresdk13TruckCategoryO">TruckCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the truck category.
<strong>Note:</strong> This is a <strong>beta release</strong> of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-truckcategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TruckCategory</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10TruckClassO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TruckClass"></a>
<a class="token" href="#/s:7heresdk10TruckClassO">TruckClass</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines truck class based on weight.
Note: This is a BETA feature and thus subject to change.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-truckclass">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TruckClass</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TruckRoadTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TruckRoadType"></a>
<a class="token" href="#/s:7heresdk13TruckRoadTypeO">TruckRoadType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies Truck road type</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-truckroadtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TruckRoadType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TruckFuelTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TruckFuelType"></a>
<a class="token" href="#/s:7heresdk13TruckFuelTypeO">TruckFuelType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Define possible fuel types for trucks provided by a fuel station.
Note: This is a BETA feature and thus subject to change.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-truckfueltype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TruckFuelType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18VehicleRestrictionV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleRestriction"></a>
<a class="token" href="#/s:7heresdk18VehicleRestrictionV">VehicleRestriction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a vehicle restriction.</p>
<p>Any non <code>nil</code> property adds more details to the restriction.
A general truck restriction is represented with <code>nil</code> values for
properties <code>restriction</code> and
<code>hazmatRestriction</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-vehiclerestriction">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleRestriction</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11VehicleTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/VehicleType"></a>
<a class="token" href="#/s:7heresdk11VehicleTypeO">VehicleType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the type of the vehicle.</p>
<p><strong>Note:</strong> This is a beta release of this vehicle type, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases or even become unsupported, without a
deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-enums-vehicletype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use sdk.transport.TransportMode instead.")</span>
<span class="kd">public</span> <span class="kd">enum</span> <span class="kt">VehicleType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14VehicleProfileV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/VehicleProfile"></a>
<a class="token" href="#/s:7heresdk14VehicleProfileV">VehicleProfile</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A vehicle profile describes the vehicle being used with the HSDK.</p>
<p>The profile is planned to be used as single source of information describing the vehicle.</p>
<p>Current modules that use this profile:</p>
<ul>
<li>Navigation: Tracking mode for truck related vehicle restrictions.</li>
</ul>
<p><strong>Note:</strong> This is a beta release of this vehicle profile, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases or even become unsupported, without a
deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-vehicleprofile">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use sdk.transport.TransportSpecification instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">VehicleProfile</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18WeightPerAxleGroupV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/WeightPerAxleGroup"></a>
<a class="token" href="#/s:7heresdk18WeightPerAxleGroupV">WeightPerAxleGroup</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Struct which defines the weight of the different axle groups of a vehicle.
The provided value must be greater or equal to 0.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-structs-weightperaxlegroup">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">WeightPerAxleGroup</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
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
