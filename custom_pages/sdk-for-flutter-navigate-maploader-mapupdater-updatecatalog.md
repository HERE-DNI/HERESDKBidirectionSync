---
title: "updateCatalog abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- updateCatalog.html -->


<div>
<h1>updateCatalog abstract method</h1></div>

<a href="sdk-for-flutter-navigate-maploader-catalogupdatetask-class">CatalogUpdateTask</a>
updateCatalog(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a> catalogInfo, </li>
<li><a href="sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class">CatalogUpdateProgressListener</a> callback</li>
</ol>)

      

    

<p>Performs an asynchronous request for each catalog to update map data to the latest available version.</p>
<p>This applies to all previously installed <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> map data and any incomplete downloads in a pending state.</p>
<p>If no regions are downloaded, this method updates only the map version.
The map cache and persisted regions are always bound to the same map version.</p>
<p>If no updates are available, <a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a> from
<a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> returns an empty list.
In this case, <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete">MapUpdateProgressListener.onComplete</a> is called immediately.</p>
<p>To check for available updates, use <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> to retrieve catalogs with newer versions.
Individual catalogs can then be updated using this method.
Ensure that the device has enough free disk space to perform a catalog update.
Information about the required disk space is available in <a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-disksizeinbytes">CatalogUpdateInfo.diskSizeInBytes</a>.</p>
<p>If there is not enough space to perform the catalog update with the default
<a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onComplete</a>, try using <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a>.
This option requires less space but follows a different strategy for handling errors during the map update.</p>
<p>If indexing is enabled through <code>OfflineSearchEngine.setIndexOptions</code>, the index is rebuilt after the map is updated.
The index helps <code>OfflineSearchEngine</code> provide better search results.</p>
<p>Note: Indexing is a beta feature and may have bugs or unexpected behavior.</p>
<ul>
<li>
<p><code>catalogInfo</code> catalog to update. CatalogUpdateInfo should be get from <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a></p>
</li>
<li>
<p><code>callback</code> Callback which receives the result on the main thread.</p>
</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-maploader-catalogupdatetask-class">CatalogUpdateTask</a>. A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">CatalogUpdateTask updateCatalog(CatalogUpdateInfo catalogInfo, CatalogUpdateProgressListener callback);</code></pre>

 



</div>
`
}</HTMLBlock>
