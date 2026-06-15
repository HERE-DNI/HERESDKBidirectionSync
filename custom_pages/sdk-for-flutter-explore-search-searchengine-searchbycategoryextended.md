---
title: "searchByCategoryExtended abstract method"
slug: "sdk-for-flutter-explore-search-searchengine-searchbycategoryextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- searchByCategoryExtended.html -->


<div>
<h1>searchByCategoryExtended abstract method</h1></div>

<a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>
searchByCategoryExtended(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-explore-search-categoryquery-class">CategoryQuery</a> query, </li>
<li><a href="sdk-for-flutter-explore-search-searchoptions-class">SearchOptions</a> options, </li>
<li><a href="sdk-for-flutter-explore-search-searchcallbackextended">SearchCallbackExtended</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to do a category search for <a href="sdk-for-flutter-explore-search-place-class">Place</a> instances.</p>
<p>A list containing at least one <a href="sdk-for-flutter-explore-search-placecategory-class">PlaceCategory</a> must be provided
as part of the <code>SearchEngine.searchByCategoryExtended.query</code>.</p>
<ul>
<li>
<p><code>query</code> Query with list of desired categories.</p>
</li>
<li>
<p><code>options</code> Search options.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-explore-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle searchByCategoryExtended(CategoryQuery query, SearchOptions options, SearchCallbackExtended callback);</code></pre>

 



</div>
`
}</HTMLBlock>
