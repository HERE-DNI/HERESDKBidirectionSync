---
title: "searchByText abstract method"
slug: "sdk-for-flutter-navigate-search-searchinterface-searchbytext"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByText.html -->


<div>
<h1>searchByText abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
searchByText(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-search-textquery-class">TextQuery</a> query, </li>
<li><a href="sdk-for-flutter-navigate-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="sdk-for-flutter-navigate-search-searchcallback">SearchCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous text query search for <a href="sdk-for-flutter-navigate-search-place-class">Place</a> instances within a given <a href="sdk-for-flutter-navigate-search-textqueryarea-class">TextQueryArea</a>.</p>
<p>The returned places are sorted by relevance.</p>
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
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByText(TextQuery query, SearchOptions options, SearchCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
