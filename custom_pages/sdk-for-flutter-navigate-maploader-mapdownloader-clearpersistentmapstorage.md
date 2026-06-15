---
title: "clearPersistentMapStorage abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-clearpersistentmapstorage"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- clearPersistentMapStorage.html -->


<div>
<h1>clearPersistentMapStorage abstract method</h1></div>

void
clearPersistentMapStorage(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous operation to clear the persistent map storage from all data.</p>
<p>All downloaded regions will be removed.
Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.</p>
<p>Any previously built index will also be deleted.
See <a href="sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions">MapDownloader.downloadRegions</a> to learn more about index.</p>
<ul>
<li><code>callback</code> Callback which receives the result of clearing on the main thread.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void clearPersistentMapStorage(SDKCacheCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
