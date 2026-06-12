---
title: "VenueSelectionListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venueselectionlistener-venueselectionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueSelectionListener.html -->


<div>
<h1>VenueSelectionListener constructor</h1></div>

VenueSelectionListener(<ol class="parameter-list single-line"> <li>void onSelectedVenueChangedLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?, </li>
<li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>?</li>
</ol>)</li>
</ol>)
    

<p>The abstract class for  for
the <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> selection event.</p>
<p>Use the <a href="/sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>
to add and remove the <a href="/sdk-for-flutter-navigate-venue-control-venueselectionlistener-class">VenueSelectionListener</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueSelectionListener(
  void Function(Venue?, Venue?) onSelectedVenueChangedLambda,

) =&gt; VenueSelectionListener$Lambdas(
  onSelectedVenueChangedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
