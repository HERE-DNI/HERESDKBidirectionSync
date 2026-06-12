---
title: "RoutingEngine"
slug: "sdk-for-ios-explore-api-reference-classes-routingengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/RoutingEngine"></a>
<a title="RoutingEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-routing">Routing</a>

        RoutingEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoutingEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">RoutingEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-routingprotocol">RoutingProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">RoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the RoutingEngine to calculate a route from A to B with
a number of waypoints in between.</p>
<p>Route calculation is done asynchronously and requires an
online connection. The resulting route contains various
information such as the polyline, route length in meters,
estimated time to traverse along the route and maneuver data.</p>
<p><strong>Note:</strong> The engine does not support an unlimited number of waypoints.
The limit is defined by the HERE backend services and may change. For now,
the maximum number of waypoints should be below 200. This value may change
and it is not guaranteed to be stable. If you need to support very large lists
of waypoints, consider to import a route (see <code>importRoute()</code> method) or use
the <code>OfflineRoutingEngine</code> which supports an unlimited number of waypoints.
The <code>OfflineRoutingEngine</code> is only available for Navigate licence.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineCACyKcfc">init()</a>
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
<a name="/s:7heresdk13RoutingEngineCyAcA09SDKNativeC0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineCyAcA09SDKNativeC0CKcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of RoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<a name="/s:7heresdk13RoutingEngineC18connectionSettingsAcA0b10ConnectionE0V_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(connectionSettings:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC18connectionSettingsAcA0b10ConnectionE0V_tKcfc">init(connectionSettings:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of RoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">connectionSettings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingconnectionsettings">RoutingConnectionSettings</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>connectionSettings</em>
</code>
</td>
<td>
<div>
<p>Settings for the route calculation.</p>
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
<a name="/s:7heresdk13RoutingEngineC_18connectionSettingsAcA09SDKNativeC0C_AA0b10ConnectionE0VtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:connectionSettings:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC_18connectionSettingsAcA09SDKNativeC0C_AA0b10ConnectionE0VtKcfc">init(_:<wbr/>connectionSettings:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of RoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">connectionSettings</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingconnectionsettings">RoutingConnectionSettings</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<tr>
<td>
<code>
<em>connectionSettings</em>
</code>
</td>
<td>
<div>
<p>Settings for the route calculation.</p>
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
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:options:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
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
<p>Options describing routing options.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:carOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>carOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a car route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-caroptions">CarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>carOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for car route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:pedestrianOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>pedestrianOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a pedestrian route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">pedestrianOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-pedestrianoptions">PedestrianOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>pedestrianOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for pedestrian route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code> is
is not supported for pedestrians and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:truckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>truckOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a truck route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckoptions">TruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>truckOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for truck route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:scooterOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>scooterOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a scooter route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">scooterOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-scooteroptions">ScooterOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scooterOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for scooter route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code> is
is not supported for scooters and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:bicycleOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>bicycleOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a bicycle route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">bicycleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-bicycleoptions">BicycleOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bicycleOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for bicycle route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code> is
is not supported for bicycles and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:taxiOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>taxiOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a taxi route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">taxiOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-taxioptions">TaxiOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>taxiOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for taxi route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code> is
is not supported for taxis and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:evCarOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>evCarOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates an electric car route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evcaroptions">EVCarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evCarOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for an electric car route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:evTruckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>evTruckOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates an electic truck route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evTruckOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for an electric truck route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:busOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>busOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a bus route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">busOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-busoptions">BusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>busOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for a bus route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivatehI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:privateBusOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivatehI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>privateBusOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a private bus route from one point to another,
passing through the given waypoints in the given order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the calculate_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">privateBusOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-privatebusoptions">PrivateBusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>waypoints</em>
</code>
</td>
<td>
<div>
<p>The list of waypoints used to calculate the route.
The first element marks the starting position, the last marks the destination.
Waypoints in between are interpreted as intermediate.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>privateBusOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for a private bus route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastK8InMeters10completionAA10TaskHandle_pAA0F0C_AA8WaypointVs5Int32VAOyAA0B5ErrorOSg_SayAKGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/returnToRoute(_:startingPoint:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastK8InMeters10completionAA10TaskHandle_pAA0F0C_AA8WaypointVs5Int32VAOyAA0B5ErrorOSg_SayAKGSgtctF">returnToRoute(_:<wbr/>startingPoint:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates a new route that leads back to the original route. The part of
the original route which was already traveled by the user is ignored.</p>
<p><strong>Note:</strong> Stopover waypoints are guaranteed to be visited. Pass-through waypoints will
be ignored.
Additionally, the following route options are ignored:
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV12alternativess5Int32Vvp">RouteOptions.alternatives</a></code>, <code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV11arrivalTime10Foundation4DateVSgvp">RouteOptions.arrivalTime</a></code>, and
<code><a href="../Structs/RouteOptions.html#/s:7heresdk12RouteOptionsV16optimizationModeAA012OptimizationE0Ovp">RouteOptions.optimizationMode</a></code>.
Most route options are only applied to the newly calculated part back to the route.</p>
<p>An application may use this method to submit a new
starting point for a previously calculated route. This method tries to avoid a costly
route re-calculation as much as possible. In case returning to the route without
re-calculation is not possible, a new route is calculated, while trying to salvage
the previous route as much as possible. However, a completely new route
containing no part of the previous route is possible, too.</p>
<p>Note that this function uses only a limited amount of map data around the new origin.
Therefore, it may also work fine with temporarily cached map data. It may also copy some of the
original route data into the new route.</p>
<p>A typical use case is to await at least 3 <code>RouteDeviation</code> events before calling this method.</p>
<ul>
<li>Or alternatively, wait at least 10 seconds after getting the first deviation event.</li>
<li>On top, the user experience can be improved by checking if the vehicle has moved at least
50 meters since calling this method for the last time.</li>
<li>Optionally, it may make sense to verify if the vehicle was ever following the route by checking if
<code>RouteDeviation.lastLocationOnRoute</code> is set.</li>
</ul>
<p>Note that deviation events are sent each time a deviation is detected, i.e. for each new location
update, regardless if the location has changed or not.
More information can be found in the Developer Guide in the “Handle route deviations” section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">returnToRoute</span><span class="p">(</span><span class="n">_</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>A <code><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></code> calculated using the online or offline route engine. For the offline case, It
should not contain an indoor <code><a href="sdk-for-ios-explore-api-reference-classes-section">Section</a></code> as such routes will fail. For the online case, it
should have <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>The current location, for example, provided by a <code>RouteDeviation</code> event. The waypoint needs to be of
type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>. Otherwise, an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code>
error is generated.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>lastTraveledSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section. Traveled part of the route won’t be reused.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnLastSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint0dE7Options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVAA07RefresheJ0CyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/refreshRoute(routeHandle:startingPoint:refreshRouteOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint0dE7Options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVAA07RefresheJ0CyAA0B5ErrorOSg_SayAA0E0CGSgtctF">refreshRoute(routeHandle:<wbr/>startingPoint:<wbr/>refreshRouteOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously refreshes a previously calculated route from the provided <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>, updating
the starting point and route metadata based on <code><a href="sdk-for-ios-explore-api-reference-classes-refreshrouteoptions">RefreshRouteOptions</a></code>. The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated. If you only want to refresh the contained traffic information or retrieve updated ETA duration,
consider using <code>RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)</code> instead.</p>
<p>Calling this method will trigger a new “HERE Routing” transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the refresh_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">refreshRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">refreshRouteOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-refreshrouteoptions">RefreshRouteOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Updates the starting point of the route. It should be of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>. Otherwise,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> error is generated. Moreover, it should be very close to the
original route specified with the <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <code><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></code> items that lie behind the new starting point (i.e. the path that
was already travelled). Plus, <code><a href="../Classes/Route.html#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp">Route.lengthInMeters</a></code> and <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code>
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">RoutingError.couldNotMatchOrigin</a></code> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
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
<p>Options to refresh the route.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters0dE7Options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVSgs5Int32VSgAsA07RefresheT0CyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/refreshRoute(routeHandle:startingPoint:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:refreshRouteOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters0dE7Options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVSgs5Int32VSgAsA07RefresheT0CyAA0B5ErrorOSg_SayAA0E0CGSgtctF">refreshRoute(routeHandle:<wbr/>startingPoint:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>refreshRouteOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously refreshes a previously calculated route from the provided <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>, updating
the starting point and route metadata based on <code><a href="sdk-for-ios-explore-api-reference-classes-refreshrouteoptions">RefreshRouteOptions</a></code>. The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated. If you only want to refresh the contained traffic information, consider to use
<code>RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)</code> instead.</p>
<p>Calling this method will trigger a new “HERE Routing” transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the refresh_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">refreshRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">?,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?,</span> <span class="nv">refreshRouteOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-refreshrouteoptions">RefreshRouteOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Updates the starting point of the route. It should be of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>. Otherwise,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> error is generated. Moreover, it should be very close to the
original route specified with the <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <code><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></code> items that lie behind the new starting point (i.e. the path that
was already travelled). Plus, <code><a href="../Classes/Route.html#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp">Route.lengthInMeters</a></code> and <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code>
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">RoutingError.couldNotMatchOrigin</a></code> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>lastTraveledSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section. Traveled part of the route won’t be reused.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnLastSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
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
<p>Options to refresh the route.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters7options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVSgs5Int32VSgAsA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/refreshRoute(routeHandle:startingPoint:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:options:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters7options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVSgs5Int32VSgAsA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">refreshRoute(routeHandle:<wbr/>startingPoint:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously refreshes a previously calculated route from the provided <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>, updating
the starting point and route metadata based on <code><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></code>. The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated. If you only want to refresh the contained traffic information, consider to use
<code>RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)</code> instead.</p>
<p>Calling this method will trigger a new “HERE Routing” transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the refresh_route(﹚ methods with RefreshRouteParameters parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">refreshRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">?,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Updates the starting point of the route. It should be of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>. Otherwise,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> error is generated. Moreover, it should be very close to the
original route specified with the <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <code><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></code> items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, <code><a href="../Classes/Route.html#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp">Route.lengthInMeters</a></code> and <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code>
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">RoutingError.couldNotMatchOrigin</a></code> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>lastTraveledSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section. Traveled part of the route won’t be reused.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnLastSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Offset in meter to the last visited position on the route section defined by the last traveled section index.</p>
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
<p>The options define the vehicle and route options to calculate the route.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint7options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVAA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/refreshRoute(routeHandle:startingPoint:options:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC12refreshRoute11routeHandle13startingPoint7options10completionAA04TaskG0_pAA0eG0V_AA8WaypointVAA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">refreshRoute(routeHandle:<wbr/>startingPoint:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously refreshes a previously calculated route from the provided <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>, updating
the starting point and route metadata based on <code><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></code>. The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated. If you only want to refresh the contained traffic information, consider to use
<code>RoutingEngine.calculateTrafficOnRoute(Route, Int32, Int32, Double, CalculateTrafficOnRouteCompletionHandler)</code> instead.</p>
<p>Calling this method will trigger a new “HERE Routing” transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the refresh_route(﹚ methods with RefreshRouteParameters parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">refreshRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The route handle holding the route to be refreshed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>startingPoint</em>
</code>
</td>
<td>
<div>
<p>Updates the starting point of the route. It should be of type <code><a href="../Enums/WaypointType.html#/s:7heresdk12WaypointTypeO8stopoveryA2CmF">WaypointType.stopover</a></code>. Otherwise,
an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO16invalidParameteryA2CmF">RoutingError.invalidParameter</a></code> error is generated. Moreover, it should be very close to the
original route specified with the <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>. Since the new starting point is expected to be
along the original route, the original route geometry is used to reach the remaining waypoints. The new route
will not include the <code><a href="sdk-for-ios-explore-api-reference-structs-waypoint">Waypoint</a></code> items that lie behind the new starting point (i.e. the path that
was already traveled). Plus, <code><a href="../Classes/Route.html#/s:7heresdk5RouteC14lengthInMeterss5Int32Vvp">Route.lengthInMeters</a></code> and <code><a href="../Classes/Route.html#/s:7heresdk5RouteC8durationSdvp">Route.duration</a></code>
values are from the new starting point to the destination. If the new waypoint is too far off the original
route, the route refresh may fail and an <code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO19couldNotMatchOriginyA2CmF">RoutingError.couldNotMatchOrigin</a></code> error is triggered.
In that case, an application may decide to calculate a new route from scratch.</p>
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
<p>The options define the vehicle and route options to calculate the route.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC12refreshRoute0dE10Parameters14routingOptions10completionAA10TaskHandle_pAA07RefresheF0V_AA0bH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/refreshRoute(refreshRouteParameters:routingOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC12refreshRoute0dE10Parameters14routingOptions10completionAA10TaskHandle_pAA07RefresheF0V_AA0bH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">refreshRoute(refreshRouteParameters:<wbr/>routingOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously refreshes a previously calculated route from the provided <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code>, updating
the starting point and route metadata based on <code><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></code>. The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">refreshRoute</span><span class="p">(</span><span class="nv">refreshRouteParameters</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-refreshrouteparameters">RefreshRouteParameters</a></span><span class="p">,</span> <span class="nv">routingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>refreshRouteParameters</em>
</code>
</td>
<td>
<div>
<p>The parameters used to refresh the route</p>
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
<p>The options define the vehicle and route options used to calculate the route.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute11routeHandle07refreshE7Options10completionAA04TaskG0_pAA0eG0V_AA07RefresheI0CyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(routeHandle:refreshRouteOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute11routeHandle07refreshE7Options10completionAA04TaskG0_pAA0eG0V_AA07RefresheI0CyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(routeHandle:<wbr/>refreshRouteOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously recreates a route from the <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code> provided, i.e. refreshes a previously
calculated route, with the specified <code><a href="sdk-for-ios-explore-api-reference-classes-refreshrouteoptions">RefreshRouteOptions</a></code>.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE backend to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time. Instead, a possible use case can be to plan a route with another HERE service.
For example, a HERE REST API that allows to calculate a route on a desktop. Then this route can be transferred via the handle to a mobile device for further use with the HERE SDK.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">refreshRouteOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-refreshrouteoptions">RefreshRouteOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The route handle holding the route to be refreshed.</p>
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
<p>The options define the vehicle and route options to calculate the route.
<strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.ElectricVehicleOptions.ensure_reachability] option is set to <code>true</code>.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10carOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA03CarH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:carOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10carOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA03CarH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>carOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-caroptions">CarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>carOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for car route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops17pedestrianOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA010PedestrianJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:pedestrianOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops17pedestrianOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA010PedestrianJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>pedestrianOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">pedestrianOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-pedestrianoptions">PedestrianOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>pedestrianOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for pedestrian route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code>
is not supported for pedestrians and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops14bicycleOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07BicycleJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:bicycleOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops14bicycleOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07BicycleJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>bicycleOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">bicycleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-bicycleoptions">BicycleOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bicycleOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for bicycle route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops14scooterOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07ScooterJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:scooterOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops14scooterOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07ScooterJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>scooterOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">scooterOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-scooteroptions">ScooterOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scooterOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for scooter route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code>
is not supported for scooters and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA010PedestrianH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:pedestrianOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA010PedestrianH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>pedestrianOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a pedestrian route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">pedestrianOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-pedestrianoptions">PedestrianOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>pedestrianOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for pedestrian route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code>
is not supported for pedestrians and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07BicycleH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:bicycleOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07BicycleH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>bicycleOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a bicycle route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">bicycleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-bicycleoptions">BicycleOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bicycleOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for bicycle route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07ScooterH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:scooterOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07ScooterH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>scooterOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a scooter route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">scooterOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-scooteroptions">ScooterOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scooterOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for scooter route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code>
is not supported for scooters and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA05TruckH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:truckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA05TruckH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>truckOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckoptions">TruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>truckOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for truck route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA04TaxiH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:taxiOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA04TaxiH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>taxiOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">taxiOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-taxioptions">TaxiOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>taxiOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for taxi route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code>
is not supported for taxis and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10busOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA03BusH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:busOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10busOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA03BusH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>busOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">busOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-busoptions">BusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>busOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for bus route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07PrivatehI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:privateBusOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07PrivatehI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>privateBusOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">privateBusOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-privatebusoptions">PrivateBusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>privateBusOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for private bus route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA05EVCarI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:evCarOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA05EVCarI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>evCarOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evcaroptions">EVCarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evCarOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for an electric car route calculation, along with
common route options.
<strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.EVCarOptions.ensure_reachability] option is set to <code>true</code>.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07EVTruckI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:evTruckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8LocationVG_AA07EVTruckI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>evTruckOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evTruckOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for an electric truck route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops10carOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA03CarJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:carOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops10carOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA03CarJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>carOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a car route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-caroptions">CarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>carOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for car route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops12truckOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA05TruckJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:truckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops12truckOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA05TruckJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>truckOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a truck route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-truckoptions">TruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>truckOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for truck route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops11taxiOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA04TaxiJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:taxiOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops11taxiOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA04TaxiJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>taxiOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a taxi route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">taxiOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-taxioptions">TaxiOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>taxiOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for taxi route calculation, along with
common route options. Note that <code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO8shortestyA2CmF">OptimizationMode.shortest</a></code>
is not supported for taxis and converted to
<code><a href="../Enums/OptimizationMode.html#/s:7heresdk16OptimizationModeO7fastestyA2CmF">OptimizationMode.fastest</a></code> automatically.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops10busOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA03BusJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:busOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops10busOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA03BusJ0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>busOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a bus route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">busOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-busoptions">BusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>busOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for bus route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops17privateBusOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07PrivatejK0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:privateBusOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops17privateBusOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07PrivatejK0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>privateBusOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a private bus route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or anyway geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">privateBusOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-privatebusoptions">PrivateBusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>privateBusOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for private bus route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops12evCarOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA05EVCarK0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:evCarOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops12evCarOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA05EVCarK0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>evCarOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates an electric car route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evcaroptions">EVCarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evCarOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for an electric car route calculation, along with
common route options.
<strong>Note</strong> An [sdk.routing.RoutingError.INVALID_PARAMETER] is generated when the [sdk.routing.EVCarOptions.ensure_reachability] option is set to <code>true</code>.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops14evTruckOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07EVTruckK0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:evTruckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops14evTruckOptions10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA07EVTruckK0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>evTruckOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates an electric truck route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>evTruckOptions</em>
</code>
</td>
<td>
<div>
<p>Options specific for an electric truck route calculation, along with
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
<div>
<h4>Return Value</h4>
<p>Handle that will be used to manipulate the execution of the task.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with7options10completionAA10TaskHandle_pSayAA8LocationVG_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:options:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with7options10completionAA10TaskHandle_pSayAA8LocationVG_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
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
<p>The options define the vehicle and route options to calculate the route.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute4with10routeStops7options10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(with:routeStops:options:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute4with10routeStops7options10completionAA10TaskHandle_pSayAA8LocationVG_SayAA0E4StopVGAA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(with:<wbr/>routeStops:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously creates a route from a sequence of geographic coordinates very close to each other. The route shape will
be kept as close as possible to the one provided. For best results please use 1Hz GPS data,
or geographic coordinates that have a spacing of a few meters one from the other. For example, such a list of geographic coordinates can
be extracted from a GPX trace or a route object from a 3rd party library. Very sparse data may be rejected by the service with an error.</p>
<p><strong>Note:</strong> Any restrictions applied to a transport type or provided options will be
discarded and reported as violations in <code><a href="../Classes/Section.html#/s:7heresdk7SectionC14sectionNoticesSayAA0B6NoticeVGvp">Section.sectionNotices</a></code> .</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">locations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-location">Location</a></span><span class="p">],</span> <span class="nv">routeStops</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routestop">RouteStop</a></span><span class="p">],</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>locations</em>
</code>
</td>
<td>
<div>
<p>The list of locations used to calculate the route. Note that only the <code><a href="../Structs/Location.html#/s:7heresdk8LocationV11coordinatesAA14GeoCoordinatesVvp">Location.coordinates</a></code> of a location are used to import the route.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>routeStops</em>
</code>
</td>
<td>
<div>
<p>The list of RouteStop’s which contains index of location from locations list used for route stop and duration in seconds spent on stop.</p>
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
<p>The options define the vehicle and route options to calculate the route.</p>
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC11importRoute11routeHandle7options10completionAA04TaskG0_pAA0eG0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(routeHandle:options:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC11importRoute11routeHandle7options10completionAA04TaskG0_pAA0eG0V_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">importRoute(routeHandle:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously recreates a route from the <code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code> provided, i.e. refreshes a previously
calculated route, with the specified <code><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></code>.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>The route handle holding the route to be refreshed.</p>
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
<p>The options define the vehicle and route options to calculate the route.</p>
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
<p>Callback object that will be invoked after refreshing the route.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC23calculateTrafficOnRoute5route24lastTraveledSectionIndex016traveledDistancef4LastK8InMeters10completionAA10TaskHandle_pAA0G0C_s5Int32VAMyAA0B5ErrorOSg_AA0efG0VSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateTrafficOnRoute(route:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC23calculateTrafficOnRoute5route24lastTraveledSectionIndex016traveledDistancef4LastK8InMeters10completionAA10TaskHandle_pAA0G0C_s5Int32VAMyAA0B5ErrorOSg_AA0efG0VSgtctF">calculateTrafficOnRoute(route:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates the traffic along a route starting from the index of the last
traveled route section and an offset (in meters) from the last visited position on the
section. Call this when only the contained traffic information or the latest ETA duration
is needed. This can be called periodically to retrieve updated ETA values during navigation.</p>
<p><strong>Note:</strong> Calling this method will trigger a new “HERE Traffic” transaction, for example,
if you are using the <a href="https://www.here.com/get-started/pricing">Base Plan</a>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateTrafficOnRoute</span><span class="p">(</span><span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></span><span class="p">,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>A <code><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></code> calculated using the online routing engine. Its
<code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code> and the original route calculation options will be used to
compute the traffic on the route. The original route remains untouched.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>lastTraveledSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section. Traveled part of the route won’t
be reused.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnLastSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Offset, in meters, to the last visited position on the route section defined by the last
traveled section index.</p>
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
<p>Callback object that will be invoked after route traffic has been calculated.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC23calculateTrafficOnRoute5route24lastTraveledSectionIndex016traveledDistancef4LastK8InMeters013currentChargeP13KilowattHours10completionAA10TaskHandle_pAA0G0C_s5Int32VANSdyAA0B5ErrorOSg_AA0efG0VSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateTrafficOnRoute(route:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:currentChargeInKilowattHours:completion:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC23calculateTrafficOnRoute5route24lastTraveledSectionIndex016traveledDistancef4LastK8InMeters013currentChargeP13KilowattHours10completionAA10TaskHandle_pAA0G0C_s5Int32VANSdyAA0B5ErrorOSg_AA0efG0VSgtctF">calculateTrafficOnRoute(route:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>currentChargeInKilowattHours:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously calculates the traffic along an EV car route starting from the index of the
last traveled route section and an offset in meters from the last visited position on the
section.
The field <code><a href="../Structs/TrafficOnSpan.html#/s:7heresdk13TrafficOnSpanV26consumptionInKilowattHoursSdSgvp">TrafficOnSpan.consumptionInKilowattHours</a></code> will contain the power consumption
in kilowatt-hours (kWh) necessary to traverse the span, and
<code><a href="../Structs/RoutePlace.html#/s:7heresdk10RoutePlaceV21chargeInKilowattHoursSdSgvp">RoutePlace.chargeInKilowattHours</a></code>, inside <code><a href="../Structs/TrafficOnSection.html#/s:7heresdk16TrafficOnSectionV14departurePlaceAA05RouteF0Vvp">TrafficOnSection.departurePlace</a></code> and
<code><a href="../Structs/TrafficOnSection.html#/s:7heresdk16TrafficOnSectionV12arrivalPlaceAA05RouteF0Vvp">TrafficOnSection.arrivalPlace</a></code>, the estimated battery charge in kilowatt-hours (kWh) when
leaving/arriving to a section.
<strong>Note:</strong> Only EV cars are supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateTrafficOnRoute</span><span class="p">(</span><span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></span><span class="p">,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">currentChargeInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk40CalculateTrafficOnRouteCompletionHandlera">CalculateTrafficOnRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>A <code><a href="sdk-for-ios-explore-api-reference-classes-route">Route</a></code> calculated using the online routing engine. Its
<code><a href="sdk-for-ios-explore-api-reference-structs-routehandle">RouteHandle</a></code> and the original route calculation options, along with EV
related information like <code><a href="sdk-for-ios-explore-api-reference-structs-batteryspecifications">BatterySpecifications</a></code>, will be used to
compute the traffic on the route. The original route remains untouched.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>lastTraveledSectionIndex</em>
</code>
</td>
<td>
<div>
<p>Indicates the index of the last traveled route section. Traveled part of the route won’t
be reused.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>traveledDistanceOnLastSectionInMeters</em>
</code>
</td>
<td>
<div>
<p>Offset, in meters, to the last visited position on the route section defined by the last
traveled section index.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>currentChargeInKilowattHours</em>
</code>
</td>
<td>
<div>
<p>Charge level of the vehicle’s battery at the current location (in kWh).
It must be non-negative and less than or equal to the value of
<code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV28totalCapacityInKilowattHoursSdvp">BatterySpecifications.totalCapacityInKilowattHours</a></code>,
otherwise the <code><a href="sdk-for-ios-explore-api-reference-structs-batteryspecifications">BatterySpecifications</a></code> instance is considered invalid.
Sets <code><a href="../Structs/BatterySpecifications.html#/s:7heresdk21BatterySpecificationsV28initialChargeInKilowattHoursSdvp">BatterySpecifications.initialChargeInKilowattHours</a></code> to the given value.</p>
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
<p>Callback object that will be invoked after route traffic has been calculated.
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
<li class="item">
<div>
<code>
<a name="/s:7heresdk13RoutingEngineC15setCustomOption4name5valueAA0B5ErrorOSgSS_SSSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomOption(name:value:)"></a>
<a class="token" href="#/s:7heresdk13RoutingEngineC15setCustomOption4name5valueAA0B5ErrorOSgSS_SSSgtF">setCustomOption(name:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom option for routing backend queries.
The custom option is applied to all the queries that <code>RoutingEngine</code> performs.
For a complete list of available parameter names and their valid values, refer to
<a href="https://www.here.com/docs/bundle/routing-api-v8-api-reference/page/index.html">HERE Routing API v8</a>.
<strong>Note:</strong> It’s easy to set a wrong option that makes queries invalid,
so make sure you read and understand the backend documentation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomOption</span><span class="p">(</span><span class="nv">name</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-enums-routingerror">RoutingError</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>name</em>
</code>
</td>
<td>
<div>
<p>An option name. If the engine already has an option with the same name, the option will be overwritten. The option name must be a non-empty string.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>value</em>
</code>
</td>
<td>
<div>
<p>An option value. If the value is <code>nil</code>, the option will be removed. The option value must be a non-empty string.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>An optional error of setting the option. It’s <code>nil</code> if the option has been set successfully.
It’s <code>RoutingError.INVALID_PARAMETER</code> if the input name and/or value haven’t passed internal validation.</p>
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
