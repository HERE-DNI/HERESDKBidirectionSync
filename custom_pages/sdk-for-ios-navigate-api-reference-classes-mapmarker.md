---
title: "sdk-for-ios-navigate-api-reference-classes-mapmarker"
slug: "sdk-for-ios-navigate-api-reference-classes-mapmarker"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapMarker"></a>
<a title="MapMarker Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapMarker Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapMarker</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapMarker</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapMarker</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p><code>MapMarker</code> is used to draw images on the map, for example to mark a specific location.
By default, the marker is centered on the given geographic coordinates.
Markers keep their size regardless of the current zoom level of the map view.</p>
<p>The image to be displayed is represented by <code><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></code> object. For performance reasons,
it is highly recommended to reuse a single instance of the image when creating multiple
identical markers.</p>
<p>To display the map marker, it needs to be added to the scene using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC03addB6MarkeryyAA0bE0CF">MapScene.addMapMarker(...)</a></code>.
To stop displaying it, remove it from the scene using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC06removeB6MarkeryyAA0bE0CF">MapScene.removeMapMarker(...)</a></code>.</p>
<p>The display of a map marker is only guaranteed in case its origin is within the viewport.
At the moment, this is a known limitation that mostly affects map markers which are visually
large and cover a sizeable part of the viewport.</p>
<p><strong>Note:</strong>
Due to technical limitations using the MapMarkers API to add a very large number of markers
(several thousands, especially 10000+) is not recommended. Adding this many markers will have a
negative impact on the performance leading to stuttering of the app and lower frame rates.
To work around this limitation the following approach can be used:
Register to map camera updates using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC11addDelegateyyAA0bcE0_pF">MapCamera.addDelegate(...)</a></code>. Query the bounding box of the
camera viewport using <code><a href="../Classes/MapCamera.html#/s:7heresdk9MapCameraC11boundingBoxAA03GeoE0VSgvp">MapCamera.boundingBox</a></code> (it may be extended)
and then use the method <code>GeoBox.contains(GeoCoordinates)</code> in combination with
<code><a href="../Classes/MapCamera/State.html#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">MapCamera.State.distanceToTargetInMeters</a></code> to determine which MapMarkers are actually visible
to the user in the current camera viewport and thus need to be added to the map.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC2at5imageAcA14GeoCoordinatesV_AA0B5ImageCtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:image:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC2at5imageAcA14GeoCoordinatesV_AA0B5ImageCtcfc">init(at:<wbr/>image:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of a marker at given coordinates, represented by specified image.</p>
<p>The altitude component of the coordinates is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">at</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The marker’s geographical coordinates.</p>
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
<p>The image to draw on the map.</p>
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
<a name="/s:7heresdk9MapMarkerC2at5image4textAcA14GeoCoordinatesV_AA0B5ImageCSStcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:image:text:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC2at5image4textAcA14GeoCoordinatesV_AA0B5ImageCSStcfc">init(at:<wbr/>image:<wbr/>text:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a <code>MapMarker</code> instance at given coordinates with specified image and text and a default text style.</p>
<p>The altitude component of the coordinates is ignored.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">at</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">,</span> <span class="nv">text</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The marker’s geographical coordinates.</p>
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
<p>The image to draw on the map.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>text</em>
</code>
</td>
<td>
<div>
<p>The text to draw on the map.</p>
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
<a name="/s:7heresdk9MapMarkerC2at5image6anchorAcA14GeoCoordinatesV_AA0B5ImageCAA8Anchor2DVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:image:anchor:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC2at5image6anchorAcA14GeoCoordinatesV_AA0B5ImageCAA8Anchor2DVtcfc">init(at:<wbr/>image:<wbr/>anchor:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of a marker at given coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the marker’s coordinates.</p>
<p>The anchor is a way of specifying position offset relative to image’s dimensions on the screen.
For example, (0, 0) places the top-left corner of the image at the marker’s coordinates.
(1, 1) would place the bottom-right corner of the image at the marker’s coordinates.
(0.5, 0.5) which is the default value would center the image at the marker’s coordinates.
Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the marker’s coordinates at the distance
in pixels that is equal to the height of the image.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">at</span> <span class="nv">coordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">,</span> <span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>coordinates</em>
</code>
</td>
<td>
<div>
<p>The marker’s geographical coordinates.</p>
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
<p>The image to draw on the map.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>anchor</em>
</code>
</td>
<td>
<div>
<p>The anchor point for the marker image which specifies the position offset relative
to the marker’s coordinates.</p>
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
<a name="/s:7heresdk9MapMarkerC11coordinatesAA14GeoCoordinatesVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/coordinates"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC11coordinatesAA14GeoCoordinatesVvp">coordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The point on the map where the map marker is drawn.
The altitude component of the coordinates is ignored.</p>
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
<a name="/s:7heresdk9MapMarkerC8metadataAA8MetadataCSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/metadata"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC8metadataAA8MetadataCSgvp">metadata</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The Metadata instance attached to this marker, see <code><a href="sdk-for-ios-navigate-api-reference-classes-metadata">Metadata</a></code>.
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
<a name="/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isOverlapAllowed"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp">isOverlapAllowed</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines whether or not the marker can overlap other markers.
If <code>false</code>, it will disappear the moment it overlaps another marker that has
a higher visibility priority. A marker that allows overlap will always be drawn.
Among markers that don’t allow overlap, the one with the highest draw order has
priority. Marker that is hidden due to overlapping with other markers is not pickable.</p>
<p>Defaults to <code>true</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isOverlapAllowed</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC14isTextOptionalSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isTextOptional"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC14isTextOptionalSbvp">isTextOptional</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Determines if the marker can be displayed with icon and without text.
Controls whenever <code>MapMarker</code> can be shown as icon only when <code><a href="../Classes/MapMarker.html#/s:7heresdk9MapMarkerC16isOverlapAllowedSbvp">MapMarker.isOverlapAllowed</a></code>
is <code>false</code>, has no effect otherwise. If <code>false</code> then the <code>MapMarker</code> will not appear
when icon or text are blocked by other labels.
If <code>true</code>, icon will appear even if the text part is blocked by other labels.</p>
<p>Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isTextOptional</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9drawOrders5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/drawOrder"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9drawOrders5Int32Vvp">drawOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The draw order of this marker relative to other markers.
Markers with higher draw order value are drawn on top of markers with lower draw order.
In case multiple markers have the same draw order value
then the order in which they were added to the scene matters. Last added marker is drawn on top.</p>
<p>Allowed range is [0, 1023]. Values outside this range will be clamped. The default value is 0.</p>
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
<a name="/s:7heresdk9MapMarkerC5imageAA0B5ImageCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/image"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC5imageAA0B5ImageCvp">image</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Image representing the marker on the screen.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC6anchorAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/anchor"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC6anchorAA8Anchor2DVvp">anchor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The anchor point for the marker image which specifies the position offset relative
to the marker’s coordinates.
For example, (0, 0) places the top-left corner of the image at the marker’s coordinates.
(1, 1) would place the bottom-right corner of the image at the marker’s coordinates.
(0.5, 0.5) which is the default value would center the image at the marker’s coordinates.
Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the marker’s coordinates at the distance
in pixels that is equal to the height of the image.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC7opacitySdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/opacity"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC7opacitySdvp">opacity</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Opacity, the factor applied to the alpha channel of the marker image.
Provided value is clamped in range [0.0, 1.0]. Default value is 1.0,
which means marker is displayed with the default opacity of the image.</p>
<p>Markers with opacity value set to 0.0 are still on map and are considered for picking.</p>
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
<a name="/s:7heresdk9MapMarkerC12fadeDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fadeDuration"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC12fadeDurationSdvp">fadeDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Duration of a fade-in effect on marker addition to a scene or a fade-out effect on marker removal from a scene.
Provided value is clamped in range [0.0, 10.0] seconds. Default value is 0 seconds which means the effect is disabled
and marker is added/removed immediately without any animation.</p>
<p>Fade-in effect is also applied when marker leaves and then re-enters screen area.</p>
<p>Change to this property is made asynchronously and is not guaranteed
to take effect on the next rendered frame. In particular, changing fade duration and removing
the marker immediately after may result in the new value being ignored for this removal.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fadeDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC4textSSvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/text"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC4textSSvp">text</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The text to be drawn on the map along with the image of the <code>MapMarker</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">text</span><span class="p">:</span> <span class="kt">String</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC9textStyleAC04TextE0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/textStyle"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9textStyleAC04TextE0Cvp">textStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker-textstyle">TextStyle</a></code> applied to the text of the <code>MapMarker</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">textStyle</span><span class="p">:</span> <span class="kt">MapMarker</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker-textstyle">TextStyle</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC16visibilityRangesSayAA0B12MeasureRangeVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/visibilityRanges"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC16visibilityRangesSayAA0B12MeasureRangeVGvp">visibilityRanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The list of visibility ranges. The map marker is visible only inside these map measure ranges.
A range is half open - [minimumZoomLevel, maximumZoomLevel), the given maximum value
is not contained in the range.</p>
<p>When empty (the default), the map marker is visible without map measure restrictions.
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
<a name="/s:7heresdk9MapMarkerC9TextStyleC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/TextStyle"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC9TextStyleC">TextStyle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Styling options for the text of a <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapmarker-textstyle">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TextStyle</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarker">MapMarker</a></span><span class="o">.</span><span class="kt">TextStyle</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapMarkerC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_pSgtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/startAnimation(_:animationDelegate:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_pSgtF">startAnimation(_:<wbr/>animationDelegate:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Starts animation of this map marker according to provided <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></code>.</p>
<p>The <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></code> may be shared between multiple instances of <code>MapMarker</code>.</p>
<p>Starting animation on one map marker does not influence any ongoing animations on other map markers.
Any ongoing animation of this marker instance will get cancelled.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">startAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">animation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></span><span class="p">,</span> <span class="nv">animationDelegate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-animationdelegate">AnimationDelegate</a></span><span class="p">?)</span></code></pre>
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
<p>The animation to start, may be used for multiple different map markers.</p>
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
<p>The delegate to receive notifications about animation start, completion or cancellation.</p>
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
<a name="/s:7heresdk9MapMarkerC15cancelAnimationyyAA0bcE0CF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/cancelAnimation(_:)"></a>
<a class="token" href="#/s:7heresdk9MapMarkerC15cancelAnimationyyAA0bcE0CF">cancelAnimation(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Cancels single ongoing animation.</p>
<p>Does nothing if animation was not started for this map marker.</p>
<p>Does not cancel other animations if the same <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></code> object was applied to multiple <code>MapMarker</code>s.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">cancelAnimation</span><span class="p">(</span><span class="n">_</span> <span class="nv">animation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></span><span class="p">)</span></code></pre>
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
<p>The animation to cancel.</p>
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
