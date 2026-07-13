---
title: "updateCatalog method - MapUpdater class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapupdater-updatecatalog"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/MapUpdater-class-sidebar.html" data-below-sidebar="">

<div>

# <span class="kind-method">updateCatalog</span> abstract method

</div>

<div class="section multi-line-signature">

<span class="returntype"><a href="sdk-for-flutter-navigate-maploader-catalogupdatetask-class">CatalogUpdateTask</a></span> <span class="name">updateCatalog</span>(<wbr></wbr>

1.  <span id="sdk-for-flutter-navigate-updateCatalog-param-catalogInfo" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a></span> <span class="parameter-name">catalogInfo</span>, </span>
2.  <span id="sdk-for-flutter-navigate-updateCatalog-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class">CatalogUpdateProgressListener</a></span> <span class="parameter-name">callback</span></span>

)

</div>

<div class="section desc markdown">

Performs an asynchronous request for each catalog to update map data to the latest available version.

This applies to all previously installed <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> map data and any incomplete downloads in a pending state.

If no regions are downloaded, this method updates only the map version. The map cache and persisted regions are always bound to the same map version.

If no updates are available, <a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a> from <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> returns an empty list. In this case, <a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-oncomplete">MapUpdateProgressListener.onComplete</a> is called immediately.

To check for available updates, use <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> to retrieve catalogs with newer versions. Individual catalogs can then be updated using this method. Ensure that the device has enough free disk space to perform a catalog update. Information about the required disk space is available in <a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-disksizeinbytes">CatalogUpdateInfo.diskSizeInBytes</a>.

If there is not enough space to perform the catalog update with the default <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onComplete</a>, try using <a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy.onFirstRegion</a>. This option requires less space but follows a different strategy for handling errors during the map update.

If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, the index is rebuilt after the map is updated. The index helps `OfflineSearchEngine` provide better search results.

Note: Indexing is a beta feature and may have bugs or unexpected behavior.

- `catalogInfo` catalog to update. CatalogUpdateInfo should be get from <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a>

- `callback` Callback which receives the result on the main thread.

Returns <a href="sdk-for-flutter-navigate-maploader-catalogupdatetask-class">CatalogUpdateTask</a>. A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.

</div>

## Implementation

``` dart
CatalogUpdateTask updateCatalog(CatalogUpdateInfo catalogInfo, CatalogUpdateProgressListener callback);
```

</pre>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

