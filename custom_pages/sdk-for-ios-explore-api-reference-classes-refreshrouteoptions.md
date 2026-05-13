---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-classes-refreshrouteoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- RefreshRouteOptions.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/RefreshRouteOptions"></a>
<a title="RefreshRouteOptions Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RefreshRouteOptions Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RefreshRouteOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>RoutingOptions</code> class instead.")</span>
<span class="kd">public</span> <span class="kd">class</span> <span class="kt">RefreshRouteOptions</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RefreshRouteOptions</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RefreshRouteOptions</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>The options to specify how to refresh an already calculated route identified by a <code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. All the
options that may result in a new route shape are ignored as no new route is calculated. Instead, only the data that
accompanies a route, such as traffic information, can be refreshed. Therefore, the following route options are ignored:
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp">RouteOptions.alternatives</a></code>, <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code>, and <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code>.
If new <code><a href="sdk-for-ios-explore-api-reference-..-structs-avoidanceoptions">AvoidanceOptions</a></code> are specified, they are ignored as well and instead new <code><a href="sdk-for-ios-explore-api-reference-..-structs-sectionnotice">SectionNotice</a></code>‘s
are generated that indicate where the requested <code><a href="sdk-for-ios-explore-api-reference-..-structs-avoidanceoptions">AvoidanceOptions</a></code> are violated. Note that when
<code><a href="../Structs/EVCarOptions.html#/s:7heresdk12EVCarOptionsV18ensureReachabilitySbvp">EVCarOptions.ensureReachability</a></code> is set to true, the route refresh request will fail as this option
is incompatible with a fixed route shape.
If any of the ignored options are important, consider calculating a new route instead.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA13TransportModeOcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA13TransportModeOcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-enums-transportmode">TransportMode</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">transportMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-transportmode">TransportMode</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>transportMode</em>
</code>
</td>
<td>
<div>
<p>Updates the transport mode for the route.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA03CarD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA03CarD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-caroptions">CarOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-caroptions">CarOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>carOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a car route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA05TruckD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA05TruckD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-truckoptions">TruckOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-truckoptions">TruckOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>truckOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a truck route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA010PedestrianD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA010PedestrianD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-pedestrianoptions">PedestrianOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">pedestrianOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-pedestrianoptions">PedestrianOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>pedestrianOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a pedestrian route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA07ScooterD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA07ScooterD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-scooteroptions">ScooterOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">scooterOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-scooteroptions">ScooterOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>scooterOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a scooter route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA04TaxiD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA04TaxiD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-taxioptions">TaxiOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">taxiOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-taxioptions">TaxiOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>taxiOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a taxi route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA05EVCarD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA05EVCarD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-evcaroptions">EVCarOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evcaroptions">EVCarOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>evCarOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to an electric car route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA07EVTruckD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA07EVTruckD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-evtruckoptions">EVTruckOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>evTruckOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to an electric truck route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA07BicycleD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA07BicycleD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-bicycleoptions">BicycleOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">bicycleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-bicycleoptions">BicycleOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>bicycleOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a bicycle route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA03BusD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA03BusD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-busoptions">BusOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">busOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-busoptions">BusOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>busOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a bus route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19RefreshRouteOptionsCyAcA010PrivateBusD0Vcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19RefreshRouteOptionsCyAcA010PrivateBusD0Vcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a RefreshRouteOptions object with <code><a href="sdk-for-ios-explore-api-reference-..-structs-privatebusoptions">PrivateBusOptions</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">privateBusOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-privatebusoptions">PrivateBusOptions</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>privateBusOptions</em>
</code>
</td>
<td>
<div>
<p>Converts the route to a private bus route, if a different transport mode was used for the
<code><a href="sdk-for-ios-explore-api-reference-..-structs-routehandle">RouteHandle</a></code>. Note that in case this is not possible,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error will be triggered.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
