---
title: "AnimationListener constructor"
slug: "sdk-for-flutter-explore-animation-animationlistener-animationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AnimationListener.html -->


<div>
<h1>AnimationListener constructor</h1></div>

AnimationListener(<ol class="parameter-list single-line"> <li>void onAnimationStateChangedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-animation-animationstate">AnimationState</a></li>
</ol>)</li>
</ol>)
    

<p>A listener for animation events.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory AnimationListener(
  void Function(AnimationState) onAnimationStateChangedLambda,

) =&gt; AnimationListener$Lambdas(
  onAnimationStateChangedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
