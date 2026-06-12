---
title: "GeoCorridor"
slug: "sdk-for-ios-explore-api-reference-structs-geocorridor"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoCorridor"></a>
<a title="GeoCorridor Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-core">Core</a>

        GeoCorridor Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GeoCorridor</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoCorridor</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A geographical area that wraps around a geographical polyline with a given distance.
The corridor has round edges at the endpoints of the polyline. The distance from
any point of the polyline to the closest border of the corridor is always the same.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoCorridorV8polylineSayAA0B11CoordinatesVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polyline"></a>
<a class="token" href="#/s:7heresdk11GeoCorridorV8polylineSayAA0B11CoordinatesVGvp">polyline</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The polyline passing through the middle of the corridor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">polyline</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoCorridorV17halfWidthInMeterss5Int32VSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/halfWidthInMeters"></a>
<a class="token" href="#/s:7heresdk11GeoCorridorV17halfWidthInMeterss5Int32VSgvp">halfWidthInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The shortest distance from any point on the polyline to the border of the corridor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">halfWidthInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoCorridorV8polyline17halfWidthInMetersACSayAA0B11CoordinatesVG_s5Int32Vtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(polyline:halfWidthInMeters:)"></a>
<a class="token" href="#/s:7heresdk11GeoCorridorV8polyline17halfWidthInMetersACSayAA0B11CoordinatesVG_s5Int32Vtcfc">init(polyline:<wbr/>halfWidthInMeters:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCorridor from the provided polyline and half-width in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">polyline</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">],</span> <span class="nv">halfWidthInMeters</span><span class="p">:</span> <span class="kt">Int32</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polyline</em>
</code>
</td>
<td>
<div>
<p>The polyline passing through the middle of the corridor.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>halfWidthInMeters</em>
</code>
</td>
<td>
<div>
<p>The shortest distance from any point on the polyline to the border of the corridor.</p>
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
<a name="/s:7heresdk11GeoCorridorV8polylineACSayAA0B11CoordinatesVG_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(polyline:)"></a>
<a class="token" href="#/s:7heresdk11GeoCorridorV8polylineACSayAA0B11CoordinatesVG_tcfc">init(polyline:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoCorridor from the provided polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">polyline</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">])</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>polyline</em>
</code>
</td>
<td>
<div>
<p>The polyline passing through the middle of the corridor.</p>
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
