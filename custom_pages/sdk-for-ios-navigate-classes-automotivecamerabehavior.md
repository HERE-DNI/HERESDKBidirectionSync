---
title: "AutomotiveCameraBehavior"
slug: "sdk-for-ios-navigate-classes-automotivecamerabehavior"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/AutomotiveCameraBehavior"></a>
<a title="AutomotiveCameraBehavior Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-navigation">Navigation</a>

        AutomotiveCameraBehavior Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>AutomotiveCameraBehavior</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">AutomotiveCameraBehavior</span> <span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-protocols-camerabehavior">CameraBehavior</a></span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AutomotiveCameraBehavior</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">AutomotiveCameraBehavior</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Provides a high-level camera controller for automotive navigation that manages both tracking
and area camera behaviors. This class acts as a facade, delegating camera operations to either
a <code><a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> for following the vehicle during navigation or an <code><a href="sdk-for-ios-navigate-classes-areacamerabehavior">AreaCameraBehavior</a></code>
for showing overview areas such as points of interest or route previews.</p>
<p>The controller supports three states: tracking mode (following the vehicle), area mode (showing
geographic regions), or inactive (no automatic camera control). The inactive state allows
external control of the camera, such as when responding to user touch events or when UI logic
temporarily disables automatic camera behavior.</p>
<p>Camera configuration, including animation durations, zoom policies, and maneuver handling
settings, can be provided through a JSON configuration string or file. The configuration is
validated and parsed during construction.</p>
<p>Note: This is a <strong>beta</strong> release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorCACycfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init()"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorCACycfc">init()</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class with default camera behaviors and configuration.
This constructor automatically creates and configures the underlying
<code><a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> and <code><a href="sdk-for-ios-navigate-classes-areacamerabehavior">AreaCameraBehavior</a></code> instances with default settings.</p>
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
<a name="/s:7heresdk24AutomotiveCameraBehaviorC10configJsonACSS_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(configJson:)"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC10configJsonACSS_tKcfc">init(configJson:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a new instance of this class configured from a JSON string.
The JSON configuration is validated during construction and applied to the
underlying <code><a href="sdk-for-ios-navigate-classes-trackingcamerabehavior">TrackingCameraBehavior</a></code> and <code><a href="sdk-for-ios-navigate-classes-areacamerabehavior">AreaCameraBehavior</a></code> instances.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> <code><a href="../Core.html#/s:7heresdk18InstantiationErrora">InstantiationError</a></code> when the JSON is malformed or contains
invalid values.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">configJson</span><span class="p">:</span> <span class="kt">String</span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>configJson</em>
</code>
</td>
<td>
<div>
<p>A JSON string containing automotive camera configuration settings.</p>
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
<a name="/s:7heresdk24AutomotiveCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/normalizedPrincipalPoint"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC24normalizedPrincipalPointAA8Anchor2DVvp">normalizedPrincipalPoint</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">normalizedPrincipalPoint</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-anchor2d">Anchor2D</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC26isManeuverDetectionEnabledSbvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/isManeuverDetectionEnabled"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC26isManeuverDetectionEnabledSbvp">isManeuverDetectionEnabled</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Enables or disables automatic camera adjustments during upcoming maneuvers.
When enabled, the tracking camera automatically adjusts zoom and framing to provide
better visibility of upcoming turns and maneuvers during navigation. The specific
adjustments and their timing are defined in the camera configuration.</p>
<p>If tracking is currently active when this property is changed, the setting takes effect
immediately. Otherwise, it will apply the next time tracking is activated. The initial
state is determined by the camera configuration provided during construction.</p>
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
<a name="/s:7heresdk24AutomotiveCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/viewRectangle"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC13viewRectangleAA11Rectangle2DVSgvp">viewRectangle</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The view rectangle for camera updates.
Defines a sub-space of the screen that the behavior should consider
for camera updates. This property is forwarded to both the tracking and area cameras,
ensuring consistent viewport constraints across all camera modes.
If not set, it uses the viewport bounds of the underlying map view.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">viewRectangle</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-rectangle2d">Rectangle2D</a></span><span class="p">?</span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/activeCameraType"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">activeCameraType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The active camera type.
Defines which camera behavior is currently active:
<code><a href="../Classes/AutomotiveCameraBehavior/ActiveCameraType.html#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4noneyA2EmF">AutomotiveCameraBehavior.ActiveCameraType.none</a></code> (free navigation), <code><a href="../Classes/AutomotiveCameraBehavior/ActiveCameraType.html#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO8trackingyA2EmF">AutomotiveCameraBehavior.ActiveCameraType.tracking</a></code>,
or <code><a href="../Classes/AutomotiveCameraBehavior/ActiveCameraType.html#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4areayA2EmF">AutomotiveCameraBehavior.ActiveCameraType.area</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">activeCameraType</span><span class="p">:</span> <span class="kt">AutomotiveCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype">ActiveCameraType</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC15orientationModeAC011OrientationF0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/orientationMode"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC15orientationModeAC011OrientationF0Ovp">orientationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>The current orientation mode of the camera.
Defines the camera’s viewing angle and orientation for tracking mode.
In <code><a href="../Classes/AutomotiveCameraBehavior/OrientationMode.html#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO6mode2dyA2EmF">AutomotiveCameraBehavior.OrientationMode.mode2d</a></code>, the camera looks straight down and rotates with the vehicle heading.
In <code><a href="../Classes/AutomotiveCameraBehavior/OrientationMode.html#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO6mode3dyA2EmF">AutomotiveCameraBehavior.OrientationMode.mode3d</a></code>, the camera is tilted for a perspective view.
In <code><a href="../Classes/AutomotiveCameraBehavior/OrientationMode.html#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO11modeNorthUpyA2EmF">AutomotiveCameraBehavior.OrientationMode.modeNorthUp</a></code>, the camera maintains north-up orientation regardless of vehicle heading.</p>
<p>Changes to this property take effect immediately on the tracking camera and are
preserved when switching between tracking and area modes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">orientationMode</span><span class="p">:</span> <span class="kt">AutomotiveCameraBehavior</span><span class="o">.</span><span class="kt"><a href="sdk-for-ios-navigate-classes-automotivecamerabehavior-orientationmode">OrientationMode</a></span> <span class="p">{</span> <span class="k">get</span> <span class="k">set</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/OrientationMode"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC15OrientationModeO">OrientationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the visual presentation modes for the camera orientation.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-automotivecamerabehavior-orientationmode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">OrientationMode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/ActiveCameraType"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO">ActiveCameraType</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Defines the type of camera currently handling camera updates.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-automotivecamerabehavior-activecameratype">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">ActiveCameraType</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk24AutomotiveCameraBehaviorC07setAreacD13VisiblePoints6points22includeCurrentPositionySayAA14GeoCoordinatesVG_SbtF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAreaCameraBehaviorVisiblePoints(points:includeCurrentPosition:)"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC07setAreacD13VisiblePoints6points22includeCurrentPositionySayAA14GeoCoordinatesVG_SbtF">setAreaCameraBehaviorVisiblePoints(points:<wbr/>includeCurrentPosition:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the Area camera to frame the specified points.
The camera calculates the optimal zoom level and center position to display
all provided coordinates within the viewport. Use this for showing a single
point of interest or multiple points such as safety cameras.</p>
<p>This function does not change <code><a href="../Classes/AutomotiveCameraBehavior.html#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">AutomotiveCameraBehavior.activeCameraType</a></code>. To display the configured
area view, set <code><a href="../Classes/AutomotiveCameraBehavior.html#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">AutomotiveCameraBehavior.activeCameraType</a></code> to <code><a href="../Classes/AutomotiveCameraBehavior/ActiveCameraType.html#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4areayA2EmF">AutomotiveCameraBehavior.ActiveCameraType.area</a></code>.</p>
<p>Calling this function overrides any previously set geographic bounding box
configured via <code><a href="../Classes/AutomotiveCameraBehavior.html#/s:7heresdk24AutomotiveCameraBehaviorC07setAreacD6Geobox6geoboxyAA6GeoBoxV_tF">AutomotiveCameraBehavior.setAreaCameraBehaviorGeobox(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setAreaCameraBehaviorVisiblePoints</span><span class="p">(</span><span class="nv">points</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geocoordinates">GeoCoordinates</a></span><span class="p">],</span> <span class="nv">includeCurrentPosition</span><span class="p">:</span> <span class="kt">Bool</span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>points</em>
</code>
</td>
<td>
<div>
<p>The list of geographic coordinates to display.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>includeCurrentPosition</em>
</code>
</td>
<td>
<div>
<p>When true, the current vehicle position is
included in the visible area calculation, ensuring the vehicle remains
visible alongside the provided points.</p>
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
<a name="/s:7heresdk24AutomotiveCameraBehaviorC07setAreacD6Geobox6geoboxyAA6GeoBoxV_tF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/setAreaCameraBehaviorGeobox(geobox:)"></a>
<a class="token" href="#/s:7heresdk24AutomotiveCameraBehaviorC07setAreacD6Geobox6geoboxyAA6GeoBoxV_tF">setAreaCameraBehaviorGeobox(geobox:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Configures the Area camera to frame the specified geographic bounding box.
The camera automatically calculates the appropriate zoom level and center
position to ensure the entire area is visible within the viewport.</p>
<p>This function does not change <code><a href="../Classes/AutomotiveCameraBehavior.html#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">AutomotiveCameraBehavior.activeCameraType</a></code>. To display the configured
area view, set <code><a href="../Classes/AutomotiveCameraBehavior.html#/s:7heresdk24AutomotiveCameraBehaviorC06activeC4TypeAC06ActivecF0Ovp">AutomotiveCameraBehavior.activeCameraType</a></code> to <code><a href="../Classes/AutomotiveCameraBehavior/ActiveCameraType.html#/s:7heresdk24AutomotiveCameraBehaviorC06ActiveC4TypeO4areayA2EmF">AutomotiveCameraBehavior.ActiveCameraType.area</a></code>.</p>
<p>Calling this function overrides any previously set visible points configured
via <code><a href="../Classes/AutomotiveCameraBehavior.html#/s:7heresdk24AutomotiveCameraBehaviorC07setAreacD13VisiblePoints6points22includeCurrentPositionySayAA14GeoCoordinatesVG_SbtF">AutomotiveCameraBehavior.setAreaCameraBehaviorVisiblePoints(...)</a></code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">setAreaCameraBehaviorGeobox</span><span class="p">(</span><span class="nv">geobox</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-geobox">GeoBox</a></span><span class="p">)</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>geobox</em>
</code>
</td>
<td>
<div>
<p>The geographic bounding box to display.</p>
</div>
</td>
</tr>
</tbody>
</table>
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
