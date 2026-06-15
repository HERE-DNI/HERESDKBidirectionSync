---
title: "PanListener constructor"
slug: "sdk-for-flutter-navigate-gestures-panlistener-panlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PanListener.html -->


<div>
<h1>PanListener constructor</h1></div>

PanListener(<ol class="parameter-list single-line"> <li>void onPanLambda(<ol class="parameter-list"> <li><a href="sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a>, </li>
<li><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>, </li>
<li><a href="sdk-for-flutter-navigate-core-point2d-class">Point2D</a>, </li>
<li>double, </li>
</ol>)</li>
</ol>)
    

<p>Abstract class for handling pan gestures.</p>
<p>Pan gesture occurs when a finger is moving on the screen.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PanListener(
  void Function(GestureState, Point2D, Point2D, double) onPanLambda,

) =&gt; PanListener$Lambdas(
  onPanLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
