---
title: "Routing / TrafficOnSpan"
slug: "sdk-for-ios-navigate-api-reference-structs-trafficonspan"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficOnSpan"></a>
<a title="TrafficOnSpan Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficOnSpan Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficOnSpan</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficOnSpan</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Traffic information of a span along a route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV28trafficSectionPolylineOffsets5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSectionPolylineOffset"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV28trafficSectionPolylineOffsets5Int32Vvp">trafficSectionPolylineOffset</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Index over <code><a href="../Structs/TrafficOnSection.html#/s:7heresdk16TrafficOnSectionV8geometrySayAA14GeoCoordinatesVGvp">TrafficOnSection.geometry</a></code> where this span starts.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficSectionPolylineOffset</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV14lengthInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lengthInMeters"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV14lengthInMetersSdvp">lengthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Length of the traffic span, in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lengthInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV8durationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/duration"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV8durationSdvp">duration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The time duration necessary to traverse the traffic span. This duration takes also into
consideration the delays caused by the traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV12trafficDelaySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficDelay"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV12trafficDelaySdvp">trafficDelay</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The estimated extra time in seconds spent due to traffic delays along this traffic span.
Negative values indicate that the traffic span can be traversed faster than usual.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficDelay</span><span class="p">:</span> <span class="kt">TimeInterval</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV26baseSpeedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/baseSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV26baseSpeedInMetersPerSecondSdvp">baseSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed, in meters per second, without taking traffic into consideration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">baseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV29trafficSpeedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSpeedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV29trafficSpeedInMetersPerSecondSdvp">trafficSpeedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The speed, in meters per second, considering traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV9jamFactorSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/jamFactor"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV9jamFactorSdvp">jamFactor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The traffic jam factor shows the traffic condition in a numeric way. It is a
value in the range [0.0, 10.0]. A large jamFactor value means more traffic jam
in general. Specifically, 0.0 means free traffic and 10.0 means stationary traffic.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">jamFactor</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV15incidentIndicesSays5Int32VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/incidentIndices"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV15incidentIndicesSays5Int32VGvp">incidentIndices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The indices of traffic incidents from the field <code><a href="../Structs/TrafficOnSection.html#/s:7heresdk16TrafficOnSectionV16trafficIncidentsSayAA0b8IncidentC5RouteCGvp">TrafficOnSection.trafficIncidents</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">incidentIndices</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV26consumptionInKilowattHoursSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/consumptionInKilowattHours"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV26consumptionInKilowattHoursSdSgvp">consumptionInKilowattHours</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The power consumption in kilowatt-hours (kWh) necessary to traverse the span.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">consumptionInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficOnSpanV28trafficSectionPolylineOffset14lengthInMeters8duration0E5Delay09baseSpeedjK9PerSecond0eojkpQ09jamFactor15incidentIndices011consumptionJ13KilowattHoursACs5Int32V_S6dSayANGSdSgtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(trafficSectionPolylineOffset:lengthInMeters:duration:trafficDelay:baseSpeedInMetersPerSecond:trafficSpeedInMetersPerSecond:jamFactor:incidentIndices:consumptionInKilowattHours:)"></a>
<a class="token" href="#/s:7heresdk13TrafficOnSpanV28trafficSectionPolylineOffset14lengthInMeters8duration0E5Delay09baseSpeedjK9PerSecond0eojkpQ09jamFactor15incidentIndices011consumptionJ13KilowattHoursACs5Int32V_S6dSayANGSdSgtcfc">init(trafficSectionPolylineOffset:<wbr/>lengthInMeters:<wbr/>duration:<wbr/>trafficDelay:<wbr/>baseSpeedInMetersPerSecond:<wbr/>trafficSpeedInMetersPerSecond:<wbr/>jamFactor:<wbr/>incidentIndices:<wbr/>consumptionInKilowattHours:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">trafficSectionPolylineOffset</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">lengthInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">trafficDelay</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">baseSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">trafficSpeedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">jamFactor</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">incidentIndices</span><span class="p">:</span> <span class="p">[</span><span class="kt">Int32</span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">consumptionInKilowattHours</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">)</span></code></pre>
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
}</HTMLBlock>
