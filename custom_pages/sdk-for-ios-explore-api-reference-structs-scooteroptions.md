---
title: "sdk-for-ios-explore-api-reference-structs-scooteroptions"
slug: "sdk-for-ios-explore-api-reference-structs-scooteroptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ScooterOptions"></a>
<a title="ScooterOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        ScooterOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ScooterOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use `RoutingOptions` class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ScooterOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how a scooter route should be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ScooterOptionsV05routeC0AA05RouteC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV05routeC0AA05RouteC0Vvp">routeOptions</a>
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
<a name="/s:7heresdk14ScooterOptionsV04textC0AA09RouteTextC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV04textC0AA09RouteTextC0Vvp">textOptions</a>
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
<a name="/s:7heresdk14ScooterOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV09avoidanceC0AA09AvoidanceC0Vvp">avoidanceOptions</a>
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
<a name="/s:7heresdk14ScooterOptionsV04tollC0AA04TollC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollOptions"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV04tollC0AA04TollC0Vvp">tollOptions</a>
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
<a name="/s:7heresdk14ScooterOptionsV15occupantsNumbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/occupantsNumber"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV15occupantsNumbers5Int32Vvp">occupantsNumber</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the number of occupants in the vehicle, including driver.
Shouldn’t be less than 1 or greater than 255. Defaults to 1.
This option is only relevant for Japan and will be ignored for other countries.</p>
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
<a name="/s:7heresdk14ScooterOptionsV27lastCharacterOfLicensePlateSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastCharacterOfLicensePlate"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV27lastCharacterOfLicensePlateSSSgvp">lastCharacterOfLicensePlate</a>
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
<a name="/s:7heresdk14ScooterOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxSpeedOnSegments"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp">maxSpeedOnSegments</a>
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
<a name="/s:7heresdk14ScooterOptionsV12allowHighwaySbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowHighway"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV12allowHighwaySbvp">allowHighway</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise. By default it is set to <code>false</code>.
Note that there is a similar parameter in <code><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></code>, to
disallow highway usage, see <code><a href="../Enums/RoadFeatures.html#/s:7heresdk12RoadFeaturesO23controlledAccessHighwayyA2CmF">RoadFeatures.controlledAccessHighway</a></code>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code>allowHighway</code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <code><a href="sdk-for-ios-explore-api-reference-structs-sectionnotice">SectionNotice</a></code> will be provided in the related <code><a href="sdk-for-ios-explore-api-reference-classes-section">Section</a></code>
to indicate that the highway usage restriction is violated on this route.
A few examples:</p>
<p>1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
highway usage, a notice is received.</p>
<p>2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
highway usage, no notice is received.</p>
<p>3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
highway usage, a notice is received.</p>
<p>4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
when no route is found without highway usage, a notice is received.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowHighway</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14ScooterOptionsV28engineSizeInCubicCentimeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/engineSizeInCubicCentimeters"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV28engineSizeInCubicCentimeterss5Int32VSgvp">engineSizeInCubicCentimeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value
is <code>nil</code>, which means the scooter route calculation ignores all engine size limits on the road.</p>
<p><strong>Note:</strong> For now, this option is only relevant in Japan and will be ignored
for other countries. Currently, map data for this option is only available
for Japan.</p>
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
<a name="/s:7heresdk14ScooterOptionsV05routeC004textC009avoidanceC004tollC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments12allowHighway28engineSizeInCubicCentimetersAcA05RouteC0V_AA0z4TextC0VAA09AvoidanceC0VAA04TollC0Vs5Int32VSSSgSayAA03MaxpQ7SegmentVGSbAVSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:textOptions:avoidanceOptions:tollOptions:occupantsNumber:lastCharacterOfLicensePlate:maxSpeedOnSegments:allowHighway:engineSizeInCubicCentimeters:)"></a>
<a class="token" href="#/s:7heresdk14ScooterOptionsV05routeC004textC009avoidanceC004tollC015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments12allowHighway28engineSizeInCubicCentimetersAcA05RouteC0V_AA0z4TextC0VAA09AvoidanceC0VAA04TollC0Vs5Int32VSSSgSayAA03MaxpQ7SegmentVGSbAVSgtcfc">init(routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>tollOptions:<wbr/>occupantsNumber:<wbr/>lastCharacterOfLicensePlate:<wbr/>maxSpeedOnSegments:<wbr/>allowHighway:<wbr/>engineSizeInCubicCentimeters:<wbr/>)</a>
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
<li>occupantsNumber: Specifies the number of occupants in the vehicle, including driver.
Shouldn’t be less than 1 or greater than 255. Defaults to 1.
This option is only relevant for Japan and will be ignored for other countries.</li>
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
<li>allowHighway: Specifies whether scooter is allowed on highway or not. <code>True</code> means scooter is
allowed to use highways and <code>false</code> means otherwise. By default it is set to <code>false</code>.
Note that there is a similar parameter in <code><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></code>, to
disallow highway usage, see <code><a href="../Enums/RoadFeatures.html#/s:7heresdk12RoadFeaturesO23controlledAccessHighwayyA2CmF">RoadFeatures.controlledAccessHighway</a></code>.
As the avoidance options takes precedence, if this parameter is also used, then
scooters are not allowed to use highways even if <code><a href="../Structs/ScooterOptions.html#/s:7heresdk14ScooterOptionsV12allowHighwaySbvp">allowHighway</a></code> is set to <code>true</code>.
However, if no alternative route is possible, the calculated route may use highways.
In such a case, a <code><a href="sdk-for-ios-explore-api-reference-structs-sectionnotice">SectionNotice</a></code> will be provided in the related <code><a href="sdk-for-ios-explore-api-reference-classes-section">Section</a></code>
to indicate that the highway usage restriction is violated on this route.
A few examples:</li>
</ul>
<p>1 - If no avoidance option is set, and <code>allowHighway = false</code>, when no route is found without
  highway usage, a notice is received.</p>
<p>2 - If no avoidance option is set, and <code>allowHighway = true</code>, when no route is found without
  highway usage, no notice is received.</p>
<p>3 - If only <code>avoid[features] = controlledAccessHighway</code> is set, when no route is found without
  highway usage, a notice is received.</p>
<p>4 - If both <code>avoid[features] = controlledAccessHighway</code> and <code>allowHighway = true</code> are set,
  when no route is found without highway usage, a notice is received.</p>
<ul>
<li>engineSizeInCubicCentimeters: Engine size of the scooter in cubic centimeters. Shouldn’t be less than 1 or greater than 65535. Default value
is <code>nil</code>, which means the scooter route calculation ignores all engine size limits on the road.</li>
</ul>
<p><strong>Note:</strong> For now, this option is only relevant in Japan and will be ignored
  for other countries. Currently, map data for this option is only available
  for Japan.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span><span class="p">(),</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span><span class="p">(),</span> <span class="nv">avoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span><span class="p">(),</span> <span class="nv">tollOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span><span class="p">(),</span> <span class="nv">occupantsNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxSpeedOnSegments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-maxspeedonsegment">MaxSpeedOnSegment</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">allowHighway</span><span class="p">:</span> <span class="kt">Bool</span> <span class="o">=</span> <span class="kc">false</span><span class="p">,</span> <span class="nv">engineSizeInCubicCentimeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
