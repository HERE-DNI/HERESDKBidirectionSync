---
title: "sdk-for-ios-explore-api-reference-classes-route"
slug: "sdk-for-ios-explore-api-reference-classes-route"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Route"></a>
<a title="Route Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Route Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Route</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Route</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Route</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Route</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A route is a path through a road network over which someone travels.</p>
<p><strong>Note:</strong> Each <code><a href="sdk-for-ios-explore-api-reference-..-classes-section">Section</a></code> of a route contains a list of <code><a href="sdk-for-ios-explore-api-reference-..-structs-sectionnotice">SectionNotice</a></code> objects
that describe <em>potential issues</em> after the route was calculated. If the list is non-empty,
it is recommended to evaluate possible violations against the requested route options and
reject the route if deemed necessary.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sections"></a>
<a class="token" href="#/s:7heresdk5RouteC8sectionsSayAA7SectionCGvp">sections</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The sections that make up this route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">sections</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-section">Section</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC8geometryAA11GeoPolylineVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometry"></a>
<a class="token" href="#/s:7heresdk5RouteC8geometryAA11GeoPolylineVvp">geometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-explore-api-reference-..-structs-geopolyline">GeoPolyline</a></code> object representing the polyline of this route. It may not contain the original
coordinates specified in the request for a route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geopolyline">GeoPolyline</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC11boundingBoxAA03GeoD0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk5RouteC11boundingBoxAA03GeoD0Vvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The closest rectangular area where this route fits in.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The length of this route in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC8languageAA12LanguageCodeOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/language"></a>
<a class="token" href="#/s:7heresdk5RouteC8languageAA12LanguageCodeOvp">language</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the language requested for all textual information related to this route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">language</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-languagecode">LanguageCode</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC16optimizationModeAA012OptimizationD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/optimizationMode"></a>
<a class="token" href="#/s:7heresdk5RouteC16optimizationModeAA012OptimizationD0Ovp">optimizationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The optimization mode requested for route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">optimizationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-optimizationmode">OptimizationMode</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC22requestedTransportModeAA0dE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/requestedTransportMode"></a>
<a class="token" href="#/s:7heresdk5RouteC22requestedTransportModeAA0dE0Ovp">requestedTransportMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The transport mode requested for route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">requestedTransportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transportmode">TransportMode</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC26consumptionInKilowattHoursSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumptionInKilowattHours"></a>
<a class="token" href="#/s:7heresdk5RouteC26consumptionInKilowattHoursSdSgvp">consumptionInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Estimated net energy consumption (in kWh) if the transportation mode used for this route
is an electric vehicle. Note that it can be negative due to energy recuperation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">consumptionInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC11routeHandleAA0bD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeHandle"></a>
<a class="token" href="#/s:7heresdk5RouteC11routeHandleAA0bD0VSgvp">routeHandle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The route handle of this route. Note that it is provided only if
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">RouteOptions.enableRouteHandle</a></code> is set before route calculation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk5RouteC8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated time in seconds needed to travel along this route, including
real-time traffic delays if available.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC12trafficDelaySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficDelay"></a>
<a class="token" href="#/s:7heresdk5RouteC12trafficDelaySdvp">trafficDelay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated time in seconds spent in traffic along this route. Negative values
indicate that the route can be traversed faster than usual.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficDelay</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC14routingOptionsAA07RoutingD0VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routingOptions"></a>
<a class="token" href="#/s:7heresdk5RouteC14routingOptionsAA07RoutingD0VSgvp">routingOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The set of options used to calculate the route.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">routingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routingoptions">RoutingOptions</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC16railwayCrossingsSayAA0B15RailwayCrossingVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/railwayCrossings"></a>
<a class="token" href="#/s:7heresdk5RouteC16railwayCrossingsSayAA0B15RailwayCrossingVGvp">railwayCrossings</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Collection of railway crossings along the route.
Railway crossing information is only available for routes created with the online <code><a href="sdk-for-ios-explore-api-reference-..-classes-routingengine">RoutingEngine</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">railwayCrossings</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routerailwaycrossing">RouteRailwayCrossing</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC11routeLabelsSayAA0B5LabelVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/routeLabels"></a>
<a class="token" href="#/s:7heresdk5RouteC11routeLabelsSayAA0B5LabelVGvp">routeLabels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A collection containing a maximum of 2 <code><a href="sdk-for-ios-explore-api-reference-..-structs-routelabel">RouteLabel</a></code> instances for the route. It will return an empty list if no labels are available.
The main street names or route numbers through which the route is going to pass that differentiate it from other alternatives routes.
The labels are ordered by importance based on how much time the route spends on each road segment, not by traversal sequence. This helps users quickly identify and distinguish between different route alternatives
when alternative routes have been quested via <code><a href="sdk-for-ios-explore-api-reference-..-structs-routeoptions">RouteOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">private(set)</span> <span class="kd">lazy</span> <span class="k">var</span> <span class="nv">routeLabels</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-routelabel">RouteLabel</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC9serializey10Foundation4DataVSgACFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/serialize(_:)"></a>
<a class="token" href="#/s:7heresdk5RouteC9serializey10Foundation4DataVSgACFZ">serialize(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Serializes given route to a binary data.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">serialize</span><span class="p">(</span><span class="n">_</span> <span class="nv">route</span><span class="p">:</span> <span class="kt">Route</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Data</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>route</em>
</code>
</td>
<td>
<div>
<p>The route which should be serialized.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The binary data of the route.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5RouteC11deserializeyACSg10Foundation4DataVFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/deserialize(_:)"></a>
<a class="token" href="#/s:7heresdk5RouteC11deserializeyACSg10Foundation4DataVFZ">deserialize(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates route from the given binary data.
<strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">deserialize</span><span class="p">(</span><span class="n">_</span> <span class="nv">routeData</span><span class="p">:</span> <span class="kt">Data</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Route</span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routeData</em>
</code>
</td>
<td>
<div>
<p>The binary of a serialized route.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The route object restored from the binary data.</p>
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
