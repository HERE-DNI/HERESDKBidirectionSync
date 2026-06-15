---
title: "MapUpdaterConstructionCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- MapUpdaterConstructionCallback.html -->


<div>
<h1>MapUpdaterConstructionCallback typedef</h1></div>

MapUpdaterConstructionCallback =
     void Function(<a href="sdk-for-flutter-navigate-maploader-mapupdater-class">MapUpdater</a> mapUpdater)


<p>A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync">MapUpdater.fromSdkEngineAsync</a> has been completed.</p>
<p>Construction requires the online configuration to be fetched, which in case of sync API, would block the calling thread.
When configuration is cached, it is enough to read it from the disk, this operation still takes relatively big time.</p>
<ul>
<li><code>mapUpdater</code> Represents a constructed <code>MapUpdater</code> object.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef MapUpdaterConstructionCallback = void Function(MapUpdater mapUpdater);</code></pre>

 



</div>
`
}</HTMLBlock>
