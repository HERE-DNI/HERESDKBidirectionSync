---
title: "Routing / RoutingProtocol"
slug: "sdk-for-ios-navigate-api-reference-protocols-routingprotocol"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/RoutingProtocol"></a>
<a title="RoutingProtocol Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        RoutingProtocol Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RoutingProtocol</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">RoutingProtocol</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Provides the protocol for the online and offline
routing engines.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:options:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with7options10completionAA10TaskHandle_pSayAA8WaypointVG_AA0B7OptionsVyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>options:<wbr/>completion:<wbr/>)</a>
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
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">options</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-routingoptions">RoutingOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:carOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with10carOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03CarH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>carOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">carOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-caroptions">CarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:pedestrianOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with17pedestrianOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA010PedestrianH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>pedestrianOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">pedestrianOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-pedestrianoptions">PedestrianOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:truckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with12truckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05TruckH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>truckOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">truckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-truckoptions">TruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:scooterOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with14scooterOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07ScooterH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>scooterOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">scooterOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-scooteroptions">ScooterOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:bicycleOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with14bicycleOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07BicycleH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>bicycleOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">bicycleOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-bicycleoptions">BicycleOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:taxiOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with11taxiOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA04TaxiH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>taxiOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">taxiOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-taxioptions">TaxiOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:evCarOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with12evCarOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA05EVCarI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>evCarOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">evCarOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evcaroptions">EVCarOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:evTruckOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with14evTruckOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07EVTruckI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>evTruckOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">evTruckOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-evtruckoptions">EVTruckOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:busOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with10busOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA03BusH0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>busOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">busOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-busoptions">BusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivatehI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/calculateRoute(with:privateBusOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP14calculateRoute4with17privateBusOptions10completionAA10TaskHandle_pSayAA8WaypointVG_AA07PrivatehI0VyAA0B5ErrorOSg_SayAA0E0CGSgtctF">calculateRoute(with:<wbr/>privateBusOptions:<wbr/>completion:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use the <code>calculate_route(﹚</code> methods with RoutingOptions parameter instead.")</span>
<span class="kd">@discardableResult</span>
<span class="kd">func</span> <span class="nf">calculateRoute</span><span class="p">(</span><span class="n">with</span> <span class="nv">waypoints</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">],</span> <span class="nv">privateBusOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-privatebusoptions">PrivateBusOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<a name="/s:7heresdk15RoutingProtocolP13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastK8InMeters10completionAA10TaskHandle_pAA0F0C_AA8WaypointVs5Int32VAOyAA0B5ErrorOSg_SayAKGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/returnToRoute(_:startingPoint:lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:completion:)"></a>
<a class="token" href="#/s:7heresdk15RoutingProtocolP13returnToRoute_13startingPoint24lastTraveledSectionIndex022traveledDistanceOnLastK8InMeters10completionAA10TaskHandle_pAA0F0C_AA8WaypointVs5Int32VAOyAA0B5ErrorOSg_SayAKGSgtctF">returnToRoute(_:<wbr/>startingPoint:<wbr/>lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>completion:<wbr/>)</a>
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
<p>A typical use case is to await at least 3 <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routedeviation">RouteDeviation</a></code> events before calling this method.</p>
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
<span class="kd">func</span> <span class="nf">returnToRoute</span><span class="p">(</span><span class="n">_</span> <span class="nv">route</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></span><span class="p">,</span> <span class="nv">startingPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-waypoint">Waypoint</a></span><span class="p">,</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Routing.html#/s:7heresdk31CalculateRouteCompletionHandlera">CalculateRouteCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-taskhandle">TaskHandle</a></span></code></pre>
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
<p>A <code><a href="sdk-for-ios-navigate-api-reference-..-classes-route">Route</a></code> calculated using the online or offline route engine. For the offline case, It
should not contain an indoor <code><a href="sdk-for-ios-navigate-api-reference-..-classes-section">Section</a></code> as such routes will fail. For the online case, it
should have <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routehandle">RouteHandle</a></code>.</p>
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
<p>The current location, for example, provided by a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-routedeviation">RouteDeviation</a></code> event. The waypoint needs to be of
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
