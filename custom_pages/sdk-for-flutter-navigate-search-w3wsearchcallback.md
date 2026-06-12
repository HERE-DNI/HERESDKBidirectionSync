---
title: "W3WSearchCallback typedef"
slug: "sdk-for-flutter-navigate-search-w3wsearchcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- W3WSearchCallback.html -->


<div>
<h1>W3WSearchCallback typedef</h1></div>

W3WSearchCallback =
     void Function(<a href="/sdk-for-flutter-navigate-search-w3wsearcherror">W3WSearchError</a>? searchError, <a href="/sdk-for-flutter-navigate-search-w3wsquare-class">W3WSquare</a>? square)


<p>The method that will be called on the main thread when a search operation in <code>W3WSearchEngine</code>
has been completed.</p>
<ul>
<li>
<p><code>searchError</code> The w3w search error.</p>
</li>
<li>
<p><code>square</code> The w3w square.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef W3WSearchCallback = void Function(W3WSearchError? searchError, W3WSquare? square);</code></pre>

 



</div>
`
}</HTMLBlock>
