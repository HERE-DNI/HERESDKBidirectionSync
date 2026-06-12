---
title: "searchByAddressExtended abstract method"
slug: "sdk-for-flutter-explore-search-searchengine-searchbyaddressextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByAddressExtended.html -->


<div>
<h1>searchByAddressExtended abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
searchByAddressExtended(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-addressquery-class">AddressQuery</a> query, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="/sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to search for places based on a given address.</p>
<p>This is the same process as forward geocoding, except that more data is returned
than just the geographic coordinates of a given address. Note that an address can
belong to more than one <a href="/sdk-for-flutter-explore-search-place-class">Place</a> result, although all found places will
share the same geographic coordinates.
Provides candidate places sorted by relevance.</p>
<ul>
<li>
<p><code>query</code> Desired free-form address query text to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByAddressExtended(AddressQuery query, SearchOptions options, SearchCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
