---
title: "cancelAnimation abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapmarker-cancelanimation"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- cancelAnimation.html -->


<div>
<h1>cancelAnimation abstract method</h1></div>

void
cancelAnimation(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a> animation</li>
</ol>)

      

    

<p>Cancels single ongoing animation.</p>
<p>Does nothing if animation was not started for this map marker.</p>
<p>Does not cancel other animations if the same <a href="sdk-for-flutter-navigate-animation-mapmarkeranimation-class">MapMarkerAnimation</a> object was applied to multiple <code>MapMarker</code>s.</p>
<ul>
<li><code>animation</code> The animation to cancel.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void cancelAnimation(MapMarkerAnimation animation);</code></pre>

 



</div>
`
}</HTMLBlock>
