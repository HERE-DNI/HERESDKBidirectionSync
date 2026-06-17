---
title: "Traffic"
slug: "sdk-for-ios-navigate-traffic"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Section/Traffic"></a>
<a title="Traffic  Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

        Traffic  Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Traffic</h1>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficDataProviderC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficDataProvider"></a>
<a class="token" href="#/s:7heresdk19TrafficDataProviderC">TrafficDataProvider</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This protocol provides traffic information from
radio signals to other HERE SDK modules.
For now, only the <code><a href="sdk-for-ios-navigate-classes-offlineroutingengine">OfflineRoutingEngine</a></code> is supported.</p>
<p>For more information, take a look at the <code><a href="sdk-for-ios-navigate-classes-trafficbroadcast">TrafficBroadcast</a></code> class, if available for your license.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficDataProvider</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficDataProvider</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficDataProvider</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficEngineC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficEngine"></a>
<a class="token" href="#/s:7heresdk13TrafficEngineC">TrafficEngine</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
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
See <code><a href="Classes/SDKNativeEngine.html#/s:7heresdk15SDKNativeEngineC19passThroughFeaturesShyAA04PassE7FeatureOGSgvp">SDKNativeEngine.passThroughFeatures</a></code></p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-trafficengine">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficEngine</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficEngine</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficEngine</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficFlow"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC">TrafficFlow</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This class provides details about traffic flow along a <code><a href="sdk-for-ios-navigate-structs-geocorridor">GeoCorridor</a></code>, inside a <code><a href="sdk-for-ios-navigate-structs-geocircle">GeoCircle</a></code> or a <code><a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a></code>, that represents particular path of the road network.<br/>
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-trafficflow">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficFlow</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-trafficflowbase">TrafficFlowBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficFlow</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficFlow</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficFlowBaseP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TrafficFlowBase"></a>
<a class="token" href="#/s:7heresdk15TrafficFlowBaseP">TrafficFlowBase</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>This interface provides details about a traffic flow.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-trafficflowbase">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TrafficFlowBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk23TrafficFlowQueryOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficFlowQueryOptions"></a>
<a class="token" href="#/s:7heresdk23TrafficFlowQueryOptionsV">TrafficFlowQueryOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify how traffic flow data should be queried.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficflowqueryoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficFlowQueryOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk33TrafficFlowQueryCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TrafficFlowQueryCompletionHandler"></a>
<a class="token" href="#/s:7heresdk33TrafficFlowQueryCompletionHandlera">TrafficFlowQueryCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Callback passed to following functions:
<code>TrafficEngine.queryForFlow(GeoBox, TrafficFlowQueryOptions, TrafficFlowQueryCompletionHandler)</code>
<code>TrafficEngine.queryForFlow(GeoCircle, TrafficFlowQueryOptions, TrafficFlowQueryCompletionHandler)</code>
<code>TrafficEngine.queryForFlow(GeoCorridor, TrafficFlowQueryOptions, TrafficFlowQueryCompletionHandler)</code>
The method will be called on the main thread when a search call has been completed.
The first argument is the error in the case of the failure. It is <code>nil</code> for an operation that succeeds.
The second argument is the list of flow items in the case of the success. It is <code>nil</code> in case of an error.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TrafficFlowQueryCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">queryError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-trafficqueryerror">TrafficQueryError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">result</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-classes-trafficflow">TrafficFlow</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>queryError</em>
</code>
</td>
<td>
<div>
<p>The error in the case of the failure. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>result</em>
</code>
</td>
<td>
<div>
<p>The list of incidents in the case of the success. It is <code>nil</code> in case of an error.</p>
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
<a name="/s:7heresdk15TrafficIncidentC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncident"></a>
<a class="token" href="#/s:7heresdk15TrafficIncidentC">TrafficIncident</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>TrafficIncident provides details about a traffic incident.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-trafficincident">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficIncident</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-trafficincidentbase">TrafficIncidentBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficIncident</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficIncident</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentBaseP"></a>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/TrafficIncidentBase"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentBaseP">TrafficIncidentBase</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>TrafficIncident provides details about a traffic incident.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-protocols-trafficincidentbase">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">TrafficIncidentBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk32TrafficIncidentCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TrafficIncidentCompletionHandler"></a>
<a class="token" href="#/s:7heresdk32TrafficIncidentCompletionHandlera">TrafficIncidentCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Callback passed to <code><a href="Classes/TrafficEngine.html#/s:7heresdk13TrafficEngineC14lookupIncident4with0D7Options10completionAA10TaskHandle_pSS_AA0be6LookupG0VyAA0B10QueryErrorOSg_AA0bE0CSgtctF">TrafficEngine.lookupIncident(...)</a></code>.
The method will be called on the main thread when a search call has been completed.
The first argument is the error in the case of the failure. It is <code>nil</code> for an operation that succeeds.
The second argument is the incident in the case of the success. It is <code>nil</code> in case of an error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TrafficIncidentCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">queryError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-trafficqueryerror">TrafficQueryError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">result</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-trafficincident">TrafficIncident</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>queryError</em>
</code>
</td>
<td>
<div>
<p>The error in the case of the failure. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>result</em>
</code>
</td>
<td>
<div>
<p>The incident in the case of the success. It is <code>nil</code> in case of an error.</p>
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
<a name="/s:7heresdk21TrafficIncidentImpactO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficIncidentImpact"></a>
<a class="token" href="#/s:7heresdk21TrafficIncidentImpactO">TrafficIncidentImpact</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Impact of a traffic incident.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-trafficincidentimpact">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficIncidentImpact</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk28TrafficIncidentLookupOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficIncidentLookupOptions"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentLookupOptionsV">TrafficIncidentLookupOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>All the options to specify how a single incident should be queried.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficincidentlookupoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficIncidentLookupOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrafficIncidentOnRouteC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficIncidentOnRoute"></a>
<a class="token" href="#/s:7heresdk22TrafficIncidentOnRouteC">TrafficIncidentOnRoute</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Traffic incidents on a route. Use <code><a href="Classes/Section.html#/s:7heresdk7SectionC16trafficIncidentsSayAA22TrafficIncidentOnRouteCGvp">Section.trafficIncidents</a></code> to get a list of incidents on a route section.
Use <code><a href="Classes/Span.html#/s:7heresdk4SpanC22trafficIncidentIndexesSays5Int32VGvp">Span.trafficIncidentIndexes</a></code> to associate incidents with spans. Each incident takes at least the whole geometry of matching spans.
Also, an incident can take some place out of the built route.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-trafficincidentonroute">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficIncidentOnRoute</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-trafficincidentbase">TrafficIncidentBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficIncidentOnRoute</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficIncidentOnRoute</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19TrafficIncidentTypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficIncidentType"></a>
<a class="token" href="#/s:7heresdk19TrafficIncidentTypeO">TrafficIncidentType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Category of a traffic incident.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-trafficincidenttype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficIncidentType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk38TrafficIncidentsQueryCompletionHandlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TrafficIncidentsQueryCompletionHandler"></a>
<a class="token" href="#/s:7heresdk38TrafficIncidentsQueryCompletionHandlera">TrafficIncidentsQueryCompletionHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Callback passed to <code>TrafficEngine.queryForIncidents(GeoCorridor, TrafficIncidentsQueryOptions, TrafficIncidentsQueryCompletionHandler)</code>.
The method will be called on the main thread when a search call has been completed.
The first argument is the error in the case of the failure. It is <code>nil</code> for an operation that succeeds.
The second argument is the list of incidents in the case of the success. It is <code>nil</code> in case of an error.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TrafficIncidentsQueryCompletionHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">queryError</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-trafficqueryerror">TrafficQueryError</a></span><span class="p">?,</span> <span class="n">_</span> <span class="nv">result</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-classes-trafficincident">TrafficIncident</a></span><span class="p">]?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>queryError</em>
</code>
</td>
<td>
<div>
<p>The error in the case of the failure. It is <code>nil</code> for an operation that succeeds.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>result</em>
</code>
</td>
<td>
<div>
<p>The list of incidents in the case of the success. It is <code>nil</code> in case of an error.</p>
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
<a name="/s:7heresdk28TrafficIncidentsQueryOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficIncidentsQueryOptions"></a>
<a class="token" href="#/s:7heresdk28TrafficIncidentsQueryOptionsV">TrafficIncidentsQueryOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The options to specify how incidents should be queried.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficincidentsqueryoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficIncidentsQueryOptions</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15TrafficLocationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficLocation"></a>
<a class="token" href="#/s:7heresdk15TrafficLocationV">TrafficLocation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The location reference to the traffic incident.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-structs-trafficlocation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficLocation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk17TrafficQueryErrorO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/TrafficQueryError"></a>
<a class="token" href="#/s:7heresdk17TrafficQueryErrorO">TrafficQueryError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents various errors that could occur from a traffic queries.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-trafficqueryerror">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">TrafficQueryError</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TraversabilityO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/Traversability"></a>
<a class="token" href="#/s:7heresdk14TraversabilityO">Traversability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Junctions traversability of some traffic incident or flow section.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-enums-traversability">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">Traversability</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
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
