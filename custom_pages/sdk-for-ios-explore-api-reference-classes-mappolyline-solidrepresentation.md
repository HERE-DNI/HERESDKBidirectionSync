---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-classes-mappolyline-solidrepresentation"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- SolidRepresentation.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SolidRepresentation"></a>
<a title="SolidRepresentation Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        SolidRepresentation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SolidRepresentation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SolidRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
<p>Representation for a solid line without outline.</p>
<p>Can represent polylines that have constant width or width dependent on the map zoom.</p>
<p>To achieve constant width lines, use <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> with a single value.</p>
<p>To achieve line width dependent on map zoom, use <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> with
multiple values.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAA7LineCapOtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lineWidth:color:capShape:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAA7LineCapOtKcfc">init(lineWidth:<wbr/>color:<wbr/>capShape:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a representation for a solid line without outline.</p>
<p>At map measures smaller than smallest map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>
line width is constant and equal to the width given for the smallest
map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>.</p>
<p>At map measures bigger than biggest map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>
line width is constant and equal to the width given for the biggest
map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>.</p>
<p>At map measures between two nearest given map measures line width is
linearly interpolated between width values given for these map measures.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<p><code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">capShape</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-linecap">LineCap</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lineWidth</em>
</code>
</td>
<td>
<div>
<p>The width of the polyline depending on the map measure.</p>
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
<p>The color of the polyline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>capShape</em>
</code>
</td>
<td>
<div>
<p>The cap shape applied to both ends of the polyline.</p>
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
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color07outlineG00I5Color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAlnA7LineCapOtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lineWidth:color:outlineWidth:outlineColor:capShape:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidth5color07outlineG00I5Color8capShapeAeA0B26MeasureDependentRenderSizeV_So7UIColorCAlnA7LineCapOtKcfc">init(lineWidth:<wbr/>color:<wbr/>outlineWidth:<wbr/>outlineColor:<wbr/>capShape:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a representation for a solid line with outline.</p>
<p>The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>
and <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">outlineWidth</a></code>, the value is constant and equal to the width given for
the smallest map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code> and <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">outlineWidth</a></code>.</p>
<p>At map measures bigger than biggest map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>
and <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">outlineWidth</a></code>, the value is constant and equal to the width given for
the biggest map measure in the <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code> and <code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">outlineWidth</a></code>.</p>
<p>At map measures between two nearest given map measure is
linearly interpolated between width values given for these map measures.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<p><code><a href="../../Classes/MapPolyline/SolidRepresentation.html#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">color</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">outlineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">capShape</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-linecap">LineCap</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lineWidth</em>
</code>
</td>
<td>
<div>
<p>The width of the polyline depending on the map measure.</p>
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
<p>The color of the polyline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>outlineWidth</em>
</code>
</td>
<td>
<div>
<p>The width of the outline on one side of the polyline depending on
the map measure.</p>
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
<p>The outline color of the polyline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>capShape</em>
</code>
</td>
<td>
<div>
<p>The cap shape applied to both ends of the polyline.</p>
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
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lineWidth"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The width of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC9lineColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lineColor"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC9lineColorSo7UIColorCvp">lineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color of the polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lineColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineWidth"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineWidthAA0B26MeasureDependentRenderSizeVvp">outlineWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The width of the outline on one side of the polyline depending on the map measure.
The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code>outlineWidth</code>,
outline width is constant and equal to the width given for the smallest
map measure in the <code>outlineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>outlineWidth</code>,
outline width is constant and equal to the width given for the biggest
map measure in the <code>outlineWidth</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/outlineColor"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC12outlineColorSo7UIColorCvp">outlineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The outline color of the polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC8capShapeAA7LineCapOvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/capShape"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC8capShapeAA7LineCapOvp">capShape</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The cap shape applied to both ends of the polyline and its outline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">capShape</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-linecap">LineCap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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

</div>
`
}</HTMLBlock>
