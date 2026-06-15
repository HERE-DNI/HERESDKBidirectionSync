---
title: "principalPointWithEasing static method"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-principalpointwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- principalPointWithEasing.html -->


<div>
<h1>principalPointWithEasing static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>
principalPointWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-animation-point2dkeyframe-class">Point2DKeyframe</a>&gt; keyframes, </li>
<li><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a> easing, </li>
<li><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a map camera principal point keyframe track.</p>
<p>It enables animations on the pixel point
where the map camera's target is placed in view coordinates. (0,0) is top left of the
viewport, (viewport width, viewport height) is bottom right.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the camera property is changed.
Point values must be in screen (pixel) coordinates with origin (0,0) in the top left of the viewport.
Point values outside of viewport boundaries will be clamped to the viewport boundaries during animation.
Keyframe time offsets are considered to be relative to the previous keyframe
in the list or relative to the start of the animation if the current keyframe
is first in the list.
Time offset of the first keyframe in the list should be 0, otherwise an error occurs
and creation of the keyframe track will fail.</p>
</li>
<li>
<p><code>easing</code> The easing to apply during keyframe interpolation.</p>
</li>
<li>
<p><code>interpolationMode</code> The type of interpolation done between keyframe values.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the principal point.</p>
<p>Throws <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraKeyframeTrack principalPointWithEasing(List&lt;Point2DKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.principalPointWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
