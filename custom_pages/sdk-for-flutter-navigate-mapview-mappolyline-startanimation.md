---
title: "startAnimation abstract method"
slug: "sdk-for-flutter-navigate-mapview-mappolyline-startanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- startAnimation.html -->


<div>
<h1>startAnimation abstract method</h1></div>

void
startAnimation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-animation-mappolylineanimation-class">MapPolylineAnimation</a> animation, </li>
<li><a href="sdk-for-flutter-navigate-animation-animationlistener-class">AnimationListener</a> listener</li>
</ol>)

      

    

<p>Starts an animation of this map polyline.</p>
<p>The <code>MapPolylineAnimation</code> may be shared between multiple instances of <code>MapPolyline</code>.</p>
<p>Starting animation on one polyline does not influence any ongoing animations on
other polylines.
Any ongoing animation of this map polyline will get cancelled.</p>
<ul>
<li>
<p><code>animation</code> The animation to start.</p>
</li>
<li>
<p><code>listener</code> The listener to receive notifications
about animation start, completion or cancellation.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void startAnimation(MapPolylineAnimation animation, AnimationListener listener);</code></pre>

 



</div>
`
}</HTMLBlock>
