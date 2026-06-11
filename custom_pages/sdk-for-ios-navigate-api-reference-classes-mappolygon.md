---
title: "sdk-for-ios-navigate-api-reference-classes-mappolygon"
slug: "sdk-for-ios-navigate-api-reference-classes-mappolygon"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolygon"></a>
<a title="MapPolygon Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapPolygon Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapPolygon</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPolygon</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolygon</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolygon</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A visual representation of a polygon on the map. Can be used to visualize areas of all shapes
and sizes.</p>
<p>The geometry to be visualized is represented by an instance of <code><a href="sdk-for-ios-navigate-api-reference-structs-geopolygon">GeoPolygon</a></code>.
To display circular areas (for example, a position accuracy indicator) use a GeoPolygon
created from a <code><a href="sdk-for-ios-navigate-api-reference-structs-geocircle">GeoCircle</a></code> using <code>GeoPolygon.init(GeoCircle)</code>.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC8geometry5colorAcA03GeoC0V_So7UIColorCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometry:color:)"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC8geometry5colorAcA03GeoC0V_So7UIColorCtcfc">init(geometry:<wbr/>color:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.</p>
<p>The winding order of the vertices can be in clockwise or counter-clockwise order.
It is recomended to provide the outer boundary ordered clockwise and closed.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolygon">GeoPolygon</a></span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span></code></pre>
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
<p>The list of vertices representing the outer boundary of polygon.</p>
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
<p>The fill color for the polygon</p>
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
<a name="/s:7heresdk10MapPolygonC8geometry5color12outlineColor0F13WidthInPixelsAcA03GeoC0V_So7UIColorCAKSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometry:color:outlineColor:outlineWidthInPixels:)"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC8geometry5color12outlineColor0F13WidthInPixelsAcA03GeoC0V_So7UIColorCAKSdtcfc">init(geometry:<wbr/>color:<wbr/>outlineColor:<wbr/>outlineWidthInPixels:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.</p>
<p>Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
will be rendered as fully opaque by interpreting the alpha value as 1.</p>
<p>The winding order of the vertices can be in clockwise or counter-clockwise order.
It is recomended to provide the outer boundary ordered clockwise and closed.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolygon">GeoPolygon</a></span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">outlineWidthInPixels</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
<p>The list of vertices representing the outer boundary of polygon.</p>
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
<p>The fill color for the polygon.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>outlineColor</em>
</code>
</td>
<td>
<div>
<p>The color of the polygon outline, alpha channel is ignored and treated as 1.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>outlineWidthInPixels</em>
</code>
</td>
<td>
<div>
<p>The width of the polygon outline (in pixels). Negative values are clamped to 0.</p>
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
<a name="/s:7heresdk10MapPolygonC8geometryAA03GeoC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometry"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC8geometryAA03GeoC0Vvp">geometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geometry of the polygon. Setting a new geometry will update the appearance.
The winding order of the vertices can be in clockwise or counter-clockwise order.
It is recomended to provide the outer boundary ordered clockwise and closed.</p>
<p>Note:</p>
<ul>
<li>The polygon shape should not cover more than half of the globe,
otherwise unexpected results may occur.</li>
<li>Polygons which are self-intersecting are not supported and may lead to render
artifacts.</li>
<li>The inner boundaries (holes) specified in the GeoPolygon are ignored.</li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolygon">GeoPolygon</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC8metadataAA8MetadataCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/metadata"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC8metadataAA8MetadataCSgvp">metadata</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The Metadata instance attached to this polygon, <code>nil</code> by default.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">metadata</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC9fillColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fillColor"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC9fillColorSo7UIColorCvp">fillColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Color of the polygon’s fill.
Fully transparent color (alpha set to 0) disables the fill completely.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fillColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC9drawOrders5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/drawOrder"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC9drawOrders5Int32Vvp">drawOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The draw order of this map polygon relative to other map polygons.
Polygons with higher draw order value are drawn on top of polygons with lower draw order.</p>
<p>In case multiple polygons have the same draw order value
then the order in which they were added to the scene matters. Last added polygon is drawn on top.</p>
<p>Allowed range is 0-1023. Values outside this range will be clamped. Default value is 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">drawOrder</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC16visibilityRangesSayAA0B12MeasureRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/visibilityRanges"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC16visibilityRangesSayAA0B12MeasureRangeVGvp">visibilityRanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of visibility ranges. The map polygon is visible only inside these map measure ranges.
A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the map polygon is visible without map measure restrictions.
Only <a href="s">MapMeasureRange</a> of <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> type are supported.
<a href="s">MapMeasureRange</a> of other unsupported types will be ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">visibilityRanges</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasurerange">MapMeasureRange</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC12outlineColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineColor"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC12outlineColorSo7UIColorCvp">outlineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color of the polygon outline.
The default outline color is opaque white.</p>
<p>Transparent outlines are not supported. Any color with transparency (alpha value other than 1)
will be rendered as fully opaque.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk10MapPolygonC12outlineWidthSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineWidth"></a>
<a class="token" href="#/s:7heresdk10MapPolygonC12outlineWidthSdvp">outlineWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The width of the polygon outline in pixels.
The value should be greater than or equal to zero.
Negative values are clamped to zero.</p>
<p>By default, the outline width is set to zero.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineWidth</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
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
</body>
</html>

`
}</HTMLBlock>
