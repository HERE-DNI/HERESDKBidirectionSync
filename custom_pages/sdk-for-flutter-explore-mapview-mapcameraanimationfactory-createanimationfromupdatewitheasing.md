---
title: "createAnimationFromUpdateWithEasing static method"
slug: "sdk-for-flutter-explore-mapview-mapcameraanimationfactory-createanimationfromupdatewitheasing"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- createAnimationFromUpdateWithEasing.html -->


<div>
<h1>createAnimationFromUpdateWithEasing static method</h1></div>

<a href="/sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a>
createAnimationFromUpdateWithEasing(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-mapview-mapcameraupdate-class">MapCameraUpdate</a> cameraUpdate, </li>
<li>Duration duration, </li>
<li><a href="/sdk-for-flutter-explore-animation-easing-class">Easing</a> easing</li>
</ol>)

      

    

<p>Creates a <a href="/sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a> to gradually update the camera properties within a specified
duration from its current values to the ones defined in the <code>MapCameraAnimationFactory.createAnimationFromUpdateWithEasing.cameraUpdate</code>.</p>
<p><code>MapCameraAnimation</code>
instances created from <a href="/sdk-for-flutter-explore-mapview-mapcameraupdatefactory-compositeupdate">MapCameraUpdateFactory.compositeUpdate</a> instances are not supported. An
<a href="/sdk-for-flutter-explore-animation-animationlistener-class">AnimationListener</a> will receive an <a href="/sdk-for-flutter-explore-animation-animationstate">AnimationState.cancelled</a> signal
when trying to apply such animations.</p>
<ul>
<li>
<p><code>cameraUpdate</code> Update which should be applied to the map camera.</p>
</li>
<li>
<p><code>duration</code> Duration of the animation. Negative duration results in no camera change when applied.</p>
</li>
<li>
<p><code>easing</code> Easing to apply.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a>. MapCameraAnimation instance</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">static MapCameraAnimation createAnimationFromUpdateWithEasing(MapCameraUpdate cameraUpdate, Duration duration, Easing easing) =&gt; $prototype.createAnimationFromUpdateWithEasing(cameraUpdate, duration, easing);</code></pre>

 



</div>
`
}</HTMLBlock>
