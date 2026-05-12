---
title: "RoutingOptions Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-routingoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RoutingOptions.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/RoutingOptions"></a>
<a title="RoutingOptions Structure Reference"></a>
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
        RoutingOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct RoutingOptions : Hashable</code></pre>
</div>
</div>
<p>The options defines how a route should be calculated.</p>
<p>The options are used for all transport modes and engines.</p>
<p>** Electric vehicle specific requirements **
Electric vehicle consumption are estimated when at least one consumption model is defined.
Currently two models are supported:</p>
<ul>
<li>PhysicalConsumptionModel
Aside from the values in PhysicalConsumptionModel additionally these values needs to be defined:

<ul>
<li><code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV24currentWeightInKilogramss5Int32VSgvp">VehicleSpecification.currentWeightInKilograms</a></code> from <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code>
from <code><a href="../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">RoutingOptions.transportSpecification</a></code></li>
<li>Additionally <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV30currentWeightChangeInKilogramss5Int32VSgvp">Waypoint.currentWeightChangeInKilograms</a></code> can be defined.</li>
</ul></li>
<li>EmpiricalConsumptionModel</li>
</ul>
<p>By setting <code><a href="../Structs/ElectricVehicleOptions.html#/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp">ElectricVehicleOptions.ensureReachability</a></code> the <code><a href="../Classes/RoutingEngine.html">RoutingEngine</a></code> inserts additional charging stations
to reach the waypoints.
This feature requires setting the <code><a href="../Structs/BatterySpecifications.html">BatterySpecifications</a></code>.
By default a vehicle might not reach the waypoint, when the initial charge is not enough to reach all waypoints.
See the parameter description below for more details.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/transportSpecification"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV22transportSpecificationAA09TransportE0Vvp">transportSpecification</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the transport specification which contains the transport mode and the vehicle specifications
for the transport mode chosen.
<strong>Notes:</strong></p>
<ul>
<li>The transport mode <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO13publicTransityA2CmF">TransportMode.publicTransit</a></code> is not supported.</li>
<li>By default all vehicle specifications from <code>RoutingOptions.transportSpecification</code> are set to <code>nil</code> and the
<code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code> from <code>RoutingOptions.transportSpecification</code> is set to <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>.</li>
<li>A route can be calculated with only the <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code> from <code>RoutingOptions.transportSpecification</code> set.</li>
<li>It is highly recommended to define the <code><a href="../Enums/TruckCategory.html">TruckCategory</a></code> that is being used in <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV13truckCategoryAA05TruckE0OSgvp">VehicleSpecification.truckCategory</a></code> from
<code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> from <code>RoutingOptions.transportSpecification</code>, if the
<code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV13transportModeAA0bE0Ovp">TransportSpecification.transportMode</a></code> from <code>RoutingOptions.transportSpecification</code> is set to <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO5truckyA2CmF">TransportMode.truck</a></code>.</li>
<li>The <code><a href="../Structs/VehicleSpecification.html#/s:7heresdk20VehicleSpecificationV9occupancys5Int32VSgvp">VehicleSpecification.occupancy</a></code> from <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV07vehicleC0AA07VehicleC0VSgvp">TransportSpecification.vehicleSpecification</a></code> won’t have effect
if HOV and/or HOT lane usage is not allowed using <code><a href="../Structs/EVTruckOptions.html#/s:7heresdk14EVTruckOptionsV05allowC0AA05AllowC0Vvp">EVTruckOptions.allowOptions</a></code>.</li>
<li>The <code><a href="../Structs/PedestrianSpecification.html#/s:7heresdk23PedestrianSpecificationV29walkingSpeedInMetersPerSecondSdvp">PedestrianSpecification.walkingSpeedInMetersPerSecond</a></code> from <code><a href="../Structs/TransportSpecification.html#/s:7heresdk22TransportSpecificationV010pedestrianC0AA010PedestrianC0VSgvp">TransportSpecification.pedestrianSpecification</a></code>
if present, will be used by the service as the walking speed for pedestrian routing. It influences the duration of walking
along the route. The provided value must be in the range [0.5, 2.0]. When the value is outside this
range, an invalid parameter error is raised. Refer to <code><a href="../Enums/RoutingError.html">RoutingError</a></code> for details. The
default speed is 1 meter per second.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var transportSpecification: TransportSpecification</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV05routeC0AA05RouteC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV05routeC0AA05RouteC0Vvp">routeOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the common route calculation options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var routeOptions: RouteOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV04textC0AA09RouteTextC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV04textC0AA09RouteTextC0Vvp">textOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Customize textual content returned from the route calculation, such
as localization, format, and unit system.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var textOptions: RouteTextOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV09avoidanceC0AA09AvoidanceC0Vvp">avoidanceOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify restrictions for route calculations.
By default no restrictions are applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var avoidanceOptions: AvoidanceOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV05allowC0AA05AllowC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowOptions"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV05allowC0AA05AllowC0Vvp">allowOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options explicitly allowed by user for route calculations.
By default no options are opt in.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var allowOptions: AllowOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV04tollC0AA04TollC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollOptions"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV04tollC0AA04TollC0Vvp">tollOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify how the tolls should be calculated,
such as transponders, vehicle category, and emission type.
<strong>Note</strong> Not used for offline calculations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var tollOptions: TollOptions</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxSpeedOnSegments"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp">maxSpeedOnSegments</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Segments with restriction on maximum <code><a href="../Structs/DynamicSpeedInfo.html#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a></code>.
<strong>Note</strong> Not used for offline calculations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var maxSpeedOnSegments: [MaxSpeedOnSegment]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV02evC0AA015ElectricVehicleC0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evOptions"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV02evC0AA015ElectricVehicleC0VSgvp">evOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the electric vehicle (EV) related parameters to calculate the consumption and reachability.
When no EV options are defined an internal combustion engine is assumed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var evOptions: ElectricVehicleOptions?</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV22transportSpecification05routeC004textC009avoidanceC005allowC004tollC018maxSpeedOnSegments02evC0AcA09TransportE0V_AA05RouteC0VAA0q4TextC0VAA09AvoidanceC0VAA05AllowC0VAA04TollC0VSayAA03MaxlM7SegmentVGAA015ElectricVehicleC0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(transportSpecification:routeOptions:textOptions:avoidanceOptions:allowOptions:tollOptions:maxSpeedOnSegments:evOptions:)"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV22transportSpecification05routeC004textC009avoidanceC005allowC004tollC018maxSpeedOnSegments02evC0AcA09TransportE0V_AA05RouteC0VAA0q4TextC0VAA09AvoidanceC0VAA05AllowC0VAA04TollC0VSayAA03MaxlM7SegmentVGAA015ElectricVehicleC0VSgtcfc">init(transportSpecification:<wbr/>routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>allowOptions:<wbr/>tollOptions:<wbr/>maxSpeedOnSegments:<wbr/>evOptions:<wbr/>)</a>
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
<pre><code>public init(transportSpecification: TransportSpecification = TransportSpecification(), routeOptions: RouteOptions = RouteOptions(), textOptions: RouteTextOptions = RouteTextOptions(), avoidanceOptions: AvoidanceOptions = AvoidanceOptions(), allowOptions: AllowOptions = AllowOptions(), tollOptions: TollOptions = TollOptions(), maxSpeedOnSegments: [MaxSpeedOnSegment] = [], evOptions: ElectricVehicleOptions? = nil)</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14RoutingOptionsV33fromDefaultParameterConfigurationACyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fromDefaultParameterConfiguration()"></a>
<a class="token" href="#/s:7heresdk14RoutingOptionsV33fromDefaultParameterConfigurationACyFZ">fromDefaultParameterConfiguration()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the default configuration for the transport specification selected in <code><a href="../Structs/ParameterConfiguration.html#/s:7heresdk22ParameterConfigurationV22transportSpecificationAA09TransportE0Vvp">ParameterConfiguration.transportSpecification</a></code>
from <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ">SDKNativeEngine.parameterConfig</a></code>.
<strong>Note</strong> By default, the [sdk.core.ParameterConfiguration.transport_specification] from [sdk.core.engine.SDKNativeEngine.parameter_config]
will return a valid <code><a href="../Structs/TransportSpecification.html">TransportSpecification</a></code> object with the [sdk.transport.TransportSpecification.transport_mode]
set to <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO3caryA2CmF">TransportMode.car</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public static func fromDefaultParameterConfiguration() -&gt; RoutingOptions</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The <code>RoutingOptions</code> object with the default configuration for the transport specification selected in
<code><a href="../Structs/ParameterConfiguration.html#/s:7heresdk22ParameterConfigurationV22transportSpecificationAA09TransportE0Vvp">ParameterConfiguration.transportSpecification</a></code> from <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC15parameterConfigAA22ParameterConfigurationVvpZ">SDKNativeEngine.parameterConfig</a></code>.</p>
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
