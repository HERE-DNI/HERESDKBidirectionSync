---
title: "TwoFingerPanListener constructor"
slug: "sdk-for-flutter-navigate-gestures-twofingerpanlistener-twofingerpanlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TwoFingerPanListener.html -->


<div>
<h1>TwoFingerPanListener constructor</h1></div>

TwoFingerPanListener(<ol class="parameter-list single-line"> <li>void onTwoFingerPanLambda(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-gestures-gesturestate">GestureState</a>, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a>, </li>
<li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a>, </li>
<li>double, </li>
</ol>)</li>
</ol>)
    

<p>Abstract class for handling two finger pan gestures.</p>
<p>Two finger pan gesture occurs when two fingers are on the screen
and both of them are moving vertically.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TwoFingerPanListener(
  void Function(GestureState, Point2D, Point2D, double) onTwoFingerPanLambda,

) =&gt; TwoFingerPanListener$Lambdas(
  onTwoFingerPanLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
