---
title: "FixedCameraBehavior"
slug: "sdk-for-ios-navigate-api-reference-classes-fixedcamerabehavior"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/FixedCameraBehavior"></a>
<a title="FixedCameraBehavior Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        FixedCameraBehavior Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>FixedCameraBehavior</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">FixedCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">FixedCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">FixedCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use this class to follow the current location of the user: The camera will permanently look at
the target location that was fed into the navigator instance. Since location updates happen in
discrete intervals, locations in-between will be interpolated to achieve a smooth camera
movement.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/normalizedPrincipalPoint"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp">normalizedPrincipalPoint</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The normalized principal point.
Normalized principal point to be used during navigation.
Defaults to (0.5, 0.775), which means the camera will use the position slightly at the bottom
of the mapview.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">normalizedPrincipalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-anchor2d">Anchor2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorC22cameraDistanceInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraDistanceInMeters"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorC22cameraDistanceInMetersSdvp">cameraDistanceInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera distance to current location. The default value is 150 meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.28.0. Use FixedCameraBehavior.zoom instead.")</span>
<span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraDistanceInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorC4zoomAA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoom"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorC4zoomAA10MapMeasureVvp">zoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zoom configuration. The default value is 150 meters.
Camera zoom configuration. The default value is 150 meters.
Note: <code><a href="../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO5scaleyA2EmF">MapMeasure.Kind.scale</a></code> is not supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorC19cameraTiltInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraTiltInDegrees"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorC19cameraTiltInDegreesSdvp">cameraTiltInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera tilt with axis parallel to the ground.
The default value is 50 degrees.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraTiltInDegrees</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk19FixedCameraBehaviorC22cameraBearingInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/cameraBearingInDegrees"></a>
<a class="token" href="#/s:7heresdk19FixedCameraBehaviorC22cameraBearingInDegreesSdSgvp">cameraBearingInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in “north up” mode.
Defaults to <code>nil</code>, which means the camera derives the bearing from the <code><a href="sdk-for-ios-navigate-api-reference-structs-location">Location</a></code>,
so that it points to the direction of travel.
If this property is <code>nil</code> and the device does not provide bearing, the last known value is
used or zero otherwise.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">cameraBearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
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
