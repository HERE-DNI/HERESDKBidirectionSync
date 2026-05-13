---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverzoomrange"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- ManeuverZoomRange.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverZoomRange"></a>
<a title="ManeuverZoomRange Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-navigation">Navigation</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        ManeuverZoomRange Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverZoomRange</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverZoomRange</span></code></pre>
</div>
</div>
<p>Defines the bounds within which the zoom level is constrained when approaching a maneuver.
Used as part of <code><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior-maneuverruleoptions">TrackingCameraBehavior.ManeuverRuleOptions</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03minF0AA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/minZoom"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03minF0AA10MapMeasureVvp">minZoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum camera zoom. Valid range is 0.0 to 22.0.
Defaults to a <code><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></code> with kind <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> and value 4.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">minZoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03maxF0AA10MapMeasureVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxZoom"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03maxF0AA10MapMeasureVvp">maxZoom</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum camera zoom. Valid range is 0.0 to 22.0. Must be greater than or equal
to <code><a href="../../Classes/TrackingCameraBehavior/ManeuverZoomRange.html#/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03minF0AA10MapMeasureVvp">TrackingCameraBehavior.ManeuverZoomRange.minZoom</a></code>.
Defaults to a <code><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></code> with kind <code><a href="../../Structs/MapMeasure/Kind.html#/s:7heresdk10MapMeasureV4KindO9zoomLevelyA2EmF">MapMeasure.Kind.zoomLevel</a></code> and value 20.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxZoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03minF003maxF0AeA10MapMeasureV_AItcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(minZoom:maxZoom:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV03minF003maxF0AeA10MapMeasureV_AItcfc">init(minZoom:<wbr/>maxZoom:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and
unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">minZoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span><span class="p">(</span><span class="nv">kind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span><span class="o">.</span><span class="n">zoomLevel</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="mf">4.0</span><span class="p">),</span> <span class="nv">maxZoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span><span class="p">(</span><span class="nv">kind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span><span class="o">.</span><span class="n">zoomLevel</span><span class="p">,</span> <span class="nv">value</span><span class="p">:</span> <span class="mf">20.0</span><span class="p">))</span></code></pre>
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

</div>
`
}</HTMLBlock>
