---
title: "onTwoFingerPan abstract method"
slug: "sdk-for-flutter-navigate-gestures-twofingerpanlistener-ontwofingerpan"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onTwoFingerPan.html -->


<div>
<h1>onTwoFingerPan abstract method</h1></div>

void
onTwoFingerPan(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a> state, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a> origin, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a> translation, </li>
<li>double velocity, </li>
</ol>)

      

    

<p>Called when the two finger pan gesture occurs.</p>
<ul>
<li>
<p><code>state</code> Determines in which state the gesture is.</p>
</li>
<li>
<p><code>origin</code> Position halfway between two touch points relative to the MapView in pixels.</p>
</li>
<li>
<p><code>translation</code> Translation offset since the last position in pixels.</p>
</li>
<li>
<p><code>velocity</code> Velocity of panning in pixels per millisecond.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onTwoFingerPan(GestureState state, Point2D origin, Point2D translation, double velocity);</code></pre>

 



</div>
`
}</HTMLBlock>
