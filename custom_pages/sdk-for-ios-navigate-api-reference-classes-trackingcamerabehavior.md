---
title: "Untitled"
slug: "sdk-for-ios-navigate-api-reference-classes-trackingcamerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- TrackingCameraBehavior.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/TrackingCameraBehavior"></a>
<a title="TrackingCameraBehavior Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-..-navigation">Navigation</a>
<img alt="" id="carat" src="../img/carat.png"/>
        TrackingCameraBehavior Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>TrackingCameraBehavior</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">TrackingCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrackingCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">TrackingCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Use this class to follow a moving target. The camera smoothly tracks the target’s
position while adjusting heading, tilt, and zoom as needed. When tracking starts
or resumes, the camera first animates a re-centering transition to align with the target.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorCACycfc">init()</a>
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
<a name="/s:7heresdk22TrackingCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/normalizedPrincipalPoint"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp">normalizedPrincipalPoint</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">normalizedPrincipalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-anchor2d">Anchor2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC25recenterAnimationDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/recenterAnimationDuration"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC25recenterAnimationDurationSdvp">recenterAnimationDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The duration of recenter animation in milliseconds.
Time to recenter the camera reaching current car position.
Defaults to 500 milliseconds, or half a second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">recenterAnimationDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewRectangle"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp">viewRectangle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates.
Defaults to <code>nil</code>. If not set, it uses the viewport bounds of the underlying map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-structs-rectangle2d">Rectangle2D</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC31principalPointAnimationDurationSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/principalPointAnimationDuration"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC31principalPointAnimationDurationSdvp">principalPointAnimationDuration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The duration of principal point animation in milliseconds.
If the principal point is changed, the change will be animated
over this duration.
Defaults to 500 milliseconds, or half a second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">principalPointAnimationDuration</span><span class="p">:</span> <span class="kt">TimeInterval</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC13tiltInDegreesSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/tiltInDegrees"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC13tiltInDegreesSdvp">tiltInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The value of camera tilt in degrees.
Camera tilt angle relative to the ground plane, in degrees.
Defaults to 50.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">tiltInDegrees</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC16bearingInDegreesSdSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/bearingInDegrees"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC16bearingInDegreesSdSgvp">bearingInDegrees</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The camera bearing in degrees.
Optional fixed bearing, from true North (0 degrees) in clockwise direction. The valid range
is [0, 360].
If set, it will prevent the map from rotating to the direction of travel. For example, a
value of zero results in “north up” mode.
Defaults to <code>nil</code>, which means the camera derives the bearing from the <code><a href="sdk-for-ios-navigate-api-reference-..-structs-location">Location</a></code>,
so that it points to the direction of travel.
If this property is <code>nil</code> and the device does not provide bearing, the last known value is
used or zero otherwise.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">bearingInDegrees</span><span class="p">:</span> <span class="kt">Double</span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC34maxRotationSpeedInDegreesPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/maxRotationSpeedInDegreesPerSecond"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC34maxRotationSpeedInDegreesPerSecondSdvp">maxRotationSpeedInDegreesPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The maximum rotation speed.
Maximum bearing rotation speed in degrees per second,
limiting how fast the camera turns.
Defaults to 20 degrees per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">maxRotationSpeedInDegreesPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC26zoomSpeedInLevelsPerSecondSdvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoomSpeedInLevelsPerSecond"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC26zoomSpeedInLevelsPerSecondSdvp">zoomSpeedInLevelsPerSecond</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The zoom level transition speed.
Speed factor controlling how quickly the camera
transitions between zoom levels
Defaults to 0.5 zoom levels per second.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoomSpeedInLevelsPerSecond</span><span class="p">:</span> <span class="kt">Double</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC10zoomPolicyAC04ZoomF0Cvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/zoomPolicy"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC10zoomPolicyAC04ZoomF0Cvp">zoomPolicy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The strategy of computing the zoom level.
Defines the strategy used to compute the zoom level based on scene heuristics.
Defaults to a fixed zoom policy at zoom level 16.5.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">zoomPolicy</span><span class="p">:</span> <span class="kt">TrackingCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-zoompolicy">ZoomPolicy</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC26isManeuverDetectionEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isManeuverDetectionEnabled"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC26isManeuverDetectionEnabledSbvp">isManeuverDetectionEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Whether maneuver detection is enabled.
When <code>true</code>, the camera detects adjacent maneuvers and reacts according to
the <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">TrackingCameraBehavior.ManeuverModeConfiguration</a></code> set via <code><a href="../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC28setManeuverModeConfiguration08maneuvergH0yAC0fgH0VSg_tF">TrackingCameraBehavior.setManeuverModeConfiguration(...)</a></code>.
A valid <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">TrackingCameraBehavior.ManeuverModeConfiguration</a></code> must be set for the camera to react. Defaults to <code>false</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">isManeuverDetectionEnabled</span><span class="p">:</span> <span class="kt">Bool</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC"></a>
<a class="dashAnchor" name="//apple_ref/swift/Class/ZoomPolicy"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC10ZoomPolicyC">ZoomPolicy</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines zoom behavior in different policy settings.</p>
<p>Note: This is a beta feature; there maybe bugs and unexpected behavior. Related API’s are
subject to change without a deprecation process.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-zoompolicy">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">ZoomPolicy</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></span><span class="o">.</span><span class="kt">ZoomPolicy</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedThreshold"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC14SpeedThresholdV">SpeedThreshold</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a zoom level triggered when the vehicle reaches a specific speed.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-speedthreshold">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedThreshold</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/FunctionalRoadClassZoomPolicyOptions"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC36FunctionalRoadClassZoomPolicyOptionsV">FunctionalRoadClassZoomPolicyOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration for mapping functional road classes to zoom levels.
For correct default initialization, use <code><a href="../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">TrackingCameraBehavior.defaultFunctionalRoadClassZoomPolicyOptions(...)</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">FunctionalRoadClassZoomPolicyOptions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/SpeedBasedZoomPolicyOptions"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC27SpeedBasedZoomPolicyOptionsV">SpeedBasedZoomPolicyOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration for computing zoom levels from speed thresholds defined per road classification.
For correct default initialization, use <code><a href="../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">TrackingCameraBehavior.defaultSpeedBasedZoomPolicyOptions(...)</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">SpeedBasedZoomPolicyOptions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverZoomRange"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC17ManeuverZoomRangeV">ManeuverZoomRange</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the bounds within which the zoom level is constrained when approaching a maneuver.
Used as part of <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuverruleoptions">TrackingCameraBehavior.ManeuverRuleOptions</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuverzoomrange">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverZoomRange</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverRuleOptions"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC19ManeuverRuleOptionsV">ManeuverRuleOptions</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a set of configurations specific to a <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuverrule">TrackingCameraBehavior.ManeuverRule</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuverruleoptions">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverRuleOptions</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverRule"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC12ManeuverRuleV">ManeuverRule</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines a single rule that determines how <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> reacts to nearby
maneuvers when the current position matches this rule.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuverrule">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverRule</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV"></a>
<a class="dashAnchor" name="//apple_ref/swift/Struct/ManeuverModeConfiguration"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV">ManeuverModeConfiguration</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configuration that defines how <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> reacts to nearby maneuvers.</p>
<p>On each frame, and based on the current position, the availability of its functional road
class, and the availability of maneuver data for at least one adjacent maneuver, the camera
checks for a match against the <code><a href="../Classes/TrackingCameraBehavior/ManeuverModeConfiguration.html#/s:7heresdk22TrackingCameraBehaviorC25ManeuverModeConfigurationV13maneuverRulesSayAC0E4RuleVGvp">TrackingCameraBehavior.ManeuverModeConfiguration.maneuverRules</a></code> in the order they are listed. If a match is
found, subsequent rules are not checked. If no match is found, if inputs are unavailable,
or if the matched rule has <code>nil</code> options, the camera does not react.</p>
<p>For correct default initialization, use <code><a href="../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ">TrackingCameraBehavior.defaultManeuverModeConfiguration(...)</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">struct</span> <span class="kt">ManeuverModeConfiguration</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC33flagFixedDurationForNextAnimationyyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/flagFixedDurationForNextAnimation()"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC33flagFixedDurationForNextAnimationyyF">flagFixedDurationForNextAnimation()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables fixed-duration animation mode for the next property change.
When called, the next setter call (e.g., tilt_in_degrees or bearing_in_degrees)
will animate using a fast fixed-duration animation instead of the default
speed-based animation. The flag is automatically reset after the next setter is called.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">flagFixedDurationForNextAnimation</span><span class="p">()</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC28setManeuverModeConfiguration08maneuvergH0yAC0fgH0VSg_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setManeuverModeConfiguration(maneuverModeConfiguration:)"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC28setManeuverModeConfiguration08maneuvergH0yAC0fgH0VSg_tF">setManeuverModeConfiguration(maneuverModeConfiguration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Sets the configuration for camera behavior near maneuvers.
Defines how the camera reacts to nearby maneuvers when
<code><a href="../Classes/TrackingCameraBehavior.html#/s:7heresdk22TrackingCameraBehaviorC26isManeuverDetectionEnabledSbvp">TrackingCameraBehavior.isManeuverDetectionEnabled</a></code> is <code>true</code>. When set to <code>nil</code>, the camera does
not react to maneuvers. The configuration must contain at least one rule to be valid.
Defaults to <code>nil</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setManeuverModeConfiguration</span><span class="p">(</span><span class="nv">maneuverModeConfiguration</span><span class="p">:</span> <span class="kt">TrackingCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">ManeuverModeConfiguration</a></span><span class="p">?)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>maneuverModeConfiguration</em>
</code>
</td>
<td>
<div>
<p>The maneuver mode configuration. Invalid configurations are rejected.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC28getManeuverModeConfigurationAC0fgH0VSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getManeuverModeConfiguration()"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC28getManeuverModeConfigurationAC0fgH0VSgyF">getManeuverModeConfiguration()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Gets the current maneuver mode configuration, or <code>nil</code> if not set.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getManeuverModeConfiguration</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">TrackingCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">ManeuverModeConfiguration</a></span><span class="p">?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The current maneuver mode configuration.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/defaultFunctionalRoadClassZoomPolicyOptions()"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC43defaultFunctionalRoadClassZoomPolicyOptionsAC0fghijK0VyFZ">defaultFunctionalRoadClassZoomPolicyOptions()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">defaultFunctionalRoadClassZoomPolicyOptions</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">TrackingCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">FunctionalRoadClassZoomPolicyOptions</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The default <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-functionalroadclasszoompolicyoptions">TrackingCameraBehavior.FunctionalRoadClassZoomPolicyOptions</a></code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/defaultSpeedBasedZoomPolicyOptions()"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC34defaultSpeedBasedZoomPolicyOptionsAC0fghiJ0VyFZ">defaultSpeedBasedZoomPolicyOptions()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">defaultSpeedBasedZoomPolicyOptions</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">TrackingCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">SpeedBasedZoomPolicyOptions</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The default <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-speedbasedzoompolicyoptions">TrackingCameraBehavior.SpeedBasedZoomPolicyOptions</a></code>.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/defaultManeuverModeConfiguration()"></a>
<a class="token" href="#/s:7heresdk22TrackingCameraBehaviorC32defaultManeuverModeConfigurationAC0fgH0VyFZ">defaultManeuverModeConfiguration()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">defaultManeuverModeConfiguration</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kt">TrackingCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">ManeuverModeConfiguration</a></span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>The default <code><a href="sdk-for-ios-navigate-api-reference-..-classes-trackingcamerabehavior-maneuvermodeconfiguration">TrackingCameraBehavior.ManeuverModeConfiguration</a></code>.</p>
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
