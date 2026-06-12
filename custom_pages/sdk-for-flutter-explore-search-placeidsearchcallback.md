---
title: "PlaceIdSearchCallback typedef"
slug: "sdk-for-flutter-explore-search-placeidsearchcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- PlaceIdSearchCallback.html -->


<div>
<h1>PlaceIdSearchCallback typedef</h1></div>

PlaceIdSearchCallback =
     void Function(<a href="/sdk-for-flutter-explore-search-searcherror">SearchError</a>? searchError, <a href="/sdk-for-flutter-explore-search-place-class">Place</a>? place)


<p>The method will be called on the main thread when a search by id call has been completed.</p>
<ul>
<li>
<p><code>searchError</code> The search error.</p>
</li>
<li>
<p><code>place</code> The place.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef PlaceIdSearchCallback = void Function(SearchError? searchError, Place? place);</code></pre>

 



</div>
`
}</HTMLBlock>
