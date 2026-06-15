---
title: "moveToWithEasing static method"
slug: "sdk-for-flutter-explore-animation-mapitemkeyframetrack-movetowitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- moveToWithEasing.html -->


<div>
<h1>moveToWithEasing static method</h1></div>

<a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a>
moveToWithEasing(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-animation-geocoordinateskeyframe-class">GeoCoordinatesKeyframe</a>&gt; keyframes, </li>
<li><a href="sdk-for-flutter-explore-animation-easing-class">Easing</a> easing, </li>
<li><a href="sdk-for-flutter-explore-animation-keyframeinterpolationmode">KeyframeInterpolationMode</a> interpolationMode</li>
</ol>)

      

    

<p>Creates a map item position keyframe track.</p>
<p>It enables animations over the geographical
coordinates where the map item is positioned.</p>
<ul>
<li>
<p><code>keyframes</code> The list of keyframes that specify how the map item position changes over time.</p>
</li>
<li>
<p><code>easing</code> The easing to apply during keyframe interpolation.</p>
</li>
<li>
<p><code>interpolationMode</code> The type of interpolation done between keyframe values.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a>. MapItemKeyFrameTrack instance.</p>
<p>Throws <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrackinstantiationexception-class">MapItemKeyFrameTrackInstantiationException</a>. If the supplied keyframe list is empty or first keyframe duration is not 0.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapItemKeyFrameTrack moveToWithEasing(List&lt;GeoCoordinatesKeyframe&gt; keyframes, Easing easing, KeyframeInterpolationMode interpolationMode) =&gt; $prototype.moveToWithEasing(keyframes, easing, interpolationMode);</code></pre>

 



</div>
`
}</HTMLBlock>
