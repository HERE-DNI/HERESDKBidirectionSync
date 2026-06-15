---
title: "VenueLoadErrorCallback typedef"
slug: "sdk-for-flutter-navigate-venue-control-venueloaderrorcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- VenueLoadErrorCallback.html -->


<div>
<h1>VenueLoadErrorCallback typedef</h1></div>

VenueLoadErrorCallback =
     void Function(<a href="sdk-for-flutter-navigate-venue-control-venueerrorcode">VenueErrorCode</a>? error)


<p>A method which is called on the main thread when <a href="sdk-for-flutter-navigate-venue-control-venuemap-selectvenueasyncwitherrorsstr">VenueMap.selectVenueAsyncWithErrorsStr</a> has been completed.</p>
<ul>
<li><code>error</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef VenueLoadErrorCallback = void Function(VenueErrorCode? error);</code></pre>

 



</div>
`
}</HTMLBlock>
