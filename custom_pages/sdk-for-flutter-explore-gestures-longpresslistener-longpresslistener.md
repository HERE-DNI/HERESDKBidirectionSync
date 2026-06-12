---
title: "LongPressListener constructor"
slug: "sdk-for-flutter-explore-gestures-longpresslistener-longpresslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LongPressListener.html -->


<div>
<h1>LongPressListener constructor</h1></div>

LongPressListener(<ol class="parameter-list single-line"> <li>void onLongPressLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-gestures-gesturestate">GestureState</a>, </li>
<li><a href="/sdk-for-flutter-explore-core-point2d-class">Point2D</a></li>
</ol>)</li>
</ol>)
    

<p>Abstract class for handling long-press gestures.</p>
<p>Long-press gesture occurs after tapping and holding the finger for a long time on the screen.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LongPressListener(
  void Function(GestureState, Point2D) onLongPressLambda,

) =&gt; LongPressListener$Lambdas(
  onLongPressLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
