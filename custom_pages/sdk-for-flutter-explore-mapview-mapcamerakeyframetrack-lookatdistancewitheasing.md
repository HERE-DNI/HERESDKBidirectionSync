---
title: "lookAtDistanceWithEasing static method"
slug: "sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-lookatdistancewitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- lookAtDistanceWithEasing.html -->


<div>
<h1>lookAtDistanceWithEasing static method</h1></div>

<div>
<ol class="annotation-list">
<li>@Deprecated("Will be removed in v4.27.0. Use [MapCameraKeyframeTrack.lookAtDistanceWithKind] instead.")</li>
</ol>
</div>
<a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>
lookAtDistanceWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-animation-scalarkeyframe-class">ScalarKeyframe</a>&gt; keyframes, </li>
<li><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a> easing, </li>
<li><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a map camera look-at distance keyframe track.</p>
<p>It enables animations of the distance
from the map camera to the target point that the camera looks at in meters. The values will
be clamped according to the minimum and maximum zoom levels set for the map camera.</p>
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
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>. A keyframe track over the distance from the map camera to its target.</p>
<p>Throws <a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrackinstantiationexception-class">MapCameraKeyframeTrackInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">@Deprecated("Will be removed in v4.27.0. Use [MapCameraKeyframeTrack.lookAtDistanceWithKind] instead.")

static MapCameraKeyframeTrack lookAtDistanceWithEasing(List&lt;ScalarKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.lookAtDistanceWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
