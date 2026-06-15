---
title: "DownloadableRegionsCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-downloadableregionscallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- DownloadableRegionsCallback.html -->


<div>
<h1>DownloadableRegionsCallback typedef</h1></div>

DownloadableRegionsCallback =
     void Function(<a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? maploaderError, List&lt;<a href="sdk-for-flutter-navigate-maploader-region-class">Region</a>&gt;? regions)


<p>A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">MapDownloader.getDownloadableRegionsWithLanguageCode</a> has been completed.</p>
<p>The first argument indicates an error in case of a failure. The second argument contains the results.
Both arguments cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.</p>
<ul>
<li>
<p><code>maploaderError</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>regions</code> Represents a list of downloadable regions. It is <code>null</code> in case of an error. Each region can contain child
regions that can contain child regions and so on. Usually, the top-level regions represent continents that contain countries
as children.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef DownloadableRegionsCallback = void Function(MapLoaderError? maploaderError, List&lt;Region&gt;? regions);</code></pre>

 



</div>
`
}</HTMLBlock>
