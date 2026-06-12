---
title: "normalizedPrincipalPointWithEasing static method"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-normalizedprincipalpointwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- normalizedPrincipalPointWithEasing.html -->


<div>
<h1>normalizedPrincipalPointWithEasing static method</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>
normalizedPrincipalPointWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-animation-anchor2dkeyframe-class">Anchor2DKeyframe</a>&gt; keyframes, </li>
<li><a href="/sdk-for-flutter-navigate-animation-easing-class">Easing</a> easing, </li>
<li><a href="/sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a map camera principal point keyframe track.</p>
<p>It enables animations on the point
where the map camera's target is placed in normalized view coordinates. (0,0) is top left of
the viewport, (1, 1) is bottom right.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the camera property is changed.
Point values must be in normalized screen coordinates with origin (0,0) in the top left and (1,1) in the bottom right of the viewport.
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
<p>Returns <a href="/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the principal point.</p>
<p>Throws <a href="/sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraKeyframeTrack normalizedPrincipalPointWithEasing(List&lt;Anchor2DKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.normalizedPrincipalPointWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
