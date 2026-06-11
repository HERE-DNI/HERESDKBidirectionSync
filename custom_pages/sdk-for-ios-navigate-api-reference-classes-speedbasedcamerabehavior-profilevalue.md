---
title: "sdk-for-ios-navigate-api-reference-classes-speedbasedcamerabehavior-profilevalue"
slug: "sdk-for-ios-navigate-api-reference-classes-speedbasedcamerabehavior-profilevalue"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ProfileValue"></a>
<a title="ProfileValue Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-classes-speedbasedcamerabehavior">SpeedBasedCameraBehavior</a>
<img alt="" id="carat" src="/carat.png"/>
        ProfileValue Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ProfileValue</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ProfileValue</span></code></pre>
</div>
</div>
<p>A single profile value which indicates the speed range in which it applies to its zoom and
tilt configuration.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV19fromMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/fromMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV19fromMetersPerSecondSdvp">fromMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Start speed of the range.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">fromMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV17toMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/toMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV17toMetersPerSecondSdvp">toMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>End speed of the range.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">toMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV4zoomAA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoom"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV4zoomAA10MapMeasureVvp">zoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zoom configuration.
Note: <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO5scaleyA2EmF">MapMeasure.Kind.scale</a></code> is not supported.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV13tiltInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tiltInDegrees"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV13tiltInDegreesSdvp">tiltInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Tilt configuration.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tiltInDegrees</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV19fromMetersPerSecond02toijK04zoom13tiltInDegreesAESd_SdAA10MapMeasureVSdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(fromMetersPerSecond:toMetersPerSecond:zoom:tiltInDegrees:)"></a>
<a class="token" href="#/s:7heresdk24SpeedBasedCameraBehaviorC12ProfileValueV19fromMetersPerSecond02toijK04zoom13tiltInDegreesAESd_SdAA10MapMeasureVSdtcfc">init(fromMetersPerSecond:<wbr/>toMetersPerSecond:<wbr/>zoom:<wbr/>tiltInDegrees:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">fromMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">toMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">,</span> <span class="nv">tiltInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
