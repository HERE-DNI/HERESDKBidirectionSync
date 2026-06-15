---
title: "lookAtOrientationWithEasing static method"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatorientationwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtOrientationWithEasing.html -->


<div>
<h1>lookAtOrientationWithEasing static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>
lookAtOrientationWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-animation-geoorientationkeyframe-class">GeoOrientationKeyframe</a>&gt; keyframes, </li>
<li><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a> easing, </li>
<li><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a map camera look-at orientation keyframe track.</p>
<p>It enables animations over the
orientation of the map camera target (bearing and tilt).</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the camera property is changed.
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
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the map camera target orientation.</p>
<p>Throws <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraKeyframeTrack lookAtOrientationWithEasing(List&lt;GeoOrientationKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.lookAtOrientationWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
