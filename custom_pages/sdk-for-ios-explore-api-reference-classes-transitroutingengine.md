---
title: "Routing / TransitRoutingEngine"
slug: "sdk-for-ios-explore-api-reference-classes-transitroutingengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TransitRoutingEngine"></a>
<a title="TransitRoutingEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TransitRoutingEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TransitRoutingEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TransitRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TransitRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TransitRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the TransitRoutingEngine to calculate a public transit route from A to B with
a number of waypoints in between.
Route calculation is done asynchronously and requires an
online connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TransitRoutingEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk20TransitRoutingEngineCACyKcfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span> <span class="k">throws</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20TransitRoutingEngineCyAcA09SDKNativeD0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk20TransitRoutingEngineCyAcA09SDKNativeD0CKcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of TransitRoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>sdkEngine</em>
</code>
</td>
<td>
<div>
<p>An SDKEngine instance.</p>
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
<a name="/s:7heresdk20TransitRoutingEngineC14calculateRoute13startingPoint11destination12routeOptions10completionAA10TaskHandle_pAA0B8WaypointV_AkA0bfK0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(startingPoint:destination:routeOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20TransitRoutingEngineC14calculateRoute13startingPoint11destination12routeOptions10completionAA10TaskHandle_pAA0B8WaypointV_AkA0bfK0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(startingPoint:<wbr/>destination:<wbr/>routeOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a public transit route from the origin to the destination.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-transitwaypoint">TransitWaypoint</a></span><span class="p">,</span> <span class="nv">destination</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-transitwaypoint">TransitWaypoint</a></span><span class="p">,</span> <span class="nv">routeOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-transitrouteoptions">TransitRouteOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Position of starting point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>destination</em>
</code>
</td>
<td>
<div>
<p>Position of destination.</p>
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
<p>Options for public transit route calculation.</p>
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
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
