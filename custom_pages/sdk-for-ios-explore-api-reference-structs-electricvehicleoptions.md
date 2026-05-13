---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-structs-electricvehicleoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ElectricVehicleOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ElectricVehicleOptions"></a>
<a title="ElectricVehicleOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        ElectricVehicleOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ElectricVehicleOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ElectricVehicleOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>These options define the parameters of the electric vehicle.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ensureReachability"></a>
<a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV18ensureReachabilitySbvp">ensureReachability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ensure that the vehicle does not run out of energy along the way.
Requires valid <code>battery_specifications</code>.
It also requires that
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code> = <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code>,
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">RouteOptions.speedCapInMetersPerSecond</a></code> is not set, and
<code><a href="sdk-for-ios-explore-api-reference-..-structs-avoidanceoptions">AvoidanceOptions</a></code> is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.</p>
<p><strong>Note</strong> An <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> is generated when
this option is set to <code>true</code> in case <code>sdk.routing.RoutingEngine.import_route</code> is called.
Defaults to <code>false</code>.</p>
<p><strong>Note</strong>
Not supported for offline routing.</p>
<p><strong>Note</strong>
Only supported for car routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">ensureReachability</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evMobilityServiceProviderPreferences"></a>
<a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityghI0Vvp">evMobilityServiceProviderPreferences</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the preferred E-Mobility Service Providers.
The The E-Mobility Service Provider Partner Ids can be received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10.
By default, all providers are used.
<strong>Note</strong> Not yet supported for offline routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evMobilityServiceProviderPreferences</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ElectricVehicleOptionsV25empiricalConsumptionModelAA09EmpiricalfG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/empiricalConsumptionModel"></a>
<a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV25empiricalConsumptionModelAA09EmpiricalfG0VSgvp">empiricalConsumptionModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the empirical consumption model.
The model is used to calculate the energy consumption for the vehicle on a given route.
<strong>Note</strong>
Only one consumption model is supported per route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">empiricalConsumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-empiricalconsumptionmodel">EmpiricalConsumptionModel</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ElectricVehicleOptionsV24physicalConsumptionModelAA08PhysicalfG0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/physicalConsumptionModel"></a>
<a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV24physicalConsumptionModelAA08PhysicalfG0VSgvp">physicalConsumptionModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the physical consumption model.
The model is used to calculate the energy consumption for the vehicle on a given route.
<strong>Note</strong>
Only one consumption model is supported per route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">physicalConsumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-physicalconsumptionmodel">PhysicalConsumptionModel</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ElectricVehicleOptionsV21batterySpecificationsAA07BatteryF0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/batterySpecifications"></a>
<a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV21batterySpecificationsAA07BatteryF0VSgvp">batterySpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parameters that describe the electric vehicle’s battery.
By default, it is set to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">batterySpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-batteryspecifications">BatterySpecifications</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22ElectricVehicleOptionsV18ensureReachability36evMobilityServiceProviderPreferences25empiricalConsumptionModel08physicalmN021batterySpecificationsACSb_AA010EVMobilityijK0VAA09EmpiricalmN0VSgAA08PhysicalmN0VSgAA07BatteryQ0VSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(ensureReachability:evMobilityServiceProviderPreferences:empiricalConsumptionModel:physicalConsumptionModel:batterySpecifications:)"></a>
<a class="token" href="#/s:7heresdk22ElectricVehicleOptionsV18ensureReachability36evMobilityServiceProviderPreferences25empiricalConsumptionModel08physicalmN021batterySpecificationsACSb_AA010EVMobilityijK0VAA09EmpiricalmN0VSgAA08PhysicalmN0VSgAA07BatteryQ0VSgtcfc">init(ensureReachability:<wbr/>evMobilityServiceProviderPreferences:<wbr/>empiricalConsumptionModel:<wbr/>physicalConsumptionModel:<wbr/>batterySpecifications:<wbr/>)</a>
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
<li>ensureReachability: Ensure that the vehicle does not run out of energy along the way.
Requires valid <code>battery_specifications</code>.
It also requires that
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code> = <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code>,
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">RouteOptions.speedCapInMetersPerSecond</a></code> is not set, and
<code><a href="sdk-for-ios-explore-api-reference-..-structs-avoidanceoptions">AvoidanceOptions</a></code> is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.</li>
</ul>
<p><strong>Note</strong> An <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> is generated when
  this option is set to <code>true</code> in case <code>sdk.routing.RoutingEngine.import_route</code> is called.
  Defaults to <code>false</code>.</p>
<p><strong>Note</strong>
  Not supported for offline routing.</p>
<p><strong>Note</strong>
  Only supported for car routing.</p>
<ul>
<li>evMobilityServiceProviderPreferences: Defines the preferred E-Mobility Service Providers.
The The E-Mobility Service Provider Partner Ids can be received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10.
By default, all providers are used.
<strong>Note</strong> Not yet supported for offline routing.</li>
<li>empiricalConsumptionModel: Defines the empirical consumption model.
The model is used to calculate the energy consumption for the vehicle on a given route.
<strong>Note</strong>
Only one consumption model is supported per route.</li>
<li>physicalConsumptionModel: Defines the physical consumption model.
The model is used to calculate the energy consumption for the vehicle on a given route.
<strong>Note</strong>
Only one consumption model is supported per route.</li>
<li>batterySpecifications: Parameters that describe the electric vehicle’s battery.
By default, it is set to <code>nil</code>.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">ensureReachability</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">evMobilityServiceProviderPreferences</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span><span class="p">(),</span> <span class="nv">empiricalConsumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-empiricalconsumptionmodel">EmpiricalConsumptionModel</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">physicalConsumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-physicalconsumptionmodel">PhysicalConsumptionModel</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">batterySpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-batteryspecifications">BatterySpecifications</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
