---
title: "Navigation / DynamicRoutingEngine"
slug: "sdk-for-ios-navigate-api-reference-classes-dynamicroutingengine"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/DynamicRoutingEngine"></a>
<a title="DynamicRoutingEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        DynamicRoutingEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DynamicRoutingEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DynamicRoutingEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DynamicRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">DynamicRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class queries the HERE routing backend
to find routes with less traffic and therefore an earlier remaining estimated time of arrival.</p>
<p><code>DynamicRoutingEngine</code> polls the HERE routing backend periodically to find the best new route out
of a given initial route.
For initial route calculation it is recommended to use the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-routingengine">RoutingEngine</a></code>
as it already requests traffic-optimized routes.</p>
<p>When a better route is found, it is recommended to follow these steps to set the new route:</p>
<ol>
<li>Stop the <code>DynamicRoutingEngine</code>.</li>
<li>Update the currently active <code><a href="sdk-for-ios-navigate-api-reference-..-classes-navigator">Navigator</a></code>instance with the newly found route.</li>
<li>Restart the <code>DynamicRoutingEngine</code>. This should be done outside of the <code>onBetterRouteFound()</code> callback.</li>
</ol>
<p>For both <code>DynamicRoutingEngine</code> and <code><a href="sdk-for-ios-navigate-api-reference-..-classes-routingengine">RoutingEngine</a></code>,
the resulting routes are optimized based on speed flow changes such as traffic jams,
street closures or road accidents.
To get the best result, it is recommended to not specify the
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV13departureTime10Foundation4DateVSgvp">RouteOptions.departureTime</a></code> as then the current time is used by default.</p>
<p>The poll interval is defined by
<code><a href="../Structs/DynamicRoutingEngineOptions.html#/s:7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">DynamicRoutingEngineOptions.pollInterval</a></code> and
triggered by <code><a href="../Classes/DynamicRoutingEngine.html#/s:7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF">DynamicRoutingEngine.updateCurrentLocation(...)</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC14StartExceptiona"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/StartException"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC14StartExceptiona">StartException</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start exception</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">StartException</span> <span class="o">=</span> <span class="kt">DynamicRoutingEngine</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-dynamicroutingengine-starterror">StartError</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC7optionsAcA0bcD7OptionsVSg_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(options:)"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC7optionsAcA0bcD7OptionsVSg_tKcfc">init(options:<wbr/>)</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when the engine was not initialized properly.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a></span><span class="p">?)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options defining the behavior of the <code>DynamicRoutingEngine</code>.</p>
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
<a name="/s:7heresdk20DynamicRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVSgtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:options:)"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVSgtKcfc">init(_:<wbr/>options:<wbr/>)</a>
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
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when the engine was not initialized properly.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a></span><span class="p">?)</span> <span class="k">throws</span></code></pre>
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
<p>Instance of an existing SDKEngine.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>options</em>
</code>
</td>
<td>
<div>
<p>The options defining the behavior of the <code>DynamicRoutingEngine</code>.</p>
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
<a name="/s:7heresdk20DynamicRoutingEngineC10StartErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/StartError"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC10StartErrorO">StartError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start error</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-dynamicroutingengine-starterror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">StartError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-dynamicroutingengine">DynamicRoutingEngine</a></span><span class="o">.</span><span class="kt">StartError</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC5start5route8delegateyAA5RouteC_AA0bC8Delegate_ptKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(route:delegate:)"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC5start5route8delegateyAA5RouteC_AA0bC8Delegate_ptKF">start(route:<wbr/>delegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts polling the HERE backend services to find a better route,
as defined by the DynamicRoutingEngineOptions.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/DynamicRoutingEngine.html#/s:7heresdk20DynamicRoutingEngineC14StartExceptiona">DynamicRoutingEngine.StartException</a></code> when the passed parameter are invalid.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></span><span class="p">,</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<p>The route to be refreshed. The route must contain a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routehandle">RouteHandle</a></code>,
therefore the route must have been requested with
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV06enableB6HandleSbvp">RouteOptions.enableRouteHandle</a></code> set to <code>true</code>.
The information to calculate new routes will be extracted from the provided route parameter.
If more information from the original waypoints is important besides their location,
consider to use one of the overloaded methods instead.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The listener to receive the events.</p>
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
<a name="/s:7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints19refreshRouteOptions8delegateyAA0jG0V_SayAA8WaypointVGAA07RefreshjK0CAA0bC8Delegate_ptKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(routeHandle:waypoints:refreshRouteOptions:delegate:)"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints19refreshRouteOptions8delegateyAA0jG0V_SayAA8WaypointVGAA07RefreshjK0CAA0bC8Delegate_ptKF">start(routeHandle:<wbr/>waypoints:<wbr/>refreshRouteOptions:<wbr/>delegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts polling the HERE backend services to find a better route,
as defined by the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a></code>.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/DynamicRoutingEngine.html#/s:7heresdk20DynamicRoutingEngineC14StartExceptiona">DynamicRoutingEngine.StartException</a></code> when the passed parameter are invalid.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>start(﹚</code> method with RoutingOptions parameter instead.")</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">refreshRouteOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-refreshrouteoptions">RefreshRouteOptions</a></span><span class="p">,</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routeHandle</em>
</code>
</td>
<td>
<div>
<p>The route handle from the HERE routing backend.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>Allows to specify detailed information on the waypoints of the route.
This parameter can be useful, when additional information needs to be
specified besides the coordinates - as the coordinates can be retrieved
from the contained <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routeplace">RoutePlace</a></code> that are already contained in
the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routehandle">RouteHandle</a></code> parameter.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>refreshRouteOptions</em>
</code>
</td>
<td>
<div>
<p>The options for the route calculation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The listener to receive the events.</p>
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
<a name="/s:7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints14routingOptions8delegateyAA05RouteG0V_SayAA8WaypointVGAA0cJ0VAA0bC8Delegate_ptKF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/start(routeHandle:waypoints:routingOptions:delegate:)"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC5start11routeHandle9waypoints14routingOptions8delegateyAA05RouteG0V_SayAA8WaypointVGAA0cJ0VAA0bC8Delegate_ptKF">start(routeHandle:<wbr/>waypoints:<wbr/>routingOptions:<wbr/>delegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts polling the HERE backend services to find a better route,
as defined by the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-dynamicroutingengineoptions">DynamicRoutingEngineOptions</a></code>.</p>
<p><strong>Note:</strong> The engine will be internally stopped, if it was started before.
Therefore, it is not necessary to stop the engine before starting it again.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/DynamicRoutingEngine.html#/s:7heresdk20DynamicRoutingEngineC14StartExceptiona">DynamicRoutingEngine.StartException</a></code> when the passed parameter are invalid.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">start</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">routingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">delegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-dynamicroutingdelegate">DynamicRoutingDelegate</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>routeHandle</em>
</code>
</td>
<td>
<div>
<p>The route handle from the HERE routing backend.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>Allows to specify detailed information on the waypoints of the route.
This parameter can be useful, when additional information needs to be
specified besides the coordinates - as the coordinates can be retrieved
from the contained <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routeplace">RoutePlace</a></code> that are already contained in
the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routehandle">RouteHandle</a></code> parameter.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routingOptions</em>
</code>
</td>
<td>
<div>
<p>The options for the route calculation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>delegate</em>
</code>
</td>
<td>
<div>
<p>The listener to receive the events.</p>
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
<a name="/s:7heresdk20DynamicRoutingEngineC4stopyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/stop()"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC4stopyyF">stop()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Stops polling the HERE backend services.</p>
<p><strong>Note:</strong> The engine is not automatically stopped when the destination is reached.
Therefore, it is recommended to stop the engine when the destination was reached.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">stop</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/updateCurrentLocation(mapMatchedLocation:sectionIndex:)"></a>
<a class="token" href="#/s:7heresdk20DynamicRoutingEngineC21updateCurrentLocation010mapMatchedG012sectionIndexyAA03MapiG0V_s5Int32VtF">updateCurrentLocation(mapMatchedLocation:<wbr/>sectionIndex:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Updates the current location. This location will be used as new starting point when the next
<code><a href="../Structs/DynamicRoutingEngineOptions.html#/s:7heresdk27DynamicRoutingEngineOptionsV12pollIntervalSdvp">DynamicRoutingEngineOptions.pollInterval</a></code> is reached and a new route is requested.
If an immediate route update is needed, consider to use the RoutingEngine instead.
All subsequently calculated routes used for the ETA calculation will start from this location.
The location needs to lie on the route or a <code><a href="sdk-for-ios-navigate-api-reference-..-enums-routingerror">RoutingError</a></code> will be issued.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">updateCurrentLocation</span><span class="p">(</span><span class="nv">mapMatchedLocation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-mapmatchedlocation">MapMatchedLocation</a></span><span class="p">,</span> <span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapMatchedLocation</em>
</code>
</td>
<td>
<div>
<p>The last known location.
It is recommended to use a <code><a href="../Structs/NavigableLocation.html#/s:7heresdk17NavigableLocationV010mapMatchedC0AA03MapeC0VSgvp">NavigableLocation.mapMatchedLocation</a></code>
as the driver is expected to be on a road.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>sectionIndex</em>
</code>
</td>
<td>
<div>
<p>The current section from <code><a href="../Structs/RouteProgress.html#/s:7heresdk13RouteProgressV12sectionIndexs5Int32Vvp">RouteProgress.sectionIndex</a></code>.</p>
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
}</HTMLBlock>
