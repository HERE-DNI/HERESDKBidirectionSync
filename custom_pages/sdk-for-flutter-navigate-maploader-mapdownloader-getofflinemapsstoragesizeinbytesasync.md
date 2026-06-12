---
title: "getOfflineMapsStorageSizeInBytesAsync abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getOfflineMapsStorageSizeInBytesAsync.html -->


<div>
<h1>getOfflineMapsStorageSizeInBytesAsync abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
getOfflineMapsStorageSizeInBytesAsync(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-maploader-offlinestoragesizecallback">OfflineStorageSizeCallback</a> callback</li>
</ol>)

      

    

<p>Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via <a href="/sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.</p>
<p>This includes also data that is currently being downloaded.</p>
<ul>
<li><code>callback</code> A callback which receives the value of offline map size or error on the main thread.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle getOfflineMapsStorageSizeInBytesAsync(OfflineStorageSizeCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
