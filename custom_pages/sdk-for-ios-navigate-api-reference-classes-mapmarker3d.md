---
title: "sdk-for-ios-navigate-api-reference-classes-mapmarker3d"
slug: "sdk-for-ios-navigate-api-reference-classes-mapmarker3d"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarker3D"></a>
<a title="MapMarker3D Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapMarker3D Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMarker3D</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarker3D</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3D</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker3D</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Represents a 3D shape drawn on the map at specified geodetic coordinates.</p>
<p>It can have a solid color or be textured, depending on the data from
<code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></code>.</p>
<p>By default, a 3D marker is drawn on top of all map content, including
3D map elements like extruded buildings or 3D landmarks. This can be
changed by enabling depth check using <code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp">MapMarker3D.isDepthCheckEnabled</a></code>.</p>
<p>The display of a 3D marker is only guaranteed in case its origin is within
the viewport. At the moment, this is a known limitation that mostly affects
a 3D marker that is visually large and covers a sizeable part of the viewport.</p>
<h1 class="heading" id="sizing-and-scaling">Sizing and scaling</h1>
<p>Two aspects determine how big the <code>MapMarker3D</code> will be on the screen
and how will it behave when the map is zoomed in and out.</p>
<p>The first, and most impactful is <code><a href="sdk-for-ios-navigate-api-reference-structs-rendersize-unit">RenderSize.Unit</a></code>, which specifies
how the vertex coordinates of the 3D model are interpreted.
Most importantly, it specifies whether the 3D model is placed
in world or screen coordinate space.</p>
<p><code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">RenderSize.Unit.meters</a></code> will make the 3D model use world
coordinate space, meaning that it will change size together with the map
when it is zoomed in and out.</p>
<p><code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> makes the 3D model use screen coordinate space,
meaning that it will have constant size on the screen regardless
of how the map zoom changes. So a simple 10 by 10 (in model space) rectangle
will have a size of 10 by 10 pixels on the screen.</p>
<p><code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">RenderSize.Unit.densityIndependentPixels</a></code> is similar to pixels,
but the resulting size will take into account the pixel density of the
display, meaning that physical size on the screen will be approximately
the same regardless of the size or resolution of the display.</p>
<p>The second aspect that determines size of <code>MapMarker3D</code> is scale.
It can be specified at construction time and can be changed later
at any time using <code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC5scaleSdvp">MapMarker3D.scale</a></code>.</p>
<h1 class="heading" id="modifying-at-runtime">Modifying at runtime</h1>
<p>A 3D marker can be moved around a map by updating its coordinates using
<code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">MapMarker3D.coordinates</a></code>.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Its orientation is specified by bearing, pitch and roll and can be changed
by using <code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC7bearingSdvp">MapMarker3D.bearing</a></code>, <code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC5pitchSdvp">MapMarker3D.pitch</a></code>
and <code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC4rollSdvp">MapMarker3D.roll</a></code>.</p>
<h1 class="heading" id="flat-marker">Flat marker</h1>
<p>A flat marker is a special case of a 3D marker, where the 3D shape being drawn
is a simple textured rectangle. In essence it’s an image drawn “on the ground”.
Such 3D marker can be conveniently created using
<code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit)</code>
constructor. Of course, once created, it can be rotated to face any direction.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC2at5modelAcA14GeoCoordinatesV_AA0bC6DModelCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:model:)"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC2at5modelAcA14GeoCoordinatesV_AA0bC6DModelCtcfc">init(at:<wbr/>model:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of a 3D marker.</p>
<p>The origin of the 3D model’s local coordinate system is placed at the specified
geographical coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">at</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">model</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>at</em>
</code>
</td>
<td>
<div>
<p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
3D model’s local coordinate system.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>model</em>
</code>
</td>
<td>
<div>
<p>The 3D model used to draw 3D marker.</p>
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
<a name="/s:7heresdk11MapMarker3DC2at5image5scale4unitAcA14GeoCoordinatesV_AA0B5ImageCSdAA10RenderSizeV4UnitOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:image:scale:unit:)"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC2at5image5scale4unitAcA14GeoCoordinatesV_AA0B5ImageCSdAA10RenderSizeV4UnitOtcfc">init(at:<wbr/>image:<wbr/>scale:<wbr/>unit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a flat marker from provided map image.</p>
<p>Such map marker is a flat 3D marker of rectangular shape textured with given image.
Aspect ratio of the flat marker is determined by aspect ratio of the image.</p>
<p>Only bitmap images are supported, using a <code><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></code> created from SVG data
will result in distorted rendering of the flat marker.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
<p>Size of the rendered flat marker can be specified in either world or screen coordinate space.</p>
<p>For <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code>, the flat marker will cover <code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale</code> * image’s width pixels
horizontally and <code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale</code> * image’s height pixels vertically. The size of the flat marker
remains constant on the screen.</p>
<p>For <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">RenderSize.Unit.densityIndependentPixels</a></code> the flat marker will cover <code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale</code> *
image’s width density independent pixels horizontally and <code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale</code> * image’s height
density independent pixels vertically. The size of the flat marker remains constant on
the screen.</p>
<p>For <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">RenderSize.Unit.meters</a></code> the flat marker will cover <code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale</code> * image’s width meters
horizontally and <code>MapMarker3D.init(GeoCoordinates, MapImage, Double, RenderSize.Unit).scale</code> * image’s height meters vertically. Unlike with pixels or
density independent pixels the size of the flat marker will grow and shrink together
with regular map content like streets or buildings.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">at</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">,</span> <span class="nv">scale</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">unit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rendersize">RenderSize</a></span><span class="o">.</span><span class="kt">Unit</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>at</em>
</code>
</td>
<td>
<div>
<p>The geographical coordinates where the flat marker is placed corresponding to center of the
provided map image.</p>
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
<p>The MapImage containing the texture data of the flat marker. SVG images are not supported.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scale</em>
</code>
</td>
<td>
<div>
<p>Scale factor applied to the dimensions of the image.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>unit</em>
</code>
</td>
<td>
<div>
<p>Determines whether the size of the flat marker is represented in world or in screen space.</p>
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
<a name="/s:7heresdk11MapMarker3DC2at5model5scaleAcA14GeoCoordinatesV_AA0bC6DModelCSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:model:scale:)"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC2at5model5scaleAcA14GeoCoordinatesV_AA0bC6DModelCSdtcfc">init(at:<wbr/>model:<wbr/>scale:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of a 3D marker with scale factor.</p>
<p>One unit of the 3D marker model will cover <code>MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double).scale</code> pixels.
The size of the 3D marker remains constant on the screen.</p>
<p>The origin of the 3D model’s local coordinate system is placed at the specified
geographical coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">at</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">model</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></span><span class="p">,</span> <span class="nv">scale</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>at</em>
</code>
</td>
<td>
<div>
<p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
3D model’s local coordinate system.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>model</em>
</code>
</td>
<td>
<div>
<p>The 3D model used to render the 3D marker.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scale</em>
</code>
</td>
<td>
<div>
<p>Scale factor to apply to the 3D model.</p>
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
<a name="/s:7heresdk11MapMarker3DC2at5model5scale4unitAcA14GeoCoordinatesV_AA0bC6DModelCSdAA10RenderSizeV4UnitOtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:model:scale:unit:)"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC2at5model5scale4unitAcA14GeoCoordinatesV_AA0bC6DModelCSdAA10RenderSizeV4UnitOtcfc">init(at:<wbr/>model:<wbr/>scale:<wbr/>unit:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new 3D marker at given world coordinates, using the supplied 3D model.</p>
<p>The unit specifies how the 3D geometry of the model is interpreted (meters for world space,
pixels or density independent pixels for screen space), while scale determines its relative size.</p>
<p>For <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6pixelsyA2EmF">RenderSize.Unit.pixels</a></code> one unit of the 3D marker model will cover <code>MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double, RenderSize.Unit).scale</code> pixels.
The size of the 3D marker remains constant on the screen.</p>
<p>For <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO24densityIndependentPixelsyA2EmF">RenderSize.Unit.densityIndependentPixels</a></code> one unit of the 3D marker model will
cover <code>MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double, RenderSize.Unit).scale</code> density independent pixels. The size of the 3D marker remains constant on
the screen.</p>
<p>For <code><a href="../Structs/RenderSize/Unit.html#/s:7heresdk10RenderSizeV4UnitO6metersyA2EmF">RenderSize.Unit.meters</a></code> one unit of the 3D marker model will cover <code>MapMarker3D.init(GeoCoordinates, MapMarker3DModel, Double, RenderSize.Unit).scale</code> meters
in the real world. Unlike with pixels or density-independent pixels the size of the
3D marker will grow and shrink together with regular map content like streets or buildings.</p>
<p>The origin of the 3D model’s local coordinate system is placed at the specified
geographical coordinates.</p>
<p>Altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">at</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">model</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></span><span class="p">,</span> <span class="nv">scale</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">unit</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-rendersize">RenderSize</a></span><span class="o">.</span><span class="kt">Unit</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>at</em>
</code>
</td>
<td>
<div>
<p>The geographical coordinates where the 3D marker is placed corresponding to origin of the
3D model’s local coordinate system.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>model</em>
</code>
</td>
<td>
<div>
<p>The 3D model used to render the 3D marker.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>scale</em>
</code>
</td>
<td>
<div>
<p>Scale factor to apply to the 3D model.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>unit</em>
</code>
</td>
<td>
<div>
<p>Determines the unit of the model vertices and whether the size of the 3D marker
is expressed in world or screen space.</p>
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
<a name="/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The position of the 3D marker on the map corresponding to the origin of the 3D marker model coordinate system.
The altitude component of the coordinates, if set, controls 3D marker’s elevation
above ground. If not set, the 3D marker is placed at ground level.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC8metadataAA8MetadataCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/metadata"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC8metadataAA8MetadataCSgvp">metadata</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></code> instance attached to this 3D marker.
The default value is <code>nil</code></p>
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
<a name="/s:7heresdk11MapMarker3DC7bearingSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearing"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC7bearingSdvp">bearing</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The bearing of the 3D model in degrees, from the true North in clockwise direction.
The bearing axis is perpendicular to the ground and passes through the 3D marker’s location.
The Z-axis of the model is aligned with bearing axis.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearing</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC4rollSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roll"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC4rollSdvp">roll</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The roll angle of the 3D model in degrees.
The roll axis is parallel to the ground, passes through the 3D marker’s
location and is aligned initially with the true North. However, when the bearing changes,
it rotates around the bearing axis with the 3D marker.
Positive/negative values cause a clockwise/counterclockwise rotation when viewing along the axis
in the direction of the true North. The Y-axis of the model is aligned with the roll axis.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roll</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC5pitchSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pitch"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC5pitchSdvp">pitch</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The pitch of the 3D model in degrees.
The pitch axis is parallel to the ground, passes through the location of the 3D marker
and aligns with the longitude axis if the bearing is 0. However, this axis rotates with
the 3D marker according to the bearing value. Negative values cause the top of the
3D marker to lean forward. The X-axis of the model is aligned with pitch axis.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">pitch</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC5scaleSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/scale"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC5scaleSdvp">scale</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Scale factor applied to the 3D model before rendering.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">scale</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isDepthCheckEnabled"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC19isDepthCheckEnabledSbvp">isDepthCheckEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines whether the depth of the 3D marker’s vertices is considered during rendering.
If set to <code>false</code>, the 3D marker will always appear in front of any other map objects.
If set to <code>true</code> the 3D marker might be occluded by other map objects like extruded buildings.</p>
<p>By default depth check is set to <code>false</code>.</p>
<p>Use the altitude of the <code><a href="../Classes/MapMarker3D.html#/s:7heresdk11MapMarker3DC11coordinatesAA14GeoCoordinatesVvp">MapMarker3D.coordinates</a></code> to position the 3D marker sufficiently high above the
surface. Setting depth check to <code>true</code> will fix visual glitches where components of the marker
3D model unexpectedly shine through.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isDepthCheckEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC24isRenderInternalsEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isRenderInternalsEnabled"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC24isRenderInternalsEnabledSbvp">isRenderInternalsEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether to render internal geometry of a 3D marker occluded by its front facing polygons.
Default value is <code>false</code>. Can be used with translucent 3D marker.</p>
<p>Note: with this flag enabled for 3D marker with depth check enabled, rendering is performed in two
passes: first pass with front-face, second pass with back-face culling enabled.
With this flag enabled for 3D marker with depth check disabled rendering is performed in a
single pass with back-face culling disabled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isRenderInternalsEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC7opacitySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/opacity"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC7opacitySdvp">opacity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The opacity factor adjusting the opacity of a 3D marker.
Provided value is clamped to the [0.0, 1.0] range. The factor is applied to the alpha channel of the resulting texture of the marker.
Default value is 1.0 meaning marker is displayed with the default opacity of the texture image or the
specified fill color specified
in <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker3dmodel">MapMarker3DModel</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">opacity</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapMarker3DC16visibilityRangesSayAA0B12MeasureRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/visibilityRanges"></a>
<a class="token" href="#/s:7heresdk11MapMarker3DC16visibilityRangesSayAA0B12MeasureRangeVGvp">visibilityRanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of visibility ranges. The 3D marker is visible only inside these map measure ranges.
A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the 3D marker is visible without map measure restrictions.
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
