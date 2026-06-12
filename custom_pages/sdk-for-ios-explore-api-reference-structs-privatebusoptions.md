---
title: "PrivateBusOptions"
slug: "sdk-for-ios-explore-api-reference-structs-privatebusoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/PrivateBusOptions"></a>
<a title="PrivateBusOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        PrivateBusOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PrivateBusOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use RoutingOptions class instead.")</span>
<span class="kd">public</span> <span class="kd">struct</span> <span class="kt">PrivateBusOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>All the options to specify how a private bus route should be calculated.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PrivateBusOptionsV05routeD0AA05RouteD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeOptions"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV05routeD0AA05RouteD0Vvp">routeOptions</a>
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
<a name="/s:7heresdk17PrivateBusOptionsV04textD0AA09RouteTextD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textOptions"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV04textD0AA09RouteTextD0Vvp">textOptions</a>
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
<a name="/s:7heresdk17PrivateBusOptionsV09avoidanceD0AA09AvoidanceD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/avoidanceOptions"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV09avoidanceD0AA09AvoidanceD0Vvp">avoidanceOptions</a>
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
<a name="/s:7heresdk17PrivateBusOptionsV04tollD0AA04TollD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tollOptions"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV04tollD0AA04TollD0Vvp">tollOptions</a>
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
<a name="/s:7heresdk17PrivateBusOptionsV05allowD0AA05AllowD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/allowOptions"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV05allowD0AA05AllowD0Vvp">allowOptions</a>
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
<a name="/s:7heresdk17PrivateBusOptionsV15occupantsNumbers5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/occupantsNumber"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV15occupantsNumbers5Int32Vvp">occupantsNumber</a>
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
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <code><a href="../Structs/PrivateBusOptions.html#/s:7heresdk17PrivateBusOptionsV05allowD0AA05AllowD0Vvp">PrivateBusOptions.allowOptions</a></code> and such lanes are available in the selected country.</p>
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
<a name="/s:7heresdk17PrivateBusOptionsV27lastCharacterOfLicensePlateSSSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastCharacterOfLicensePlate"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV27lastCharacterOfLicensePlateSSSgvp">lastCharacterOfLicensePlate</a>
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
<a name="/s:7heresdk17PrivateBusOptionsV18maxSpeedOnSegmentsSayAA03MaxfG7SegmentVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxSpeedOnSegments"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV18maxSpeedOnSegmentsSayAA03MaxfG7SegmentVGvp">maxSpeedOnSegments</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Segments with restriction on maximum baseSpeed.</p>
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
<a name="/s:7heresdk17PrivateBusOptionsV17busSpecificationsAA0cF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/busSpecifications"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV17busSpecificationsAA0cF0Vvp">busSpecifications</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Detailed bus specifications such as dimensions and weight.</p>
<p><strong>Note:</strong> Some members of <code>bus_specifications</code> have limited value range.</p>
<ul>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV22grossWeightInKilogramss5Int32VSgvp">BusSpecifications.grossWeightInKilograms</a></code> must not be negative.</li>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV19heightInCentimeterss5Int32VSgvp">BusSpecifications.heightInCentimeters</a></code> must be in the range [0, 5000].</li>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV18widthInCentimeterss5Int32VSgvp">BusSpecifications.widthInCentimeters</a></code> must be in the range [0, 5000].</li>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV19lengthInCentimeterss5Int32VSgvp">BusSpecifications.lengthInCentimeters</a></code> must be in the range [0, 30000].
The validation of the range is done in the method that takes <code>PrivateBusOptions</code> as parameter.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">busSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-busspecifications">BusSpecifications</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17PrivateBusOptionsV05routeD004textD009avoidanceD004tollD005allowD015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments17busSpecificationsAcA05RouteD0V_AA0w4TextD0VAA09AvoidanceD0VAA04TollD0VAA05AllowD0Vs5Int32VSSSgSayAA03MaxrS7SegmentVGAA0cV0Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(routeOptions:textOptions:avoidanceOptions:tollOptions:allowOptions:occupantsNumber:lastCharacterOfLicensePlate:maxSpeedOnSegments:busSpecifications:)"></a>
<a class="token" href="#/s:7heresdk17PrivateBusOptionsV05routeD004textD009avoidanceD004tollD005allowD015occupantsNumber27lastCharacterOfLicensePlate18maxSpeedOnSegments17busSpecificationsAcA05RouteD0V_AA0w4TextD0VAA09AvoidanceD0VAA04TollD0VAA05AllowD0Vs5Int32VSSSgSayAA03MaxrS7SegmentVGAA0cV0Vtcfc">init(routeOptions:<wbr/>textOptions:<wbr/>avoidanceOptions:<wbr/>tollOptions:<wbr/>allowOptions:<wbr/>occupantsNumber:<wbr/>lastCharacterOfLicensePlate:<wbr/>maxSpeedOnSegments:<wbr/>busSpecifications:<wbr/>)</a>
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
<p><strong>Note:</strong> This parameter has no effect unless HOV and/or HOT lane usage is enabled via <code><a href="../Structs/PrivateBusOptions.html#/s:7heresdk17PrivateBusOptionsV05allowD0AA05AllowD0Vvp">PrivateBusOptions.allowOptions</a></code> and such lanes are available in the selected country.</p>
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
<li>maxSpeedOnSegments: Segments with restriction on maximum baseSpeed.</li>
<li>busSpecifications: Detailed bus specifications such as dimensions and weight.</li>
</ul>
<p><strong>Note:</strong> Some members of <code>bus_specifications</code> have limited value range.</p>
<ul>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV22grossWeightInKilogramss5Int32VSgvp">BusSpecifications.grossWeightInKilograms</a></code> must not be negative.</li>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV19heightInCentimeterss5Int32VSgvp">BusSpecifications.heightInCentimeters</a></code> must be in the range [0, 5000].</li>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV18widthInCentimeterss5Int32VSgvp">BusSpecifications.widthInCentimeters</a></code> must be in the range [0, 5000].</li>
<li><code><a href="../Structs/BusSpecifications.html#/s:7heresdk17BusSpecificationsV19lengthInCentimeterss5Int32VSgvp">BusSpecifications.lengthInCentimeters</a></code> must be in the range [0, 30000].
  The validation of the range is done in the method that takes <code>PrivateBusOptions</code> as parameter.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routeoptions">RouteOptions</a></span><span class="p">(),</span> <span class="nv">textOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routetextoptions">RouteTextOptions</a></span><span class="p">(),</span> <span class="nv">avoidanceOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-avoidanceoptions">AvoidanceOptions</a></span><span class="p">(),</span> <span class="nv">tollOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-tolloptions">TollOptions</a></span><span class="p">(),</span> <span class="nv">allowOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-allowoptions">AllowOptions</a></span><span class="p">(),</span> <span class="nv">occupantsNumber</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">1</span><span class="p">,</span> <span class="nv">lastCharacterOfLicensePlate</span><span class="p">:</span> <span class="kt">String</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">maxSpeedOnSegments</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-maxspeedonsegment">MaxSpeedOnSegment</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">busSpecifications</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-busspecifications">BusSpecifications</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-busspecifications">BusSpecifications</a></span><span class="p">())</span></code></pre>
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
