---
title: "searchByCoordinatesExtended abstract method"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbycoordinatesextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinatesExtended.html -->


<div>
<h1>searchByCoordinatesExtended abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByCoordinatesExtended(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocoordinates-class">GeoCoordinates</a> coordinates, </li>
<li><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="sdk-for-flutter-navigate-search-searchcallbackextended">SearchCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for places based on given geographic coordinates.</p>
<p>This is the same process as reverse geocoding, except that more data is returned
than just the <a href="sdk-for-flutter-navigate-search-address-class">Address</a> that belongs to given coordinates. Note that coordinates
can belong to more than one <a href="sdk-for-flutter-navigate-search-place-class">Place</a> result.
Provides candidate places sorted by relevance.</p>
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
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinatesExtended(GeoCoordinates coordinates, SearchOptions options, SearchCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
