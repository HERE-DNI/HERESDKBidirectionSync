---
title: "MapCameraKeyframeTrack"
slug: "sdk-for-ios-navigate-classes-mapcamerakeyframetrack"
---

<HTMLBlock> {
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraKeyframeTrack"></a>
<a title="MapCameraKeyframeTrack Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-index">heresdk</a>

<a href="sdk-for-ios-navigate-maps">Maps</a>

        MapCameraKeyframeTrack Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapCameraKeyframeTrack</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraKeyframeTrack</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraKeyframeTrack</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Stores keyframes for interpolation of a camera property using a specific easing function
and interpolation mode. Can only hold keyframes of a single type.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create <code>MapCameraKeyframeTrack</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack-instantiationerrorcode">InstantiationErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC17interpolationModeAA0d13InterpolationG0Ovp"></a>
<a class="dashAnchor" name="//apple_ref/swift/Property/interpolationMode"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC17interpolationModeAA0d13InterpolationG0Ovp">interpolationMode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Interpolation mode affects the shape of the spline going through all keyframes.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="k">var</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span> <span class="p">{</span> <span class="k">get</span> <span class="p">}</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to create a MapCameraKeyframeTrack.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC18getScalarKeyframesSayAA0gD0VGSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getScalarKeyframes()"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC18getScalarKeyframesSayAA0gD0VGSgyF">getScalarKeyframes()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getScalarKeyframes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a></span><span class="p">]?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>a copy of the scalar keyframes or nothing if this is not a scalar keyframe track.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC19getPoint2DKeyframesSayAA0G9DKeyframeVGSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getPoint2DKeyframes()"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC19getPoint2DKeyframesSayAA0G9DKeyframeVGSgyF">getPoint2DKeyframes()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getPoint2DKeyframes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-point2dkeyframe">Point2DKeyframe</a></span><span class="p">]?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>a copy of the point 2d keyframes or nothing if this is not a point 2d keyframe track.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC20getAnchor2DKeyframesSayAA0G9DKeyframeVGSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getAnchor2DKeyframes()"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC20getAnchor2DKeyframesSayAA0G9DKeyframeVGSgyF">getAnchor2DKeyframes()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getAnchor2DKeyframes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-anchor2dkeyframe">Anchor2DKeyframe</a></span><span class="p">]?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>a copy of the anchor 2d keyframes or nothing if this is not an anchor 2d keyframe track.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC26getGeoCoordinatesKeyframesSayAA0ghD0VGSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeoCoordinatesKeyframes()"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC26getGeoCoordinatesKeyframesSayAA0ghD0VGSgyF">getGeoCoordinatesKeyframes()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeoCoordinatesKeyframes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a></span><span class="p">]?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>a copy of the geo coordinates keyframes or nothing if this is not a geo coordinates keyframe track.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC26getGeoOrientationKeyframesSayAA0ghD0VGSgyF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/getGeoOrientationKeyframes()"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC26getGeoOrientationKeyframesSayAA0ghD0VGSgyF">getGeoOrientationKeyframes()</a>
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
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">func</span> <span class="nf">getGeoOrientationKeyframes</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geoorientationkeyframe">GeoOrientationKeyframe</a></span><span class="p">]?</span></code></pre>
</div>
</div>
<div>
<h4>Return Value</h4>
<p>a copy of the geo orientation keyframes or nothing if this is not a geo orientation keyframe track.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC14lookAtDistance9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAtDistance(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC14lookAtDistance9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ">lookAtDistance(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera look-at distance keyframe track. It enables animations of the distance
from the map camera to the target point that the camera looks at in meters. The values will
be clamped according to the minimum and maximum zoom levels set for the map camera.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">@available(*, deprecated, message: "Will be removed in v4.27.0. Use MapCameraKeyframeTrack.lookAtDistance(MapMeasure.Kind, [ScalarKeyframe], Easing, KeyframeInterpolationMode﹚ instead.")</span>
<span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAtDistance</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the distance from the map camera to its target.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC14lookAtDistance6ofKind9keyframes6easing17interpolationModeAcA0B7MeasureV0J0O_SayAA06ScalarD0VGAA6EasingCAA0d13InterpolationN0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAtDistance(ofKind:keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC14lookAtDistance6ofKind9keyframes6easing17interpolationModeAcA0B7MeasureV0J0O_SayAA06ScalarD0VGAA6EasingCAA0d13InterpolationN0OtKFZ">lookAtDistance(ofKind:<wbr/>keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera look-at distance keyframe track. It enables animations of the distance
from the map camera to the target point that the camera looks at. The measure kind of that distance can be
specified. The values will be clamped according to the minimum and maximum zoom levels set for the map
camera.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAtDistance</span><span class="p">(</span><span class="n">ofKind</span> <span class="nv">distanceKind</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-structs-mapmeasure">MapMeasure</a></span><span class="o">.</span><span class="kt">Kind</span><span class="p">,</span> <span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>distanceKind</em>
</code>
</td>
<td>
<div>
<p>The kind of measure of distance between camera and target point.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the distance from the map camera to its target.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC12lookAtTarget9keyframes6easing17interpolationModeACSayAA014GeoCoordinatesD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAtTarget(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC12lookAtTarget9keyframes6easing17interpolationModeACSayAA014GeoCoordinatesD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ">lookAtTarget(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera look-at target keyframe track. It enables animations over the
geographical coordinates of the target point that the map camera is looking at.
Altitude components of coordinates are ignored.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAtTarget</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the map camera target coordinates.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC17lookAtOrientation9keyframes6easing17interpolationModeACSayAA03GeohD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/lookAtOrientation(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC17lookAtOrientation9keyframes6easing17interpolationModeACSayAA03GeohD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ">lookAtOrientation(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera look-at orientation keyframe track. It enables animations over the
orientation of the map camera target (bearing and tilt).</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">lookAtOrientation</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-geoorientationkeyframe">GeoOrientationKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the map camera target orientation.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC14principalPoint9keyframes6easing17interpolationModeACSayAA15Point2DKeyframeVG_AA6EasingCAA0d13InterpolationK0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/principalPoint(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC14principalPoint9keyframes6easing17interpolationModeACSayAA15Point2DKeyframeVG_AA6EasingCAA0d13InterpolationK0OtKFZ">principalPoint(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera principal point keyframe track. It enables animations on the pixel point
where the map camera’s target is placed in view coordinates. (0,0) is top left of the
viewport, (viewport width, viewport height) is bottom right.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">principalPoint</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-point2dkeyframe">Point2DKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Point values must be in screen (pixel) coordinates with origin (0,0) in the top left of the viewport.
Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the principal point.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC24normalizedPrincipalPoint9keyframes6easing17interpolationModeACSayAA16Anchor2DKeyframeVG_AA6EasingCAA0d13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/normalizedPrincipalPoint(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC24normalizedPrincipalPoint9keyframes6easing17interpolationModeACSayAA16Anchor2DKeyframeVG_AA6EasingCAA0d13InterpolationL0OtKFZ">normalizedPrincipalPoint(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera principal point keyframe track. It enables animations on the point
where the map camera’s target is placed in normalized view coordinates. (0,0) is top left of
the viewport, (1, 1) is bottom right.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">normalizedPrincipalPoint</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-anchor2dkeyframe">Anchor2DKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport.
Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the principal point.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk22MapCameraKeyframeTrackC11fieldOfView9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/fieldOfView(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk22MapCameraKeyframeTrackC11fieldOfView9keyframes6easing17interpolationModeACSayAA06ScalarD0VG_AA6EasingCAA0d13InterpolationL0OtKFZ">fieldOfView(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map camera field-of-view keyframe track. It enables animations over the angle of
the field of view captured by the map camera in degrees. Values will be clamped to a range
from 1 to 150.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraKeyframeTrack.html#/s:7heresdk22MapCameraKeyframeTrackC18InstantiationErrora">MapCameraKeyframeTrack.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">fieldOfView</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-structs-scalarkeyframe">ScalarKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapCameraKeyframeTrack</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>keyframes</em>
</code>
</td>
<td>
<div>
<p>The list of keyframes that specify how the camera property is changed.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>easing</em>
</code>
</td>
<td>
<div>
<p>The easing to apply during keyframe interpolation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>interpolationMode</em>
</code>
</td>
<td>
<div>
<p>The type of interpolation done between keyframe values.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>A keyframe track over the map camera field-of-view.</p>
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
