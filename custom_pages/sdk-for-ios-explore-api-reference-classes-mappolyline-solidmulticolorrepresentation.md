---
title: "sdk-for-ios-explore-api-reference-classes-mappolyline-solidmulticolorrepresentation"
slug: "sdk-for-ios-explore-api-reference-classes-mappolyline-solidmulticolorrepresentation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/SolidMultiColorRepresentation"></a>
<a title="SolidMultiColorRepresentation Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-maps">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        SolidMultiColorRepresentation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SolidMultiColorRepresentation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SolidMultiColorRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
<p>Representation allows map polyline to be colored in multiple specified color segments.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code><a href="../../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">MapPolyline.progressColor</a></code> overrides any of the multiple color.</p>
<p>Examples:
The following configuration will color map polyline as follows:</p>
<ul>
<li>from the start to the middle of it at the 0.5 point - in Red</li>
<li>from the middle point 0.5 to the 0.7 point - in Green</li>
<li>from 0.7 to 1.0 - in Red
‘colorStops: {0.0, 0.5, 0.7}, colorIndices: {0, 1, 0}, colors: {Red, Green}’</li>
</ul>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC9lineWidth8capShape10colorStops0L7Indices6colors14gradientLengthAeA0B26MeasureDependentRenderSizeV_AA7LineCapOSaySdGSays6UInt32VGSaySo7UIColorCGSdtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lineWidth:capShape:colorStops:colorIndices:colors:gradientLength:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC9lineWidth8capShape10colorStops0L7Indices6colors14gradientLengthAeA0B26MeasureDependentRenderSizeV_AA7LineCapOSaySdGSays6UInt32VGSaySo7UIColorCGSdtKcfc">init(lineWidth:<wbr/>capShape:<wbr/>colorStops:<wbr/>colorIndices:<wbr/>colors:<wbr/>gradientLength:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a representation for a multicolored line without an outline.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code><a href="../../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">MapPolyline.progressColor</a></code> overrides any of the multiple color.</p>
<p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the smallest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
line width is constant and equal to the width given for the biggest
map measure in the <code>lineWidth</code>.</p>
<p>At map measures between two nearest given map measures line width is
linearly interpolated between width values given for these map measures.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<p><code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.</p>
</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">capShape</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-linecap">LineCap</a></span><span class="p">,</span> <span class="nv">colorStops</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span><span class="p">],</span> <span class="nv">colorIndices</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt32</span><span class="p">],</span> <span class="nv">colors</span><span class="p">:</span> <span class="p">[</span><span class="kt">UIColor</span><span class="p">],</span> <span class="nv">gradientLength</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<em>capShape</em>
</code>
</td>
<td>
<div>
<p>The cap shape applied to both ends of the polyline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colorStops</em>
</code>
</td>
<td>
<div>
<p>List containing color stop values indicating a change of color on a polyline.
Color stops must be in the range of [0.0, 1.0].
Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
Color stop list must be of the same size as color indices list.
Maximum size is 100 color stops.
An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colorIndices</em>
</code>
</td>
<td>
<div>
<p>List of color indices (from the color list) corresponding to the color stops.
Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
Color indices list must be of the same size as color stop list.
Maximum size is 100 color indices.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colors</em>
</code>
</td>
<td>
<div>
<p>List of colors.
Maximum size is 16 colors.
An empty list is not allowed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>gradientLength</em>
</code>
</td>
<td>
<div>
<p>Multiple color segment gradient length.</p>
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
<a name="/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC9lineWidth07outlineI00jF08capShape10colorStops0M7Indices6colors14gradientLengthAeA0B26MeasureDependentRenderSizeV_AOSo7UIColorCAA7LineCapOSaySdGSays6UInt32VGSayAQGSdtKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lineWidth:outlineWidth:outlineColor:capShape:colorStops:colorIndices:colors:gradientLength:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC9lineWidth07outlineI00jF08capShape10colorStops0M7Indices6colors14gradientLengthAeA0B26MeasureDependentRenderSizeV_AOSo7UIColorCAA7LineCapOSaySdGSays6UInt32VGSayAQGSdtKcfc">init(lineWidth:<wbr/>outlineWidth:<wbr/>outlineColor:<wbr/>capShape:<wbr/>colorStops:<wbr/>colorIndices:<wbr/>colors:<wbr/>gradientLength:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a representation for a multicolored line with an outline.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code><a href="../../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">MapPolyline.progressColor</a></code> overrides any of the multiple color.</p>
<p>The total width of the polyline is <code>line width + 2 * outline width</code>.</p>
<p>At map measures smaller than smallest map measure in the <code>lineWidth</code>
and <code>outlineWidth</code>, the value is constant and equal to the width given for
the smallest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.</p>
<p>At map measures bigger than biggest map measure in the <code>lineWidth</code>
and <code>outlineWidth</code>, the value is constant and equal to the width given for
the biggest map measure in the <code>lineWidth</code> and <code>outlineWidth</code>.</p>
<p>At map measures between two nearest given map measure is
linearly interpolated between width values given for these map measures.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-explore-api-reference-..-..-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<p><code>lineWidth</code> must not be 0 (<code>lineWidth.sizes</code> with all values set to 0.0).</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<p><code><a href="../../Classes/MapPolyline/Representation.html#/s:7heresdk11MapPolylineC14RepresentationC18InstantiationErrora">MapPolyline.Representation.InstantiationError</a></code> In case of invalid input parameters.</p>
</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">outlineWidth</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span><span class="p">,</span> <span class="nv">outlineColor</span><span class="p">:</span> <span class="kt">UIColor</span><span class="p">,</span> <span class="nv">capShape</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-..-enums-linecap">LineCap</a></span><span class="p">,</span> <span class="nv">colorStops</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span><span class="p">],</span> <span class="nv">colorIndices</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt32</span><span class="p">],</span> <span class="nv">colors</span><span class="p">:</span> <span class="p">[</span><span class="kt">UIColor</span><span class="p">],</span> <span class="nv">gradientLength</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="k">throws</span></code></pre>
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
<em>outlineWidth</em>
</code>
</td>
<td>
<div>
<p>The width of the outline on one side of the polyline depending on the map measure.</p>
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
<tr>
<td>
<code>
<em>colorStops</em>
</code>
</td>
<td>
<div>
<p>List containing color stop values indicating a change of color on a polyline.
Color stops must be in the range of [0.0, 1.0].
Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
Color stop list must be of the same size as color indices list.
Maximum size is 100 color stops.
An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colorIndices</em>
</code>
</td>
<td>
<div>
<p>List of color indices (from the color list) corresponding to the color stops.
Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
Color indices list must be of the same size as color stop list.
Maximum size is 100 color indices.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colors</em>
</code>
</td>
<td>
<div>
<p>List of colors.
Maximum size is 16 colors.
An empty list is not allowed.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>gradientLength</em>
</code>
</td>
<td>
<div>
<p>Multiple color segment gradient length.</p>
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
<a name="/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC03setE6Colors10colorStops0J7Indices6colorsSbSaySdG_Says6UInt32VGSaySo7UIColorCGtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setMultiColors(colorStops:colorIndices:colors:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC03setE6Colors10colorStops0J7Indices6colorsSbSaySdG_Says6UInt32VGSaySo7UIColorCGtF">setMultiColors(colorStops:<wbr/>colorIndices:<wbr/>colors:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets lists of colors and multiple color segment stops for the polyline to be colored in.
When this representation is already set on any <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code>, values will be applied on that <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code> right away.
If this representation is not set on any <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code>, values will be applied once representation is set on a <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setMultiColors</span><span class="p">(</span><span class="nv">colorStops</span><span class="p">:</span> <span class="p">[</span><span class="kt">Double</span><span class="p">],</span> <span class="nv">colorIndices</span><span class="p">:</span> <span class="p">[</span><span class="kt">UInt32</span><span class="p">],</span> <span class="nv">colors</span><span class="p">:</span> <span class="p">[</span><span class="kt">UIColor</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>colorStops</em>
</code>
</td>
<td>
<div>
<p>List containing color stop values indicating a change of color on a polyline.
Color stops must be in the range of [0.0, 1.0].
Color stop values must be sorted in ascending order (e.g. 0.0, 0.2, 0.3, 1.0). Duplicate values are not allowed.
Color stop list must be of the same size as color indices list.
Maximum size is 100 color stops.
An empty list is not allowed. The first color stop value in the list must be 0.0.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colorIndices</em>
</code>
</td>
<td>
<div>
<p>List of color indices (from the color list) corresponding to the color stops.
Value range is: [0, (color list size - 1)]. Values outside of the range are not allowed.
Color indices list must be of the same size as color stop list.
Maximum size is 100 color indices.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>colors</em>
</code>
</td>
<td>
<div>
<p>List of colors.
Maximum size is 16 colors.
An empty list is not allowed.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Value indicating whether parameters are valid and can be applied.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC03seteF14GradientLength6lengthSbSd_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setMultiColorGradientLength(length:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC03seteF14GradientLength6lengthSbSd_tF">setMultiColorGradientLength(length:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the multiple color segment gradient length.</p>
<p>Colors of two adjacent color segments can be blended to have a nicer visual appeal. Blending produces color
gradient of specific length which is part of the color segment being blended.</p>
<p>Start of the segment is blended with a color from the previous segment.
Blending length is specified as a ratio of the smallest color segment length (from the list of color stops).
E.g. a value of ‘0.1’ means 10% of the length of the smallest segment will be blended with a color from its previous segment.
For this smallest segment gradient length is applied as-is, for all other segments it is scaled proportionally based on the
smallest segment’s size to other segment size ratio.</p>
<p>Length of ‘0.0’ is the default value which means blending will not be applied.
Valid value range is [0.0, 1.0]. Out of range values are not supported.
When this representation is already set on any <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code>, value will be applied on that <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code> right away.
If this representation is not set on any <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code>, value will be applied once representation is set on a <code><a href="sdk-for-ios-explore-api-reference-..-..-classes-mappolyline">MapPolyline</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setMultiColorGradientLength</span><span class="p">(</span><span class="nv">length</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">Bool</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>length</em>
</code>
</td>
<td>
<div>
<p>Multiple color segment gradient length. Length of ‘0.0’ is the default value which means blending will not be applied.
Valid value range is [0.0, 1.0]. Out of range values are not supported.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>Value indicating whether specified value is valid and can be applied.</p>
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
