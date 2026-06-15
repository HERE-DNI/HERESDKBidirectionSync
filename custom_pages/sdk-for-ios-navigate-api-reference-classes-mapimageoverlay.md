---
title: "MapImageOverlay"
slug: "sdk-for-ios-navigate-api-reference-classes-mapimageoverlay"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapImageOverlay"></a>
<a title="MapImageOverlay Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

        MapImageOverlay Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapImageOverlay</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapImageOverlay</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImageOverlay</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapImageOverlay</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p><code>MapImageOverlay</code> is used to draw images over the map, at a view coordinate inside the map viewport.</p>
<p>The image to be displayed is represented by a <code><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></code> object.
By default, the overlay is centered on the given view coordinate.</p>
<p>The resulting viewport area covered by the overlay is computed out of the overlay’s view coordinate,
the anchor point and the image size. The overlay subareas that fall outside of the map viewport get clipped.</p>
<p>To display the map overlay, it needs to be added to the scene using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC03addB12ImageOverlayyyAA0beF0CF">MapScene.addMapImageOverlay(...)</a></code>.
To stop displaying it, remove it from the scene using <code><a href="../Classes/MapScene.html#/s:7heresdk8MapSceneC06removeB12ImageOverlayyyAA0beF0CF">MapScene.removeMapImageOverlay(...)</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapImageOverlayC2at5imageAcA7Point2DV_AA0bC0Ctcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:image:)"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC2at5imageAcA7Point2DV_AA0bC0Ctcfc">init(at:<wbr/>image:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of an overlay at given view coordinates, represented by specified image.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">at</span> <span class="nv">viewCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-point2d">Point2D</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">)</span></code></pre>
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
<p>The overlay’s view coordinates in pixels.</p>
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
<a name="/s:7heresdk15MapImageOverlayC2at5image6anchorAcA7Point2DV_AA0bC0CAA8Anchor2DVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(at:image:anchor:)"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC2at5image6anchorAcA7Point2DV_AA0bC0CAA8Anchor2DVtcfc">init(at:<wbr/>image:<wbr/>anchor:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an instance of an overlay at given view coordinates, represented by specified image,
with anchor point specifying how the image is positioned relative to the overlay’s view coordinates.</p>
<p>The anchor is a way of specifying position offset relative to image’s dimensions on the view.
For example, (0, 0) places the top-left corner of the image at the overlay’s view coordinates.
(1, 1) would place the bottom-right corner of the image at the overlay’s view coordinates.
(0.5, 0.5) which is the default value would center the image at the overlay’s view coordinates.</p>
<p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the overlay’s view coordinates at the distance
in pixels that is equal to the height of the image.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="n">at</span> <span class="nv">viewCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-point2d">Point2D</a></span><span class="p">,</span> <span class="nv">image</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapimage">MapImage</a></span><span class="p">,</span> <span class="nv">anchor</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span><span class="p">)</span></code></pre>
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
<p>The overlay’s view coordinates in pixels.</p>
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
<p>The anchor point for the overlay image which specifies the position offset relative
to the overlay’s view coordinates.</p>
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
<a name="/s:7heresdk15MapImageOverlayC15viewCoordinatesAA7Point2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewCoordinates"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC15viewCoordinatesAA7Point2DVvp">viewCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The view point in pixels on the map viewport where the map overlay is drawn.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">viewCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-point2d">Point2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk15MapImageOverlayC9drawOrders5Int32Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/drawOrder"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC9drawOrders5Int32Vvp">drawOrder</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Draw order of this <code>MapImageOverlay</code>.
Overlays with higher draw order value are drawn on top of overlays with lower draw order.</p>
<p>In case multiple overlays have the same draw order value
then the order in which they were added to the scene matters. Last added overlay is drawn on top.</p>
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
<a name="/s:7heresdk15MapImageOverlayC5imageAA0bC0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/image"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC5imageAA0bC0Cvp">image</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Image overlayed on the map.</p>
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
<a name="/s:7heresdk15MapImageOverlayC6anchorAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/anchor"></a>
<a class="token" href="#/s:7heresdk15MapImageOverlayC6anchorAA8Anchor2DVvp">anchor</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The anchor point for the overlay image which specifies the position offset relative
to the overlay’s view coordinates.
For example, (0, 0) places the top-left corner of the image at the overlay’s view coordinates.
(1, 1) would place the bottom-right corner of the image at the overlay’s view coordinates.
(0.5, 0.5) which is the default value would center the image at the overlay’s view coordinates.</p>
<p>Values outside the 0..1 range are also allowed, for example (0.5, 2) would display the image
centered horizontally with its bottom edge above the overlay’s view coordinates at the distance
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
