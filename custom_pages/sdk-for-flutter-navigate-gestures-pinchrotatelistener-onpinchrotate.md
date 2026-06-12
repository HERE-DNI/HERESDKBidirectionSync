---
title: "onPinchRotate abstract method"
slug: "sdk-for-flutter-navigate-gestures-pinchrotatelistener-onpinchrotate"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onPinchRotate.html -->


<div>
<h1>onPinchRotate abstract method</h1></div>

void
onPinchRotate(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a> state, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a> pinchOrigin, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a> rotationOrigin, </li>
<li>double twoFingerDistance, </li>
<li><a href="/sdk-for-flutter-navigate-core-angle-class">Angle</a> rotation, </li>
</ol>)

      

    

<p>Called when the pinch rotate gesture occurs.</p>
<ul>
<li>
<p><code>state</code> Determines in which state the gesture is.</p>
</li>
<li>
<p><code>pinchOrigin</code> Position where the pinch happened relative to the MapView in pixels.</p>
</li>
<li>
<p><code>rotationOrigin</code> Position where the rotation happened relative to the MapView in pixels.</p>
</li>
<li>
<p><code>twoFingerDistance</code> Distance between the two fingers in pixels.</p>
</li>
<li>
<p><code>rotation</code> Fingers rotation angle delta. Indicates how much the fingers rotation angle has changed
since the previous gesture update. Clockwise finger rotation gives positive deltas,
counter clockwise finger rotation gives negative deltas.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onPinchRotate(GestureState state, Point2D pinchOrigin, Point2D rotationOrigin, double twoFingerDistance, Angle rotation);</code></pre>

 



</div>
`
}</HTMLBlock>
