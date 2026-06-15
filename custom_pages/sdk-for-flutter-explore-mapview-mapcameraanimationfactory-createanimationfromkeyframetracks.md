---
title: "createAnimationFromKeyframeTracks static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromkeyframetracks"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createAnimationFromKeyframeTracks.html -->


<div>
<h1>createAnimationFromKeyframeTracks static method</h1></div>

<a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a>
createAnimationFromKeyframeTracks(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-explore-mapview-mapcamerakeyframetrack-class">MapCameraKeyframeTrack</a>&gt; tracks</li>
</ol>)

      

    

<p>Creates a MapCameraAnimation for a movement defined by the supplied list of <code>MapCameraAnimationFactory.createAnimationFromKeyframeTracks.tracks</code>.</p>
<p>Keyframe tracks specify how the map camera properties change during the animation.
For the animation to be possible, no two different tracks can
affect the same map camera property. The input tracks are validated with that in mind.</p>
<p>However, the following cases can only be detected at the time when animation is started:</p>
<ul>
<li>
<p>Changing altitude of camera position also changes camera look-at distance
and at high altitudes, also camera look-at orientation.</p>
</li>
<li>
<p>Changing tilt of camera orientation also changes camera look-at distance
and camera look-at target.</p>
</li>
<li>
<p>Changing bearing of camera orientation also changes
camera look-at target if current tilt is not 0.</p>
</li>
<li>
<p>Changing tilt or bearing of camera look-at orientation also changes
camera position.</p>
</li>
<li>
<p>Changing camera look-at orientation also changes camera look-at distance
if tilt is not 0.</p>
</li>
<li>
<p><code>tracks</code> The list of tracks</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a>. MapCameraAnimation instance</p>
<p>Throws <a href="sdk-for-flutter-explore-mapview-mapcameraanimationinstantiationexception-class">MapCameraAnimationInstantiationException</a>. Indicates an instantiation issue.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraAnimation createAnimationFromKeyframeTracks(List&lt;MapCameraKeyframeTrack&gt; tracks) =&gt; $prototype.createAnimationFromKeyframeTracks(tracks);</code></pre>

 



</div>
`
}</HTMLBlock>
