---
title: "RouteMatchedLocation"
slug: "sdk-for-ios-navigate-api-reference-structs-routematchedlocation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/RouteMatchedLocation"></a>
<a title="RouteMatchedLocation Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        RouteMatchedLocation Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>RouteMatchedLocation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">RouteMatchedLocation</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a location matched to a specific position on a navigation route.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RouteMatchedLocationV12sectionIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/sectionIndex"></a>
<a class="token" href="#/s:7heresdk20RouteMatchedLocationV12sectionIndexs5Int32Vvp">sectionIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zero-based index of the route section containing this location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RouteMatchedLocationV9spanIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spanIndex"></a>
<a class="token" href="#/s:7heresdk20RouteMatchedLocationV9spanIndexs5Int32Vvp">spanIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zero-based index of the span within the current route section.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">spanIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RouteMatchedLocationV18spanOffsetInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spanOffsetInMeters"></a>
<a class="token" href="#/s:7heresdk20RouteMatchedLocationV18spanOffsetInMetersSdvp">spanOffsetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance in meters from the beginning of the current span to this location.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">spanOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RouteMatchedLocationV23spanGeometryVertexIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/spanGeometryVertexIndex"></a>
<a class="token" href="#/s:7heresdk20RouteMatchedLocationV23spanGeometryVertexIndexs5Int32Vvp">spanGeometryVertexIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zero-based index of the geometry vertex that precedes this location.</p>
<p>The span geometry is represented as a series of vertices. This index
points to the vertex immediately before the matched location,
allowing for interpolation between vertices if needed.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">spanGeometryVertexIndex</span><span class="p">:</span> <span class="kt">Int32</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20RouteMatchedLocationV12sectionIndex04spanF00G14OffsetInMeters0g14GeometryVertexF0ACs5Int32V_AISdAItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(sectionIndex:spanIndex:spanOffsetInMeters:spanGeometryVertexIndex:)"></a>
<a class="token" href="#/s:7heresdk20RouteMatchedLocationV12sectionIndex04spanF00G14OffsetInMeters0g14GeometryVertexF0ACs5Int32V_AISdAItcfc">init(sectionIndex:<wbr/>spanIndex:<wbr/>spanOffsetInMeters:<wbr/>spanGeometryVertexIndex:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>sectionIndex: Zero-based index of the route section containing this location.</li>
<li>spanIndex: Zero-based index of the span within the current route section.</li>
<li>spanOffsetInMeters: Distance in meters from the beginning of the current span to this location.</li>
<li>spanGeometryVertexIndex: Zero-based index of the geometry vertex that precedes this location.</li>
</ul>
<p>The span geometry is represented as a series of vertices. This index
  points to the vertex immediately before the matched location,
  allowing for interpolation between vertices if needed.</p></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">sectionIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">spanIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">,</span> <span class="nv">spanOffsetInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">spanGeometryVertexIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="o">=</span> <span class="mi">0</span><span class="p">)</span></code></pre>
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
