---
title: "sdk-for-ios-navigate-api-reference-structs-trafficonroute"
slug: "sdk-for-ios-navigate-api-reference-structs-trafficonroute"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/TrafficOnRoute"></a>
<a title="TrafficOnRoute Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-routing">Routing</a>
<img alt="" id="carat" src="/carat.png"/>
        TrafficOnRoute Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrafficOnRoute</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">TrafficOnRoute</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Traffic information on a route. Information for the already traveled portion of the route is
omitted.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TrafficOnRouteV24lastTraveledSectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lastTraveledSectionIndex"></a>
<a class="token" href="#/s:7heresdk14TrafficOnRouteV24lastTraveledSectionIndexs5Int32Vvp">lastTraveledSectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates the index of the last traveled route section. Traveled part of the route won’t
be reused.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TrafficOnRouteV016traveledDistanceC19LastSectionInMeterss5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/traveledDistanceOnLastSectionInMeters"></a>
<a class="token" href="#/s:7heresdk14TrafficOnRouteV016traveledDistanceC19LastSectionInMeterss5Int32Vvp">traveledDistanceOnLastSectionInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Offset, in meter, to the last visited position on the route section defined by the last
traveled section index.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TrafficOnRouteV15trafficSectionsSayAA0bC7SectionVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/trafficSections"></a>
<a class="token" href="#/s:7heresdk14TrafficOnRouteV15trafficSectionsSayAA0bC7SectionVGvp">trafficSections</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of traffic sections.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">trafficSections</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-trafficonsection">TrafficOnSection</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk14TrafficOnRouteV24lastTraveledSectionIndex016traveledDistancec4LastG8InMeters15trafficSectionsACs5Int32V_AHSayAA0bcG0VGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lastTraveledSectionIndex:traveledDistanceOnLastSectionInMeters:trafficSections:)"></a>
<a class="token" href="#/s:7heresdk14TrafficOnRouteV24lastTraveledSectionIndex016traveledDistancec4LastG8InMeters15trafficSectionsACs5Int32V_AHSayAA0bcG0VGtcfc">init(lastTraveledSectionIndex:<wbr/>traveledDistanceOnLastSectionInMeters:<wbr/>trafficSections:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lastTraveledSectionIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">traveledDistanceOnLastSectionInMeters</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">trafficSections</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-trafficonsection">TrafficOnSection</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[])</span></code></pre>
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
