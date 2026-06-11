---
title: "sdk-for-ios-navigate-api-reference-classes-mappolyline"
slug: "sdk-for-ios-navigate-api-reference-classes-mappolyline"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolyline"></a>
<a title="MapPolyline Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapPolyline Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapPolyline</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPolyline</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolyline</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolyline</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A visual representation of a line on the map.</p>
<p>The geometry to be visualized is represented by an instance of <code><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></code>.</p>
<p>Altitude component of <code><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></code>‘s vertices is ignored.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC8geometry14representationAcA03GeoC0V_AC14RepresentationCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(geometry:representation:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC8geometry14representationAcA03GeoC0V_AC14RepresentationCtcfc">init(geometry:<wbr/>representation:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new <code>MapPolyline</code> instance with a specified visual representation.</p>
<p>Altitude component of <code><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></code>‘s vertices is ignored.</p>
<p>After creating a <code>MapPolyline</code> with this representation, the deprecated <code>MapPolyline</code>
properties do not work and any change to them will be ignored. Any modifications to polyline’s
appearance must be done with <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC17setRepresentationyyAC0E0CF">MapPolyline.setRepresentation(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></span><span class="p">,</span> <span class="nv">representation</span><span class="p">:</span> <span class="kt">MapPolyline</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span><span class="p">)</span></code></pre>
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
<p>The list of vertices representing the polyline.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>representation</em>
</code>
</td>
<td>
<div>
<p>The styling properties of the polyline.</p>
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
<a name="/s:7heresdk11MapPolylineC8geometryAA03GeoC0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometry"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC8geometryAA03GeoC0Vvp">geometry</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of vertices that represent the geometry of the polyline.
Altitude component of <code><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></code>‘s vertices is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geometry</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geopolyline">GeoPolyline</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC8metadataAA8MetadataCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/metadata"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC8metadataAA8MetadataCSgvp">metadata</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></code> instance attached to this polyline.
This will be <code>nil</code> if nothing has been attached before.</p>
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
<a name="/s:7heresdk11MapPolylineC9drawOrders5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/drawOrder"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC9drawOrders5Int32Vvp">drawOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The draw order of the polyline.
Polylines with a higher draw order are drawn on top of
polylines with a lower draw order.</p>
<p>In case multiple polylines have the same draw order, they
can be rendered in different ways depending on the <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp">MapPolyline.drawOrderType</a></code> set.</p>
<p>The value is clamped to the range [0; 1023].
The default draw order is 0.</p>
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
<a name="/s:7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/drawOrderType"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC13drawOrderTypeAA04DraweF0Ovp">drawOrderType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The draw order type of the polyline.
The default value is <code><a href="../Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">DrawOrderType.mapSceneAdditionOrderDependent</a></code>.</p>
<p>For <code><a href="../Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">DrawOrderType.mapSceneAdditionOrderDependent</a></code>, map polylines with outlines having the
same draw order are drawn as a whole in the order of addition to a map scene. There is no
possibility that parts of another polyline, regardless of its draw order value, are drawn
between outline and mainline of another polyline.</p>
<p>With <code><a href="../Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC9DependentyA2CmF">DrawOrderType.mapSceneAdditionOrderDependent</a></code> polylines are rendered one by one.
For <code><a href="../Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">DrawOrderType.mapSceneAdditionOrderIndependent</a></code> for multiple polylines with outlines
having the same draw order, all outlines are rendered first in an arbitrary order and then all
mainlines are drawn on top of those polylines in an arbitrary order.</p>
<p><code><a href="../Enums/DrawOrderType.html#/s:7heresdk13DrawOrderTypeO016mapSceneAdditionC11IndependentyA2CmF">DrawOrderType.mapSceneAdditionOrderIndependent</a></code> allows speeding up the rendering process
and keeping high frame rates when many similar polylines (with same styling attributes and
<code><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">MapPolyline.Representation</a></code>) are present in a map scene.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">drawOrderType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-drawordertype">DrawOrderType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC16visibilityRangesSayAA0B12MeasureRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/visibilityRanges"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC16visibilityRangesSayAA0B12MeasureRangeVGvp">visibilityRanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of visibility ranges. The map polyline is visible only inside these map measure ranges.
A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the map polyline is visible without map measure restrictions.
Only <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasurerange">MapMeasureRange</a></code>(s) of <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> type are supported.
<code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasurerange">MapMeasureRange</a></code>(s) of other unsupported types will be ignored.</p>
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
<a name="/s:7heresdk11MapPolylineC8progressSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/progress"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC8progressSdvp">progress</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The progress from the polyline’s starting point, as a ratio of its total length clamped to
the range [0, 1].
As the progress varies, the equivalent part of the polyline gets covered
by the progress color and progress outline color. The rest of the polyline until its end
point retains the line color and outline color along with an optional dash pattern.</p>
<p>The default progress is 0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">progress</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/progressColor"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">progressColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color used for the progress part of the polyline.
The default progress color is opaque white.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">progressColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC20progressOutlineColorSo7UIColorCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/progressOutlineColor"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC20progressOutlineColorSo7UIColorCvp">progressOutlineColor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The color used for outline of the progress part of the polyline.
The default progress color is opaque white.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">progressOutlineColor</span><span class="p">:</span> <span class="kt">UIColor</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC22progressGradientLengthAA0B26MeasureDependentRenderSizeVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/progressGradientLength"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC22progressGradientLengthAA0B26MeasureDependentRenderSizeVvp">progressGradientLength</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum gradient length between <code>MapPolyline.lineColor' and
'MapPolyline.progressColor</code> in zoom level dependent pixels.
To achieve a constant gradient length, use <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code>
with a single value. To achieve a gradient length dependent on map zoom,
use <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> with multiple values. The default value is a constant
gradient length of zero pixels. The gradient is guaranteed to fit into polyline, i.e. the
actual gradient can be shorter then <code>progressGradientLength</code>.</p>
<p>For <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.
For <code><a href="sdk-for-ios-navigate-api-reference-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.
When setting the attribute with with unsupported values, the operation is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">progressGradientLength</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC27mapContentCategoriesToBlockSayAA0bE8CategoryOGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapContentCategoriesToBlock"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC27mapContentCategoriesToBlockSayAA0bE8CategoryOGvp">mapContentCategoriesToBlock</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of map content categories this polyline should block.
Map content categories overlapping the polyline geometry
(progress and non-progress) will be discarded from being rendered.</p>
<p>Duplicate entries will be ignored and will have no additional effect.</p>
<p>Default value is an empty list meaning none of the map categories will be blocked.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">mapContentCategoriesToBlock</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-mapcontentcategory">MapContentCategory</a></span><span class="p">]</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC14RepresentationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/Representation"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC14RepresentationC">Representation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Base class to represent the visual appearance of a <code><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Representation</span> <span class="p">:</span> <span class="kt"><a href="../Maps.html#/s:7heresdk21MapItemRepresentationC">MapItemRepresentation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC23DashImageRepresentationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DashImageRepresentation"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC23DashImageRepresentationC">DashImageRepresentation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a dash pattern for the map polyline consisting of images rendered with certain gaps
from each other.</p>
<p>This dash pattern representation consists only of images rendered at certain
points along the polyline. For rendering them without any distortions, polyline gets sliced into
series of straight segments that are multiple of sum of dash and gap lengths. For this
reason, the new polyline geometry might not align fully with original geometry.</p>
<p>The <code><a href="../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC04dashE0AA0bE0Cvp">MapPolyline.DashImageRepresentation.dashImage</a></code> is stretched according to <code><a href="../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC10dashLengthAA0B26MeasureDependentRenderSizeVvp">MapPolyline.DashImageRepresentation.dashLength</a></code>
and <code><a href="../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9dashWidthAA0B26MeasureDependentRenderSizeVvp">MapPolyline.DashImageRepresentation.dashWidth</a></code>, with image’s width matched to <code>dashLength</code> and
image’s height matched to <code>dashWidth</code>. The image is oriented so that its bottom is on the
left-hand side between vertices <code>n</code> and <code>n+1</code>.</p>
<p>The spacing between images is specified by <code><a href="../Classes/MapPolyline/DashImageRepresentation.html#/s:7heresdk11MapPolylineC23DashImageRepresentationC9gapLengthAA0B26MeasureDependentRenderSizeVvp">MapPolyline.DashImageRepresentation.gapLength</a></code>.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mappolyline-dashimagerepresentation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DashImageRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC19SolidRepresentationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SolidRepresentation"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC19SolidRepresentationC">SolidRepresentation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Representation for a solid line without outline.</p>
<p>Can represent polylines that have constant width or width dependent on the map zoom.</p>
<p>To achieve constant width lines, use <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> with a single value.</p>
<p>To achieve line width dependent on map zoom, use <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasuredependentrendersize">MapMeasureDependentRenderSize</a></code> with
multiple values.</p>
<p>For <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure-kind">MapMeasure.Kind</a></code> only <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> is supported.</p>
<p>For <code><a href="sdk-for-ios-navigate-api-reference-structs-rendersize-unit">RenderSize.Unit</a></code> only <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> is supported.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mappolyline-solidrepresentation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SolidRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC18DashRepresentationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/DashRepresentation"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC18DashRepresentationC">DashRepresentation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Represents a dash pattern for map polyline where the dash can be rendered as a colored
line and the gap can be either empty or colored.</p>
<p>The length of the dash and gap are set independently, allowing for patterns
like <code>'  —  —  —  —'</code> (dash length = gap length) or <code>' ——— ——— ———'</code> (dash length != gap length).</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mappolyline-dashrepresentation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">DashRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/SolidMultiColorRepresentation"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC29SolidMultiColorRepresentationC">SolidMultiColorRepresentation</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Representation allows map polyline to be colored in multiple specified color segments.</p>
<p>Color segment is defined by color stops. Color stop is specified as a polyline
length ratio (0.0 - start of the polyline, 1.0 - end of the polyline).
Color stop represents a color change starting at that exact point up until
either the next color stop (if one exists) or the end of the polyline.</p>
<p>Progress color <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC13progressColorSo7UIColorCvp">MapPolyline.progressColor</a></code> overrides any of the multiple color.</p>
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
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mappolyline-solidmulticolorrepresentation">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">SolidMultiColorRepresentation</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline">MapPolyline</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapPolylineC17setRepresentationyyAC0E0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setRepresentation(_:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC17setRepresentationyyAC0E0CF">setRepresentation(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Changes the appearance of the <code>MapPolyline</code> instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setRepresentation</span><span class="p">(</span><span class="n">_</span> <span class="nv">representation</span><span class="p">:</span> <span class="kt">MapPolyline</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolyline-representation">Representation</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>representation</em>
</code>
</td>
<td>
<div>
<p>The representation describing a new appearance of the <code>MapPolyline</code>.</p>
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
<a name="/s:7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/startAnimation(_:animationDelegate:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF">startAnimation(_:<wbr/>animationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts an animation of this map polyline.</p>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></code> may be shared between multiple instances of <code>MapPolyline</code>.</p>
<p>Starting animation on one polyline does not influence any ongoing animations on
other polylines.
Any ongoing animation of this map polyline will get cancelled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">startAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">animation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></span><span class="p">,</span> <span class="nv">animationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-animationdelegate">AnimationDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>animation</em>
</code>
</td>
<td>
<div>
<p>The animation to start.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>animationDelegate</em>
</code>
</td>
<td>
<div>
<p>The delegate to receive notifications
about animation start, completion or cancellation.</p>
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
<a name="/s:7heresdk11MapPolylineC15cancelAnimationyyAA0bcE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/cancelAnimation(_:)"></a>
<a class="token" href="#/s:7heresdk11MapPolylineC15cancelAnimationyyAA0bcE0CF">cancelAnimation(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cancels single ongoing animation of this map polyline.</p>
<p>Does nothing if the specified animation is not currently in progress for this polyline.
Does not affect other polylines that might be running this animation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">cancelAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">animation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>animation</em>
</code>
</td>
<td>
<div>
<p>The animation to cancel</p>
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
</body>
</html>

`
}</HTMLBlock>
