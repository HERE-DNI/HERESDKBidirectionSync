---
title: "DashRepresentation"
slug: "sdk-for-ios-navigate-classes-mappolyline-dashrepresentation"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/DashRepresentation"></a>
<a title="DashRepresentation Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-maps">Maps</a>

<a href="sdk-for-ios-navigate-classes-mappolyline">MapPolyline</a>

        DashRepresentation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DashRepresentation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DashRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
<p>Represents a dash pattern for map polyline where the dash can be rendered as a colored
line and the gap can be either empty or colored.</p>
<p>The length of the dash and gap are set independently, allowing for patterns
like <code>'  —  —  —  —'</code> (dash length = gap length) or <code>' ——— ——— ———'</code> (dash length != gap length).</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5ColorAeA0B26MeasureDependentRenderSizeV_A2KSo7UIColorCtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lineWidth:dashLength:gapLength:dashColor:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5ColorAeA0B26MeasureDependentRenderSizeV_A2KSo7UIColorCtKcfc">init(lineWidth:<wbr/>dashLength:<wbr/>gapLength:<wbr/>dashColor:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a representation for a dashed line. Gaps are not displayed.</p>
<p>At map measures smaller than the smallest map measure in the <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>,
<code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code> and <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a></code>, the value used for rendering is constant
and equal to the value given for the smallest map measure in the
respective <code><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> object.</p>
<p>At map measures bigger than the biggest map measure in the <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>,
<code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code> and <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a></code>, the value used for rendering is constant
and equal to the value given for the biggest map measure in the
respective <code><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> object.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
<p>For <code><a href="sdk-for-ios-navigate-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-navigate-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<p>All sizes must not be 0 (<code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code> with all values set to 0.0).</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">dashLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">gapLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">dashColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<em>dashLength</em>
</code>
</td>
<td>
<div>
<p>The dash length of the polyline depending on the map measure.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>gapLength</em>
</code>
</td>
<td>
<div>
<p>The gap length of the polyline depending on the map measure.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>dashColor</em>
</code>
</td>
<td>
<div>
<p>The dash color of the polyline.</p>
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
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5Color0jK0AeA0B26MeasureDependentRenderSizeV_A2LSo7UIColorCANtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lineWidth:dashLength:gapLength:dashColor:gapColor:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidth10dashLength03gapI00H5Color0jK0AeA0B26MeasureDependentRenderSizeV_A2LSo7UIColorCANtKcfc">init(lineWidth:<wbr/>dashLength:<wbr/>gapLength:<wbr/>dashColor:<wbr/>gapColor:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a representation for a dashed line with both dash and the gap being colored.</p>
<p>At map measures smaller than the smallest map measure in the <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>,
<code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code> and <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a></code>, the value used for rendering is constant
and equal to the value given for the smallest map measure in the
respective <code><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> object.</p>
<p>At map measures bigger than the biggest map measure in the <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a></code>,
<code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code> and <code><a href="../../Classes/MapPolyline/DashRepresentation.html#/s:7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a></code>, the value used for rendering is constant
and equal to the value given for the biggest map measure in the
respective <code><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> object.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
<p>For <code><a href="sdk-for-ios-navigate-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-navigate-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<p>All sizes must not be 0 (<code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code> with all values set to 0.0).</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">dashLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">gapLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">dashColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">gapColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<em>dashLength</em>
</code>
</td>
<td>
<div>
<p>The dash length of the polyline depending on the map measure.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>gapLength</em>
</code>
</td>
<td>
<div>
<p>The gap length of the polyline depending on the map measure.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>dashColor</em>
</code>
</td>
<td>
<div>
<p>The color of the dashes.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>gapColor</em>
</code>
</td>
<td>
<div>
<p>The color of the gaps.</p>
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
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lineWidth"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC9lineWidthAA0B26MeasureDependentRenderSizeVvp">lineWidth</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dashLength"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The dash length of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>dashLength</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>dashLength</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>dashLength</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>dashLength</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dashLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/gapLength"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The gap length of the polyline depending on the map measure.
At map measures smaller than smallest map measure in the <code>gapLength</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>gapLength</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>gapLength</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>gapLength</code>.</p>
<p>At map measures between two nearest given map measures, the values are
linearly interpolated between values given for these map measures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">gapLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC9dashColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dashColor"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC9dashColorSo7UIColorCvp">dashColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color of the dashes of the polyline.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dashColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC8gapColorSo7UIColorCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/gapColor"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC8gapColorSo7UIColorCSgvp">gapColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color for the gaps of the polyline. The default value is <code>nil</code> and
no color is used.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">gapColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
} </HTMLBlock>
