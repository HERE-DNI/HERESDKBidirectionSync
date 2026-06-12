---
title: "SearchCallback typedef"
slug: "sdk-for-flutter-explore-search-searchcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SearchCallback.html -->


<div>
<h1>SearchCallback typedef</h1></div>

SearchCallback =
     void Function(<a href="/sdk-for-flutter-explore-search-searcherror">SearchError</a>? searchError, List&lt;<a href="/sdk-for-flutter-explore-search-place-class">Place</a>&gt;? places)


<p>The method will be called on the main thread when a search call has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li>
<p><code>searchError</code> An error enum indicating what went wrong. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>places</code> The list of search results. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef SearchCallback = void Function(SearchError? searchError, List&lt;Place&gt;? places);</code></pre>

 



</div>
`
}</HTMLBlock>
