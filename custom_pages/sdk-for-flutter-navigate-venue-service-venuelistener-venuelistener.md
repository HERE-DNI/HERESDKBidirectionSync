---
title: "VenueListener constructor"
slug: "sdk-for-flutter-navigate-venue-service-venuelistener-venuelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueListener.html -->


<div>
<h1>VenueListener constructor</h1></div>

VenueListener(<ol class="parameter-list single-line"> <li>void onGetVenueCompletedLambda(<ol class="parameter-list"> <li>int, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>?, </li>
<li>bool, </li>
<li><a href="/sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a>?, </li>
</ol>)</li>
</ol>)
    

<p>The abstract class for listeners for
venue loading events in <a href="/sdk-for-flutter-navigate-venue-service-venueservice-class">VenueService</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueListener(
  void Function(int, VenueModel?, bool, VenueStyle?) onGetVenueCompletedLambda,

) =&gt; VenueListener$Lambdas(
  onGetVenueCompletedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
