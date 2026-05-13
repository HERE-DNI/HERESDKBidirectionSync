---
title: "LineDataBuilder Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-linedatabuilder"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- LineDataBuilder.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/LineDataBuilder"></a>
<a title="LineDataBuilder Class Reference"></a>
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
        LineDataBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class LineDataBuilder</code></pre>
<pre><code>extension LineDataBuilder: NativeBase</code></pre>
<pre><code>extension LineDataBuilder: Hashable</code></pre>
</div>
</div>
<p>Builder of <code><a href="../MapLoader.html#/s:7heresdk8LineDataC">LineData</a></code> instances.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LineDataBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk15LineDataBuilderCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a builder instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init()</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LineDataBuilderC12withGeometryyAcA11GeoPolylineVF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withGeometry(_:)"></a>
<a class="token" href="#/s:7heresdk15LineDataBuilderC12withGeometryyAcA11GeoPolylineVF">withGeometry(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder with geometry for line to be created.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withGeometry(_ geometry: GeoPolyline) -&gt; LineDataBuilder</code></pre>
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
<p>Geometry of the polyline. Each vertex defines two line segments: one
with a previous vertex and one with a next vertex. First and last vertices don’t have
resp. previous and next vertices and thus belong to single line segments.
Consecutive duplicate vertices are ignored.
Altitude of polyline vertices is ignored.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The builder.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LineDataBuilderC14withAttributesyAcA0cF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withAttributes(_:)"></a>
<a class="token" href="#/s:7heresdk15LineDataBuilderC14withAttributesyAcA0cF0CF">withAttributes(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder with custom attributes for line to be created.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func withAttributes(_ attributes: DataAttributes) -&gt; LineDataBuilder</code></pre>
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
<p>Custom data attributes to be associated with the line.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The builder.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15LineDataBuilderC5buildAA0bC0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk15LineDataBuilderC5buildAA0bC0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds an instance of <code><a href="../MapLoader.html#/s:7heresdk8LineDataC">LineData</a></code> and resets the builder instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public func build() -&gt; LineData</code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code><a href="../MapLoader.html#/s:7heresdk8LineDataC">LineData</a></code> created with the configured parameters.</p>
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
