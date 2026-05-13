---
title: "LineDataAccessor Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-linedataaccessor"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LineDataAccessor.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataAccessor"></a>
<a title="LineDataAccessor Class Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-maploader">MapLoader</a>
<img alt="" id="carat" src="../img/carat.png"/>
        LineDataAccessor Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class LineDataAccessor</code></pre>
<pre><code>extension LineDataAccessor: NativeBase</code></pre>
<pre><code>extension LineDataAccessor: Hashable</code></pre>
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
<pre><code>public func getGeometry() -&gt; GeoPolyline</code></pre>
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
<pre><code>public func getAttributes() -&gt; DataAttributesAccessor</code></pre>
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
<pre><code>public func setGeometry(_ geometry: GeoPolyline)</code></pre>
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
