---
title: "DoubleTapListener constructor"
slug: "sdk-for-flutter-explore-gestures-doubletaplistener-doubletaplistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DoubleTapListener.html -->


<div>
<h1>DoubleTapListener constructor</h1></div>

DoubleTapListener(<ol class="parameter-list single-line"> <li>void onDoubleTapLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-point2d-class">Point2D</a></li>
</ol>)</li>
</ol>)
    

<p>Abstract class for handling double tap gestures.</p>
<p>Double-tap gesture occurs after double-tapping on the screen.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory DoubleTapListener(
  void Function(Point2D) onDoubleTapLambda,

) =&gt; DoubleTapListener$Lambdas(
  onDoubleTapLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
