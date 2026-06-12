---
title: "LocationListener constructor"
slug: "sdk-for-flutter-explore-core-locationlistener-locationlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- LocationListener.html -->


<div>
<h1>LocationListener constructor</h1></div>

LocationListener(<ol class="parameter-list single-line"> <li>void onLocationUpdatedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-location-class">Location</a></li>
</ol>)</li>
</ol>)
    

<p>This abstract class should be implemented in order to receive notifications
about location updates.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory LocationListener(
  void Function(Location) onLocationUpdatedLambda,

) =&gt; LocationListener$Lambdas(
  onLocationUpdatedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
