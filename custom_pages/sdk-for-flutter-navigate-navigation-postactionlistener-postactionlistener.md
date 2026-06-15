---
title: "PostActionListener constructor"
slug: "sdk-for-flutter-navigate-navigation-postactionlistener-postactionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PostActionListener.html -->


<div>
<h1>PostActionListener constructor</h1></div>

PostActionListener(<ol class="parameter-list single-line"> <li>void onPostActionsLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-routing-postaction-class">PostAction</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to
receive post action notifications.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory PostActionListener(
  void Function(List&lt;PostAction&gt;) onPostActionsLambda,

) =&gt; PostActionListener$Lambdas(
  onPostActionsLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
