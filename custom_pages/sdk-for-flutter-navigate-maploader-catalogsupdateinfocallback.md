---
title: "CatalogsUpdateInfoCallback typedef"
slug: "sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- CatalogsUpdateInfoCallback.html -->


<div>
<h1>CatalogsUpdateInfoCallback typedef</h1></div>

CatalogsUpdateInfoCallback =
     void Function(<a href="/sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>? error, List&lt;<a href="/sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a>&gt;? catalogs)


<p>This method will be called on the main thread when <a href="/sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> has been completed.</p>
<p>The first parameter indicates an error in case of a failure. The second parameter contains the results.
Both parameters cannot be <code>null</code> at the same time - or not <code>null</code> at the same time.
An empty <code>CatalogUpdateInfo</code> list  represent no map updates.</p>
<ul>
<li>
<p><code>error</code> Represents an error in case of a failure. It is <code>null</code> for an operation that succeeds.</p>
</li>
<li>
<p><code>catalogs</code> Represents a list of all catalogs that can be updated. It is <code>null</code> in case of an error.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef CatalogsUpdateInfoCallback = void Function(MapLoaderError? error, List&lt;CatalogUpdateInfo&gt;? catalogs);</code></pre>

 



</div>
`
}</HTMLBlock>
