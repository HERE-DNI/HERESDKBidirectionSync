---
title: "LineDataAccessor"
slug: "sdk-for-ios-explore-api-reference-classes-linedataaccessor"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataAccessor"></a>
<a title="LineDataAccessor Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maploader">MapLoader</a>

        LineDataAccessor Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>LineDataAccessor</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">LineDataAccessor</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataAccessor</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">LineDataAccessor</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Line data accessor used for manipulating polylines that are part of a LineDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LineDataAccessorC11getGeometryAA11GeoPolylineVyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeometry()"></a>
<a class="token" href="#/s:7heresdk16LineDataAccessorC11getGeometryAA11GeoPolylineVyF">getGeometry()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets polyline geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeometry</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geopolyline">GeoPolyline</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The line geometry.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LineDataAccessorC13getAttributesAA0cfD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAttributes()"></a>
<a class="token" href="#/s:7heresdk16LineDataAccessorC13getAttributesAA0cfD0CyF">getAttributes()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets polyline attributes accessor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getAttributes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-dataattributesaccessor">DataAttributesAccessor</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The polyline attributes accessor.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16LineDataAccessorC11setGeometryyyAA11GeoPolylineVF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setGeometry(_:)"></a>
<a class="token" href="#/s:7heresdk16LineDataAccessorC11setGeometryyyAA11GeoPolylineVF">setGeometry(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Replaces polyline geometry.
Altitude of the vertices is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setGeometry</span><span class="p">(</span><span class="n">_</span> <span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geopolyline">GeoPolyline</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometry</em>
</code>
</td>
<td>
<div>
<p>The geometry.</p>
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
<a name="/s:7heresdk16LineDataAccessorC13setAttributesyyAA0cF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAttributes(_:)"></a>
<a class="token" href="#/s:7heresdk16LineDataAccessorC13setAttributesyyAA0cF0CF">setAttributes(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Replaces polyline attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setAttributes</span><span class="p">(</span><span class="n">_</span> <span class="nv">attributes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-dataattributes">DataAttributes</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>attributes</em>
</code>
</td>
<td>
<div>
<p>The attributes.</p>
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
}</HTMLBlock>
