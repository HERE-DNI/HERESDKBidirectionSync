---
title: "TapListener constructor"
slug: "sdk-for-flutter-navigate-gestures-taplistener-taplistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TapListener.html -->


<div>
<h1>TapListener constructor</h1></div>

TapListener(<ol class="parameter-list single-line"> <li>void onTapLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-point2d-class">Point2D</a></li>
</ol>)</li>
</ol>)
    

<p>Abstract class for handling tap gestures.</p>
<p>Tap gesture occurs after tapping on the screen.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TapListener(
  void Function(Point2D) onTapLambda,

) =&gt; TapListener$Lambdas(
  onTapLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
