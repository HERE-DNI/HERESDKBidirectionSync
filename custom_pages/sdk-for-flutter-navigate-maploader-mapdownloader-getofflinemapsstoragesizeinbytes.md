---
title: "getOfflineMapsStorageSizeInBytes abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytes"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getOfflineMapsStorageSizeInBytes.html -->


<div>
<h1>getOfflineMapsStorageSizeInBytes abstract method</h1></div>

int
getOfflineMapsStorageSizeInBytes()

      

    

<p>Get the total size of all downloaded regions currently persisted on disk at the location that
is specified via <a href="/sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.</p>
<p>This includes also data that is currently being downloaded.</p>
<p>Returns <code>int</code>. Value of offline map size.</p>
<p>Throws <a href="/sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class">MapLoaderExceptionException</a>. Specifies reason, why current map size is not returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">int getOfflineMapsStorageSizeInBytes();</code></pre>

 



</div>
`
}</HTMLBlock>
