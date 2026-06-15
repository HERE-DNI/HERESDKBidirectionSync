---
title: "MapPolylineAnimation constructor"
slug: "sdk-for-flutter-explore-animation-mappolylineanimation-mappolylineanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapPolylineAnimation.html -->


<div>
<h1>MapPolylineAnimation constructor</h1></div>

MapPolylineAnimation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a> track</li>
</ol>)
    

<p>Creates an animation of <a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a> based on provided keyframe track.</p>
<p>Supports tracks created with <a href="sdk-for-flutter-explore-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a> 'polylineProgress*' methods.
For starting the animation, see <a href="sdk-for-flutter-explore-mapview-mappolyline-startanimation">MapPolyline.startAnimation</a>.</p>
<ul>
<li><code>track</code> The track holding the keyframes for the animation.</li>
</ul>
<p>Throws <a href="sdk-for-flutter-explore-animation-mappolylineanimationinstantiationexception-class">MapPolylineAnimationInstantiationException</a>. If the specified keyframe track cannot be used to create animation of a <a href="sdk-for-flutter-explore-mapview-mappolyline-class">MapPolyline</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapPolylineAnimation(MapItemKeyFrameTrack track) =&gt; $prototype.$init(track);</code></pre>

 



</div>
`
}</HTMLBlock>
