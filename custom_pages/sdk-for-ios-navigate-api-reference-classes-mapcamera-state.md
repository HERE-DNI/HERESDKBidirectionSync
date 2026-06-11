---
title: "State"
slug: "sdk-for-ios-navigate-api-reference-classes-mapcamera-state"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/State"></a>
<a title="State Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-classes-mapcamera">MapCamera</a>

        State Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>State</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">State</span></code></pre>
</div>
</div>
<p>Encapsulates state of the camera.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5StateV17targetCoordinatesAA03GeoF0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/targetCoordinates"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5StateV17targetCoordinatesAA03GeoF0Vvp">targetCoordinates</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s ‘LookAt’ target position in geodetic space.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">targetCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5StateV19orientationAtTargetAA14GeoOrientationVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/orientationAtTarget"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5StateV19orientationAtTargetAA14GeoOrientationVvp">orientationAtTarget</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s orientation at target point.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">orientationAtTarget</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geoorientation">GeoOrientation</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToTargetInMeters"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5StateV24distanceToTargetInMetersSdvp">distanceToTargetInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance from the camera to the target point in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToTargetInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5StateV9zoomLevelSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoomLevel"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5StateV9zoomLevelSdvp">zoomLevel</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zoom level corresponding to the current distance to target.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoomLevel</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk9MapCameraC5StateV17targetCoordinates19orientationAtTarget010distanceToI8InMeters9zoomLevelAeA03GeoF0V_AA0P11OrientationVS2dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(targetCoordinates:orientationAtTarget:distanceToTargetInMeters:zoomLevel:)"></a>
<a class="token" href="#/s:7heresdk9MapCameraC5StateV17targetCoordinates19orientationAtTarget010distanceToI8InMeters9zoomLevelAeA03GeoF0V_AA0P11OrientationVS2dtcfc">init(targetCoordinates:<wbr/>orientationAtTarget:<wbr/>distanceToTargetInMeters:<wbr/>zoomLevel:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<ul>
<li><p>Parameters</p>
<ul>
<li>targetCoordinates: Camera’s ‘LookAt’ target position in geodetic space.</li>
</ul>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
  will consider the target point as being located on the ground.</p>
<ul>
<li>orientationAtTarget: Camera’s orientation at target point.</li>
<li>distanceToTargetInMeters: Distance from the camera to the target point in meters.</li>
<li>zoomLevel: Zoom level corresponding to the current distance to target.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">targetCoordinates</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinates">GeoCoordinates</a></span><span class="p">,</span> <span class="nv">orientationAtTarget</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geoorientation">GeoOrientation</a></span><span class="p">,</span> <span class="nv">distanceToTargetInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">zoomLevel</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
