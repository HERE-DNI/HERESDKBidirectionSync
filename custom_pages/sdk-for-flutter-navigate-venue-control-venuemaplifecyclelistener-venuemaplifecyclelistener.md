---
title: "VenueMapLifecycleListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-venuemaplifecyclelistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueMapLifecycleListener.html -->


<div>
<h1>VenueMapLifecycleListener constructor</h1></div>

VenueMapLifecycleListener(<ol class="parameter-list single-line"> <li>void onVenueAddedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a></li>
</ol>), </li>
<li>void onVenueRemovedLambda(<ol class="parameter-list single-line"> <li>String</li>
</ol>)</li>
</ol>)
    

<p>The abstract class for  for
the <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> lifecycle events.</p>
<p>Use the <a href="/sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>
to add and remove the <a href="/sdk-for-flutter-navigate-venue-control-venuemaplifecyclelistener-class">VenueMapLifecycleListener</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueMapLifecycleListener(
  void Function(Venue) onVenueAddedLambda,
  void Function(String) onVenueRemovedLambda,

) =&gt; VenueMapLifecycleListener$Lambdas(
  onVenueAddedLambda,
  onVenueRemovedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
