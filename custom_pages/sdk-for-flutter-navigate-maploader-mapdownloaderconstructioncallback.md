---
title: "MapDownloaderConstructionCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapDownloaderConstructionCallback.html -->


<div>
<h1>MapDownloaderConstructionCallback typedef</h1></div>

MapDownloaderConstructionCallback =
     void Function(<a href="/sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a> mapDownloader)


<p>A method which is called on the main thread when <a href="/sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">MapDownloader.fromSdkEngineAsync</a> has been completed.</p>
<p>The <code>MapDownloader</code> instance is created on a background thread to not block the calling
thread.</p>
<p>During construction an online connection is established to fetch configuration data for
internal use. If no online connection is available, cached or default values will be used.
This is only for internal reasons and has no effect on the operability of the resulting
instance. When configuration data is available from the cache, construction can still take
a reasonable amount of time. Applications should consider to show a loading indicator.</p>
<ul>
<li><code>mapDownloader</code> Represents a constructed MapDownloader object.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapDownloaderConstructionCallback = void Function(MapDownloader mapDownloader);</code></pre>

 



</div>
`
}</HTMLBlock>
