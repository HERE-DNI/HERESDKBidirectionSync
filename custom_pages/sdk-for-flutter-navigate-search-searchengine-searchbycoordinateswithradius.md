---
title: "searchByCoordinatesWithRadius abstract method"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbycoordinateswithradius"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinatesWithRadius.html -->


<div>
<h1>searchByCoordinatesWithRadius abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByCoordinatesWithRadius(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a> circle, </li>
<li><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for places based on given circular spatial filter.</p>
<p>This is the same process as reverse geocoding, except that more data is returned
than just the <a href="sdk-for-flutter-navigate-search-address-class">Address</a> that belongs to given coordinates. Note that coordinates
can belong to more than one <a href="sdk-for-flutter-navigate-search-place-class">Place</a> result.
Provides candidate places sorted by relevance and located inside the radius of filter.</p>
<ul>
<li>
<p><code>circle</code> The coordinates where to search and radius of the circular spatial filter.
Passed in form of <a href="sdk-for-flutter-navigate-core-geocircle-class">GeoCircle</a>.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinatesWithRadius(GeoCircle circle, SearchOptions options, SearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
