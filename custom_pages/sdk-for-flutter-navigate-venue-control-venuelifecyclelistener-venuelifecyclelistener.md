---
title: "VenueLifecycleListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-venuelifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLifecycleListener.html -->


<div>
<h1>VenueLifecycleListener constructor</h1></div>

VenueLifecycleListener(<ol class="parameter-list single-line"> <li>void onVenueAddedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></li>
</ol>), </li>
<li>void onVenueRemovedLambda(<ol class="parameter-list single-line"> <li>int</li>
</ol>)</li>
</ol>)
    

<p>The abstract class for  for
the <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> lifecycle events.</p>
<p>Use the <a href="/sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>
to add and remove the <a href="/sdk-for-flutter-navigate-venue-control-venuelifecyclelistener-class">VenueLifecycleListener</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueLifecycleListener(
  void Function(Venue) onVenueAddedLambda,
  void Function(int) onVenueRemovedLambda,

) =&gt; VenueLifecycleListener$Lambdas(
  onVenueAddedLambda,
  onVenueRemovedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
