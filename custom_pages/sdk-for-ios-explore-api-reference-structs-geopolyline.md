---
title: "Core / GeoPolyline"
slug: "sdk-for-ios-explore-api-reference-structs-geopolyline"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoPolyline"></a>
<a title="GeoPolyline Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        GeoPolyline Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>GeoPolyline</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">GeoPolyline</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A list of geographic coordinates representing the vertices of a polyline.
An instance of this class, initialized with appropriate vertices.
Represents a <code>GeoPolyline</code> as a series of geographic coordinates.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vertices"></a>
<a class="token" href="#/s:7heresdk11GeoPolylineV8verticesSayAA0B11CoordinatesVGvp">vertices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of vertices representing the polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">let</span> <span class="nv">vertices</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoPolylineV8verticesACSayAA0B11CoordinatesVG_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(vertices:)"></a>
<a class="token" href="#/s:7heresdk11GeoPolylineV8verticesACSayAA0B11CoordinatesVG_tKcfc">init(vertices:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs a GeoPolyline from the provided vertices.
Throws an InstantiationError if the number of vertices is less than two.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Instantiation error.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">vertices</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">])</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>vertices</em>
</code>
</td>
<td>
<div>
<p>List of vertices representing the polyline.</p>
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
<a name="/s:7heresdk11GeoPolylineV6geoBoxAcA0bE0V_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geoBox:)"></a>
<a class="token" href="#/s:7heresdk11GeoPolylineV6geoBoxAcA0bE0V_tcfc">init(geoBox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an instance of this class from <code><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geoBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoBox</em>
</code>
</td>
<td>
<div>
<p>A rectangle defined by the <code><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></code> to be converted into <code>GeoPolyline</code>.
The corner coordinates of the <code><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></code> will define the points of the resulting <code>GeoPolyline</code>.</p>
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
<a name="/s:7heresdk11GeoPolylineV17getNearestIndexTo5points6UInt32VAA0B11CoordinatesV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getNearestIndexTo(point:)"></a>
<a class="token" href="#/s:7heresdk11GeoPolylineV17getNearestIndexTo5points6UInt32VAA0B11CoordinatesV_tF">getNearestIndexTo(point:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the index of the nearest vertex to the given point.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getNearestIndexTo</span><span class="p">(</span><span class="nv">point</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">UInt32</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>point</em>
</code>
</td>
<td>
<div>
<p>Coordinates of the point.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Index of the closest vertex of the polyline.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11GeoPolylineV13coordinatesAt14offsetInMeters9directionAA0B11CoordinatesVSd_AA0bC9DirectionOtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/coordinatesAt(offsetInMeters:direction:)"></a>
<a class="token" href="#/s:7heresdk11GeoPolylineV13coordinatesAt14offsetInMeters9directionAA0B11CoordinatesVSd_AA0bC9DirectionOtF">coordinatesAt(offsetInMeters:<wbr/>direction:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns the coordinates at the given distance along the polyline. When the polyline is
traversed from the beginning, the distance is calculated from the start of the
polyline; while a direction from the end indicates a distance from the last vertex.</p>
<p>The offset is expected to be non-negative and smaller than the length of the polyline.
When the offset is negative, the function returns the starting end point of the polyline,
i.e. the first vertex in positive direction and the last vertex in the negative direction.
Similarly, when the offset is larger than the length of the polyline, then the function
returns the opposite end point of the polyline.</p>
<p>The distance between two consecutive vertices is calculated using the
<code><a href="../Structs/GeoCoordinates.html#/s:7heresdk14GeoCoordinatesV8distance2toSdAC_tF">GeoCoordinates.distance(...)</a></code> function. Therefore, it computes the distance (in meters) along
the great circle between the two vertices. Similarly, the full length of the polyline is the
sum of the distances between its vertices. The interpolation coordinates between two vertices
is calculated using the <code><a href="../Structs/GeoCoordinates.html#/s:7heresdk14GeoCoordinatesV11interpolate6toward2byA2C_SdtF">GeoCoordinates.interpolate(...)</a></code> function.</p>
<p>Note: the result may different from the analogue result from other matching components since
they may adapt the result to the length of the underlying object described by the polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">coordinatesAt</span><span class="p">(</span><span class="nv">offsetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">direction</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-enums-geopolylinedirection">GeoPolylineDirection</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>offsetInMeters</em>
</code>
</td>
<td>
<div>
<p>The distance along the polyline in meters</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>direction</em>
</code>
</td>
<td>
<div>
<p>The direction in which the polyline is traversed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The coordinates of the point at the given distance</p>
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
