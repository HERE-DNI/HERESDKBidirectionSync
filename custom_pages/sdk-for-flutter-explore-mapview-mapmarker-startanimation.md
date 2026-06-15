---
title: "startAnimation abstract method"
slug: "sdk-for-flutter-explore-mapview-mapmarker-startanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimation.html -->


<div>
<h1>startAnimation abstract method</h1></div>

void
startAnimation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-animation-mapmarkeranimation-class">MapMarkerAnimation</a> animation, </li>
<li><a href="sdk-for-flutter-explore-animation-animationlistener-class">AnimationListener</a>? animationListener</li>
</ol>)

      

    

<p>Starts animation of this map marker according to provided <a href="sdk-for-flutter-explore-animation-mapmarkeranimation-class">MapMarkerAnimation</a>.</p>
<p>The <code>MapMarkerAnimation</code> may be shared between multiple instances of <code>MapMarker</code>.</p>
<p>Starting animation on one map marker does not influence any ongoing animations on other map markers.
Any ongoing animation of this marker instance will get cancelled.</p>
<ul>
<li>
<p><code>animation</code> The animation to start, may be used for multiple different map markers.</p>
</li>
<li>
<p><code>animationListener</code> The listener to receive notifications about animation start, completion or cancellation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAnimation(MapMarkerAnimation animation, AnimationListener? animationListener);</code></pre>

 



</div>
`
}</HTMLBlock>
