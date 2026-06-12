---
title: "addVenueAsyncWithErrorsStr abstract method"
slug: "sdk-for-flutter-navigate-venue-control-venuemap-addvenueasyncwitherrorsstr"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addVenueAsyncWithErrorsStr.html -->


<div>
<h1>addVenueAsyncWithErrorsStr abstract method</h1></div>

void
addVenueAsyncWithErrorsStr(<ol class="parameter-list single-line"> <li>String venueIdentifier, </li>
<li><a href="/sdk-for-flutter-navigate-venue-control-venueloaderrorcallback">VenueLoadErrorCallback</a> callback</li>
</ol>)

      

    

<p>Downloads and adds a <a href="/sdk-for-flutter-navigate-venue-control-venue-class">Venue</a> to the <a href="/sdk-for-flutter-navigate-venue-control-venuemap-class">VenueMap</a>.</p>
<p>Method will do nothing if the venue already exists on the venue map.</p>
<ul>
<li>
<p><code>venueIdentifier</code> The ID of the venue to download and add.</p>
</li>
<li>
<p><code>callback</code> Callback to receives the error while venue load on the main thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addVenueAsyncWithErrorsStr(String venueIdentifier, VenueLoadErrorCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
