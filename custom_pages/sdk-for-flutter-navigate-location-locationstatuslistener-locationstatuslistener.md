---
title: "LocationStatusListener constructor"
slug: "sdk-for-flutter-navigate-location-locationstatuslistener-locationstatuslistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationStatusListener.html -->


<div>
<h1>LocationStatusListener constructor</h1></div>

LocationStatusListener(<ol class="parameter-list single-line"> <li>void onStatusChangedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus</a></li>
</ol>), </li>
<li>void onFeaturesNotAvailableLambda(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-location-locationfeature">LocationFeature</a>&gt;</li>
</ol>)</li>
</ol>)
    

<p>Abstract class for listening the
LocationEngine status updates.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LocationStatusListener(
  void Function(LocationEngineStatus) onStatusChangedLambda,
  void Function(List&lt;LocationFeature&gt;) onFeaturesNotAvailableLambda,

) =&gt; LocationStatusListener$Lambdas(
  onStatusChangedLambda,
  onFeaturesNotAvailableLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
