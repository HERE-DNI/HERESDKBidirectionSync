---
title: "CameraBehavior constructor"
slug: "sdk-for-flutter-navigate-navigation-camerabehavior-camerabehavior"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CameraBehavior.html -->


<div>
<h1>CameraBehavior constructor</h1></div>

CameraBehavior(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a> normalizedPrincipalPointGetLambda(), </li>
<li>void normalizedPrincipalPointSetLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-anchor2d-class">Anchor2D</a></li>
</ol>)</li>
</ol>)
    

<p>Abstract class used to change implement different
camera behaviors.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory CameraBehavior(
  Anchor2D Function() normalizedPrincipalPointGetLambda,
  void Function(Anchor2D) normalizedPrincipalPointSetLambda
) =&gt; CameraBehavior$Lambdas(
  normalizedPrincipalPointGetLambda,
  normalizedPrincipalPointSetLambda
);</code></pre>

 



</div>
`
}</HTMLBlock>
