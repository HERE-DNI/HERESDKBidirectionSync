---
title: "PolygonDataAccessor Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-polygondataaccessor"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- PolygonDataAccessor.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/PolygonDataAccessor"></a>
<a title="PolygonDataAccessor Class Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        PolygonDataAccessor Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class PolygonDataAccessor</code></pre>
<pre><code>extension PolygonDataAccessor: NativeBase</code></pre>
<pre><code>extension PolygonDataAccessor: Hashable</code></pre>
</div>
</div>
<p>Polygon data accessor used for manipulating polygons that are part of a PolygonDataSource.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PolygonDataAccessorC11getGeometryAA03GeoB0VyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeometry()"></a>
<a class="token" href="#/s:7heresdk19PolygonDataAccessorC11getGeometryAA03GeoB0VyF">getGeometry()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets polygon geometry.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getGeometry() -&gt; GeoPolygon</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The polygon geometry.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PolygonDataAccessorC13getAttributesAA0cfD0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAttributes()"></a>
<a class="token" href="#/s:7heresdk19PolygonDataAccessorC13getAttributesAA0cfD0CyF">getAttributes()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets polygon attributes accessor.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func getAttributes() -&gt; DataAttributesAccessor</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The polygon attributes accessor.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19PolygonDataAccessorC11setGeometryyyAA03GeoB0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setGeometry(_:)"></a>
<a class="token" href="#/s:7heresdk19PolygonDataAccessorC11setGeometryyyAA03GeoB0VF">setGeometry(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Replaces polygon geometry.
The outer boundary has to be ordered clockwise and closed.</p>
<p>Altitude of the vertices is ignored.</p>
<p>The visual behaviour for self-intersecting outer boundary is undefined.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setGeometry(_ geometry: GeoPolygon)</code></pre>
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
<p>Geometry of the polygon. The outer boundary has to be ordered clockwise and closed.
Altitude of the vertices is ignored.
The visual behaviour for self-intersecting outer boundary is undefined.</p>
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
<a name="/s:7heresdk19PolygonDataAccessorC13setAttributesyyAA0cF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAttributes(_:)"></a>
<a class="token" href="#/s:7heresdk19PolygonDataAccessorC13setAttributesyyAA0cF0CF">setAttributes(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Replaces polygon attributes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func setAttributes(_ attributes: DataAttributes)</code></pre>
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



</div>
`
}</HTMLBlock>
