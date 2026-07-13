---
title: "maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-maploader-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maploader-library.html -->
<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="" data-below-sidebar="maploader/maploader-library-sidebar.html">

<div>

# <span class="kind-library">maploader</span> library

</div>

## Classes

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a></span>  
Holds information for the catalog update intent.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class">CatalogUpdateProgressListener</a></span>  
Abstract class to get notified on status updates when updating catalog, previously downloaded by <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatetask-class">CatalogUpdateTask</a></span>  
A class to control the catalog update process.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a></span>  
Abstract class to get notified on status updates when downloading map regions.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedcatalog-class">InstalledCatalog</a></span>  
Represents installed catalog.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregion-class">InstalledRegion</a></span>  
Represents a region, from persistent map storage.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a></span>  
A class for downloading and managing map data for various regions worldwide.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a></span>  
A class to control map download process.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class">MapUpdateProgressListener</a></span>  
Abstract class to get notified on status updates when updating map data, previously downloaded by <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdater-class">MapUpdater</a></span>  
A class for updating regions previously downloaded using the <a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatetask-class">MapUpdateTask</a></span>  
A class to control the map update process.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapversionhandle-class">MapVersionHandle</a></span>  
Represents version of the map.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-region-class">Region</a></span>  
Defines an area, especially part of a country or the world that can be downloaded.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>  
Specify a unique identifier for Region.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcache-class">SDKCache</a></span>  
A class to manage SDK Cache.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-updatestatistics-class">UpdateStatistics</a></span>  
Defines statistics related to the success or failure of patched bundles.

## Enums

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogupdatestate">CatalogUpdateState</a></span>  
Represents the state of catalog map updates.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-installedregionstatus">InstalledRegionStatus</a></span>  
Represents download status of region in the persistent map storage.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a></span>  
Specifies possible errors that may result from map downloading/prefetching.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy">MapUpdaterMapUpdateVersionCommitPolicy</a></span>  
Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-navigabilitytype">NavigabilityType</a></span>  
Represents the navigability level of a map region.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a></span>  
Specifies possible errors that may result after a map repair operation has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span>  
Specifies possible statuses of the already downloaded map regions as a whole.

## Typedefs

<span class="name"><a href="sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback">CatalogsUpdateInfoCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span><span id="sdk-for-flutter-navigate-param-catalogs" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-catalogupdateinfo-class">CatalogUpdateInfo</a></span>\></span>?</span> <span class="parameter-name">catalogs</span></span>)</span></span> </span>  
This method will be called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo">MapUpdater.retrieveCatalogsUpdateInfo</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-deletedregionscallback">DeletedRegionsCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-maploaderError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">maploaderError</span>, </span><span id="sdk-for-flutter-navigate-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span>?</span> <span class="parameter-name">regions</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions">MapDownloader.deleteRegions</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-maploaderError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">maploaderError</span>, </span><span id="sdk-for-flutter-navigate-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-region-class">Region</a></span>\></span>?</span> <span class="parameter-name">regions</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">MapDownloader.getDownloadableRegionsWithLanguageCode</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback">MapDownloaderConstructionCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-mapDownloader" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-class">MapDownloader</a></span> <span class="parameter-name">mapDownloader</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">MapDownloader.fromSdkEngineAsync</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback">MapUpdaterConstructionCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-mapUpdater" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapupdater-class">MapUpdater</a></span> <span class="parameter-name">mapUpdater</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync">MapUpdater.fromSdkEngineAsync</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-offlinestoragesizecallback">OfflineStorageSizeCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span><span id="sdk-for-flutter-navigate-param-size" class="parameter"><span class="type-annotation">int?</span> <span class="parameter-name">size</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync">MapDownloader.getOfflineMapsStorageSizeInBytesAsync</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-repairpersistentmapcallback">RepairPersistentMapCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-persistentMapRepairError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-persistentmaprepairerror">PersistentMapRepairError</a>?</span> <span class="parameter-name">persistentMapRepairError</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap">MapDownloader.repairPersistentMap</a> has been completed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a></span><span class="signature"> <span class="returntype parameter">= void Function<span class="signature">(<span id="sdk-for-flutter-navigate-param-maploaderError" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">maploaderError</span></span>)</span></span> </span>  
A method which is called on the main thread when <a href="sdk-for-flutter-navigate-maploader-sdkcache-clearappcache">SDKCache.clearAppCache</a> has been completed.

## Exceptions / Errors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class">MapLoaderExceptionException</a></span>  
Error occurred during map operation.

</div>

<!-- /.main-content --> <!--/sidebar-offcanvas-right--> <span class="no-break"> here_sdk 4.26.0 </span>

</div>
`
}</HTMLBlock>
