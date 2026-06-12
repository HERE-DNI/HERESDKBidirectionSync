---
title: "PointDataBuilder"
slug: "sdk-for-ios-explore-api-reference-classes-pointdatabuilder"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/PointDataBuilder"></a>
<a title="PointDataBuilder Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        PointDataBuilder Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>PointDataBuilder</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">PointDataBuilder</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataBuilder</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">PointDataBuilder</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Builder of <code><a href="../Maps.html#/s:7heresdk9PointDataC">PointData</a></code> instances.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16PointDataBuilderCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk16PointDataBuilderCACycfc">init()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk16PointDataBuilderC15withCoordinatesyAcA03GeoF0VF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withCoordinates(_:)"></a>
<a class="token" href="#/s:7heresdk16PointDataBuilderC15withCoordinatesyAcA03GeoF0VF">withCoordinates(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder with geodetic coordinates for point to be created.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withCoordinates</span><span class="p">(</span><span class="n">_</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">PointDataBuilder</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>Geodetic coordinates of the point.
Altitude of coordinates is ignored.</p>
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
<a name="/s:7heresdk16PointDataBuilderC14withAttributesyAcA0cF0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/withAttributes(_:)"></a>
<a class="token" href="#/s:7heresdk16PointDataBuilderC14withAttributesyAcA0cF0CF">withAttributes(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the builder with custom attributes for point to be created.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">withAttributes</span><span class="p">(</span><span class="n">_</span> <span class="nv">attributes</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-dataattributes">DataAttributes</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">PointDataBuilder</span></code></pre>
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
<p>Custom data attributes to be associated with the point.</p>
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
<a name="/s:7heresdk16PointDataBuilderC5buildAA0bC0CyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/build()"></a>
<a class="token" href="#/s:7heresdk16PointDataBuilderC5buildAA0bC0CyF">build()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Builds an instance of <code><a href="../Maps.html#/s:7heresdk9PointDataC">PointData</a></code> and resets the builder instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">build</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt"><a href="../Maps.html#/s:7heresdk9PointDataC">PointData</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>Instance of <code><a href="../Maps.html#/s:7heresdk9PointDataC">PointData</a></code> created with the configured parameters.</p>
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
