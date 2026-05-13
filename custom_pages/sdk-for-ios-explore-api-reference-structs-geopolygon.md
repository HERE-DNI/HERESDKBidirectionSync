---
title: "GeoPolygon Structure Reference"
slug: "sdk-for-ios-explore-api-reference-structs-geopolygon"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- GeoPolygon.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/GeoPolygon"></a>
<a title="GeoPolygon Structure Reference"></a>
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
<a href="sdk-for-ios-explore-api-reference-..-core">Core</a>
<img alt="" id="carat" src="../img/carat.png"/>
        GeoPolygon Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct GeoPolygon : Hashable</code></pre>
</div>
</div>
<p>Represents a <code>GeoPolygon</code> area as a series of geographic coordinates, and optionally,
a list of inner boundaries (also known as holes).
An instance of this class, initialized with appropriate vertices.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10GeoPolygonV8verticesSayAA0B11CoordinatesVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/vertices"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV8verticesSayAA0B11CoordinatesVGvp">vertices</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of geographic coordinates representing the outer boundary vertices of polygon.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let vertices: [GeoCoordinates]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10GeoPolygonV15innerBoundariesSaySayAA0B11CoordinatesVGGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/innerBoundaries"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV15innerBoundariesSaySayAA0B11CoordinatesVGGvp">innerBoundaries</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of polygon inner boundaries (holes), each defined as a list of geographic coordinates.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public let innerBoundaries: [[GeoCoordinates]]</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10GeoPolygonV8verticesACSayAA0B11CoordinatesVG_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(vertices:)"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV8verticesACSayAA0B11CoordinatesVG_tKcfc">init(vertices:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an instance of this class from the provided vertices.
Throws InstantiationError if the number of vertices is less than three.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Instantiation error.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(vertices: [GeoCoordinates]) throws</code></pre>
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
<p>List of vertices representing the polygon outer boundary in clockwise order.</p>
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
<a name="/s:7heresdk10GeoPolygonV8vertices15innerBoundariesACSayAA0B11CoordinatesVG_SayAHGtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(vertices:innerBoundaries:)"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV8vertices15innerBoundariesACSayAA0B11CoordinatesVG_SayAHGtKcfc">init(vertices:<wbr/>innerBoundaries:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an instance of this class from the provided vertices and inner boundaries (holes).
Throws InstantiationError if the number of vertices is less than three.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> Instantiation error.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(vertices: [GeoCoordinates], innerBoundaries: [[GeoCoordinates]]) throws</code></pre>
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
<p>List of vertices representing the polygon outer boundary in clockwise order.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>innerBoundaries</em>
</code>
</td>
<td>
<div>
<p>List of polygon inner boundaries (holes), each in counterclockwise order.</p>
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
<a name="/s:7heresdk10GeoPolygonV9geoCircleAcA0bE0V_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geoCircle:)"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV9geoCircleAcA0bE0V_tcfc">init(geoCircle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an instance of this class from <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocircle">GeoCircle</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(geoCircle: GeoCircle)</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoCircle</em>
</code>
</td>
<td>
<div>
<p>A <code><a href="sdk-for-ios-explore-api-reference-..-structs-geocircle">GeoCircle</a></code> to be converted into <code>GeoPolygon</code>.</p>
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
<a name="/s:7heresdk10GeoPolygonV6geoBoxAcA0bE0V_tcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geoBox:)"></a>
<a class="token" href="#/s:7heresdk10GeoPolygonV6geoBoxAcA0bE0V_tcfc">init(geoBox:<wbr/>)</a>
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
<pre><code>public init(geoBox: GeoBox)</code></pre>
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
<p>A rectangle defined by the <code><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></code> to be converted into <code>GeoPolygon</code>.
The corner coordinates defined by the <code><a href="sdk-for-ios-explore-api-reference-..-structs-geobox">GeoBox</a></code> will define the outer boundary verticies of the <code>GeoPolygon</code>.</p>
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
