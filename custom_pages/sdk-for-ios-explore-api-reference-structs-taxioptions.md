---
title: "TaxiOptions"
slug: "sdk-for-ios-explore-api-reference-structs-taxioptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TaxiOptions"></a>
<a title="TaxiOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        TaxiOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TaxiOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use RoutingOptions class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TaxiOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how a taxi route should be calculated. See, <code><a href="../Enums/TransportMode.html#/s:7heresdk13TransportModeO4taxiyA2CmF">TransportMode.taxi</a></code>.</p>
<p><strong>Note:</strong> Specify the optional <code><a href="../Structs/Waypoint.html#/s:7heresdk8WaypointV16sideOfStreetHintAA14GeoCoordinatesVSgvp">Waypoint.sideOfStreetHint</a></code> to indicate at which side of
the street a passenger wants to leave the taxi.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TaxiOptionsV05routeC0AA05RouteC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV05routeC0AA05RouteC0Vvp">routeOptions</a>
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
<a name="/s:7heresdk11TaxiOptionsV04textC0AA09RouteTextC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV04textC0AA09RouteTextC0Vvp">textOptions</a>
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
<a name="/s:7heresdk11TaxiOptionsV09avoidanceC0AA09AvoidanceC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV09avoidanceC0AA09AvoidanceC0Vvp">avoidanceOptions</a>
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
<a name="/s:7heresdk11TaxiOptionsV04tollC0AA04TollC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollOptions"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV04tollC0AA04TollC0Vvp">tollOptions</a>
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
<a name="/s:7heresdk11TaxiOptionsV27lastCharacterOfLicensePlateSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastCharacterOfLicensePlate"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV27lastCharacterOfLicensePlateSSSgvp">lastCharacterOfLicensePlate</a>
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
<a name="/s:7heresdk11TaxiOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxSpeedOnSegments"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV18maxSpeedOnSegmentsSayAA03MaxeF7SegmentVGvp">maxSpeedOnSegments</a>
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
<a name="/s:7heresdk11TaxiOptionsV017allowDriveThroughB5RoadsSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowDriveThroughTaxiRoads"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV017allowDriveThroughB5RoadsSbvp">allowDriveThroughTaxiRoads</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies if a vehicle is allowed to drive through the taxi-only roads and lanes.
When set to <code>false</code>, it is still allowed on taxi roads after the route start and
before the route destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">allowDriveThroughTaxiRoads</span><span class="p">:</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TaxiOptionsV17carSpecificationsAA03CarE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/carSpecifications"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV17carSpecificationsAA03CarE0Vvp">carSpecifications</a>
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
<a name="/s:7heresdk11TaxiOptionsVACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsVACycfc">init()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TaxiOptionsV05routeC004textC009avoidanceC0AcA05RouteC0V_AA0g4TextC0VAA09AvoidanceC0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:textOptions:avoidanceOptions:)"></a>
<a class="token" href="#/s:7heresdk11TaxiOptionsV05routeC004textC009avoidanceC0AcA05RouteC0V_AA0g4TextC0VAA09AvoidanceC0Vtcfc">init(routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span><span class="p">,</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span><span class="p">,</span> <span class="nv">avoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span><span class="p">)</span></code></pre>
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
