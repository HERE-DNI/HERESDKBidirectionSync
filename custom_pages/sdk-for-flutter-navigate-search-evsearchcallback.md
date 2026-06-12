---
title: "EVSearchCallback typedef"
slug: "sdk-for-flutter-navigate-search-evsearchcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSearchCallback.html -->


<div>
<h1>EVSearchCallback typedef</h1></div>

EVSearchCallback =
     void Function(<a href="/sdk-for-flutter-navigate-search-evsearcherror">EVSearchError</a>? error, List&lt;<a href="/sdk-for-flutter-navigate-search-evcharginglocation-class">EVChargingLocation</a>&gt;? chargingLocations)


<p>The method that will be called on the main thread when a search operation in <code>EVSearchEngine</code>
has been completed.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>error</code> The ev search error.</p>
</li>
<li>
<p><code>chargingLocations</code> The ev charging locations.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef EVSearchCallback = void Function(EVSearchError? error, List&lt;EVChargingLocation&gt;? chargingLocations);</code></pre>

 



</div>
`
}</HTMLBlock>
