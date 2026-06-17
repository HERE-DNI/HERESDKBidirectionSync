---
title: "TrafficEngine"
slug: "sdk-for-ios-navigate-classes-trafficengine"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficEngine"></a>
<a title="TrafficEngine Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-traffic">Traffic</a>

        TrafficEngine Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficEngine</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use the TrafficEngine to get information about current traffic flow and incidents in an area
specified by <code><a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a></code>, <code><a href="sdk-for-ios-navigate-structs-geocircle">GeoCircle</a></code>, or <code><a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a></code>.
Provides optional parameters given in <code><a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a></code> and <code><a href="sdk-for-ios-navigate-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a></code> to filter the result.</p>
<p>By default, incidents are localized based on their geographical
location. You can override that behavior by specifying the
desired language that should be used for the incidents description and summary.</p>
<p>The resulting traffic data contains information on incident
types such as congestion, construction for road works, road hazard,
road closure, weather updates for road condition, lane restriction
and others.</p>
<p>Traffic data is fetched online to get the most precise and freshest data available.
In offline mode, live traffic data can be fetched using the traffic pass-through features.
See <code><a href="../Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">SDKNativeEngine.passThroughFeatures</a></code></p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficEngineCACyKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineCACyKcfc">init()</a>
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
<a name="/s:7heresdk13TrafficEngineCyAcA09SDKNativeC0CKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(_:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineCyAcA09SDKNativeC0CKcfc">init(_:<wbr/>)</a>
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
<a name="/s:7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/queryForIncidents(inside:queryOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF">queryForIncidents(inside:<wbr/>queryOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic incidents using a bounding box as a filter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">queryForIncidents</span><span class="p">(</span><span class="n">inside</span> <span class="nv">boxArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">queryOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>boxArea</em>
</code>
</td>
<td>
<div>
<p>The bounding box area to search for traffic incidents.
The maximum width and height for a bounding box filter is 1 degree.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>queryOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for incidents query.</p>
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
<p>It is always invoked on the main thread.</p>
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
<a name="/s:7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/queryForIncidents(inside:queryOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF">queryForIncidents(inside:<wbr/>queryOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic incidents using a circle as a filter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">queryForIncidents</span><span class="p">(</span><span class="n">inside</span> <span class="nv">circleArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geocircle">GeoCircle</a></span><span class="p">,</span> <span class="nv">queryOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>circleArea</em>
</code>
</td>
<td>
<div>
<p>The circle area to search for traffic incidents.
The maximum radius of the circle filter is 50000 meters.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>queryOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for incidents query.</p>
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
<p>It is always invoked on the main thread.</p>
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
<a name="/s:7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/queryForIncidents(inside:queryOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC17queryForIncidents6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0B8IncidentCGSgtctF">queryForIncidents(inside:<wbr/>queryOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic incidents by a corridor as a filter.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">queryForIncidents</span><span class="p">(</span><span class="n">inside</span> <span class="nv">corridorArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a></span><span class="p">,</span> <span class="nv">queryOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions">TrafficIncidentsQueryOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>corridorArea</em>
</code>
</td>
<td>
<div>
<p>The corridor box to search for traffic incidents.
The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.
If the number of points in corridor is greater than 300 then request is split into smaller ones and results are
aggregated into single response, this will result in multiple requests to the backend. This process does not change a shape of the corridor.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>queryOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for incidents query.</p>
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
<p>It is always invoked on the main thread.</p>
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
<a name="/s:7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookupIncident(with:lookupOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF">lookupIncident(with:<wbr/>lookupOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic incident by the original id.
See <code><a href="../Classes/TrafficIncident.html#/s:7heresdk15TrafficIncidentC10originalIdSSvp">TrafficIncident.originalId</a></code> for more information.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">lookupIncident</span><span class="p">(</span><span class="n">with</span> <span class="nv">originalId</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">lookupOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficincidentlookupoptions">TrafficIncidentLookupOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>originalId</em>
</code>
</td>
<td>
<div>
<p>The requested incident original id.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>lookupOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for the incident lookup query.</p>
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
<p>The callback object that will be invoked after the incident lookup query.
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
<a name="/s:7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/queryForFlow(inside:queryOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA6GeoBoxV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF">queryForFlow(inside:<wbr/>queryOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic flow using a bounding box as a filter.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">queryForFlow</span><span class="p">(</span><span class="n">inside</span> <span class="nv">boxArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a></span><span class="p">,</span> <span class="nv">queryOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>boxArea</em>
</code>
</td>
<td>
<div>
<p>The bounding box area to search for traffic flow.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>queryOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for flow query.</p>
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
<p>It is always invoked on the main thread.</p>
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
<a name="/s:7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/queryForFlow(inside:queryOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA9GeoCircleV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF">queryForFlow(inside:<wbr/>queryOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic flow using a circle as a filter.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">queryForFlow</span><span class="p">(</span><span class="n">inside</span> <span class="nv">circleArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geocircle">GeoCircle</a></span><span class="p">,</span> <span class="nv">queryOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>circleArea</em>
</code>
</td>
<td>
<div>
<p>The circle area to search for traffic flow.
The maximum radius of the circle filter is 50000 meters.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>queryOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for flow query.</p>
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
<p>It is always invoked on the main thread.</p>
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
<a name="/s:7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/queryForFlow(inside:queryOptions:completion:)"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC12queryForFlow6inside0D7Options10completionAA10TaskHandle_pAA11GeoCorridorV_AA0bf5QueryH0VyAA0bN5ErrorOSg_SayAA0bF0CGSgtctF">queryForFlow(inside:<wbr/>queryOptions:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Asynchronously queries for traffic flow by a corridor as a filter.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@discardableResult</span>
<span class="kd">public</span> <span class="kd">func</span> <span class="nf">queryForFlow</span><span class="p">(</span><span class="n">inside</span> <span class="nv">corridorArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a></span><span class="p">,</span> <span class="nv">queryOptions</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-trafficflowqueryoptions">TrafficFlowQueryOptions</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt"><a href="../Traffic.html#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-taskhandle">TaskHandle</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>corridorArea</em>
</code>
</td>
<td>
<div>
<p>The corridor box to search for traffic flow.
The maximum length for the corridor is 500000 meters and the maximum <code>GeoCorridor.half_width_in_meters</code> is 5000 meters.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>queryOptions</em>
</code>
</td>
<td>
<div>
<p>The options which are specific for flow query.</p>
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
<p>It is always invoked on the main thread.</p>
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
} </HTMLBlock>
