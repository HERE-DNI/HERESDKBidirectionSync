---
title: "getDownloadableRegions abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getDownloadableRegions.html -->


<div>
<h1>getDownloadableRegions abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
getDownloadableRegions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to fetch a list of <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> objects
for downloading map data in a separate request.</p>
<p>The default language for <a href="sdk-for-flutter-navigate-maploader-region-name">Region.name</a> is <a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode.enUs</a>.</p>
<ul>
<li><code>callback</code> Callback which receives the result on the main thread.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle getDownloadableRegions(DownloadableRegionsCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
