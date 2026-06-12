---
title: "RoadTextsListener constructor"
slug: "sdk-for-flutter-navigate-navigation-roadtextslistener-roadtextslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadTextsListener.html -->


<div>
<h1>RoadTextsListener constructor</h1></div>

RoadTextsListener(<ol class="parameter-list single-line"> <li>void onRoadTextsUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-routing-roadtexts-class">RoadTexts</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive textual attributes of the current road.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RoadTextsListener(
  void Function(RoadTexts) onRoadTextsUpdatedLambda,

) =&gt; RoadTextsListener$Lambdas(
  onRoadTextsUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
