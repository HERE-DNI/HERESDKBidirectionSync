---
title: "retrieveCatalogsUpdateInfo abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- retrieveCatalogsUpdateInfo.html -->


<div>
<h1>retrieveCatalogsUpdateInfo abstract method</h1></div>

<a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>
retrieveCatalogsUpdateInfo(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a> callback</li>
</ol>)

      

    

<p>Retrieves information of all catalogs that have newer version available.</p>
<p>This method can also be used to query
catalog information like HRN, current installed version and newer available version on server.
An empty list in <a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a> represent no map updates.</p>
<ul>
<li><code>callback</code> Callback which receives the result on the main thread.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a>. A handle to cancel a pending operation.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">TaskHandle retrieveCatalogsUpdateInfo(CatalogsUpdateInfoCallback callback);</code></pre>

 



</div>
`
}</HTMLBlock>
