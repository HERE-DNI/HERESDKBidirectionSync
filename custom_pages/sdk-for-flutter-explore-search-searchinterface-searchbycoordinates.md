---
title: "searchByCoordinates abstract method"
slug: "sdk-for-flutter-explore-search-searchinterface-searchbycoordinates"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinates.html -->


<div>
<h1>searchByCoordinates abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
searchByCoordinates(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallback">SearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous search for <a href="/sdk-for-flutter-explore-search-place-class">Place</a> instances based on the given
geographic coordinates.</p>
<p>This is the same search type as reverse geocoding, except that more data is returned
than just the <a href="/sdk-for-flutter-explore-search-address-class">Address</a> related to the given coordinates.
Note that more than one <a href="/sdk-for-flutter-explore-search-place-class">Place</a> can be related to the given coordinates.
The returned places are sorted by relevance.</p>
<ul>
<li>
<p><code>coordinates</code> The coordinates where to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinates(GeoCoordinates coordinates, SearchOptions options, SearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
