---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-trafficflow"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficFlow.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrafficFlow"></a>
<a title="TrafficFlow Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-traffic">Traffic</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficFlow Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficFlow</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrafficFlow</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-trafficflowbase">TrafficFlowBase</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficFlow</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrafficFlow</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>This class provides details about traffic flow along a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geocorridor">GeoCorridor</a></code>, inside a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geocircle">GeoCircle</a></code> or a <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></code>, that represents particular path of the road network.<br/>
Backends for TrafficEngine and traffic vector tiles are different however backends may share the same data.<br/>
For additional information about fields, refer to <a href="https://www.here.com/docs/bundle/traffic-api-v7-api-reference/page/index.html#tag/Real-Time-Traffic">Traffic API v7 API Reference: Traffic API v7</a>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC04freeC22SpeedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/freeFlowSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC04freeC22SpeedInMetersPerSecondSdvp">freeFlowSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The reference speed in meters per second along the roadway when no traffic is present.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">freeFlowSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC9jamFactorSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/jamFactor"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC9jamFactorSdvp">jamFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A value for the amount of traffic on the roadway.
The value, between 0.0 and 10.0, indicate the expected quality of travel.
A value of 0.0 indicates that there is no congestion on the roadway.
As the value approaches 10.0, it indicates increasing congestion.
A value of 10.0 is reserved to represent a blocked roadway (closure).</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">jamFactor</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC8locationAA0B8LocationVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/location"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC8locationAA0B8LocationVvp">location</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the location affected by traffic flow.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">location</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-trafficlocation">TrafficLocation</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC22speedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC22speedInMetersPerSecondSdSgvp">speedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The expected speed in meters per second along the roadway; will not exceed the legal speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC30speedUncappedInMetersPerSecondSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedUncappedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC30speedUncappedInMetersPerSecondSdSgvp">speedUncappedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The expected speed in meters per second that a car can drive along a roadway right now; may exceed the legal speed limit.
It is based on probe data (GPS coordinates sent by vehicles or mobile devices driving along that roadway).
The calculated ‘expected speed’ may be over the legal speed limit for that roadway because people are driving over the speed limit.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedUncappedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC11jamTendencys5Int16VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/jamTendency"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC11jamTendencys5Int16VSgvp">jamTendency</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The jamTendency field denotes whether the congestion is increasing, decreasing, or constant.
The congestion tendency may take the following values:</p>
<ul>
<li>+2 - rapidly increasing congestion</li>
<li>+1 - increasing congestion</li>
<li>0 - constant congestion</li>
<li>-1 - decreasing congestion</li>
<li>-2 - rapidly decreasing congestion
Default value of 0 can be assumed when this attribute is not present.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">jamTendency</span><span class="p">:</span> <span class="kt">Int16</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC10confidenceSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/confidence"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC10confidenceSdSgvp">confidence</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The confidence field indicates the proportion of real-time data included in the speed calculation.
It is a normalized value between 0.0 and 1.0 with the following meaning:</p>
<ul>
<li>0.7 &lt; confidence &lt;= 1.0 indicates real time speeds</li>
<li>0.5 &lt; confidence &lt;= 0.7 indicates historical speeds</li>
<li>0.0 &lt; confidence &lt;= 0.5 indicates speed limit</li>
</ul>
<p>This field can be used to identify whether the data for a location is derived from
real-time probe sources or historical information only.
All confidence data 0.71 and above is based on real-time information,
where a confidence value of 0.75 or greater indicates high confidence real-time information.
A confidence value equal to 0.70 or lower means that the data is derived from historical data only.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">confidence</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC14traversabilityAA14TraversabilityOSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/traversability"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC14traversabilityAA14TraversabilityOSgvp">traversability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traversability of roadway.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">traversability</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-traversability">Traversability</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11TrafficFlowC23junctionsTraversabilityAA09JunctionsE0OSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/junctionsTraversability"></a>
<a class="token" href="#/s:7heresdk11TrafficFlowC23junctionsTraversabilityAA09JunctionsE0OSgvp">junctionsTraversability</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traversability of junctions along the affected road.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">junctionsTraversability</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-junctionstraversability">JunctionsTraversability</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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

</div>
`
}</HTMLBlock>
