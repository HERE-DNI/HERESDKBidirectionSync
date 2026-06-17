---
title: "JunctionViewLaneAssistance"
slug: "sdk-for-ios-navigate-structs-junctionviewlaneassistance"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/JunctionViewLaneAssistance"></a>
<a title="JunctionViewLaneAssistance Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        JunctionViewLaneAssistance Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>JunctionViewLaneAssistance</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">JunctionViewLaneAssistance</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides lane assistance information for the next complex junction
in order to keep following the route. It is recommended to indicate <code>JunctionViewLaneAssistance</code>
and <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> separately or to indicate only <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> information -
<code>JunctionViewLaneAssistance</code> will recommend all lanes that allow to pass the upcoming complex junction, regardless
if they will lead to the next maneuver or not.
If the location of a maneuver lies on an upcoming complex junction, the recommended lanes will be
the same as the ones from <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code>.</p>
<p>A junction is recognized as complex only if:</p>
<ul>
<li>it is at least a bifurcation;</li>
<li>it has at least two lanes whose directions do not follow the current route.
In opposition to <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code>, notifications are also forwarded when there is
no maneuver action occurring at the next complex junction.
Therefore, <code>JunctionViewLaneAssistance</code> can be disjointed from maneuvers. If lane assistance should be used to
associate it with upcoming maneuvers, consider to use <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> instead.
Note that <code><a href="sdk-for-ios-navigate-structs-maneuverviewlaneassistance">ManeuverViewLaneAssistance</a></code> notifications are synchronized with maneuver events,
whereas <code>JunctionViewLaneAssistance</code> events are not strictly synchronized with maneuver events.</li>
</ul>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lanesForNextJunction"></a>
<a class="token" href="#/s:7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp">lanesForNextJunction</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of lanes on the next complex junction.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.</p>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lanesForNextJunction</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-lane">Lane</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26JunctionViewLaneAssistanceV010distanceToB8InMetersSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/distanceToJunctionInMeters"></a>
<a class="token" href="#/s:7heresdk26JunctionViewLaneAssistanceV010distanceToB8InMetersSdvp">distanceToJunctionInMeters</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Distance to the next complex junction in meters.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">distanceToJunctionInMeters</span><span class="p">:</span> <span class="kt">Double</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0010distanceToB8InMetersACSayAA0D0VG_Sdtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lanesForNextJunction:distanceToJunctionInMeters:)"></a>
<a class="token" href="#/s:7heresdk26JunctionViewLaneAssistanceV012lanesForNextB0010distanceToB8InMetersACSayAA0D0VG_Sdtcfc">init(lanesForNextJunction:<wbr/>distanceToJunctionInMeters:<wbr/>)</a>
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
<li>lanesForNextJunction: A list of lanes on the next complex junction.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane. This is valid for right-hand and left-hand driving
countries. An empty list means that the complex junction has been passed and that the lane information is not
valid anymore. Exactly one event with a non-empty list is delivered before reaching a complex junction and
one event with an empty list afterwards.</li>
</ul>
<p><strong>Note:</strong> Lanes going in opposite direction are not included in the list.</p>
<ul>
<li>distanceToJunctionInMeters: Distance to the next complex junction in meters.</li>
</ul></li>
</ul>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lanesForNextJunction</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-lane">Lane</a></span><span class="p">],</span> <span class="nv">distanceToJunctionInMeters</span><span class="p">:</span> <span class="kt">Double</span><span class="p">)</span></code></pre>
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
