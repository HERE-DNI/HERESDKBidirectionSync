---
title: "PinchRotateListener constructor"
slug: "sdk-for-flutter-navigate-gestures-pinchrotatelistener-pinchrotatelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PinchRotateListener.html -->


<div>
<h1>PinchRotateListener constructor</h1></div>

PinchRotateListener(<ol class="parameter-list single-line"> <li>void onPinchRotateLambda(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a>, </li>
<li><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>, </li>
<li><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>, </li>
<li>double, </li>
<li><a href="sdk-for-flutter-navigate-core-angle-class">Angle</a>, </li>
</ol>)</li>
</ol>)
    

<p>Abstract class for handling pinch rotate gestures.</p>
<p>Pinch rotate gesture occurs when two fingers are on the screen
and at least one of them moves.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PinchRotateListener(
  void Function(GestureState, Point2D, Point2D, double, Angle) onPinchRotateLambda,

) =&gt; PinchRotateListener$Lambdas(
  onPinchRotateLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
