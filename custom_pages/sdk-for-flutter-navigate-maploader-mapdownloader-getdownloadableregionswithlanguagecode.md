---
title: "getDownloadableRegionsWithLanguageCode abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getDownloadableRegionsWithLanguageCode.html -->


<div>
<h1>getDownloadableRegionsWithLanguageCode abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
getDownloadableRegionsWithLanguageCode(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-core-languagecode">LanguageCode</a> languageCode, </li>
<li><a href="/sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request to fetch a list of <a href="/sdk-for-flutter-navigate-maploader-region-class">Region</a> objects with <a href="/sdk-for-flutter-navigate-maploader-region-name">Region.name</a>
in given <code>MapDownloader.getDownloadableRegionsWithLanguageCode.languageCode</code>, that can be used to download the actual map data in a separate request.</p>
<ul>
<li>
<p><code>languageCode</code> The language code determines the language of <a href="/sdk-for-flutter-navigate-maploader-region-name">Region.name</a>.</p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle getDownloadableRegionsWithLanguageCode(LanguageCode languageCode, DownloadableRegionsCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
