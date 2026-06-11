---
title: "sdk-for-ios-explore-api-reference-structs-evtruckoptions"
slug: "sdk-for-ios-explore-api-reference-structs-evtruckoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/EVTruckOptions"></a>
<a title="EVTruckOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        EVTruckOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>EVTruckOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">EVTruckOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how a route for an electric truck should be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVTruckOptionsV05routeC0AA05RouteC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV05routeC0AA05RouteC0Vvp">routeOptions</a>
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
<a name="/s:7heresdk14EVTruckOptionsV04textC0AA09RouteTextC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV04textC0AA09RouteTextC0Vvp">textOptions</a>
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
<a name="/s:7heresdk14EVTruckOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV09avoidanceC0AA09AvoidanceC0Vvp">avoidanceOptions</a>
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
<a name="/s:7heresdk14EVTruckOptionsV04tollC0AA04TollC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollOptions"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV04tollC0AA04TollC0Vvp">tollOptions</a>
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
<a name="/s:7heresdk14EVTruckOptionsV05allowC0AA05AllowC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowOptions"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV05allowC0AA05AllowC0Vvp">allowOptions</a>
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
<a name="/s:7heresdk14EVTruckOptionsV15occupantsNumbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/occupantsNumber"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV15occupantsNumbers5Int32Vvp">occupantsNumber</a>
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
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <code><a href="../Structs/EVTruckOptions.html#/s:7heresdk14EVTruckOptionsV05allowC0AA05AllowC0Vvp">EVTruckOptions.allowOptions</a></code> and such lanes are available in the selected country.</p>
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
<a name="/s:7heresdk14EVTruckOptionsV27lastCharacterOfLicensePlateSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastCharacterOfLicensePlate"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV27lastCharacterOfLicensePlateSSSgvp">lastCharacterOfLicensePlate</a>
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
<a name="/s:7heresdk14EVTruckOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxSpeedOnSegments"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp">maxSpeedOnSegments</a>
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
<a name="/s:7heresdk14EVTruckOptionsV19truckSpecificationsAA05TruckE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/truckSpecifications"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV19truckSpecificationsAA05TruckE0Vvp">truckSpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Detailed truck specifications such as dimensions and weight.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">truckSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckspecifications">TruckSpecifications</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVTruckOptionsV18linkTunnelCategoryAA0eF0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/linkTunnelCategory"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV18linkTunnelCategoryAA0eF0OSgvp">linkTunnelCategory</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-tunnelcategory">TunnelCategory</a></code> for the available options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">linkTunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVTruckOptionsV18hazardousMaterialsSayAA17HazardousMaterialOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hazardousMaterials"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV18hazardousMaterialsSayAA17HazardousMaterialOGvp">hazardousMaterials</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a list of hazardous materials shipped in the vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-hazardousmaterial">HazardousMaterial</a></code> for the available options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVTruckOptionsV21avoidedTruckRoadTypesSayAA0eF4TypeOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidedTruckRoadTypes"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV21avoidedTruckRoadTypesSayAA0eF4TypeOGvp">avoidedTruckRoadTypes</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies a list of avoided truck road types for vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></code> for the available options.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">avoidedTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14EVTruckOptionsV16consumptionModelAA013EVConsumptionE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumptionModel"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV16consumptionModelAA013EVConsumptionE0Vvp">consumptionModel</a>
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
<a name="/s:7heresdk14EVTruckOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments19truckSpecifications18linkTunnelCategory18hazardousMaterials21avoidedTruckRoadTypes16consumptionModelAcA05RouteC0V_AA09RouteTextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGAA05TruckU0VAA0wX0OSgSayAA17HazardousMaterialOGSayAA13TruckRoadTypeOGAA18EVConsumptionModelVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:textOptions:avoidanceOptions:tollOptions:allowOptions:occupantsNumber:lastCharacterOfLicensePlate:maxSpeedOnSegments:truckSpecifications:linkTunnelCategory:hazardousMaterials:avoidedTruckRoadTypes:consumptionModel:)"></a>
<a class="token" href="#/s:7heresdk14EVTruckOptionsV05routeC004textC009avoidanceC004tollC005allowC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments19truckSpecifications18linkTunnelCategory18hazardousMaterials21avoidedTruckRoadTypes16consumptionModelAcA05RouteC0V_AA09RouteTextC0VAA09AvoidanceC0VAA04TollC0VAA05AllowC0Vs5Int32VSSSgSayAA03MaxqR7SegmentVGAA05TruckU0VAA0wX0OSgSayAA17HazardousMaterialOGSayAA13TruckRoadTypeOGAA18EVConsumptionModelVtcfc">init(routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>tollOptions:<wbr/>allowOptions:<wbr/>occupantsNumber:<wbr/>lastCharacterOfLicensePlate:<wbr/>maxSpeedOnSegments:<wbr/>truckSpecifications:<wbr/>linkTunnelCategory:<wbr/>hazardousMaterials:<wbr/>avoidedTruckRoadTypes:<wbr/>consumptionModel:<wbr/>)</a>
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
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <code><a href="../Structs/EVTruckOptions.html#/s:7heresdk14EVTruckOptionsV05allowC0AA05AllowC0Vvp">EVTruckOptions.allowOptions</a></code> and such lanes are available in the selected country.</p>
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
<li>truckSpecifications: Detailed truck specifications such as dimensions and weight.</li>
<li>linkTunnelCategory: Specifies the tunnel categories to restrict certain route links.
The route will pass only through tunnels of a less strict category.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-tunnelcategory">TunnelCategory</a></code> for the available options.</li>
<li>hazardousMaterials: Specifies a list of hazardous materials shipped in the vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-hazardousmaterial">HazardousMaterial</a></code> for the available options.</li>
<li>avoidedTruckRoadTypes: Specifies a list of avoided truck road types for vehicle.
Refer to <code><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></code> for the available options.</li>
<li>consumptionModel: Vehicle specific parameters, which are then used to calculate energy consumption
for the vehicle on a given route.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span><span class="p">(),</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span><span class="p">(),</span> <span class="nv">avoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span><span class="p">(),</span> <span class="nv">tollOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span><span class="p">(),</span> <span class="nv">allowOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span><span class="p">(),</span> <span class="nv">occupantsNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxSpeedOnSegments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-maxspeedonsegment">MaxSpeedOnSegment</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">truckSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckspecifications">TruckSpecifications</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckspecifications">TruckSpecifications</a></span><span class="p">(),</span> <span class="nv">linkTunnelCategory</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-tunnelcategory">TunnelCategory</a></span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">hazardousMaterials</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-hazardousmaterial">HazardousMaterial</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">avoidedTruckRoadTypes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-truckroadtype">TruckRoadType</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">consumptionModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evconsumptionmodel">EVConsumptionModel</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evconsumptionmodel">EVConsumptionModel</a></span><span class="p">())</span></code></pre>
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
