---
title: "lookAtTargetWithEasing static method"
slug: "sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-lookattargetwitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtTargetWithEasing.html -->


<div>
<h1>lookAtTargetWithEasing static method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>
lookAtTargetWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-animation-geocoordinateskeyframe-class">GeoCoordinatesKeyframe</a>&gt; keyframes, </li>
<li><a href="sdk-for-flutter-navigate-animation-easing-class">Easing</a> easing, </li>
<li><a href="sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a map camera look-at target keyframe track.</p>
<p>It enables animations over the
geographical coordinates of the target point that the map camera is looking at.
Altitude components of coordinates are ignored.</p>
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
<p>Returns <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the map camera target coordinates.</p>
<p>Throws <a href="sdk-for-flutter-navigate-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraKeyframeTrack lookAtTargetWithEasing(List&lt;GeoCoordinatesKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.lookAtTargetWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
