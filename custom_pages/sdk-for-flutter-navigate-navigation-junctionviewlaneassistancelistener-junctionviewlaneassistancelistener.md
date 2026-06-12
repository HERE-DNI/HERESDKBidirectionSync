---
title: "JunctionViewLaneAssistanceListener constructor"
slug: "sdk-for-flutter-navigate-navigation-junctionviewlaneassistancelistener-junctionviewlaneassistancelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- JunctionViewLaneAssistanceListener.html -->


<div>
<h1>JunctionViewLaneAssistanceListener constructor</h1></div>

JunctionViewLaneAssistanceListener(<ol class="parameter-list single-line"> <li>void onLaneAssistanceUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be
implemented in order to receive notifications on <a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a>.</p>
<p>See <a href="/sdk-for-flutter-navigate-navigation-junctionviewlaneassistance-class">JunctionViewLaneAssistance</a> documentation for further details.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory JunctionViewLaneAssistanceListener(
  void Function(JunctionViewLaneAssistance) onLaneAssistanceUpdatedLambda,

) =&gt; JunctionViewLaneAssistanceListener$Lambdas(
  onLaneAssistanceUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
