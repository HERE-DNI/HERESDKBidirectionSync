---
title: "com.here.sdk.maploader (API Reference)"
slug: "sdk-for-android-navigate-navigate-com-here-sdk-maploader-package-summary"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- package-summary.html -->
<!DOCTYPE HTML>






<div class="flex-box">
<header class="flex-header" role="banner">
<nav role="navigation">
<!-- ========= START OF TOP NAVBAR ======= -->
<div class="top-nav" id="navbar-top">
<div class="skip-nav"><a href="#skip-navbar-top" title="Skip navigation links">Skip navigation links</a></div>
<ul class="nav-list" id="navbar-top-firstrow" title="Navigation">
<li><a href="sdk-for-android-navigate-index">Overview</a></li>
<li class="nav-bar-cell1-rev">Package</li>
<li>Class</li>
<li><a href="sdk-for-android-navigate-package-tree">Tree</a></li>
<li><a href="sdk-for-android-navigate-deprecated-list">Deprecated</a></li>
<li><a href="sdk-for-android-navigate-index-all">Index</a></li>
<li><a href="sdk-for-android-navigate-help-doc#package">Help</a></li>
</ul>
</div>
<div class="sub-nav">
<div>
<ul class="sub-nav-list">
<li>Package: </li>
<li>Description | </li>
<li>Related Packages | </li>
<li><a href="#class-summary">Classes and Interfaces</a></li>
</ul>
</div>

</div>
<!-- ========= END OF TOP NAVBAR ========= -->
<span class="skip-nav" id="skip-navbar-top"></span></nav>
</header>
<div class="flex-content">
<main role="main">
<div class="header">

</div>
<hr/>
<div class="package-signature">package <span class="element-name">com.here.sdk.maploader</span></div>
<section class="summary">
<ul class="summary-list">
<li>
<div id="class-summary">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"></div>
<div aria-labelledby="class-summary-tab0" id="class-summary.tabpanel" role="tabpanel">
<div class="summary-table two-column-summary">
<div class="table-header col-first">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader">CatalogsUpdateInfoCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">This method will be called on the main thread when <a href="sdk-for-android-navigate-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)"><code>MapUpdater.retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)</code></a> has been completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Holds information for the catalog update intent.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-catalogupdateprogresslistener" title="interface in com.here.sdk.maploader">CatalogUpdateProgressListener</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Interface to get notified on status updates
 when updating catalog, previously downloaded by <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-catalogupdatestate" title="enum class in com.here.sdk.maploader">CatalogUpdateState</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Represents the state of catalog map updates.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-catalogupdatetask" title="class in com.here.sdk.maploader">CatalogUpdateTask</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">A class to control the catalog update process.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-deletedregionscallback" title="interface in com.here.sdk.maploader">DeletedRegionsCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#deleteRegions(java.util.List,com.here.sdk.maploader.DeletedRegionsCallback)"><code>MapDownloader.deleteRegions(java.util.List&lt;com.here.sdk.maploader.RegionId&gt;, com.here.sdk.maploader.DeletedRegionsCallback)</code></a> has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback)"><code>MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)</code></a> has been completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">Interface to get notified on
 status updates when downloading map regions.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-installedcatalog" title="class in com.here.sdk.maploader">InstalledCatalog</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Represents installed catalog.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-installedregion" title="class in com.here.sdk.maploader">InstalledRegion</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents a region, from persistent map storage.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Represents download status of region in the persistent map storage.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader">MapDownloader</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class for downloading and managing map data for various regions worldwide.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-mapdownloaderconstructioncallback" title="interface in com.here.sdk.maploader">MapDownloaderConstructionCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapDownloaderConstructionCallback)"><code>MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback)</code></a> has been completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class to control map download process.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Specifies possible errors that may result from map downloading/prefetching.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab5"><a href="sdk-for-android-navigate-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab5">
<div class="block">Error occurred during map operation.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-mapupdateprogresslistener" title="interface in com.here.sdk.maploader">MapUpdateProgressListener</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">Interface to get notified on status updates
 when updating map data, previously downloaded by <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class for updating regions previously downloaded using the <a href="sdk-for-android-navigate-mapdownloader" title="class in com.here.sdk.maploader"><code>MapDownloader</code></a>.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-mapupdater.mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Defines if installed regions and subregions are updated one-by-one or if all regions are
 updated only once the updates for all installed regions have been downloaded entirely.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-mapupdaterconstructioncallback" title="interface in com.here.sdk.maploader">MapUpdaterConstructionCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapupdater#fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine,com.here.sdk.maploader.MapUpdaterConstructionCallback)"><code>MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback)</code></a> has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-mapupdatetask" title="class in com.here.sdk.maploader">MapUpdateTask</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">A class to control the map update process.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-mapversionhandle" title="class in com.here.sdk.maploader">MapVersionHandle</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Represents version of the map.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-navigabilitytype" title="enum class in com.here.sdk.maploader">NavigabilityType</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Represents the navigability level of a map region.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-offlinestoragesizecallback" title="interface in com.here.sdk.maploader">OfflineStorageSizeCallback</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#getOfflineMapsStorageSizeInBytes(com.here.sdk.maploader.OfflineStorageSizeCallback)"><code>MapDownloader.getOfflineMapsStorageSizeInBytes(OfflineStorageSizeCallback)</code></a> has been completed.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a></div>
<div class="col-last even-row-color class-summary class-summary-tab3">
<div class="block">Specifies possible errors that may result after a map repair operation has been completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab3"><a href="sdk-for-android-navigate-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab3">
<div class="block">Specifies possible statuses of the already downloaded map regions as a whole.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-region" title="class in com.here.sdk.maploader">Region</a></div>
<div class="col-last even-row-color class-summary class-summary-tab2">
<div class="block">Defines an area, especially part of a country or the world that can be downloaded.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-regionid" title="class in com.here.sdk.maploader">RegionId</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Specify a unique identifier for Region.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-repairpersistentmapcallback" title="interface in com.here.sdk.maploader">RepairPersistentMapCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-mapdownloader#repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback)"><code>MapDownloader.repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback)</code></a> has been completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-sdkcache" title="class in com.here.sdk.maploader">SDKCache</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">A class to manage SDK Cache.</div>
</div>
<div class="col-first even-row-color class-summary class-summary-tab1"><a href="sdk-for-android-navigate-sdkcachecallback" title="interface in com.here.sdk.maploader">SDKCacheCallback</a></div>
<div class="col-last even-row-color class-summary class-summary-tab1">
<div class="block">A method which is called on the main thread when <a href="sdk-for-android-navigate-sdkcache#clearCache(com.here.sdk.maploader.SDKCacheCallback)"><code>SDKCache.clearCache(com.here.sdk.maploader.SDKCacheCallback)</code></a> has been completed.</div>
</div>
<div class="col-first odd-row-color class-summary class-summary-tab2"><a href="sdk-for-android-navigate-updatestatistics" title="class in com.here.sdk.maploader">UpdateStatistics</a></div>
<div class="col-last odd-row-color class-summary class-summary-tab2">
<div class="block">Defines statistics related to the success or failure of patched bundles.</div>
</div>
</div>
</div>
</div>
</li>
</ul>
</section>
</main>
</div>
</div>



</div>
`
}</HTMLBlock>
