---
title: "VenueDrawingSelectionListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-venuedrawingselectionlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueDrawingSelectionListener.html -->


<div>
<h1>VenueDrawingSelectionListener constructor</h1></div>

VenueDrawingSelectionListener(<ol class="parameter-list single-line"> <li>void onDrawingSelectedLambda(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>, </li>
<li><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a>?, </li>
<li><a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a></li>
</ol>)</li>
</ol>)
    

<p>The abstract class for  for
the <a href="sdk-for-flutter-navigate-venue-data-venuedrawing-class">VenueDrawing</a> selection event.</p>
<p>Use the <a href="sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>
to add and remove the <a href="sdk-for-flutter-navigate-venue-control-venuedrawingselectionlistener-class">VenueDrawingSelectionListener</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueDrawingSelectionListener(
  void Function(Venue, VenueDrawing?, VenueDrawing) onDrawingSelectedLambda,

) =&gt; VenueDrawingSelectionListener$Lambdas(
  onDrawingSelectedLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
