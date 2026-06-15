---
title: "Venue"
slug: "sdk-for-ios-navigate-api-reference-classes-venue"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/Venue"></a>
<a title="Venue Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-venues">Venues</a>

        Venue Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>Venue</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">Venue</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Venue</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">Venue</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Controls the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> inside the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemap">VenueMap</a></code> object.
The venue controls the selection of the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuedrawing">VenueDrawing</a></code> and the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code>
of the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code>. It provides the possibility to customize styles for the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometry">VenueGeometry</a></code>.
Objects of this class can only be created using methods
<code>VenueMap.addVenueAsync(String, VenueLoadErrorHandler)</code> and <code>VenueMap.selectVenueAsync(String, VenueLoadErrorHandler)</code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC10venueModelAA0bD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueModel"></a>
<a class="token" href="#/s:7heresdk5VenueC10venueModelAA0bD0Cvp">venueModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code> controlled by this object.
It can be used to get the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code>
belonging to this object, like a building or a complex of buildings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC10venueStyleAA0bD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueStyle"></a>
<a class="token" href="#/s:7heresdk5VenueC10venueStyleAA0bD0Cvp">venueStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-venuestyle">VenueStyle</a></code> associated with the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuemodel">VenueModel</a></code>
controlled by this object.
It can be used to get the style of the venue. Contains the information about
the geometry and label styles available for the venue.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueStyle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuestyle">VenueStyle</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC15selectedDrawingAA0bD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/selectedDrawing"></a>
<a class="token" href="#/s:7heresdk5VenueC15selectedDrawingAA0bD0Cvp">selectedDrawing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The selected drawing.
Only the selected drawing will be visible as active on the map. All others will be
hidden or displayed without details, depending on the implementation of the renderer.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">selectedDrawing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuedrawing">VenueDrawing</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC13selectedLevelAA0bD0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/selectedLevel"></a>
<a class="token" href="#/s:7heresdk5VenueC13selectedLevelAA0bD0Cvp">selectedLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The selected level.
Only the selected level will be visible as active on the map. All others will be
hidden or displayed without details, depending on a renderer implementation.
If the level doesn’t belong to the currently selected drawing, it can not be selected.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">selectedLevel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC19selectedLevelZIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/selectedLevelZIndex"></a>
<a class="token" href="#/s:7heresdk5VenueC19selectedLevelZIndexs5Int32Vvp">selectedLevelZIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The Z index value of the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code> selected.
Z index 0 represents the ground level, negative values represent
underground levels, positive values - levels above the ground.
Z index can also be taken from <code><a href="../Classes/VenueLevel.html#/s:7heresdk10VenueLevelC6zIndexs5Int32Vvp">VenueLevel.zIndex</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">selectedLevelZIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC18selectedLevelIndexs5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/selectedLevelIndex"></a>
<a class="token" href="#/s:7heresdk5VenueC18selectedLevelIndexs5Int32Vvp">selectedLevelIndex</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The index of the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuelevel">VenueLevel</a></code> selected from the level array
of the <code><a href="sdk-for-ios-navigate-api-reference-classes-venuedrawing">VenueDrawing</a></code>.
Unlike the Z index, it can’t have a negative value.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">selectedLevelIndex</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC17isTopologyVisibleSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTopologyVisible"></a>
<a class="token" href="#/s:7heresdk5VenueC17isTopologyVisibleSbvp">isTopologyVisible</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns true if topology is visible.
It can be used to check the status of topology visibility.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTopologyVisible</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk5VenueC14setCustomStyle10geometries5style05labelE0ySayAA0B8GeometryCG_AA0biE0CSgAA0b5LabelE0CSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomStyle(geometries:style:labelStyle:)"></a>
<a class="token" href="#/s:7heresdk5VenueC14setCustomStyle10geometries5style05labelE0ySayAA0B8GeometryCG_AA0biE0CSgAA0b5LabelE0CSgtF">setCustomStyle(geometries:<wbr/>style:<wbr/>labelStyle:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom style for geometries and related labels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomStyle</span><span class="p">(</span><span class="nv">geometries</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometry">VenueGeometry</a></span><span class="p">],</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometrystyle">VenueGeometryStyle</a></span><span class="p">?,</span> <span class="nv">labelStyle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuelabelstyle">VenueLabelStyle</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometries</em>
</code>
</td>
<td>
<div>
<p>The list of geometries to apply the new style.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>The style for geometries, or <code>nil</code> to reset the style to default.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>labelStyle</em>
</code>
</td>
<td>
<div>
<p>The style for geometry labels, or <code>nil</code> to reset the label style to default.</p>
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
<a name="/s:7heresdk5VenueC14setCustomStyle10topologies5styleySayAA0B8TopologyCG_AA0b8GeometryE0CSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomStyle(topologies:style:)"></a>
<a class="token" href="#/s:7heresdk5VenueC14setCustomStyle10topologies5styleySayAA0B8TopologyCG_AA0b8GeometryE0CSgtF">setCustomStyle(topologies:<wbr/>style:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom style for topologies.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomStyle</span><span class="p">(</span><span class="nv">topologies</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuetopology">VenueTopology</a></span><span class="p">],</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometrystyle">VenueGeometryStyle</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>topologies</em>
</code>
</td>
<td>
<div>
<p>The list of topologies to apply the new style.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>The style for geometries, or <code>nil</code> to reset the style to default.</p>
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
<a name="/s:7heresdk5VenueC25setCustomStyleToCrosswalk10crosswalks5styleySayAA0G0CG_AA0b8GeometryE0CSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setCustomStyleToCrosswalk(crosswalks:style:)"></a>
<a class="token" href="#/s:7heresdk5VenueC25setCustomStyleToCrosswalk10crosswalks5styleySayAA0G0CG_AA0b8GeometryE0CSgtF">setCustomStyleToCrosswalk(crosswalks:<wbr/>style:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets a custom style for crosswalk.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setCustomStyleToCrosswalk</span><span class="p">(</span><span class="nv">crosswalks</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-crosswalk">Crosswalk</a></span><span class="p">],</span> <span class="nv">style</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-venuegeometrystyle">VenueGeometryStyle</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>crosswalks</em>
</code>
</td>
<td>
<div>
<p>The list of crosswalk to apply the new style.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>style</em>
</code>
</td>
<td>
<div>
<p>The style for geometries, or <code>nil</code> to reset the style to default.</p>
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
} </HTMLBlock>
