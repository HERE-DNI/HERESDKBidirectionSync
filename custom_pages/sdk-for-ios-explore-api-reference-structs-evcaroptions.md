---
title: "EVCarOptions"
slug: "sdk-for-ios-explore-api-reference-structs-evcaroptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVCarOptions"></a>
<a title="EVCarOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        EVCarOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVCarOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use RoutingOptions class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVCarOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how a route for an electric car should be calculated.
At minimum, a valid <code><a href="sdk-for-ios-explore-api-reference-structs-evconsumptionmodel">EVConsumptionModel</a></code> must be set or the route calculation will fail.
<br/>
Note: <code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">EVCarOptions.ensureReachability</a></code> must be <code>true</code> to make sure that all stopovers are reachable. For this,
charging stations may be added to the route. If <code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">EVCarOptions.ensureReachability</a></code> is true, you need to
specify the required route options and battery specifications that include the current charge level
of the battery (<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp">BatterySpecifications.initialChargeInKilowattHours</a></code>).
See the parameter description below for more details.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV05routeC0AA05RouteC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV05routeC0AA05RouteC0Vvp">routeOptions</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV04textC0AA09RouteTextC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV04textC0AA09RouteTextC0Vvp">textOptions</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV09avoidanceC0AA09AvoidanceC0Vvp">avoidanceOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify restrictions for route calculations. By default
no restrictions are applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV04tollC0AA04TollC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollOptions"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV04tollC0AA04TollC0Vvp">tollOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Options to specify how the tolls should be calculated,
such as transponders, vehicle category, and emission type.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tollOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowOptions"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp">allowOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options explicitly allowed by user for route calculations. By default
no options are opt in.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV15occupantsNumbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/occupantsNumber"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV15occupantsNumbers5Int32Vvp">occupantsNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle’s ability to use HOV/carpool restricted lanes.
Shouldn’t be less than 1 or greater than 255. Defaults to 1.</p>
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp">EVCarOptions.allowOptions</a></code> and such lanes are available in the selected country.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">occupantsNumber</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV27lastCharacterOfLicensePlateSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastCharacterOfLicensePlate"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV27lastCharacterOfLicensePlateSSSgvp">lastCharacterOfLicensePlate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the last character of a vehicle’s license plate, typically used to
evaluate traffic restrictions in certain environmental or low-emission zones.
In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may
be restricted on certain days or in certain areas to reduce congestion and emissions.
When this value is provided, the HERE SDK considers it during route calculation to
avoid roads or areas where your vehicle may be restricted based on local regulations.
Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.</p>
<p>If this value is not set, such license plate-based restrictions are ignored, and
routing is performed without considering them.</p>
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
<a name="/s:7heresdk12EVCarOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxSpeedOnSegments"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp">maxSpeedOnSegments</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Segments with restriction on maximum <code><a href="../Structs/DynamicSpeedInfo.html#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxSpeedOnSegments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-maxspeedonsegment">MaxSpeedOnSegment</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/ensureReachability"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">ensureReachability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ensure that the vehicle does not run out of energy along the way.
Requires valid <code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp">EVCarOptions.batterySpecifications</a></code>.
It also requires that
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code> = <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code>,
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">RouteOptions.speedCapInMetersPerSecond</a></code> is not set, and
<code><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></code> is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.
<strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when
the [sdk.routing.EVCarOptions.ensure_reachability] is set to <code>true</code> in case [sdk.routing.RoutingEngine.import_route] is called.
Defaults to <code>false</code>.</p>
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
<a name="/s:7heresdk12EVCarOptionsV16consumptionModelAA013EVConsumptionE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumptionModel"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV16consumptionModelAA013EVConsumptionE0Vvp">consumptionModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Vehicle specific parameters, which are then used to calculate energy consumption
for the vehicle on a given route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">consumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evconsumptionmodel">EVConsumptionModel</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/batterySpecifications"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp">batterySpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Parameters that describe the electric vehicle’s battery.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">batterySpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-batteryspecifications">BatterySpecifications</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV17carSpecificationsAA03CarE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/carSpecifications"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV17carSpecificationsAA03CarE0Vvp">carSpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Detailed car specifications such as dimensions and weight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">carSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-carspecifications">CarSpecifications</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityfgH0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/evMobilityServiceProviderPreferences"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV36evMobilityServiceProviderPreferencesAA010EVMobilityfgH0Vvp">evMobilityServiceProviderPreferences</a>
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
By default, all providers are used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">evMobilityServiceProviderPreferences</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12EVCarOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments18ensureReachability16consumptionModel21batterySpecifications03carY036evMobilityServiceProviderPreferencesAcA05RouteC0V_AA09RouteTextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGSbAA013EVConsumptionW0VAA07BatteryY0VAA03CarY0VAA36EVMobilityServiceProviderPreferencesVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:textOptions:avoidanceOptions:tollOptions:allowOptions:occupantsNumber:lastCharacterOfLicensePlate:maxSpeedOnSegments:ensureReachability:consumptionModel:batterySpecifications:carSpecifications:evMobilityServiceProviderPreferences:)"></a>
<a class="token" href="#/s:7heresdk12EVCarOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments18ensureReachability16consumptionModel21batterySpecifications03carY036evMobilityServiceProviderPreferencesAcA05RouteC0V_AA09RouteTextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGSbAA013EVConsumptionW0VAA07BatteryY0VAA03CarY0VAA36EVMobilityServiceProviderPreferencesVtcfc">init(routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>tollOptions:<wbr/>allowOptions:<wbr/>occupantsNumber:<wbr/>lastCharacterOfLicensePlate:<wbr/>maxSpeedOnSegments:<wbr/>ensureReachability:<wbr/>consumptionModel:<wbr/>batterySpecifications:<wbr/>carSpecifications:<wbr/>evMobilityServiceProviderPreferences:<wbr/>)</a>
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
<li>routeOptions: Specifies the common route calculation options.</li>
<li>textOptions: Customize textual content returned from the route calculation, such
as localization, format, and unit system.</li>
<li>avoidanceOptions: Options to specify restrictions for route calculations. By default
no restrictions are applied.</li>
<li>tollOptions: Options to specify how the tolls should be calculated,
such as transponders, vehicle category, and emission type.</li>
<li>allowOptions: The options explicitly allowed by user for route calculations. By default
no options are opt in.</li>
<li>occupantsNumber: Specifies the number of occupants in the vehicle, including driver,
can affect the vehicle’s ability to use HOV/carpool restricted lanes.
Shouldn’t be less than 1 or greater than 255. Defaults to 1.</li>
</ul>
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV05allowC0AA05AllowC0Vvp">EVCarOptions.allowOptions</a></code> and such lanes are available in the selected country.</p>
<ul>
<li>lastCharacterOfLicensePlate: Specifies the last character of a vehicle’s license plate, typically used to
evaluate traffic restrictions in certain environmental or low-emission zones.
In cities like Bogotá, Mexico City, or Jakarta, specific license plate digits may
be restricted on certain days or in certain areas to reduce congestion and emissions.
When this value is provided, the HERE SDK considers it during route calculation to
avoid roads or areas where your vehicle may be restricted based on local regulations.
Example usage: “7”, when the license plate of a vehicle looks like “B-ET-182487”.</li>
</ul>
<p>If this value is not set, such license plate-based restrictions are ignored, and
  routing is performed without considering them.</p>
<ul>
<li>maxSpeedOnSegments: Segments with restriction on maximum <code><a href="../Structs/DynamicSpeedInfo.html#/s:7heresdk16DynamicSpeedInfoV04baseC17InMetersPerSecondSdvp">DynamicSpeedInfo.baseSpeedInMetersPerSecond</a></code>.</li>
<li>ensureReachability: Ensure that the vehicle does not run out of energy along the way.
Requires valid <code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV21batterySpecificationsAA07BatteryE0Vvp">EVCarOptions.batterySpecifications</a></code>.
It also requires that
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code> = <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code>,
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV25speedCapInMetersPerSecondSdSgvp">RouteOptions.speedCapInMetersPerSecond</a></code> is not set, and
<code><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></code> is empty. Otherwise, this object is considered invalid.
Setting this flag enables calculation of a route optimized for electric vehicles.
Charging stations may be added along the route to ensure that the vehicle does
not run out of energy along the way.
It is especially useful for longer routes, because after all, charging stations are much
less common than petrol stations.
<strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when
the [sdk.routing.EVCarOptions.ensure_reachability] is set to <code>true</code> in case [sdk.routing.RoutingEngine.import_route] is called.
Defaults to <code>false</code>.</li>
<li>consumptionModel: Vehicle specific parameters, which are then used to calculate energy consumption
for the vehicle on a given route.</li>
<li>batterySpecifications: Parameters that describe the electric vehicle’s battery.</li>
<li>carSpecifications: Detailed car specifications such as dimensions and weight.</li>
<li>evMobilityServiceProviderPreferences: Defines the preferred E-Mobility Service Providers.
The The E-Mobility Service Provider Partner Ids can be received from
<a href="https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html">https://www.here.com/docs/bundle/ev-charge-points-api-developer-guide/page/topics/resource-roamings.html</a>
An alternative way to get <code>partnerId</code> is the <code>eMobilityServiceProviders.partnerId</code> as part of <code>HERE SDK Search</code>.
Maximum number of E-Mobility Service Providers is limited to 10.
By default, all providers are used.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span><span class="p">(),</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span><span class="p">(),</span> <span class="nv">avoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span><span class="p">(),</span> <span class="nv">tollOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span><span class="p">(),</span> <span class="nv">allowOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span><span class="p">(),</span> <span class="nv">occupantsNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxSpeedOnSegments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-maxspeedonsegment">MaxSpeedOnSegment</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">ensureReachability</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">consumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evconsumptionmodel">EVConsumptionModel</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evconsumptionmodel">EVConsumptionModel</a></span><span class="p">(),</span> <span class="nv">batterySpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-batteryspecifications">BatterySpecifications</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-batteryspecifications">BatterySpecifications</a></span><span class="p">(),</span> <span class="nv">carSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-carspecifications">CarSpecifications</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-carspecifications">CarSpecifications</a></span><span class="p">(),</span> <span class="nv">evMobilityServiceProviderPreferences</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evmobilityserviceproviderpreferences">EVMobilityServiceProviderPreferences</a></span><span class="p">())</span></code></pre>
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
} </HTMLBlock>
