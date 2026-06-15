---
title: "clearAppCache abstract method"
slug: "sdk-for-flutter-navigate-maploader-sdkcache-clearappcache"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- clearAppCache.html -->


<div>
<h1>clearAppCache abstract method</h1></div>

void
clearAppCache(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a> callback</li>
</ol>)

      

    

<p>Clears all data that is currently stored in the SDK cache.</p>
<p>Path for cache is specified by <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-cachepath">SDKOptions.cachePath</a>.
The operation can have unexpected behaviour when it is called during a map interaction, during turn-by-turn navigation (only available for the Navigate license) or
during ongoing requests initiated by the OfflineSearchEngine or the OfflineRouteEngine (only available for the Navigate license).</p>
<ul>
<li><code>callback</code> Callback which receives the result on the main thread.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void clearAppCache(SDKCacheCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
