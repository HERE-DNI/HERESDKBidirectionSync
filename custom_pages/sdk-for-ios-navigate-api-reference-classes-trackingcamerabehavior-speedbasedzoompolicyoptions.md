---
title: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-speedbasedzoompolicyoptions"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-speedbasedzoompolicyoptions"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedBasedZoomPolicyOptions"></a>
<a title="SpeedBasedZoomPolicyOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
<img alt="" id="carat" src="/carat.png"/>
        SpeedBasedZoomPolicyOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>SpeedBasedZoomPolicyOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedBasedZoomPolicyOptions</span></code></pre>
</div>
</div>
<p>Configuration for computing zoom levels from speed thresholds defined per road classification.
For correct default initialization, use <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChangesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/delayBetweenThresholdChanges"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChangesSdSgvp">delayBetweenThresholdChanges</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Minimum time interval that must pass before the zoom level is
allowed to switch to a new speed threshold. If <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)</a></code> is not used
for <code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code>, it will be <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">delayBetweenThresholdChanges</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV020roadClassificationToE9ThresholdSDyAA04RoadK0OSayAC0eM0VGGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/roadClassificationToSpeedThreshold"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV020roadClassificationToE9ThresholdSDyAA04RoadK0OSayAC0eM0VGGvp">roadClassificationToSpeedThreshold</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines, per road classification, how the zoom level should change in
response to different vehicle speeds. If <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)</a></code> is not used
for <code>TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</code>, it will be an empty map.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">roadClassificationToSpeedThreshold</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadclassification">RoadClassification</a></span> <span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-speedthreshold">SpeedThreshold</a></span><span class="p">]]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChanges020roadClassificationToeL0AESdSg_SDyAA04RoadO0OSayAC0eL0VGGtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(delayBetweenThresholdChanges:roadClassificationToSpeedThreshold:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV28delayBetweenThresholdChanges020roadClassificationToeL0AESdSg_SDyAA04RoadO0OSayAC0eL0VGGtcfc">init(delayBetweenThresholdChanges:<wbr/>roadClassificationToSpeedThreshold:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">delayBetweenThresholdChanges</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">?</span> <span class="o">=</span> <span class="kc">nil</span><span class="p">,</span> <span class="nv">roadClassificationToSpeedThreshold</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-roadclassification">RoadClassification</a></span> <span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-speedthreshold">SpeedThreshold</a></span><span class="p">]]</span> <span class="o">=</span> <span class="p">[:])</span></code></pre>
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
