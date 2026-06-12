---
title: "VenueLevelSelectionListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-venuelevelselectionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLevelSelectionListener.html -->


<div>
<h1>VenueLevelSelectionListener constructor</h1></div>

VenueLevelSelectionListener(<ol class="parameter-list single-line"> <li>void onLevelSelectedLambda(<ol class="parameter-list"> <li><a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>?, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a>, </li>
</ol>)</li>
</ol>)
    

<p>The abstract class for  for
the <a href="/sdk-for-flutter-navigate-venue-data-venuelevel-class">VenueLevel</a> selection event.</p>
<p>Use the <a href="/sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>
to add and remove the <a href="/sdk-for-flutter-navigate-venue-control-venuelevelselectionlistener-class">VenueLevelSelectionListener</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueLevelSelectionListener(
  void Function(Venue, VenueDrawing, VenueLevel?, VenueLevel) onLevelSelectedLambda,

) =&gt; VenueLevelSelectionListener$Lambdas(
  onLevelSelectedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
