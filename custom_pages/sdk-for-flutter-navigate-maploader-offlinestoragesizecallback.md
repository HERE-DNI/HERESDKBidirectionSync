---
title: "OfflineStorageSizeCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-offlinestoragesizecallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- OfflineStorageSizeCallback.html -->


<div>
<h1>OfflineStorageSizeCallback typedef</h1></div>

OfflineStorageSizeCallback =
     void Function(<a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? error, int? size)


<p>A method which is called on the main thread when <a href="/sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync">MapDownloader.getOfflineMapsStorageSizeInBytesAsync</a> has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li>
<p><code>error</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>size</code> The size of  offline map. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef OfflineStorageSizeCallback = void Function(MapLoaderError? error, int? size);</code></pre>

 



</div>
`
}</HTMLBlock>
