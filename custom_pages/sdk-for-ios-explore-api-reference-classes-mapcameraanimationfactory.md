---
title: "Untitled"
slug: "sdk-for-ios-explore-api-reference-classes-mapcameraanimationfactory"
---

<HTMLBlock>{
`
<div class="sdk-for-ios">
<!-- MapCameraAnimationFactory.html -->
<!DOCTYPE html>

<html lang="en">

<body>
<a class="dashAnchor" name="//apple_ref/swift/Class/MapCameraAnimationFactory"></a>
<a title="MapCameraAnimationFactory Class Reference"></a>

<div class="content-wrapper">
<p id="breadcrumbs">
<a href="sdk-for-ios-explore-api-reference-..-index">heresdk</a>
<img alt="" id="carat" src="../img/carat.png"/>
<a href="sdk-for-ios-explore-api-reference-..-maps">Maps</a>
<img alt="" id="carat" src="../img/carat.png"/>
        MapCameraAnimationFactory Class Reference
      </p>
</div>
<div class="content-wrapper">

<article class="main-content">
<section>
<section class="section">
<h1>MapCameraAnimationFactory</h1>
<div class="declaration">
<div class="language">
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">class</span> <span class="kt">MapCameraAnimationFactory</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraAnimationFactory</span><span class="p">:</span> <span class="kt">NativeBase</span></code></pre>
<pre class="highlight swift"><code><span class="kd">extension</span> <span class="kt">MapCameraAnimationFactory</span><span class="p">:</span> <span class="kt">Hashable</span></code></pre>
</div>
</div>
<p>Factory for creating MapCameraAnimation objects to change map’s camera over time.</p>
</section>
<section class="section task-group-section">
<div class="task-group">
<ul>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC06createD04from8duration6easingAA0bcD0CAA0bC6UpdateC_SdAA6EasingCtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/createAnimation(from:duration:easing:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC06createD04from8duration6easingAA0bcD0CAA0bC6UpdateC_SdAA6EasingCtFZ">createAnimation(from:<wbr/>duration:<wbr/>easing:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></code> to gradually update the camera properties within a specified
duration from its current values to the ones defined in the <code>MapCameraAnimationFactory.createAnimation(MapCameraUpdate, TimeInterval, Easing).cameraUpdate</code>. <code><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></code>
instances created from <code><a href="../Classes/MapCameraUpdateFactory.html#/s:7heresdk22MapCameraUpdateFactoryC09compositeD0yAA0bcD0CSayAFGKFZ">MapCameraUpdateFactory.compositeUpdate(...)</a></code> instances are not supported. An
<code><a href="sdk-for-ios-explore-api-reference-..-protocols-animationdelegate">AnimationDelegate</a></code> will receive an <code><a href="../Enums/AnimationState.html#/s:7heresdk14AnimationStateO9cancelledyA2CmF">AnimationState.cancelled</a></code> signal
when trying to apply such animations.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">createAnimation</span><span class="p">(</span><span class="n">from</span> <span class="nv">cameraUpdate</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraupdate">MapCameraUpdate</a></span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">,</span> <span class="nv">easing</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-easing">Easing</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>cameraUpdate</em>
</code>
</td>
<td>
<div>
<p>Update which should be applied to the map camera.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>duration</em>
</code>
</td>
<td>
<div>
<p>Duration of the animation. Negative duration results in no camera change when applied.</p>
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
<p>Easing to apply.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC06createD05trackAA0bcD0CAA0bC13KeyframeTrackC_tFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/createAnimation(track:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC06createD05trackAA0bcD0CAA0bC13KeyframeTrackC_tFZ">createAnimation(track:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a MapCameraAnimation for a movement defined by the supplied <code>MapCameraAnimationFactory.createAnimation(MapCameraKeyframeTrack).track</code>.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">createAnimation</span><span class="p">(</span><span class="nv">track</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
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
<p>The track</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC06createD06tracksAA0bcD0CSayAA0bC13KeyframeTrackCG_tKFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/createAnimation(tracks:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC06createD06tracksAA0bcD0CSayAA0bC13KeyframeTrackCG_tKFZ">createAnimation(tracks:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a MapCameraAnimation for a movement defined by the supplied list of <code>MapCameraAnimationFactory.createAnimation([MapCameraKeyframeTrack]).tracks</code>.
Keyframe tracks specify how the map camera properties change during the animation.
For the animation to be possible, no two different tracks can
affect the same map camera property. The input tracks are validated with that in mind.</p>
<p>However, the following cases can only be detected at the time when animation is started:</p>
<ul>
<li>Changing altitude of camera position also changes camera look-at distance
and at high altitudes, also camera look-at orientation.</li>
<li>Changing tilt of camera orientation also changes camera look-at distance
and camera look-at target.</li>
<li>Changing bearing of camera orientation also changes
camera look-at target if current tilt is not 0.</li>
<li>Changing tilt or bearing of camera look-at orientation also changes
camera position.</li>
<li>Changing camera look-at orientation also changes camera look-at distance
if tilt is not 0.</li>
</ul><div class="aside aside-throws">
<p class="aside-title">Throws</p>
<code><a href="../Classes/MapCameraAnimation.html#/s:7heresdk18MapCameraAnimationC18InstantiationErrora">MapCameraAnimation.InstantiationError</a></code> Indicates an instantiation issue.

</div>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">createAnimation</span><span class="p">(</span><span class="nv">tracks</span><span class="p">:</span> <span class="p">[</span><span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcamerakeyframetrack">MapCameraKeyframeTrack</a></span><span class="p">])</span> <span class="k">throws</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>tracks</em>
</code>
</td>
<td>
<div>
<p>The list of tracks</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_S2dtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/flyTo(target:bowFactor:duration:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_S2dtFZ">flyTo(target:<wbr/>bowFactor:<wbr/>duration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</p>
<p>The beginning and end of the animation will use the current zoom.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">flyTo</span><span class="p">(</span><span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">bowFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The coordinates of the camera destination point.
Any target sub-element value that is not finite will be set to the current camera target sub-element value.
Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bowFactor</em>
</code>
</td>
<td>
<div>
<p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>duration</em>
</code>
</td>
<td>
<div>
<p>Duration of the flight. Negative duration results in no camera change when applied.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0m11OrientationO0VS2dtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/flyTo(target:orientation:bowFactor:duration:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0m11OrientationO0VS2dtFZ">flyTo(target:<wbr/>orientation:<wbr/>bowFactor:<wbr/>duration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</p>
<p>The beginning and end of the animation will use the current zoom.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">flyTo</span><span class="p">(</span><span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">bowFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The coordinates of the camera destination point.
Any target sub-element value that is not finite will be set to the current camera target sub-element value.
Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>The orientation at destination.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bowFactor</em>
</code>
</td>
<td>
<div>
<p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>duration</em>
</code>
</td>
<td>
<div>
<p>Duration of the flight. Negative duration results in no camera change when applied.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0B7MeasureVS2dtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/flyTo(target:zoom:bowFactor:duration:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0B7MeasureVS2dtFZ">flyTo(target:<wbr/>zoom:<wbr/>bowFactor:<wbr/>duration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position along an adaptive ballistic curve.</p>
<p>The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">flyTo</span><span class="p">(</span><span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure">MapMeasure</a></span><span class="p">,</span> <span class="nv">bowFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The coordinates of the camera destination point.
Any target sub-element value that is not finite will be set to the current camera target sub-element value.
Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>zoom</em>
</code>
</td>
<td>
<div>
<p>The zoom at the end of the animation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bowFactor</em>
</code>
</td>
<td>
<div>
<p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>duration</em>
</code>
</td>
<td>
<div>
<p>Duration of the flight. Negative duration results in no camera change when applied.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
</div>
</section>
</div>
</li>
<li class="item">
<div>
<code>
<a name="/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0n11OrientationP0VAA0B7MeasureVS2dtFZ"></a>
<a class="dashAnchor" name="//apple_ref/swift/Method/flyTo(target:orientation:zoom:bowFactor:duration:)"></a>
<a class="token" href="#/s:7heresdk25MapCameraAnimationFactoryC5flyTo6target11orientation4zoom9bowFactor8durationAA0bcD0CAA20GeoCoordinatesUpdateV_AA0n11OrientationP0VAA0B7MeasureVS2dtFZ">flyTo(target:<wbr/>orientation:<wbr/>zoom:<wbr/>bowFactor:<wbr/>duration:<wbr/>)</a>
</code>
</div>
<div class="height-container">
<div class="pointer-container"></div>
<section class="section">
<div class="pointer"></div>
<div class="abstract">
<p>Creates a MapCameraAnimation to move the current map camera look-at coordinates to the new position and orientation along an adaptive ballistic curve.</p>
<p>The beginning of the animation will use the current zoom and the end of the animation will use the provided zoom.</p>
<p>Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
<div class="declaration">
<h4>Declaration</h4>
<div class="language">
<p class="aside-title">Swift</p>
<pre class="highlight swift"><code><span class="kd">public</span> <span class="kd">static</span> <span class="kd">func</span> <span class="nf">flyTo</span><span class="p">(</span><span class="nv">target</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geocoordinatesupdate">GeoCoordinatesUpdate</a></span><span class="p">,</span> <span class="nv">orientation</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-geoorientationupdate">GeoOrientationUpdate</a></span><span class="p">,</span> <span class="nv">zoom</span><span class="p">:</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-structs-mapmeasure">MapMeasure</a></span><span class="p">,</span> <span class="nv">bowFactor</span><span class="p">:</span> <span class="kt">Double</span><span class="p">,</span> <span class="nv">duration</span><span class="p">:</span> <span class="kt">TimeInterval</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kt"><a href="sdk-for-ios-explore-api-reference-..-classes-mapcameraanimation">MapCameraAnimation</a></span></code></pre>
</div>
</div>
<div>
<h4>Parameters</h4>
<table class="graybox">
<tbody>
<tr>
<td>
<code>
<em>target</em>
</code>
</td>
<td>
<div>
<p>The coordinates of the camera destination point.
Any target sub-element value that is not finite will be set to the current camera target sub-element value.
Note: The altitude of the target point is ignored. Any subsequent camera updates and animations
will consider the target point as being located on the ground.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>orientation</em>
</code>
</td>
<td>
<div>
<p>The orientation at destination.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>zoom</em>
</code>
</td>
<td>
<div>
<p>The zoom at the end of the animation.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>bowFactor</em>
</code>
</td>
<td>
<div>
<p>A bow factor that specifies how high (bowFactor &gt; 0) or low (bowFactor &lt; 0) the camera will fly.</p>
</div>
</td>
</tr>
<tr>
<td>
<code>
<em>duration</em>
</code>
</td>
<td>
<div>
<p>Duration of the flight. Negative duration results in no camera change when applied.</p>
</div>
</td>
</tr>
</tbody>
</table>
</div>
<div>
<h4>Return Value</h4>
<p>MapCameraAnimation instance</p>
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
