---
title: "MapArrow Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-maparrow"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapArrow.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MapArrow"></a>
<a title="MapArrow Class Reference"></a>
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
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapArrow Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MapArrow</code></pre>
<pre><code>extension MapArrow: NativeBase</code></pre>
<pre><code>extension MapArrow: Hashable</code></pre>
</div>
</div>
<p>A visual representation of an arrow on the map. It consists of a tail - a polyline with an arbitrary
number of points - and a head at its end.</p>
<p>The map arrows are only visible on zoom levels &gt;= 13.</p>
<p>Altitude component of <code><a href="../Structs/GeoPolyline.html">GeoPolyline</a></code>‘s vertices is ignored.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapArrowC8geometry13widthInPixels5colorAcA11GeoPolylineV_SdSo7UIColorCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometry:widthInPixels:color:)"></a>
<a class="token" href="#/s:7heresdk8MapArrowC8geometry13widthInPixels5colorAcA11GeoPolylineV_SdSo7UIColorCtcfc">init(geometry:<wbr/>widthInPixels:<wbr/>color:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new <code>MapArrow</code> instance.</p>
<p>Altitude component of <code><a href="../Structs/GeoPolyline.html">GeoPolyline</a></code>‘s vertices is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(geometry: GeoPolyline, widthInPixels: Double, color: UIColor)</code></pre>
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
<p>The geometry of the arrow tail. The last coordinate in the list defines the position where the
head of the arrow is located.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>widthInPixels</em>
</code>
</td>
<td>
<div>
<p>The width of the arrow tail in pixel. Negative values are clamped to 0. The tip is scaled accordingly.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>color</em>
</code>
</td>
<td>
<div>
<p>The color of the arrow. The alpha channel is ignored, the color is
interpreted as fully opaque.</p>
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
<a name="/s:7heresdk8MapArrowC25measureDependentTailWidthSDyAA0B7MeasureVSdGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/measureDependentTailWidth"></a>
<a class="token" href="#/s:7heresdk8MapArrowC25measureDependentTailWidthSDyAA0B7MeasureVSdGvp">measureDependentTailWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The width of the arrow tail in pixels, where the key is a <code><a href="../Structs/MapMeasure.html">MapMeasure</a></code> and the value is
a tail width in pixels at this <code><a href="../Structs/MapMeasure.html">MapMeasure</a></code>.
The width values are linearly interpolated between nearest dictionary entries.
Width values for <code><a href="../Structs/MapMeasure.html">MapMeasure</a></code> outside the dictionary entries are kept constant, using the
value of the largest/smallest key.</p>
<p>Only <code><a href="../Structs/MapMeasure.html">MapMeasure</a></code> of <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> type is supported.
Other <code><a href="../Structs/MapMeasure.html">MapMeasure</a></code> types are unsupported and hence, will be ignored.</p>
<p><code>measureDependentTailWidth</code> with a single entry is equivalent to the use of the <code>widthInPixels</code> value
in the constructor, so a constant width setting, independent of camera.</p>
<p>Empty <code>measureDependentTailWidth</code> is ignored and existing width is maintained.</p>
<p>The width values should be positive. Dictionary entries with width values less than or equal to 0 are ignored.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var measureDependentTailWidth: [MapMeasure : Double] { get set }</code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk8MapArrowC16visibilityRangesSayAA0B12MeasureRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/visibilityRanges"></a>
<a class="token" href="#/s:7heresdk8MapArrowC16visibilityRangesSayAA0B12MeasureRangeVGvp">visibilityRanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of visibility ranges, in which the map arrow is visible.
A range is half-open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the map arrows are visible without map measure restrictions.
Only <code><a href="../Structs/MapMeasureRange.html">MapMeasureRange</a></code>(s) of <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> type are supported.
<code><a href="../Structs/MapMeasureRange.html">MapMeasureRange</a></code>(s) of other unsupported types will be ignored.}</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public var visibilityRanges: [MapMeasureRange] { get set }</code></pre>
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
