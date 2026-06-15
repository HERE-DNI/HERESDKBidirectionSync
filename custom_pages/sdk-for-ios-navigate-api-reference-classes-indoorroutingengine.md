---
title: "IndoorRoutingEngine"
slug: "sdk-for-ios-navigate-api-reference-classes-indoorroutingengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/IndoorRoutingEngine"></a>
<a title="IndoorRoutingEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>

        IndoorRoutingEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>IndoorRoutingEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">IndoorRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">IndoorRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the IndoorRoutingEngine to calculate a route inside a venue.
<br/>
Route calculation is done asynchronously and requires an
internet connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.
<br/>
Note: This feature is in BETA state and thus there can be bugs and unexpected behavior.
Related APIs may change for new releases without a deprecation process.
Currently, the indoor route calculation may not be accurate so that e.g. a pedestrian
end user might be routed via a vehicle access and route or similar. Therefore end users
must use this feature with caution and always be aware of the surroundings. The signs
and instructions given at the premises must be observed. You are required to inform
the end user about this in an appropriate manner, whether in the UI of your application,
your end user terms or similar.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19IndoorRoutingEngineCyAcA12VenueServiceCcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk19IndoorRoutingEngineCyAcA12VenueServiceCcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">venueService</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venueservice">VenueService</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>venueService</em>
</code>
</td>
<td>
<div>
<p>A venue service instance.</p>
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
<a name="/s:7heresdk19IndoorRoutingEngineC14calculateRoute4from2to12routeOptions10completionyAA0B8WaypointC_AjA0bfJ0VyAA0bC5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(from:to:routeOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk19IndoorRoutingEngineC14calculateRoute4from2to12routeOptions10completionyAA0B8WaypointC_AjA0bfJ0VyAA0bC5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(from:<wbr/>to:<wbr/>routeOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a route inside a venue.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="nv">from</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-indoorwaypoint">IndoorWaypoint</a></span><span class="p">,</span> <span class="nv">to</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-indoorwaypoint">IndoorWaypoint</a></span><span class="p">,</span> <span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-indoorrouteoptions">IndoorRouteOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk37CalculateIndoorRouteCompletionHandlera">CalculateIndoorRouteCompletionHandler</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>from</em>
</code>
</td>
<td>
<div>
<p>A starting position of the route to calculate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>to</em>
</code>
</td>
<td>
<div>
<p>A destination position of the route to calculate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for indoor route calculation, along with
common route options.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback object that will be invoked after route calculation.
It is always invoked on the main thread.</p>
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

`
} </HTMLBlock>
