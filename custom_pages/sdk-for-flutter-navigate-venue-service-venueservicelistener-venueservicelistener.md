---
title: "VenueServiceListener constructor"
slug: "sdk-for-flutter-navigate-venue-service-venueservicelistener-venueservicelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueServiceListener.html -->


<div>
<h1>VenueServiceListener constructor</h1></div>

VenueServiceListener(<ol class="parameter-list single-line"> <li>void onInitializationCompletedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-service-venueserviceinitstatus">VenueServiceInitStatus</a></li>
</ol>), </li>
<li>void onVenueServiceStoppedLambda()</li>
</ol>)
    

<p>The abstract class for listeners for
lifecycle events in <a href="/sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueServiceListener(
  void Function(VenueServiceInitStatus) onInitializationCompletedLambda,
  void Function() onVenueServiceStoppedLambda,

) =&gt; VenueServiceListener$Lambdas(
  onInitializationCompletedLambda,
  onVenueServiceStoppedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
