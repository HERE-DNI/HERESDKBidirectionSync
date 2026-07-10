---
title: "com.here.sdk.maploader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-package-summary"
---

<div class="header">

</div>

<div class="package-signature">

package <span class="element-name">com.here.sdk.maploader</span>

</div>

- <div id="sdk-for-android-navigate-class-summary">

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader">CatalogsUpdateInfoCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  This method will be called on the main thread when MapUpdater.retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback) has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Holds information for the catalog update intent.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateprogresslistener" title="interface in com.here.sdk.maploader">CatalogUpdateProgressListener</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Interface to get notified on status updates when updating catalog, previously downloaded by MapDownloader .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatestate" title="enum class in com.here.sdk.maploader">CatalogUpdateState</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents the state of catalog map updates.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatetask" title="class in com.here.sdk.maploader">CatalogUpdateTask</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  A class to control the catalog update process.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-deletedregionscallback" title="interface in com.here.sdk.maploader">DeletedRegionsCallback</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when MapDownloader.deleteRegions(java.util.List\<com.here.sdk.maploader.RegionId\>, com.here.sdk.maploader.DeletedRegionsCallback) has been completed.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when MapDownloader.getDownloadableRegions(LanguageCode, DownloadableRegionsCallback) has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  Interface to get notified on status updates when downloading map regions.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-installedcatalog" title="class in com.here.sdk.maploader">InstalledCatalog</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Represents installed catalog.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion" title="class in com.here.sdk.maploader">InstalledRegion</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Represents a region, from persistent map storage.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregionstatus" title="enum class in com.here.sdk.maploader">InstalledRegionStatus</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents download status of region in the persistent map storage.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader" title="class in com.here.sdk.maploader">MapDownloader</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class for downloading and managing map data for various regions worldwide.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloaderconstructioncallback" title="interface in com.here.sdk.maploader">MapDownloaderConstructionCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when MapDownloader.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback) has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class to control map download process.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploadererror" title="enum class in com.here.sdk.maploader">MapLoaderError</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Specifies possible errors that may result from map downloading/prefetching.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab5">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab5">

  <div class="block">

  Error occurred during map operation.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdateprogresslistener" title="interface in com.here.sdk.maploader">MapUpdateProgressListener</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  Interface to get notified on status updates when updating map data, previously downloaded by MapDownloader .

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater" title="class in com.here.sdk.maploader">MapUpdater</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class for updating regions previously downloaded using the MapDownloader .

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdaterconstructioncallback" title="interface in com.here.sdk.maploader">MapUpdaterConstructionCallback</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when MapUpdater.fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapUpdaterConstructionCallback) has been completed.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdatetask" title="class in com.here.sdk.maploader">MapUpdateTask</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  A class to control the map update process.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapversionhandle" title="class in com.here.sdk.maploader">MapVersionHandle</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Represents version of the map.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-navigabilitytype" title="enum class in com.here.sdk.maploader">NavigabilityType</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Represents the navigability level of a map region.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-offlinestoragesizecallback" title="interface in com.here.sdk.maploader">OfflineStorageSizeCallback</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when MapDownloader.getOfflineMapsStorageSizeInBytes(OfflineStorageSizeCallback) has been completed.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmaprepairerror" title="enum class in com.here.sdk.maploader">PersistentMapRepairError</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab3">

  <div class="block">

  Specifies possible errors that may result after a map repair operation has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab3">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab3">

  <div class="block">

  Specifies possible statuses of the already downloaded map regions as a whole.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-region" title="class in com.here.sdk.maploader">Region</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab2">

  <div class="block">

  Defines an area, especially part of a country or the world that can be downloaded.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Specify a unique identifier for Region.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-repairpersistentmapcallback" title="interface in com.here.sdk.maploader">RepairPersistentMapCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when MapDownloader.repairPersistentMap(com.here.sdk.maploader.RepairPersistentMapCallback) has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-sdkcache" title="class in com.here.sdk.maploader">SDKCache</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  A class to manage SDK Cache.

  </div>

  </div>

  <div class="col-first even-row-color class-summary class-summary-tab1">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-sdkcachecallback" title="interface in com.here.sdk.maploader">SDKCacheCallback</a>

  </div>

  <div class="col-last even-row-color class-summary class-summary-tab1">

  <div class="block">

  A method which is called on the main thread when SDKCache.clearCache(com.here.sdk.maploader.SDKCacheCallback) has been completed.

  </div>

  </div>

  <div class="col-first odd-row-color class-summary class-summary-tab2">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-updatestatistics" title="class in com.here.sdk.maploader">UpdateStatistics</a>

  </div>

  <div class="col-last odd-row-color class-summary class-summary-tab2">

  <div class="block">

  Defines statistics related to the success or failure of patched bundles.

  </div>

  </div>

  </div>

  </div>

