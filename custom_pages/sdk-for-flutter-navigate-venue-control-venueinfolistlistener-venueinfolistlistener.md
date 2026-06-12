---
title: "VenueInfoListListener constructor"
slug: "sdk-for-flutter-navigate-venue-control-venueinfolistlistener-venueinfolistlistener"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueInfoListListener.html -->


<div>
<h1>VenueInfoListListener constructor</h1></div>

VenueInfoListListener(<ol class="parameter-list single-line"> <li>void onVenueInfoListLoadLambda(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-venue-control-venueinfodatalist">VenueInfoDataList</a></li>
</ol>)</li>
</ol>)
    

<p>The abstract class for  for
the list of <a href="/sdk-for-flutter-navigate-venue-data-venueinfo-class">VenueInfo</a> load event.</p>
<p>Use <a href="/sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>
to add and remove the <a href="/sdk-for-flutter-navigate-venue-control-venueinfolistlistener-class">VenueInfoListListener</a>.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory VenueInfoListListener(
  void Function(VenueInfoDataList) onVenueInfoListLoadLambda,

) =&gt; VenueInfoListListener$Lambdas(
  onVenueInfoListLoadLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
