---
title: "deleteRegions abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- deleteRegions.html -->


<div>
<h1>deleteRegions abstract method</h1></div>

void
deleteRegions(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>&gt; regions, </li>
<li><a href="sdk-for-flutter-navigate-maploader-deletedregionscallback">DeletedRegionsCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>.</p>
<p>Note: Deleting a region when there is a pending download returns error
<a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.internalError</a>. Also, deleting a region when there is an ongoing download returns
error <a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError.parallelRequest</a>.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, then after
the requested regions have been deleted, the index over remaining regions will be rebuilt,
so that entries related to deleted regions are removed.
The index is used by <code>OfflineSearchEngine</code> to find better results.
Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.</p>
<ul>
<li>
<p><code>regions</code> List of regions to be deleted.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result of deletion on the main thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void deleteRegions(List&lt;RegionId&gt; regions, DeletedRegionsCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
