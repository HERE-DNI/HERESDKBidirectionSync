---
title: "RoadAttributesListener constructor"
slug: "sdk-for-flutter-navigate-navigation-roadattributeslistener-roadattributeslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- RoadAttributesListener.html -->


<div>
<h1>RoadAttributesListener constructor</h1></div>

RoadAttributesListener(<ol class="parameter-list single-line"> <li>void onRoadAttributesUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-roadattributes-class">RoadAttributes</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive attributes of the current road.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory RoadAttributesListener(
  void Function(RoadAttributes) onRoadAttributesUpdatedLambda,

) =&gt; RoadAttributesListener$Lambdas(
  onRoadAttributesUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
