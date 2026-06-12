---
title: "MapMarkerAnimation constructor"
slug: "sdk-for-flutter-navigate-animation-mapmarkeranimation-mapmarkeranimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapMarkerAnimation.html -->


<div>
<h1>MapMarkerAnimation constructor</h1></div>

MapMarkerAnimation(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a> track</li>
</ol>)
    

<p>Creates an animation of <a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a> based on provided keyframe track.</p>
<p>Supports tracks created with <a href="/sdk-for-flutter-navigate-animation-mapitemkeyframetrack-class">MapItemKeyFrameTrack</a> 'moveTo*' methods.</p>
<p>For starting the animation see <a href="/sdk-for-flutter-navigate-mapview-mapmarker-startanimation">MapMarker.startAnimation</a>.</p>
<ul>
<li><code>track</code> The track holding the keyframes for the animation.</li>
</ul>
<p>Throws <a href="/sdk-for-flutter-navigate-animation-mapmarkeranimationinstantiationexception-class">MapMarkerAnimationInstantiationException</a>. If the specified keyframe track cannot be used to create animation of a <a href="/sdk-for-flutter-navigate-mapview-mapmarker-class">MapMarker</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory MapMarkerAnimation(MapItemKeyFrameTrack track) =&gt; $prototype.$init(track);</code></pre>

 



</div>
`
}</HTMLBlock>
