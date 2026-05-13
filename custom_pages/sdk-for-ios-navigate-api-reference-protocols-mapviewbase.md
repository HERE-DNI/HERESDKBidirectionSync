---
title: "Maps / MapViewBase"
slug: "sdk-for-ios-navigate-api-reference-protocols-mapviewbase"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Protocol/MapViewBase"></a>
<a title="MapViewBase Protocol Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapViewBase Protocol Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapViewBase</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">protocol</span> <span class="kt">MapViewBase</span> <span class="p">:</span> <span class="kt">AnyObject</span></code></pre>
</div>
</div>
<p>Represents the available public API from  <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapview">MapView</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP04PickB7Handlera"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/PickMapHandler"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP04PickB7Handlera">PickMapHandler</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Callback for a pick request. In case of an error the result is not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">typealias</span> <span class="kt">PickMapHandler</span> <span class="o">=</span> <span class="p">(</span><span class="n">_</span> <span class="nv">mapPickResult</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-mappickresult">MapPickResult</a></span><span class="p">?)</span> <span class="o">-&gt;</span> <span class="kt">Void</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>mapPickResult</em>
</code>
</td>
<td>
<div>
<p>The operation result.</p>
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
<a name="/s:7heresdk11MapViewBaseP7isValidSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isValid"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP7isValidSbvp">isValid</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Indicates whether this instance is valid.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">isValid</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP6cameraAA0B6CameraCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/camera"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP6cameraAA0B6CameraCvp">camera</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The camera to control the view for the map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">camera</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-mapcamera">MapCamera</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP8gesturesAA8GesturesCvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/gestures"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP8gesturesAA8GesturesCvp">gestures</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The gestures control object for setting up the capture of gestures.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">gestures</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-gestures">Gestures</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapScene"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP8mapSceneAA0bF0Cvp">mapScene</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map scene associated with this map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">mapScene</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-mapscene">MapScene</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP10mapContextAA0bF0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/mapContext"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP10mapContextAA0bF0Cvp">mapContext</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Map context associated with this map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">mapContext</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-mapcontext">MapContext</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/hereMap"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP04hereB0AA04HereB0Cvp">hereMap</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Here Map associated with this map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">hereMap</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-heremap">HereMap</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP12viewportSizeAA6Size2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewportSize"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP12viewportSizeAA6Size2DVvp">viewportSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The size of this map view in physical pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">viewportSize</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-size2d">Size2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP9frameRates5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/frameRate"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP9frameRates5Int32Vvp">frameRate</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum render frame rate in frames per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">frameRate</span><span class="p">:</span> <span class="kt">Int32</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP10pixelScaleSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/pixelScale"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP10pixelScaleSdvp">pixelScale</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The pixel scale factor used by this <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapview">MapView</a></code>.</p>
<p>Pixel scale is 0.0 if the map view is not initialized.</p>
<p>In cases where the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapview">MapView</a></code> moves in between screens (e.g. from main screen to a CarPlay screen),
/ the most up-to-date pixel scale value can be obtained after a render target gets attached to the view.
/ To get notified when a render target gets attached to the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-mapview">MapView</a></code>, see <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">pixelScale</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP13watermarkSizeAA6Size2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/watermarkSize"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP13watermarkSizeAA6Size2DVvp">watermarkSize</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Provides the size of the watermark in physical pixels.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">var</span> <span class="nv">watermarkSize</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-size2d">Size2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP20viewToGeoCoordinates0eH0AA0gH0VSgAA7Point2DV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/viewToGeoCoordinates(viewCoordinates:)"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP20viewToGeoCoordinates0eH0AA0gH0VSgAA7Point2DV_tF">viewToGeoCoordinates(viewCoordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Converts view coordinates (in pixels) to geographical coordinates.</p>
<p>An optional altitude component of the resulting geographical coordinate is not set.</p>
<p>If the view coordinates specify a point above a horizon, then the result
is geographical coordinates of the point on a horizon below the specified
view coordinates.</p>
<p>The fog effect is ignored for the calculation, meaning that for the view point
within the area covered by the fog, the result is geographical coordinates
that would be displayed at the specified point if the fog effect was
not applied.</p>
<p>If the render surface is not attached, it will return <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">viewToGeoCoordinates</span><span class="p">(</span><span class="nv">viewCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-point2d">Point2D</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>viewCoordinates</em>
</code>
</td>
<td>
<div>
<p>Point inside the view to convert.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The geographical coordinates under specified view point or <code>nil</code> if there is no render surface attached.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP05geoToC11Coordinates0eG0AA7Point2DVSgAA03GeoG0V_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/geoToViewCoordinates(geoCoordinates:)"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP05geoToC11Coordinates0eG0AA7Point2DVSgAA03GeoG0V_tF">geoToViewCoordinates(geoCoordinates:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Converts geographical coordinates to view coordinates (in pixels).</p>
<p>If specified, altitude of the input coordinates is interpreted as altitude above sea level.
If not specified, the input coordinates are interpreted as being on ground elevation.
The above distinction is only relevant when 3D terrain feature is enabled.</p>
<p>The resulting view coordinates might be outside of current viewport, i.e. result might contain values
less than zero or greater than view’s dimensions.</p>
<p>If the render surface is not attached, it will return <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">geoToViewCoordinates</span><span class="p">(</span><span class="nv">geoCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-geocoordinates">GeoCoordinates</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-point2d">Point2D</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geoCoordinates</em>
</code>
</td>
<td>
<div>
<p>Geographical coordinates to convert.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>The view coordinates of the specified geographical point or <code>nil</code>
if there is no render surface attached.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk11MapViewBaseP20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setWatermarkLocation(anchor:offset:)"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP20setWatermarkLocation6anchor6offsetyAA8Anchor2DV_AA7Point2DVtF">setWatermarkLocation(anchor:<wbr/>offset:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the position of the HERE logo watermark within the map view.</p>
<p>By default, the watermark is aligned to the bottom-right corner of the view:
Anchor2D(1.0, 1.0) and Point2D(-watermarkSize.width / 2, -watermarkSize.height / 2).
It is recommended to change the default position only if necessary to avoid overlapping UI elements.
The watermark should always be fully visible within the view.
The anchor point on the watermark is its center (width/2, height/2), around which it will be placed
in the map view.
For map views smaller than 250 dip in both width and height, the watermark will not be shown.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">setWatermarkLocation</span><span class="p">(</span><span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-anchor2d">Anchor2D</a></span><span class="p">,</span> <span class="nv">offset</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-point2d">Point2D</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>anchor</em>
</code>
</td>
<td>
<div>
<p>Anchor point in normalized view coordinates [0, 1]. Map view’s origin at (0, 0) indicates
a top-left corner of the map view.
Out of boundary anchor point values will be clamped to the [0, 1] range.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>offset</em>
</code>
</td>
<td>
<div>
<p>A horizontal and vertical offset (expressed in positive/negative pixel coordinates) that
allows shifting the watermark from the anchor point position in one or the other
direction.
For the quadrant of values expressing visible part of the map view negative offset shifts
the watermark to the direction of the origin, positive - away from it.
For example, the offset of (-10, 5) will shift the watermark 10px to the left and 5px to
the bottom.
If specified offset will result in watermark being completely or partially out-of-view
the offset will be adjusted internally so that watermark is fully visible.
Offset is not being scaled when the map view size changes.</p>
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
<a name="/s:7heresdk11MapViewBaseP20addLifecycleDelegateyyAA0bcfG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/addLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP20addLifecycleDelegateyyAA0bcfG0_pF">addLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Adds a <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></code> to this map view.
Adding the same object multiple times has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">addLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">lifecycleListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lifecycleListener</em>
</code>
</td>
<td>
<div>
<p>An object to be notified of lifecycle events.</p>
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
<a name="/s:7heresdk11MapViewBaseP23removeLifecycleDelegateyyAA0bcfG0_pF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/removeLifecycleDelegate(_:)"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP23removeLifecycleDelegateyyAA0bcfG0_pF">removeLifecycleDelegate(_:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Removes a <code><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></code> from this map view.
Trying to remove an object that was not added or was removed before
has no effect.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">removeLifecycleDelegate</span><span class="p">(</span><span class="n">_</span> <span class="nv">lifecycleListener</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-mapviewlifecycledelegate">MapViewLifecycleDelegate</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>lifecycleListener</em>
</code>
</td>
<td>
<div>
<p>An object to stop being notified of lifecycle events.</p>
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
<a name="/s:7heresdk11MapViewBaseP4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bJ6ResultCSgctF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/pick(filter:inside:completion:)"></a>
<a class="token" href="#/s:7heresdk11MapViewBaseP4pick6filter6inside10completionyAA0B5SceneC0B10PickFilterCSg_AA11Rectangle2DVyAA0bJ6ResultCSgctF">pick(filter:<wbr/>inside:<wbr/>completion:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Returns all map content located inside the specified pick area. Content to be picked is
specified by a pick content filter.
The pick area is defined by a rectangle in map view coordinates
in pixels, relative to the map view’s origin at (0, 0) which indicates the top-left corner
of the map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">func</span> <span class="nf">pick</span><span class="p">(</span><span class="nv">filter</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-mapscene">MapScene</a></span><span class="o">.</span><span class="kt">MapPickFilter</span><span class="p">?,</span> <span class="n">inside</span> <span class="nv">viewArea</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-rectangle2d">Rectangle2D</a></span><span class="p">,</span> <span class="nv">completion</span><span class="p">:</span> <span class="kd">@escaping</span> <span class="kt">MapViewBase</span><span class="o">.</span><span class="kt"><a href="../Protocols/MapViewBase.html#/s:7heresdk11MapViewBaseP04PickB7Handlera">PickMapHandler</a></span><span class="p">)</span></code></pre>
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
<p>Filter for the map content to be picked. When a filter is not set all of the pickable content will be picked.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>viewArea</em>
</code>
</td>
<td>
<div>
<p>The rectangular pixel area of the view inside which map content will be picked.
View area is relative to the map view’s origin at (0, 0) at the top-left corner
of the map view.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>completion</em>
</code>
</td>
<td>
<div>
<p>Callback to call with the result. This will be called on a main thread when pick operation
completes.</p>
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
