---
title: "MapPolylineAnimation Class Reference"
slug: "sdk-for-ios-explore-api-reference-classes-mappolylineanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapPolylineAnimation.html -->
<!DOCTYPE html>




<a class="dashAnchor" name="//apple_ref/swift/Class/MapPolylineAnimation"></a>
<a title="MapPolylineAnimation Class Reference"></a>
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
        MapPolylineAnimation Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">

<div class="declaration">
<div class="language">
<pre><code>public class MapPolylineAnimation</code></pre>
<pre><code>extension MapPolylineAnimation: NativeBase</code></pre>
<pre><code>extension MapPolylineAnimation: Hashable</code></pre>
</div>
</div>
<p>An animation that can be applied to the <code><a href="../Classes/MapPolyline.html">MapPolyline</a></code> object.</p>
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
<pre><code>public typealias InstantiationError = InstantiationErrorCode</code></pre>
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
<p>Creates an animation of <code><a href="../Classes/MapPolyline.html">MapPolyline</a></code> based on provided keyframe track.
Supports tracks created with <code><a href="../Classes/MapItemKeyFrameTrack.html">MapItemKeyFrameTrack</a></code> ‘polylineProgress*’ methods.
For starting the animation, see <code><a href="../Classes/MapPolyline.html#/s:7heresdk11MapPolylineC14startAnimation_17animationDelegateyAA0bcE0C_AA0eG0_ptF">MapPolyline.startAnimation(...)</a></code>.</p>
<div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapPolylineAnimation.html#/s:7heresdk20MapPolylineAnimationC18InstantiationErrora">MapPolylineAnimation.InstantiationError</a></code> If the specified keyframe track cannot be used to create animation of a <code><a href="../Classes/MapPolyline.html">MapPolyline</a></code>.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public init(track: MapItemKeyFrameTrack) throws</code></pre>
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
<p>Describes a reason for failing to create a <code><a href="../Classes/MapPolylineAnimation.html">MapPolylineAnimation</a></code>.</p>
<a class="slightly-smaller" href="../Classes/MapPolylineAnimation/InstantiationErrorCode.html">See more</a>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre><code>public enum InstantiationErrorCode : UInt32, CaseIterable, Codable</code></pre>
<pre><code>extension MapPolylineAnimation.InstantiationErrorCode : Error</code></pre>
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



</div>
`
}</HTMLBlock>
