---
title: "DeletedRegionsCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-deletedregionscallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DeletedRegionsCallback.html -->


<div>
<h1>DeletedRegionsCallback typedef</h1></div>

DeletedRegionsCallback =
     void Function(<a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? maploaderError, List&lt;<a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>&gt;? regions)


<p>A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions">MapDownloader.deleteRegions</a> has been completed.</p>
<ul>
<li>
<p><code>maploaderError</code> Represents an error in case of a failure. It is [null] for an operation that succeeds.</p>
</li>
<li>
<p><code>regions</code> Represents a list of successfully removed map regions. It is [null] in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef DeletedRegionsCallback = void Function(MapLoaderError? maploaderError, List&lt;RegionId&gt;? regions);</code></pre>

 



</div>
`
}</HTMLBlock>
