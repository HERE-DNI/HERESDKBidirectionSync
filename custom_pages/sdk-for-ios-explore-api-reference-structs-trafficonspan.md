---
title: "TrafficOnSpan Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-trafficonspan"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrafficOnSpan.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficOnSpan"></a>
<a title="TrafficOnSpan Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="sdk-for-ios-explore-api-reference-..-index">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-routing">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrafficOnSpan Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct TrafficOnSpan : Hashable</code></pre>
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
<pre><code>public var trafficSectionPolylineOffset: Int32</code></pre>
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
<pre><code>public var lengthInMeters: Double</code></pre>
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
<pre><code>public var duration: TimeInterval</code></pre>
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
<pre><code>public var trafficDelay: TimeInterval</code></pre>
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
<pre><code>public var baseSpeedInMetersPerSecond: Double</code></pre>
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
<pre><code>public var trafficSpeedInMetersPerSecond: Double</code></pre>
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
<pre><code>public var jamFactor: Double</code></pre>
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
<pre><code>public var incidentIndices: [Int32]</code></pre>
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
<pre><code>public var consumptionInKilowattHours: Double?</code></pre>
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
<pre><code>public init(trafficSectionPolylineOffset: Int32 = 0, lengthInMeters: Double = 0.0, duration: TimeInterval = 0, trafficDelay: TimeInterval = 0, baseSpeedInMetersPerSecond: Double = 0.0, trafficSpeedInMetersPerSecond: Double = 0.0, jamFactor: Double = 0.0, incidentIndices: [Int32] = [], consumptionInKilowattHours: Double? = nil)</code></pre>
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



</div>
`
}</HTMLBlock>
