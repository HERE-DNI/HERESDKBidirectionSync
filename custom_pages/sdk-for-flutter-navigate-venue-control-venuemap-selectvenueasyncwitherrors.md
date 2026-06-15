---
title: "selectVenueAsyncWithErrors abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrors"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- selectVenueAsyncWithErrors.html -->


<div>
<h1>selectVenueAsyncWithErrors abstract method</h1></div>

void
selectVenueAsyncWithErrors(<ol class="parameter-list single-line"> <li>int venueId, </li>
<li><a href="sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a> callback</li>
</ol>)

      

    

<p>Downloads a <a href="sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a> if needed and selects a <a href="sdk-for-flutter-navigate-venue-control-venue-class">Venue</a>.</p>
<ul>
<li>
<p><code>venueId</code> The ID of the venue to download and select.</p>
</li>
<li>
<p><code>callback</code> Callback to receives the error while venue load on the main thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void selectVenueAsyncWithErrors(int venueId, VenueLoadErrorCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
