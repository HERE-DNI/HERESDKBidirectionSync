---
title: "SpeedThreshold"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-speedthreshold"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedThreshold"></a>
<a title="SpeedThreshold Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

<a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a>

        SpeedThreshold Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpeedThreshold</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedThreshold</span></code></pre>
</div>
</div>
<p>Defines a zoom level triggered when the vehicle reaches a specific speed.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV22speedInMetersPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/speedInMetersPerSecond"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV22speedInMetersPerSecondSdvp">speedInMetersPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Speed that activates the threshold. Defaults to 0.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV4zoomAA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoom"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV4zoomAA10MapMeasureVvp">zoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Zoom applied once the threshold is reached.
Defaults to a <code><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></code> with kind <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> and value 16.5.</p>
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
<a name="/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV22speedInMetersPerSecond4zoomAESd_AA10MapMeasureVtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(speedInMetersPerSecond:zoom:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV22speedInMetersPerSecond4zoomAESd_AA10MapMeasureVtcfc">init(speedInMetersPerSecond:<wbr/>zoom:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">speedInMetersPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="p">(</span><span class="nv">kind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span><span class="o">.</span><span class="n">zoomLevel</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="mf">16.5</span><span class="p">))</span></code></pre>
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
