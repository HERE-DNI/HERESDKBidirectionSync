---
title: "DashImageRepresentation"
slug: "sdk-for-ios-navigate-api-reference-classes-mappolyline-dashimagerepresentation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/DashImageRepresentation"></a>
<a title="DashImageRepresentation Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a>

        DashImageRepresentation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>DashImageRepresentation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DashImageRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
<p>Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
from each other.</p>
<p>This dash pattern representation consists only of images rendered at certain
points along the polyline. For rendering them without any distortions, polyline gets sliced into
series of straight segments that are multiple of sum of dash and gap lengths. For this
reason, the new polyline geometry might not align fully with original geometry.</p>
<p>The <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp">MapPolyline.DashImageRepresentation.dashImage</a></code> is stretched according to <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">MapPolyline.DashImageRepresentation.dashLength</a></code>
and <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">MapPolyline.DashImageRepresentation.dashWidth</a></code>, with image’s width matched to <code>dashLength</code> and
image’s height matched to <code>dashWidth</code>. The image is oriented so that its bottom is on the
left-hand side between vertices <code>n</code> and <code>n+1</code>.</p>
<p>The spacing between images is specified by <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">MapPolyline.DashImageRepresentation.gapLength</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLength0G5Width5imageAeA0B26MeasureDependentRenderSizeV_AjA0bE0CtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(dashLength:dashWidth:image:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLength0G5Width5imageAeA0B26MeasureDependentRenderSizeV_AjA0bE0CtKcfc">init(dashLength:<wbr/>dashWidth:<wbr/>image:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a uniform dash pattern in which the length of a gap is the same as the length of
a dash. Dashes are rendered as image.</p>
<p>This allows for patterns like <code>' — — — —'</code> or <code>'  ——  ——  ——'</code>.</p>
<p>For <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> supplied for <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code> and <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">dashWidth</a></code>,
only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported for <code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">MapMeasureDependentRenderSize.measureKind</a></code>
and only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">RenderSize.Unit.meters</a></code> is supported for <code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">MapMeasureDependentRenderSize.sizeUnit</a></code>.</p>
<p>Only map measure values in range [3-19] are supported.</p>
<p>The value of the keys in <code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code> is truncated to integer values,
hence only a single value can be provided per zoom level.</p>
<p>The values are interpolated linearly between zoom levels.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">dashLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">dashWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>dashLength</em>
</code>
</td>
<td>
<div>
<p>The map measure dependent length of a dash, to which image width is stretched.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>dashWidth</em>
</code>
</td>
<td>
<div>
<p>The map measure dependent width of a dash, to which image height is stretched.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>image</em>
</code>
</td>
<td>
<div>
<p>Image to be rendered in place of dash space. It is stretched to match <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">dashWidth</a></code> and <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code>.</p>
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
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLength03gapH00G5Width5imageAeA0B26MeasureDependentRenderSizeV_A2kA0bE0CtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(dashLength:gapLength:dashWidth:image:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLength03gapH00G5Width5imageAeA0B26MeasureDependentRenderSizeV_A2kA0bE0CtKcfc">init(dashLength:<wbr/>gapLength:<wbr/>dashWidth:<wbr/>image:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a simple dash pattern in which the lengths of a dash and gap can be different.
Dashes are rendered as image.</p>
<p>This allows for patterns like <code>'  —  —  —  —'</code> or <code>' ——— ——— ———'</code>.</p>
<p>For <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> supplied for <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code>, <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a></code> and <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">dashWidth</a></code>,
only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported for <code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV11measureKindAA0bC0V0H0Ovp">MapMeasureDependentRenderSize.measureKind</a></code>
and only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">RenderSize.Unit.meters</a></code> is supported for <code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV8sizeUnitAA0eF0V0H0Ovp">MapMeasureDependentRenderSize.sizeUnit</a></code>.</p>
<p>Only map measure values in range [3-19] are supported.</p>
<p>The value of the keys in <code><a href="../../Structs/MapMeasureDependentRenderSize.html#/s:7heresdk29MapMeasureDependentRenderSizeV5sizesSDyS2dGvp">MapMeasureDependentRenderSize.sizes</a></code> is truncated to integer values,
hence only a single value can be provided per zoom level.</p>
<p>The values are interpolated linearly between zoom levels.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">dashLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">gapLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">dashWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>dashLength</em>
</code>
</td>
<td>
<div>
<p>The map measure dependent length of a dash, to which image width is stretched.</p>
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
<p>The map measure dependent length of a gap between dash images.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>dashWidth</em>
</code>
</td>
<td>
<div>
<p>The map measure dependent width of a dash, to which image height is stretched.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>image</em>
</code>
</td>
<td>
<div>
<p>Image to be rendered in place of dash space. It is stretched to match <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">dashWidth</a></code> and <code><a href="../../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a></code>.</p>
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
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dashImage"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp">dashImage</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Image to be rendered in place of dash space.
It is stretched to fill whole polyline width and length of each dash.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dashImage</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dashLength"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">dashLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map measure dependent length of a dash, to which image width is stretched.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dashLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/gapLength"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">gapLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map measure dependent length of a gap between dash images.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">gapLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/dashWidth"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">dashWidth</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map measure dependent width of a dash, to which image height is stretched.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">dashWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
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
