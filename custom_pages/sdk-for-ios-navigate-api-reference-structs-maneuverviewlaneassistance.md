---
title: "ManeuverViewLaneAssistance"
slug: "sdk-for-ios-navigate-api-reference-structs-maneuverviewlaneassistance"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverViewLaneAssistance"></a>
<a title="ManeuverViewLaneAssistance Structure Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-navigation">Navigation</a>

        ManeuverViewLaneAssistance Structure Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>ManeuverViewLaneAssistance</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverViewLaneAssistance</span> <span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>A struct that provides lane assistance information for the next maneuver(s).
During turn-by-turn navigation lane assistance can help a driver to choose the recommended lanes
in order to complete the upcoming maneuvers.
The notifications are synchronized with the <code><a href="sdk-for-ios-navigate-api-reference-protocols-eventtextdelegate">EventTextDelegate</a></code>.
<code><a href="sdk-for-ios-navigate-api-reference-protocols-eventtextdelegate">EventTextDelegate</a></code> has 4 notification types for each maneuver:
Range, Reminder, Distance and Action.
Only the maneuver notification of type Distance will also notify a ManeuverViewLaneAssistance object
(e.g. “After 400 meters, turn right onto Invalidenstraße”).
The notification will not be sent when other types of maneuver notification are given.
The notification will not be sent when no lane data is available.
During tracking mode, no notifications are delivered.
This ManeuverViewLaneAssistance information is valid until the next maneuver is reached.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lanesForNextManeuver"></a>
<a class="token" href="#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp">lanesForNextManeuver</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of lanes on the current road that leads to the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
The list is guaranteed to be non-empty.
<code><a href="../Structs/RoadAttributes.html#/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp">RoadAttributes.isRightDrivingSide</a></code> indicates if this is a left-hand driving country or not.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lanesForNextManeuver</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lane">Lane</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNexthB0SayAA0D0VGvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/lanesForNextNextManeuver"></a>
<a class="token" href="#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNexthB0SayAA0D0VGvp">lanesForNextNextManeuver</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>A list of lanes on the road that leads to the maneuver after the upcoming maneuver.
The lanes are sorted from left to right: The lane at index 0 represents the leftmost lane and
the last index represents the rightmost lane.
This is valid for both right-hand and left-hand driving countries.
Contraflow lanes are not included in the list.
<code><a href="../Structs/RoadAttributes.html#/s:7heresdk14RoadAttributesV18isRightDrivingSideSbvp">RoadAttributes.isRightDrivingSide</a></code> indicates if this is a left-hand driving country or not.
By default, this list is empty. It will be filled when the next two maneuvers are too
close to each other, or when the next two maneuvers are roundabout maneuvers.
Note: This notification is delivered at the same time as the <code><a href="../Structs/ManeuverViewLaneAssistance.html#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB0SayAA0D0VGvp">ManeuverViewLaneAssistance.lanesForNextManeuver</a></code>.
There is no separate maneuver notification on the second maneuver when two maneuvers are
are too close to each other.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">lanesForNextNextManeuver</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lane">Lane</a></span><span class="p">]</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB00fghhB0ACSayAA0D0VG_AHtcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(lanesForNextManeuver:lanesForNextNextManeuver:)"></a>
<a class="token" href="#/s:7heresdk26ManeuverViewLaneAssistanceV012lanesForNextB00fghhB0ACSayAA0D0VG_AHtcfc">init(lanesForNextManeuver:<wbr/>lanesForNextNextManeuver:<wbr/>)</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">lanesForNextManeuver</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lane">Lane</a></span><span class="p">],</span> <span class="nv">lanesForNextNextManeuver</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-lane">Lane</a></span><span class="p">])</span></code></pre>
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
