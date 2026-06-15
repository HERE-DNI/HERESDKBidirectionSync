---
title: "SpeedLimitListener constructor"
slug: "sdk-for-flutter-navigate-navigation-speedlimitlistener-speedlimitlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SpeedLimitListener.html -->


<div>
<h1>SpeedLimitListener constructor</h1></div>

SpeedLimitListener(<ol class="parameter-list single-line"> <li>void onSpeedLimitUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-speedlimit-class">SpeedLimit</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class
should be implemented in order to receive the speed limit of the current road.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory SpeedLimitListener(
  void Function(SpeedLimit) onSpeedLimitUpdatedLambda,

) =&gt; SpeedLimitListener$Lambdas(
  onSpeedLimitUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
