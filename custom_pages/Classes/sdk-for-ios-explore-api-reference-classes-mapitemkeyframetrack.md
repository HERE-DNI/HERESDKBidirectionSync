---
title: "MapItemKeyFrameTrack Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mapitemkeyframetrack"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapItemKeyFrameTrack.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MapItemKeyFrameTrack"></a>
<a title="MapItemKeyFrameTrack Class Reference"></a>
<header>
<div class="content-wrapper">
<p><a href="../index.html">heresdk Docs</a> (99% documented)</p>
<div class="header-right">

</div>
</div>
</header>
<div class="content-wrapper">
<p id="breadcrumbs">
<a href="../index.html">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="../Maps.html">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapItemKeyFrameTrack Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MapItemKeyFrameTrack</code></pre>
<pre><code>extension MapItemKeyFrameTrack: NativeBase</code></pre>
<pre><code>extension MapItemKeyFrameTrack: Hashable</code></pre>
</div>
</div>
<p>Stores keyframes for interpolation of a map item property using a specific
easing function and interpolation mode.</p>
<p>The keyframe track object is used to create animations,
see <code><a href="../Classes/MapMarkerAnimation.html">MapMarkerAnimation</a></code> and <code><a href="../Classes/MapPolylineAnimation.html">MapPolylineAnimation</a></code>.</p>
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
<pre><code>public typealias InstantiationError = InstantiationErrorCode</code></pre>
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
<p>Describes a reason for failing to create a <code><a href="../Classes/MapItemKeyFrameTrack.html">MapItemKeyFrameTrack</a></code>.</p>
<a class="slightly-smaller" href="../Classes/MapItemKeyFrameTrack/InstantiationErrorCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
<pre><code>extension MapItemKeyFrameTrack.InstantiationErrorCode : Error</code></pre>
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
<pre><code>public static func moveTo(keyframes: [GeoCoordinatesKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -&gt; MapItemKeyFrameTrack</code></pre>
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
<pre><code>public static func polylineProgress(keyframes: [ScalarKeyframe], easing: Easing, interpolationMode: KeyframeInterpolationMode) throws -&gt; MapItemKeyFrameTrack</code></pre>
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



</div>
`
}</HTMLBlock>
