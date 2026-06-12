---
title: "PlaceIdSearchCallbackExtended typedef"
slug: "sdk-for-flutter-navigate-search-placeidsearchcallbackextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceIdSearchCallbackExtended.html -->


<div>
<h1>PlaceIdSearchCallbackExtended typedef</h1></div>

PlaceIdSearchCallbackExtended =
     void Function(<a href="/sdk-for-flutter-navigate-search-searcherror">SearchError</a>? searchError, <a href="/sdk-for-flutter-navigate-search-place-class">Place</a>? place, <a href="/sdk-for-flutter-navigate-search-responsedetails-class">ResponseDetails</a>? responseDetails)


<p>The method will be called on the main thread when a search by id call has been completed.</p>
<ul>
<li>
<p><code>searchError</code> The search error.</p>
</li>
<li>
<p><code>place</code> The place.</p>
</li>
<li>
<p><code>responseDetails</code> The response details.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef PlaceIdSearchCallbackExtended = void Function(SearchError? searchError, Place? place, ResponseDetails? responseDetails);</code></pre>

 



</div>
`
}</HTMLBlock>
