---
title: "ManeuverViewLaneAssistanceListener constructor"
slug: "sdk-for-flutter-navigate-navigation-maneuverviewlaneassistancelistener-maneuverviewlaneassistancelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- ManeuverViewLaneAssistanceListener.html -->


<div>
<h1>ManeuverViewLaneAssistanceListener constructor</h1></div>

ManeuverViewLaneAssistanceListener(<ol class="parameter-list single-line"> <li>void onLaneAssistanceUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be
implemented in order to receive notifications on <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a>.</p>
<p>See <a href="sdk-for-flutter-navigate-navigation-maneuverviewlaneassistance-class">ManeuverViewLaneAssistance</a> documentation for further details.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory ManeuverViewLaneAssistanceListener(
  void Function(ManeuverViewLaneAssistance) onLaneAssistanceUpdatedLambda,

) =&gt; ManeuverViewLaneAssistanceListener$Lambdas(
  onLaneAssistanceUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
