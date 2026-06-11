---
title: "InstantiationErrorCode"
slug: "sdk-for-ios-navigate-api-reference-classes-mapcameraanimation-instantiationerrorcode"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a title="InstantiationErrorCode Enumeration Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-navigate-api-reference-index">heresdk</a>

<a href="sdk-for-ios-navigate-api-reference-maps">Maps</a>

<a href="sdk-for-ios-navigate-api-reference-classes-mapcameraanimation">MapCameraAnimation</a>

        InstantiationErrorCode Enumeration Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>InstantiationErrorCode</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-navigate-api-reference-classes-mapcameraanimation">MapCameraAnimation</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
</div>
</div>
<p>Describes a reason for failing to create a multi-track <code><a href="sdk-for-ios-navigate-api-reference-classes-mapcameraanimation">MapCameraAnimation</a></code>.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO14emptyTrackListyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/emptyTrackList"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO14emptyTrackListyA2EmF">emptyTrackList</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks is empty.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">emptyTrackList</span> <span class="o">=</span> <span class="mi">1</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC14PositionTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraPositionTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC14PositionTracksyA2EmF">multipleCameraPositionTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera position tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraPositionTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC17LookatTargetTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraPositionModifiedByCameraLookatTargetTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC17LookatTargetTrackyA2EmF">cameraPositionModifiedByCameraLookatTargetTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s position is already modified by an earlier track that modifies camera’s look-at target.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraPositionModifiedByCameraLookatTargetTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC22LookatOrientationTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraPositionModifiedByCameraLookatOrientationTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC22LookatOrientationTrackyA2EmF">cameraPositionModifiedByCameraLookatOrientationTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s position is already modified by an earlier track that modifies camera’s look-at orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraPositionModifiedByCameraLookatOrientationTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC19LookatDistanceTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraPositionModifiedByCameraLookatDistanceTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO024cameraPositionModifiedByC19LookatDistanceTrackyA2EmF">cameraPositionModifiedByCameraLookatDistanceTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s position is already modified by an earlier track that modifies camera’s look-at distance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraPositionModifiedByCameraLookatDistanceTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17OrientationTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraOrientationTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17OrientationTracksyA2EmF">multipleCameraOrientationTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera orientation tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraOrientationTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByc6LookatI5TrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraOrientationModifiedByCameraLookatOrientationTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByc6LookatI5TrackyA2EmF">cameraOrientationModifiedByCameraLookatOrientationTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s orientation is already modified by an earlier track that modifies camera’s look-at orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraOrientationModifiedByCameraLookatOrientationTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByC19LookatDistanceTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraOrientationModifiedByCameraLookatDistanceTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO027cameraOrientationModifiedByC19LookatDistanceTrackyA2EmF">cameraOrientationModifiedByCameraLookatDistanceTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s orientation is already modified by an earlier track that modifies camera’s look-at distance.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraOrientationModifiedByCameraLookatDistanceTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC18LookatTargetTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraLookatTargetTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC18LookatTargetTracksyA2EmF">multipleCameraLookatTargetTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera look-at target tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraLookatTargetTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC13PositionTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraLookatTargetModifiedByCameraPositionTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC13PositionTrackyA2EmF">cameraLookatTargetModifiedByCameraPositionTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s look-at target is already modified by an earlier track that modifies camera’s position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraLookatTargetModifiedByCameraPositionTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC16OrientationTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraLookatTargetModifiedByCameraOrientationTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO028cameraLookatTargetModifiedByC16OrientationTrackyA2EmF">cameraLookatTargetModifiedByCameraOrientationTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s look-at target is already modified by an earlier track that modifies camera’s orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraLookatTargetModifiedByCameraOrientationTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC23LookatOrientationTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraLookatOrientationTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC23LookatOrientationTracksyA2EmF">multipleCameraLookatOrientationTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera look-at orientation tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraLookatOrientationTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedByC13PositionTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraLookatOrientationModifiedByCameraPositionTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedByC13PositionTrackyA2EmF">cameraLookatOrientationModifiedByCameraPositionTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s look-at orientation is already modified by an earlier track that modifies camera’s position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraLookatOrientationModifiedByCameraPositionTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedBycJ5TrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraLookatOrientationModifiedByCameraOrientationTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO033cameraLookatOrientationModifiedBycJ5TrackyA2EmF">cameraLookatOrientationModifiedByCameraOrientationTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s look-at orientation is already modified by an earlier track that modifies camera’s orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraLookatOrientationModifiedByCameraOrientationTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20LookatDistanceTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraLookatDistanceTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20LookatDistanceTracksyA2EmF">multipleCameraLookatDistanceTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera look-at distance tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraLookatDistanceTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC13PositionTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraLookatDistanceModifiedByCameraPositionTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC13PositionTrackyA2EmF">cameraLookatDistanceModifiedByCameraPositionTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s look-at distance is already modified by an earlier track that modifies camera’s position.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraLookatDistanceModifiedByCameraPositionTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC16OrientationTrackyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/cameraLookatDistanceModifiedByCameraOrientationTrack"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO030cameraLookatDistanceModifiedByC16OrientationTrackyA2EmF">cameraLookatDistanceModifiedByCameraOrientationTrack</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Camera’s look-at distance is already modified by an earlier track that modifies camera’s orientation.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">cameraLookatDistanceModifiedByCameraOrientationTrack</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FieldOfViewTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraFieldOfViewTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FieldOfViewTracksyA2EmF">multipleCameraFieldOfViewTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera field-of-view tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraFieldOfViewTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FocalLengthTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraFocalLengthTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC17FocalLengthTracksyA2EmF">multipleCameraFocalLengthTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera focal length tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraFocalLengthTracks</span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20PrincipalPointTracksyA2EmF"></a>
<a class="dashAnchor" name="//apple_ref/swift/Element/multipleCameraPrincipalPointTracks"></a>
<a class="token" href="#/s:7heresdk18MapCameraAnimationC22InstantiationErrorCodeO08multipleC20PrincipalPointTracksyA2EmF">multipleCameraPrincipalPointTracks</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>List of keyframe tracks contains multiple camera principal point tracks.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="k">case</span> <span class="n">multipleCameraPrincipalPointTracks</span></code></pre>
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
