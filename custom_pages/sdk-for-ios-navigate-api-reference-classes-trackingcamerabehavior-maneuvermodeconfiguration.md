---
title: "TrackingCameraBehavior / ManeuverModeConfiguration"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior-maneuvermodeconfiguration"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverModeConfiguration"></a>
<a title="ManeuverModeConfiguration Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-..-index">heresdk</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-navigation">Navigation</a>
<img alt="" id="carat" src="../../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a>
<img alt="" id="carat" src="../../img/carat.png"/>
        ManeuverModeConfiguration Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverModeConfiguration</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverModeConfiguration</span></code></pre>
</div>
</div>
<p>Configuration that defines how <code><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> reacts to nearby maneuvers.</p>
<p>On each frame, and based on the current position, the availability of its functional road
class, and the availability of maneuver data for at least one adjacent maneuver, the camera
checks for a match against the <code><a href="../../Classes/TrackingCameraBehavior/ManeuverModeConfiguration.html#/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRulesSayAC0E4RuleVGvp">TrackingCameraBehavior.ManeuverModeConfiguration.maneuverRules</a></code> in the order they are listed. If a match is
found, subsequent rules are not checked. If no match is found, if inputs are unavailable,
or if the matched rule has <code>nil</code> options, the camera does not react.</p>
<p>For correct default initialization, use <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ">TrackingCameraBehavior.defaultManeuverModeConfiguration(...)</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRulesSayAC0E4RuleVGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maneuverRules"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRulesSayAC0E4RuleVGvp">maneuverRules</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Ordered list of maneuver rules. Rules are evaluated in order; the first matching rule
determines the camera behavior. If empty, this configuration is not valid and the
camera does not react to maneuvers. If <code><a href="../../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ">TrackingCameraBehavior.defaultManeuverModeConfiguration(...)</a></code> is not used
for <code>TrackingCameraBehavior.ManeuverModeConfiguration</code>, it will be an empty list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maneuverRules</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior-maneuverrule">ManeuverRule</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV25bearingThresholdInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearingThresholdInDegrees"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV25bearingThresholdInDegreesSdvp">bearingThresholdInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Maximum angle difference in degrees between the current bearing and the bearing to the
maneuver point. If the difference exceeds this threshold, the camera does not turn
towards the maneuver. Valid range is 0.0 to 180.0. Defaults to 25.0.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearingThresholdInDegrees</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRules25bearingThresholdInDegreesAESayAC0E4RuleVG_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(maneuverRules:bearingThresholdInDegrees:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRules25bearingThresholdInDegreesAESayAC0E4RuleVG_Sdtcfc">init(maneuverRules:<wbr/>bearingThresholdInDegrees:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">maneuverRules</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-..-classes-trackingcamerabehavior-maneuverrule">ManeuverRule</a></span><span class="p">]</span> <span class="o">=</span> <span class="p">[],</span> <span class="nv">bearingThresholdInDegrees</span><span class="p">:</span> <span class="kt">Double</span> <span class="o">=</span> <span class="mf">25.0</span><span class="p">)</span></code></pre>
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
