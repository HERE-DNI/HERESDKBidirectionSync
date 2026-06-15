---
title: "polylineProgressWithEasing static method"
slug: "sdk-for-flutter-navigate-animation-mapitemkeyframetrack-polylineprogresswitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- polylineProgressWithEasing.html -->


<div>
<h1>polylineProgressWithEasing static method</h1></div>

<a href="sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a>
polylineProgressWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-animation-scalarkeyframe-class">ScalarKeyframe</a>&gt; keyframes, </li>
<li><a href="sdk-for-flutter-navigate-animation-easing-class">Easing</a> easing, </li>
<li><a href="sdk-for-flutter-navigate-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a keyframe track used to animate the progress of a polyline.</p>
<p>Each scalar keyframe specifies the value of <a href="sdk-for-flutter-navigate-mapview-mappolyline-progress">MapPolyline.progress</a>
at key points of the animation.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the polyline progress changes
over time.</p>
</li>
<li>
<p><code>easing</code> The easing to apply during keyframe interpolation.</p>
</li>
<li>
<p><code>interpolationMode</code> The type of interpolation done between keyframe values.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a>. MapItemKeyFrameTrack instance.</p>
<p>Throws <a href="sdk-for-flutter-navigate-animation-mapitemkeyframetrackinstantiationexception-class">MapItemKeyFrameTrackInstantiationException</a>. If the supplied keyframe list is empty or first keyframe duration is not 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapItemKeyFrameTrack polylineProgressWithEasing(List&lt;ScalarKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.polylineProgressWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
