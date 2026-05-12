---
title: "State Structure Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapcamera-state"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- State.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Struct/State"></a>
<a title="State Structure Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../../index.html">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Maps.html">Maps</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="../../Classes/MapCamera.html">MapCamera</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        State Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public struct State</code></pre>
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
<pre><code>public var targetCoordinates: GeoCoordinates</code></pre>
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
<pre><code>public var orientationAtTarget: GeoOrientation</code></pre>
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
<pre><code>public var distanceToTargetInMeters: Double</code></pre>
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
<pre><code>public var zoomLevel: Double</code></pre>
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
<pre><code>public init(targetCoordinates: GeoCoordinates, orientationAtTarget: GeoOrientation, distanceToTargetInMeters: Double, zoomLevel: Double)</code></pre>
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



</div>
`
}</HTMLBlock>
