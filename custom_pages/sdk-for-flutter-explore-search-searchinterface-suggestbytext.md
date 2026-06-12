---
title: "suggestByText abstract method"
slug: "sdk-for-flutter-explore-search-searchinterface-suggestbytext"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- suggestByText.html -->


<div>
<h1>suggestByText abstract method</h1></div>

<a href="/sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
suggestByText(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-explore-search-textquery-class">TextQuery</a> query, </li>
<li><a href="/sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="/sdk-for-flutter-explore-search-suggestcallback">SuggestCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to suggest places for text queries and
returns suggestions sorted by relevance.</p>
<p>Note that while <code>OfflineSearchEngine</code> includes as many details as are available,
<code>SearchEngine</code> includes only the information that is relevant for autosuggest use cases.
Complete details can be obtained by searching with <a href="/sdk-for-flutter-explore-search-placeidquery-class">PlaceIdQuery</a>.</p>
<ul>
<li>
<p><code>query</code> Desired text query to search.</p>
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
<pre class="language-dart"><code class="language-dart">TaskHandle suggestByText(TextQuery query, SearchOptions options, SuggestCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
