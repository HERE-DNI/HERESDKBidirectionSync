---
title: "onGetVenueCompleted abstract method"
slug: "sdk-for-flutter-navigate-venue-service-venuemaplistener-ongetvenuecompleted"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- onGetVenueCompleted.html -->


<div>
<h1>onGetVenueCompleted abstract method</h1></div>

void
onGetVenueCompleted(<ol class="parameter-list"> <li>String venueIdentifier, </li>
<li><a href="/sdk-for-flutter-navigate-venue-data-venuemodel-class">VenueModel</a>? venueModel, </li>
<li>bool online, </li>
<li><a href="/sdk-for-flutter-navigate-venue-style-venuestyle-class">VenueStyle</a>? venueStyle, </li>
</ol>)

      

    

<p>Called when loading of a venue or its retrieval from the cache is completed.</p>
<ul>
<li>
<p><code>venueIdentifier</code> The id of the venue.</p>
</li>
<li>
<p><code>venueModel</code> The venue model.</p>
</li>
<li>
<p><code>online</code> <code>True</code> if a new venue was loaded from the server and <code>false</code> otherwise.</p>
</li>
<li>
<p><code>venueStyle</code> The style associated with the venue.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void onGetVenueCompleted(String venueIdentifier, VenueModel? venueModel, bool online, VenueStyle? venueStyle);</code></pre>

 



</div>
`
}</HTMLBlock>
