---
title: "MapPolylineAnimation"
slug: "sdk-for-ios-explore-api-reference-classes-mappolylineanimation"
---

<HTMLBlock>{
`
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolylineAnimation"></a>
<a title="MapPolylineAnimation Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-index">heresdk</a>

<a href="sdk-for-ios-explore-api-reference-maps">Maps</a>

        MapPolylineAnimation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapPolylineAnimation</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapPolylineAnimation</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolylineAnimation</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapPolylineAnimation</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>An animation that can be applied to the <code><a href="sdk-for-ios-explore-api-reference-classes-mappolyline">MapPolyline</a></code> object.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapPolylineAnimationC18InstantiationErrora"></a>
<a class="dashAnchor" name="//apple_ref/swift/Alias/InstantiationError"></a>
<a class="token" href="#/s:7heresdk20MapPolylineAnimationC18InstantiationErrora">InstantiationError</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Thrown when a problem occurs while trying to create a <code>MapPolylineAnimation</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">typealias</span> <span class="kt">InstantiationError</span> <span class="o">=</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mappolylineanimation-instantiationerrorcode">InstantiationErrorCode</a></span></code></pre>
</div>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk20MapPolylineAnimationC5trackAcA0B17ItemKeyFrameTrackC_tKcfc"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/init(track:)"></a>
<a class="token" href="#/s:7heresdk20MapPolylineAnimationC5trackAcA0B17ItemKeyFrameTrackC_tKcfc">init(track:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates an animation of <code><a href="sdk-for-ios-explore-api-reference-classes-mappolyline">MapPolyline</a></code> based on provided keyframe track.
Supports tracks created with <code><a href="sdk-for-ios-explore-api-reference-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a></code> ‘polylineProgress*’ methods.
For starting the animation, see <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF">MapPolyline.startAnimation(...)</a></code>.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapPolylineAnimation.html#/s:7heresdk20MapPolylineAnimationC18InstantiationErrora">MapPolylineAnimation.InstantiationError</a></code> If the specified keyframe track cannot be used to create animation of a <code><a href="sdk-for-ios-explore-api-reference-classes-mappolyline">MapPolyline</a></code>.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="nf">init</span><span class="p">(</span><span class="nv">track</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mapitemkeyframetrack">MapItemKeyFrameTrack</a></span><span class="p">)</span> <span class="k">throws</span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>track</em>
</code>
</td>
<td>
<div>
<p>The track holding the keyframes for the animation.</p>
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
<a name="/s:7heresdk20MapPolylineAnimationC22InstantiationErrorCodeO"></a>
<a class="dashAnchor" name="//apple_ref/swift/Enum/InstantiationErrorCode"></a>
<a class="token" href="#/s:7heresdk20MapPolylineAnimationC22InstantiationErrorCodeO">InstantiationErrorCode</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Describes a reason for failing to create a <code><a href="sdk-for-ios-explore-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></code>.</p>
<a class="slightly-smaller" href="sdk-for-ios-explore-api-reference-classes-mappolylineanimation-instantiationerrorcode">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">enum</span> <span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">UInt32</span><span class="p">,</span> <span class="kt">CaseIterable</span><span class="p">,</span> <span class="kt">Codable</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-classes-mappolylineanimation">MapPolylineAnimation</a></span><span class="o">.</span><span class="kt">InstantiationErrorCode</span> <span class="p">:</span> <span class="kt">Error</span></code></pre>
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
