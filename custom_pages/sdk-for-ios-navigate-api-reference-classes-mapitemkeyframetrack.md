---
title: "sdk-for-ios-navigate-api-reference-classes-mapitemkeyframetrack"
slug: "sdk-for-ios-navigate-api-reference-classes-mapitemkeyframetrack"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapItemKeyFrameTrack"></a>
<a title="MapItemKeyFrameTrack Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>
<img alt="" id="carat" src="/carat.png"/>
<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>
<img alt="" id="carat" src="/carat.png"/>
        MapItemKeyFrameTrack Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapItemKeyFrameTrack</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapItemKeyFrameTrack</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapItemKeyFrameTrack</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapItemKeyFrameTrack</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Stores keyframes for interpolation of a map item property using a specific
easing function and interpolation mode.</p>
<p>The keyframe track object is used to create animations,
see <code><a href="sdk-for-ios-navigate-api-reference-classes-mapmarkeranimation">MapMarkerAnimation</a></code> and <code><a href="sdk-for-ios-navigate-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapItemKeyFrameTrackC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk20MapItemKeyFrameTrackC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create <code>MapItemKeyFrameTrack</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapitemkeyframetrack-instantiationerrorcode">InstantiationErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapItemKeyFrameTrackC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk20MapItemKeyFrameTrackC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to create a <code><a href="sdk-for-ios-navigate-api-reference-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-navigate-api-reference-classes-mapitemkeyframetrack-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapItemKeyFrameTrackC6moveTo9keyframes6easing17interpolationModeACSayAA22GeoCoordinatesKeyframeVG_AA6EasingCAA0o13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/moveTo(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk20MapItemKeyFrameTrackC6moveTo9keyframes6easing17interpolationModeACSayAA22GeoCoordinatesKeyframeVG_AA6EasingCAA0o13InterpolationL0OtKFZ">moveTo(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a map item position keyframe track. It enables animations over the geographical
coordinates where the map item is positioned.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapItemKeyFrameTrack.html#/s:7heresdk20MapItemKeyFrameTrackC18InstantiationErrora">MapItemKeyFrameTrack.InstantiationError</a></code> If the supplied keyframe list is empty or first keyframe duration is not 0.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">moveTo</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-geocoordinateskeyframe">GeoCoordinatesKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapItemKeyFrameTrack</span></code></pre>
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
<p>The list of keyframes that specify how the map item position changes over time.</p>
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
<p>MapItemKeyFrameTrack instance.</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapItemKeyFrameTrackC16polylineProgress9keyframes6easing17interpolationModeACSayAA14ScalarKeyframeVG_AA6EasingCAA0n13InterpolationL0OtKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/polylineProgress(keyframes:easing:interpolationMode:)"></a>
<a class="token" href="#/s:7heresdk20MapItemKeyFrameTrackC16polylineProgress9keyframes6easing17interpolationModeACSayAA14ScalarKeyframeVG_AA6EasingCAA0n13InterpolationL0OtKFZ">polylineProgress(keyframes:<wbr/>easing:<wbr/>interpolationMode:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a keyframe track used to animate the progress of a polyline.</p>
<p>Each scalar keyframe specifies the value of <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC8progressSdvp">MapPolyline.progress</a></code>
at key points of the animation.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapItemKeyFrameTrack.html#/s:7heresdk20MapItemKeyFrameTrackC18InstantiationErrora">MapItemKeyFrameTrack.InstantiationError</a></code> If the supplied keyframe list is empty or first keyframe duration is not 0.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">polylineProgress</span><span class="p">(</span><span class="nv">keyframes</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-navigate-api-reference-structs-scalarkeyframe">ScalarKeyframe</a></span><span class="p">],</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-easing">Easing</a></span><span class="p">,</span> <span class="nv">interpolationMode</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-enums-keyframeinterpolationmode">KeyframeInterpolationMode</a></span><span class="p">)</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt">MapItemKeyFrameTrack</span></code></pre>
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
<p>The list of keyframes that specify how the polyline progress changes
over time.</p>
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
<p>MapItemKeyFrameTrack instance.</p>
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
