---
title: "TrafficSignal"
slug: "sdk-for-ios-navigate-structs-trafficsignal"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficSignal"></a>
<a title="TrafficSignal Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-mapdata">MapData</a>

        TrafficSignal Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficSignal</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficSignal</span></code></pre>
</div>
</div>
<p>Identifies the presence and the location of traffic lights at an intersection</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficSignalV14offsetInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/offsetInMeters"></a>
<a class="token" href="#/s:7heresdk13TrafficSignalV14offsetInMeterss5Int32Vvp">offsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The offset of the traffic signal in meters from the beginning of the segment in positive direction.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">offsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficSignalV15travelDirectionAA06TravelE0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/travelDirection"></a>
<a class="token" href="#/s:7heresdk13TrafficSignalV15travelDirectionAA06TravelE0Ovp">travelDirection</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Segment direction which the traffic signal is applied.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-traveldirection">TravelDirection</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficSignalV15signalLocationsSayAA0bC8LocationOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/signalLocations"></a>
<a class="token" href="#/s:7heresdk13TrafficSignalV15signalLocationsSayAA0bC8LocationOGvp">signalLocations</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The location information of the traffic lights.
An empty list will be returned when signal location is unspecified/unknown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">signalLocations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-trafficsignallocation">TrafficSignalLocation</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk13TrafficSignalV14offsetInMeters15travelDirection15signalLocationsACs5Int32V_AA06TravelH0OSayAA0bC8LocationOGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(offsetInMeters:travelDirection:signalLocations:)"></a>
<a class="token" href="#/s:7heresdk13TrafficSignalV14offsetInMeters15travelDirection15signalLocationsACs5Int32V_AA06TravelH0OSayAA0bC8LocationOGtcfc">init(offsetInMeters:<wbr/>travelDirection:<wbr/>signalLocations:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">offsetInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">,</span> <span class="nv">travelDirection</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-traveldirection">TravelDirection</a></span><span class="p">,</span> <span class="nv">signalLocations</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-enums-trafficsignallocation">TrafficSignalLocation</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
