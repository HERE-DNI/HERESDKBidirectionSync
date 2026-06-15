---
title: "TruckRestrictionsWarningListener constructor"
slug: "sdk-for-flutter-navigate-navigation-truckrestrictionswarninglistener-truckrestrictionswarninglistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TruckRestrictionsWarningListener.html -->


<div>
<h1>TruckRestrictionsWarningListener constructor</h1></div>

TruckRestrictionsWarningListener(<ol class="parameter-list single-line"> <li>void onTruckRestrictionsWarningUpdatedLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-navigation-truckrestrictionwarning-class">TruckRestrictionWarning</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive truck restriction warnings.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TruckRestrictionsWarningListener(
  void Function(List&lt;TruckRestrictionWarning&gt;) onTruckRestrictionsWarningUpdatedLambda,

) =&gt; TruckRestrictionsWarningListener$Lambdas(
  onTruckRestrictionsWarningUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
