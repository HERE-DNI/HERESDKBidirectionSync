---
title: "searchByTextExtended abstract method"
slug: "sdk-for-flutter-navigate-search-searchengine-searchbytextextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByTextExtended.html -->


<div>
<h1>searchByTextExtended abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByTextExtended(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-search-textquery-class">TextQuery</a> query, </li>
<li><a href="/sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="/sdk-for-flutter-navigate-search-searchcallbackextended">SearchCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to do a text query search for <a href="/sdk-for-flutter-navigate-search-place-class">Place</a> instances.</p>
<p>Optionally, search along a polyline, such as a route, by specifying a <a href="/sdk-for-flutter-navigate-core-geocorridor-class">GeoCorridor</a>.
Provides candidate places sorted by relevance.</p>
<ul>
<li>
<p><code>query</code> Desired free-form text query to search.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByTextExtended(TextQuery query, SearchOptions options, SearchCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
