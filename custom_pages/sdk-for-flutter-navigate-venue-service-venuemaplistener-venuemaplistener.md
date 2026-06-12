---
title: "VenueMapListener constructor"
slug: "sdk-for-flutter-navigate-venue-service-venuemaplistener-venuemaplistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueMapListener.html -->


<div>
<h1>VenueMapListener constructor</h1></div>

VenueMapListener(<ol class="parameter-list single-line"> <li>void onGetVenueCompletedLambda(<ol class="parameter-list"> <li>String, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>?, </li>
<li>bool, </li>
<li><a href="/sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a>?, </li>
</ol>)</li>
</ol>)
    

<p>The abstract class for listeners for
venue loading events in <a href="/sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueMapListener(
  void Function(String, VenueModel?, bool, VenueStyle?) onGetVenueCompletedLambda,

) =&gt; VenueMapListener$Lambdas(
  onGetVenueCompletedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
