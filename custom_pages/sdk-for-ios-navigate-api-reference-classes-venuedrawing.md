---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-venuedrawing"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- VenueDrawing.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/VenueDrawing"></a>
<a title="VenueDrawing Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-venues">Venues</a>
<img alt="" id="carat" src="../img/carat.png"/>
        VenueDrawing Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>VenueDrawing</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">VenueDrawing</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueDrawing</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">VenueDrawing</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a drawing inside the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venuemodel">VenueModel</a></code>. The drawing can be
a separate building in a complex of buildings, or show a different
view of a venue. For example, in an airport, one drawing can be used
as an overview of all buildings in this venue, while other drawings
contains details for each terminal in this airport.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC13GeometryArraya"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/GeometryArray"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC13GeometryArraya">GeometryArray</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">GeometryArray</span> <span class="o">=</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry">VenueGeometry</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC19StringToPropertyMapa"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/StringToPropertyMap"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC19StringToPropertyMapa">StringToPropertyMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">StringToPropertyMap</span> <span class="o">=</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-property">Property</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC10LevelArraya"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/LevelArray"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC10LevelArraya">LevelArray</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">LevelArray</span> <span class="o">=</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuelevel">VenueLevel</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC24StringToGeometryArrayMapa"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/StringToGeometryArrayMap"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC24StringToGeometryArrayMapa">StringToGeometryArrayMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">StringToGeometryArrayMap</span> <span class="o">=</span> <span class="p">[</span><span class="kt">String</span> <span class="p">:</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC13GeometryArraya">GeometryArray</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC11DoubleArraya"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/DoubleArray"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC11DoubleArraya">DoubleArray</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">DoubleArray</span> <span class="o">=</span> <span class="p">[</span><span class="kt">Double</span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC13TopologyArraya"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/TopologyArray"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC13TopologyArraya">TopologyArray</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Undocumented</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">TopologyArray</span> <span class="o">=</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuetopology">VenueTopology</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC10identifierSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/identifier"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC10identifierSSvp">identifier</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code>id</code> of the drawing.
This describes the identifier for drawing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">identifier</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC8isIsRootSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isIsRoot"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC8isIsRootSbvp">isIsRoot</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p><code>True</code> if this is the root drawing and <code>false</code> otherwise.
This can be used to check if this is top level
drawing in venue.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isIsRoot</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC10venueModelAA0bE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/venueModel"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC10venueModelAA0bE0Cvp">venueModel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The parent venue model.
It can be used to get the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venuemodel">VenueModel</a></code>
where this Drawing belong.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">venueModel</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuemodel">VenueModel</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC6levelsSayAA0B5LevelCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/levels"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC6levelsSayAA0B5LevelCGvp">levels</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The array with Level objects.
This describes for which all level this
drawing belongs.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">levels</span><span class="p">:</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC10LevelArraya">LevelArray</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC6centerAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/center"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC6centerAA14GeoCoordinatesVvp">center</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The Geographic coordinates of the center of the drawing.
It can be used to get center coordinates of drawing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">center</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC11boundingBoxAA03GeoE0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/boundingBox"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC11boundingBoxAA03GeoE0Vvp">boundingBox</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></code> of the bounding area of the drawing.
This is used to check if at certain zoom level
and inside view this GeoBox belongs, then need to render.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">boundingBox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geobox">GeoBox</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC10propertiesSDySSAA8PropertyCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/properties"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC10propertiesSDySSAA8PropertyCGvp">properties</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The key-value pairs of properties.
This can be used to get different properties
like name belonging to Drawing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">properties</span><span class="p">:</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC19StringToPropertyMapa">StringToPropertyMap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC16geometriesByNameSayAA0B8GeometryCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometriesByName"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC16geometriesByNameSayAA0B8GeometryCGvp">geometriesByName</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The geometries ordered by the name.
This can be used to search geometries by name.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geometriesByName</span><span class="p">:</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC13GeometryArraya">GeometryArray</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC21geometriesByIconNamesSDySSSayAA0B8GeometryCGGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/geometriesByIconNames"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC21geometriesByIconNamesSDySSSayAA0B8GeometryCGGvp">geometriesByIconNames</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The map from the icon names to the geometries in the drawing.
This can be used to search the geometries by icon names.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">geometriesByIconNames</span><span class="p">:</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC24StringToGeometryArrayMapa">StringToGeometryArrayMap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC10topologiesSayAA0B8TopologyCGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/topologies"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC10topologiesSayAA0B8TopologyCGvp">topologies</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of topologies of the drawing.
This can be used to check for which
all topologies are realted to Drawing.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">topologies</span><span class="p">:</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC13TopologyArraya">TopologyArray</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC15getGeometryById08geometryG0AA0bE0CSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeometryById(geometryId:)"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC15getGeometryById08geometryG0AA0bE0CSgSS_tF">getGeometryById(geometryId:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a geometry by an id.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeometryById</span><span class="p">(</span><span class="nv">geometryId</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry">VenueGeometry</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometryId</em>
</code>
</td>
<td>
<div>
<p>The id of the geometry.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The geometry with the given id or <code>nil</code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC20getGeometryByAddress08geometryG0AA0bE0CSgSS_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeometryByAddress(geometryAddress:)"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC20getGeometryByAddress08geometryG0AA0bE0CSgSS_tF">getGeometryByAddress(geometryAddress:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets a geometry by the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry-internaladdress">VenueGeometry.InternalAddress</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeometryByAddress</span><span class="p">(</span><span class="nv">geometryAddress</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-venuegeometry">VenueGeometry</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geometryAddress</em>
</code>
</td>
<td>
<div>
<p>The internal address as a String.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The geometry with the given address or <code>nil</code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk12VenueDrawingC14filterGeometry0D00D4TypeSayAA0bE0CGSS_AA0be6FilterF0OtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/filterGeometry(filter:filterType:)"></a>
<a class="token" href="#/s:7heresdk12VenueDrawingC14filterGeometry0D00D4TypeSayAA0bE0CGSS_AA0be6FilterF0OtF">filterGeometry(filter:<wbr/>filterType:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets filtered geometries in an ascending order.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">filterGeometry</span><span class="p">(</span><span class="nv">filter</span><span class="p">:</span> <span class="kt">String</span><span class="p">,</span> <span class="nv">filterType</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-enums-venuegeometryfiltertype">VenueGeometryFilterType</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt">VenueDrawing</span><span class="o">.</span><span class="kt"><a href="../Classes/VenueDrawing.html#/s:7heresdk12VenueDrawingC13GeometryArraya">GeometryArray</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>filter</em>
</code>
</td>
<td>
<div>
<p>The filter string.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>filterType</em>
</code>
</td>
<td>
<div>
<p>The filter type.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The list of the filtered geometries or an empty list.</p>
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
