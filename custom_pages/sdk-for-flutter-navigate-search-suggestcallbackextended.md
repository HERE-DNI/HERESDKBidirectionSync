---
title: "SuggestCallbackExtended typedef"
slug: "sdk-for-flutter-navigate-search-suggestcallbackextended"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- SuggestCallbackExtended.html -->


<div>
<h1>SuggestCallbackExtended typedef</h1></div>

SuggestCallbackExtended =
     void Function(<a href="/sdk-for-flutter-navigate-search-searcherror">SearchError</a>? searchError, List&lt;<a href="/sdk-for-flutter-navigate-search-suggestion-class">Suggestion</a>&gt;? suggestions, <a href="/sdk-for-flutter-navigate-search-responsedetails-class">ResponseDetails</a>? responseDetails)


<p>The method will be called on the main thread when a suggest call has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.
This API is not supported by offline search.</p>
<ul>
<li>
<p><code>searchError</code> An error enum indicating what went wrong. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>suggestions</code> The list of suggestion results. It is <code>null</code> in case of an error.</p>
</li>
<li>
<p><code>responseDetails</code> Additional information provided with response. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef SuggestCallbackExtended = void Function(SearchError? searchError, List&lt;Suggestion&gt;? suggestions, ResponseDetails? responseDetails);</code></pre>

 



</div>
`
}</HTMLBlock>
