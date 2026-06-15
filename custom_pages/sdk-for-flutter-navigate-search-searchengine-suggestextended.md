---
title: "suggestExtended abstract method"
slug: "sdk-for-flutter-navigate-search-searchengine-suggestextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- suggestExtended.html -->


<div>
<h1>suggestExtended abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
suggestExtended(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-search-textquery-class">TextQuery</a> query, </li>
<li><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="sdk-for-flutter-navigate-search-suggestcallbackextended">SuggestCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to suggest places for text queries and
returns candidate suggestions sorted by relevance.</p>
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
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle suggestExtended(TextQuery query, SearchOptions options, SuggestCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
