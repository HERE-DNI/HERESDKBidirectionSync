---
title: "OfflineRoutingEngine"
slug: "sdk-for-ios-navigate-classes-offlineroutingengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/OfflineRoutingEngine"></a>
<a title="OfflineRoutingEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-routing">Routing</a>

        OfflineRoutingEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>OfflineRoutingEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">OfflineRoutingEngine</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-routingprotocol">RoutingProtocol</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineRoutingEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">OfflineRoutingEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use this class to calculate a route offline from A to B with
a number of waypoints in between.</p>
<p>Route calculation is done asynchronously, and requires map data that is
available offline. This can be temporarily cached map data or downloaded
offline map data stored in the persisted storage via <code><a href="sdk-for-ios-navigate-classes-mapdownloader">MapDownloader</a></code>.
Note that when using the cache there is a risk of missing data and this may
reduce the overall quality of the route or can result in a
<code><a href="../Enums/RoutingError.html#/s:7heresdk12RoutingErrorO12noRouteFoundyA2CmF">RoutingError.noRouteFound</a></code> error.</p>
<p>The resulting route contains various information such as the polyline,
route length in meters, estimated time to traverse along the route
and maneuver data, but it does not contain traffic information.</p>
<p>Unlike the <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code> (which requires an online connection), this engine
allows to use an unlimited number of waypoints.</p>
<p>As an alternative to this engine, consider to use the <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code> for online
route calculations to get fresher traffic, maneuver, route handles and street
information, and to use a more elaborate algorithms to calculate the fastest route.</p>
<p>For offline bus routing, enable “OFFLINE_BUS_ROUTING” as feature configuration.
For more details, please look at <code><a href="sdk-for-ios-navigate-structs-sdkoptions">SDKOptions</a></code>. If this feature is not
enabled, the engine may not be able to find bus routes.</p>
<p><strong>Note:</strong> EV routing is available when calculating a route using the <code><a href="sdk-for-ios-navigate-structs-routingoptions">RoutingOptions</a></code>, by setting
the <code><a href="../Structs/RoutingOptions.html#/s:7heresdk14RoutingOptionsV02evC0AA015ElectricVehicleC0VSgvp">RoutingOptions.evOptions</a></code>.</p>
<p><strong>Note:</strong> Traffic related information is completely excluded.
No historic traffic patterns are taking into consideration for the ETA.
Currently blocked or closed roads or roads with traffic incident are not considered offline, i.e.
the road may pass through such road.
Only seasonal road closures are considered based on the departure time, if given.
Traffic information is only considered for online route calculation with the <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code>.</p>
<p><strong>Note:</strong> Route handles produced by this engine are not compatible with those created by
the <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code>. Importing, refreshing, or returning to a route via a route
handle is supported only when the route was calculated with the same engine. However,
this engine supports returning to a route calculated with the <code><a href="sdk-for-ios-navigate-classes-routingengine">RoutingEngine</a></code> when
the route object is provided.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20OfflineRoutingEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineCACyKcfc">init()</a>
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
<a name="/s:7heresdk20OfflineRoutingEngineCyAcA09SDKNativeD0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineCyAcA09SDKNativeD0CKcfc">init(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of OfflineRoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:options:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC_7optionsAcA09SDKNativeD0C_AA0bcD7OptionsVtKcfc">init(_:<wbr/>options:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of OfflineRoutingEngine.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Indicates what went wrong when the instantiation was attempted.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">_</span> <span class="nv">sdkEngine</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-sdknativeengine">SDKNativeEngine</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-offlineroutingengineoptions">OfflineRoutingEngineOptions</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<em>options</em>
</code>
</td>
<td>
<div>
<p>Options to configure offline routing engine.</p>
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
<a name="/s:7heresdk20OfflineRoutingEngineC19trafficDataProviderAA07TrafficfG0CSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficDataProvider"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC19trafficDataProviderAA07TrafficfG0CSgvp">trafficDataProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traffic data provider that gets internal traffic information considering in routing.
If the traffic data provider is <code>nil</code>, traffic is not considered in routing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficDataProvider</span><span class="p">:</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:options:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:carOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>carOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-caroptions">CarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:pedestrianOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>pedestrianOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">pedestrianOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-pedestrianoptions">PedestrianOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:truckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>truckOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-truckoptions">TruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:scooterOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>scooterOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">scooterOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-scooteroptions">ScooterOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:bicycleOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>bicycleOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">bicycleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-bicycleoptions">BicycleOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:taxiOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>taxiOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">taxiOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-taxioptions">TaxiOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:evCarOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>evCarOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-evcaroptions">EVCarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:evTruckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>evTruckOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:busOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>busOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">busOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-busoptions">BusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivateiJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:privateBusOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivateiJ0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">calculateRoute(with:<wbr/>privateBusOptions:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">privateBusOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-privatebusoptions">PrivateBusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters10completionAA10TaskHandle_pAA0G0C_AA8WaypointVs5Int32VAOyAA0C5ErrorOSg_SayAKGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/returnToRoute(_:startingPoint:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastL8InMeters10completionAA10TaskHandle_pAA0G0C_AA8WaypointVs5Int32VAOyAA0C5ErrorOSg_SayAKGSgtctF">returnToRoute(_:<wbr/>startingPoint:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>completion:<wbr/>)</a>
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
<p>A typical use case is to await at least 3 <code><a href="sdk-for-ios-navigate-structs-routedeviation">RouteDeviation</a></code> events before calling this method.</p>
<ul>
<li>Or alternatively, wait at least 10 seconds after getting the first deviation event.</li>
<li>On top, the user experience can be improved by checking if the vehicle has moved at least
50 meters since calling this method for the last time.</li>
<li>Optionally, it may make sense to verify if the vehicle was ever following the route by checking if
<code><a href="../Structs/RouteDeviation.html#/s:7heresdk14RouteDeviationV014lastLocationOnB0AA09NavigableE0VSgvp">RouteDeviation.lastLocationOnRoute</a></code> is set.</li>
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
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">returnToRoute</span><span class="p">(</span><span class="n">_</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-route">Route</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>A <code><a href="sdk-for-ios-navigate-classes-route">Route</a></code> calculated using the online or offline route engine. For the offline case, It
should not contain an indoor <code><a href="sdk-for-ios-navigate-classes-section">Section</a></code> as such routes will fail. For the online case, it
should have <code><a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a></code>.</p>
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
<p>The current location, for example, provided by a <code><a href="sdk-for-ios-navigate-structs-routedeviation">RouteDeviation</a></code> event. The waypoint needs to be of
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
<a name="/s:7heresdk20OfflineRoutingEngineC12refreshRoute0eF10Parameters14routingOptions10completionAA10TaskHandle_pAA07RefreshfG0V_AA0cI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/refreshRoute(refreshRouteParameters:routingOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC12refreshRoute0eF10Parameters14routingOptions10completionAA10TaskHandle_pAA07RefreshfG0V_AA0cI0VyAA0C5ErrorOSg_SayAA0F0CGSgtctF">refreshRoute(refreshRouteParameters:<wbr/>routingOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously refreshes a previously calculated route from the provided <code><a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a></code>, updating
the starting point and route metadata based on <code><a href="sdk-for-ios-navigate-structs-routingoptions">RoutingOptions</a></code>. The route shape from the new
starting point to the destination remains unchanged, and only metadata such as arrival time and traffic
delays are updated.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">refreshRoute</span><span class="p">(</span><span class="nv">refreshRouteParameters</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-refreshrouteparameters">RefreshRouteParameters</a></span><span class="p">,</span> <span class="nv">routingOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk20OfflineRoutingEngineC11importRoute11routeHandle07refreshF7Options10completionAA04TaskH0_pAA0fH0V_AA07RefreshfJ0CyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(routeHandle:refreshRouteOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC11importRoute11routeHandle07refreshF7Options10completionAA04TaskH0_pAA0fH0V_AA07RefreshfJ0CyAA0C5ErrorOSg_SayAA0F0CGSgtctF">importRoute(routeHandle:<wbr/>refreshRouteOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously recreates a route from the <code><a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a></code> provided, i.e. refreshes a previously
calculated route, with the specified <code><a href="sdk-for-ios-navigate-classes-refreshrouteoptions">RefreshRouteOptions</a></code>.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the import_route(﹚ method with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">refreshRouteOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-refreshrouteoptions">RefreshRouteOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>Options to import the route from handle.</p>
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
<a name="/s:7heresdk20OfflineRoutingEngineC11importRoute11routeHandle7options10completionAA04TaskH0_pAA0fH0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/importRoute(routeHandle:options:completion:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC11importRoute11routeHandle7options10completionAA04TaskH0_pAA0fH0V_AA0C7OptionsVyAA0C5ErrorOSg_SayAA0F0CGSgtctF">importRoute(routeHandle:<wbr/>options:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously recreates a route from the <code><a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a></code> provided, i.e. refreshes a previously
calculated route, with the specified <code><a href="sdk-for-ios-navigate-classes-refreshrouteoptions">RefreshRouteOptions</a></code>.</p>
<p>A route handle can be invalid when the map data changes that is used by the HERE sdk to recreate the route. This happens regularly.
Therefore, the route handle is not meant to be persisted for a longer time.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">importRoute</span><span class="p">(</span><span class="nv">routeHandle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-routehandle">RouteHandle</a></span><span class="p">,</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>Options to import the route from handle.</p>
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
<a name="/s:7heresdk20OfflineRoutingEngineC17setInternalOption3key5valueySS_SStF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setInternalOption(key:value:)"></a>
<a class="token" href="#/s:7heresdk20OfflineRoutingEngineC17setInternalOption3key5valueySS_SStF">setInternalOption(key:<wbr/>value:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This method sets internal options that controls offline route calculation behavior.
Unsupported options will be logged as warnings.
Undocumented options can change their meaning without going through deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setInternalOption</span><span class="p">(</span><span class="nv">key</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>key</em>
</code>
</td>
<td>
<div>
<p>Option name</p>
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
<p>New option value</p>
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
