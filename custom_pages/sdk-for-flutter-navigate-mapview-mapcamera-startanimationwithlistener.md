---
title: "startAnimationWithListener abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcamera-startanimationwithlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimationWithListener.html -->


<div>
<h1>startAnimationWithListener abstract method</h1></div>

void
startAnimationWithListener(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-mapview-mapcameraanimation-class">MapCameraAnimation</a> cameraAnimation, </li>
<li><a href="/sdk-for-flutter-navigate-animation-animationlistener-class">AnimationListener</a> animationListener</li>
</ol>)

      

    

<p>Starts a given camera animation.</p>
<p>The state of the animation can be tracked with the provided listener.</p>
<p>Starting an animation can cause the cancelling of an ongoing animation when they both affect the same category of camera properties,
like for example any of the look-at properties (target, orientation, map measure) or any of the projection properties (field of view, principal point, focal length).
The corresponding listener of an ongoing animation will be notified about the cancellation in these cases.</p>
<ul>
<li>
<p><code>cameraAnimation</code> The animation to be started.</p>
</li>
<li>
<p><code>animationListener</code> Animation listener. A strong reference is kept internally up until the animation gets cancelled or completed.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAnimationWithListener(MapCameraAnimation cameraAnimation, AnimationListener animationListener);</code></pre>

 



</div>
`
}</HTMLBlock>
