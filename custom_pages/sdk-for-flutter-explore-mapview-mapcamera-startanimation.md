---
title: "startAnimation abstract method"
slug: "sdk-for-flutter-explore-mapview-mapcamera-startanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimation.html -->


<div>
<h1>startAnimation abstract method</h1></div>

void
startAnimation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-mapview-mapcameraanimation-class">MapCameraAnimation</a> cameraAnimation</li>
</ol>)

      

    

<p>Starts a given camera animation.</p>
<p>Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties,
like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length).
The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.</p>
<ul>
<li><code>cameraAnimation</code> The animation to be started.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAnimation(MapCameraAnimation cameraAnimation);</code></pre>

 



</div>
`
}</HTMLBlock>
