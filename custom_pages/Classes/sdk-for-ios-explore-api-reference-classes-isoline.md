---
title: "Isoline Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-isoline"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- Isoline.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/Isoline"></a>
<a title="Isoline Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Routing.html">Routing</a>
<img alt="" id="carat" src="../img/carat.png"/>
        Isoline Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class Isoline</code></pre>
<pre><code>extension Isoline: NativeBase</code></pre>
<pre><code>extension Isoline: Hashable</code></pre>
</div>
</div>
<p>Represents an isoline polygon around a center point. Any possible route between
the center and any point on the edges of the polygon can be travelled within the
given range restriction. The edges of the polygon are not guaranteed to be on the road as
all reachable road endpoints are smoothened to fit into one polygon shape. This
process can be influenced by setting <code><a href="../Structs/IsolineOptions/Calculation.html#/s:7heresdk14IsolineOptionsV11CalculationV9maxPointss5Int32VSgvp">IsolineOptions.Calculation.maxPoints</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7IsolineC9rangeType0C5Value6center8polygonsAcA0b5RangeD0O_SdAA21MapMatchedCoordinatesVSayAA10GeoPolygonVGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(rangeType:rangeValue:center:polygons:)"></a>
<a class="token" href="#/s:7heresdk7IsolineC9rangeType0C5Value6center8polygonsAcA0b5RangeD0O_SdAA21MapMatchedCoordinatesVSayAA10GeoPolygonVGtcfc">init(rangeType:<wbr/>rangeValue:<wbr/>center:<wbr/>polygons:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Constructs an isoline instance. This instance is provided by the
<code><a href="../Routing.html#/s:7heresdk33CalculateIsolineCompletionHandlera">CalculateIsolineCompletionHandler</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(rangeType: IsolineRangeType, rangeValue: Double, center: MapMatchedCoordinates, polygons: [GeoPolygon])</code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>rangeType</em>
</code>
</td>
<td>
<div>
<p>Specifies the range type of the provided <code>Isoline.init(...).rangeValue</code> list.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>rangeValue</em>
</code>
</td>
<td>
<div>
<p>A list of range values. At least one value must be set.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>center</em>
</code>
</td>
<td>
<div>
<p>The center of the isoline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>polygons</em>
</code>
</td>
<td>
<div>
<p>A list of polygons that belong to this isoline. At least one value must be set.</p>
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
<a name="/s:7heresdk7IsolineC9rangeTypeAA0b5RangeD0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rangeType"></a>
<a class="token" href="#/s:7heresdk7IsolineC9rangeTypeAA0b5RangeD0Ovp">rangeType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the type of the restriction that was used to calculate this isoline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var rangeType: IsolineRangeType { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7IsolineC10rangeValueSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/rangeValue"></a>
<a class="token" href="#/s:7heresdk7IsolineC10rangeValueSdvp">rangeValue</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Specifies the numerical value of the restriction that was used to calculate this isoline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var rangeValue: Double { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7IsolineC6centerAA21MapMatchedCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/center"></a>
<a class="token" href="#/s:7heresdk7IsolineC6centerAA21MapMatchedCoordinatesVvp">center</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The center point that was used to calculate this isoline.
Specifies the center point that was used to calculate this isoline.
This includes the original center that was passed to the RoutingEngine.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var center: MapMatchedCoordinates { get }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk7IsolineC8polygonsSayAA10GeoPolygonVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/polygons"></a>
<a class="token" href="#/s:7heresdk7IsolineC8polygonsSayAA10GeoPolygonVGvp">polygons</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of polygons that belong to this isoline. An isoline can consist of multiple
polygons. For example, islands that can be reached by a ferry are included.
Each island is then represented as a separate polygon. However, in most cases
only a single polygon is included.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var polygons: [GeoPolygon] { get }</code></pre>
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



</div>
`
}</HTMLBlock>
