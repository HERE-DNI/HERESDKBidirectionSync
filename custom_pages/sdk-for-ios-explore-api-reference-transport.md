---
title: "Transport  Reference"
slug: "sdk-for-ios-explore-api-reference-transport"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Transport.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Section/Transport"></a>
<a title="Transport  Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="img/carat.png"/>
        Transport  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-busspecifications">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.")
public struct BusSpecifications : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-carspecifications">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.")
public struct CarSpecifications : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-generalvehiclespeedlimits">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct GeneralVehicleSpeedLimits : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-pedestrianspecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct PedestrianSpecification : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-scooterspecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct ScooterSpecification : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-taxispecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct TaxiSpecification : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-transportmode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum TransportMode : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-transportspecification">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct TransportSpecification : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-truckcategory">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum TruckCategory : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-truckclass">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum TruckClass : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-truckroadtype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum TruckRoadType : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-truckfueltype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum TruckFuelType : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-enums-vehicletype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use <code>sdk.transport.TransportMode</code> instead.")
public enum VehicleType : UInt32, CaseIterable, Codable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-vehicleprofile">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>@available(*, deprecated, message: "Will be removed in v4.28.0. Use <code>sdk.transport.TransportSpecification</code> instead.")
public struct VehicleProfile : Hashable</code></pre>
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
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-structs-weightperaxlegroup">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public struct WeightPerAxleGroup : Hashable</code></pre>
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
