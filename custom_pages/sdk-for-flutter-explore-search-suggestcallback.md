---
title: "SuggestCallback typedef"
slug: "sdk-for-flutter-explore-search-suggestcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SuggestCallback.html -->


<div>
<h1>SuggestCallback typedef</h1></div>

SuggestCallback =
     void Function(<a href="sdk-for-flutter-explore-search-searcherror">SearchError</a>? searchError, List&lt;<a href="sdk-for-flutter-explore-search-suggestion-class">Suggestion</a>&gt;? suggestions)


<p>The method will be called on the main thread when a suggest call has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li>
<p><code>searchError</code> An error enum indicating what went wrong. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>suggestions</code> The list of suggestion results. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef SuggestCallback = void Function(SearchError? searchError, List&lt;Suggestion&gt;? suggestions);</code></pre>

 



</div>
`
}</HTMLBlock>
