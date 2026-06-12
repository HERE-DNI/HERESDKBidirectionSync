---
title: "searchByCoordinatesWithRadiusExtended abstract method"
slug: "sdk-for-flutter-explore-search-searchengine-searchbycoordinateswithradiusextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCoordinatesWithRadiusExtended.html -->


<div>
<h1>searchByCoordinatesWithRadiusExtended abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
searchByCoordinatesWithRadiusExtended(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a> circle, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for places based on given circular spatial filter.</p>
<p>This is the same process as reverse geocoding, except that more data is returned
than just the <a href="/sdk-for-flutter-explore-search-address-class">Address</a> that belongs to given coordinates. Note that coordinates
can belong to more than one <a href="/sdk-for-flutter-explore-search-place-class">Place</a> result.
Provides candidate places sorted by relevance and located inside the radius of filter.</p>
<ul>
<li>
<p><code>circle</code> The coordinates where to search and radius of the circular spatial filter.
Passed in form of <a href="/sdk-for-flutter-explore-core-geocircle-class">GeoCircle</a>.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCoordinatesWithRadiusExtended(GeoCircle circle, SearchOptions options, SearchCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
