---
title: "ManeuverRuleOptions"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverruleoptions"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverRuleOptions"></a>
<a title="ManeuverRuleOptions Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

<a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a>

        ManeuverRuleOptions Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverRuleOptions</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverRuleOptions</span></code></pre>
</div>
</div>
<p>Defines a set of configurations specific to a <code><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverrule">TrackingCameraBehavior.ManeuverRule</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRangeAC0e4ZoomI0Vvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoomRange"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRangeAC0e4ZoomI0Vvp">zoomRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The zoom range for this rule. Defines the minimum and maximum zoom levels.
Defaults to a default-constructed <code><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverzoomrange">TrackingCameraBehavior.ManeuverZoomRange</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoomRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverzoomrange">ManeuverZoomRange</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV08earlyPreE27ActivationThresholdInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/earlyPreManeuverActivationThresholdInMeters"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV08earlyPreE27ActivationThresholdInMetersSdvp">earlyPreManeuverActivationThresholdInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance in meters for early activation. If the current position enters this threshold
of the upcoming maneuver while still within <code><a href="../../Classes/TrackingCameraBehavior/ManeuverRuleOptions.html#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV04postE27ActivationThresholdInMetersSdvp">TrackingCameraBehavior.ManeuverRuleOptions.postManeuverActivationThresholdInMeters</a></code>
of the previous maneuver, the camera behaves as though it were already in the upcoming
maneuver’s pre-activation zone. Must be non-negative. Defaults to 0.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">earlyPreManeuverActivationThresholdInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV03preE27ActivationThresholdInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/preManeuverActivationThresholdInMeters"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV03preE27ActivationThresholdInMetersSdvp">preManeuverActivationThresholdInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance in meters before the next maneuver point within which this rule becomes active.
Must be non-negative. Defaults to 0.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">preManeuverActivationThresholdInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV04postE27ActivationThresholdInMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/postManeuverActivationThresholdInMeters"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV04postE27ActivationThresholdInMetersSdvp">postManeuverActivationThresholdInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance in meters after the previous maneuver point within which this rule remains
active. Must be non-negative. Defaults to 0.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">postManeuverActivationThresholdInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRange08earlyPreE27ActivationThresholdInMeters03preelmnO004postelmnO0AeC0e4ZoomI0V_S3dtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(zoomRange:earlyPreManeuverActivationThresholdInMeters:preManeuverActivationThresholdInMeters:postManeuverActivationThresholdInMeters:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV9zoomRange08earlyPreE27ActivationThresholdInMeters03preelmnO004postelmnO0AeC0e4ZoomI0V_S3dtcfc">init(zoomRange:<wbr/>earlyPreManeuverActivationThresholdInMeters:<wbr/>preManeuverActivationThresholdInMeters:<wbr/>postManeuverActivationThresholdInMeters:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">zoomRange</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverzoomrange">ManeuverZoomRange</a></span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuverzoomrange">ManeuverZoomRange</a></span><span class="p">(),</span> <span class="nv">earlyPreManeuverActivationThresholdInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">preManeuverActivationThresholdInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">,</span> <span class="nv">postManeuverActivationThresholdInMeters</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">0.0</span><span class="p">)</span></code></pre>
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
