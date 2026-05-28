---
title: "maploader library"
slug: "sdk-for-flutter-navigate-maploader-maploader-library"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- maploader-library.html -->
<div class="doc-with-sidebar"><div class="sidebar-nav"><ol>
<li class="section-title"><a href="maploader/maploader-library.html#classes">Classes</a></li>
<li><a href="maploader/CatalogUpdateInfo-class.html">CatalogUpdateInfo</a></li>
<li><a href="maploader/CatalogUpdateProgressListener-class.html">CatalogUpdateProgressListener</a></li>
<li><a href="maploader/CatalogUpdateTask-class.html">CatalogUpdateTask</a></li>
<li><a href="maploader/DownloadRegionsStatusListener-class.html">DownloadRegionsStatusListener</a></li>
<li><a href="maploader/InstalledCatalog-class.html">InstalledCatalog</a></li>
<li><a href="maploader/InstalledRegion-class.html">InstalledRegion</a></li>
<li><a href="maploader/MapDownloader-class.html">MapDownloader</a></li>
<li><a href="maploader/MapDownloaderTask-class.html">MapDownloaderTask</a></li>
<li><a href="maploader/MapUpdateProgressListener-class.html">MapUpdateProgressListener</a></li>
<li><a href="maploader/MapUpdater-class.html">MapUpdater</a></li>
<li><a href="maploader/MapUpdateTask-class.html">MapUpdateTask</a></li>
<li><a href="maploader/MapVersionHandle-class.html">MapVersionHandle</a></li>
<li><a href="maploader/Region-class.html">Region</a></li>
<li><a href="maploader/RegionId-class.html">RegionId</a></li>
<li><a href="maploader/SDKCache-class.html">SDKCache</a></li>
<li><a href="maploader/UpdateStatistics-class.html">UpdateStatistics</a></li>
<li class="section-title"><a href="maploader/maploader-library.html#enums">Enums</a></li>
<li><a href="maploader/CatalogUpdateState.html">CatalogUpdateState</a></li>
<li><a href="maploader/InstalledRegionStatus.html">InstalledRegionStatus</a></li>
<li><a href="maploader/MapLoaderError.html">MapLoaderError</a></li>
<li><a href="maploader/MapUpdaterMapUpdateVersionCommitPolicy.html">MapUpdaterMapUpdateVersionCommitPolicy</a></li>
<li><a href="maploader/NavigabilityType.html">NavigabilityType</a></li>
<li><a href="maploader/PersistentMapRepairError.html">PersistentMapRepairError</a></li>
<li><a href="maploader/PersistentMapStatus.html">PersistentMapStatus</a></li>
<li class="section-title"><a href="maploader/maploader-library.html#typedefs">Typedefs</a></li>
<li><a href="maploader/CatalogsUpdateInfoCallback.html">CatalogsUpdateInfoCallback</a></li>
<li><a href="maploader/DeletedRegionsCallback.html">DeletedRegionsCallback</a></li>
<li><a href="maploader/DownloadableRegionsCallback.html">DownloadableRegionsCallback</a></li>
<li><a href="maploader/MapDownloaderConstructionCallback.html">MapDownloaderConstructionCallback</a></li>
<li><a href="maploader/MapUpdaterConstructionCallback.html">MapUpdaterConstructionCallback</a></li>
<li><a href="maploader/OfflineStorageSizeCallback.html">OfflineStorageSizeCallback</a></li>
<li><a href="maploader/RepairPersistentMapCallback.html">RepairPersistentMapCallback</a></li>
<li><a href="maploader/SDKCacheCallback.html">SDKCacheCallback</a></li>
<li class="section-title"><a href="maploader/maploader-library.html#exceptions">Exceptions</a></li>
<li><a href="maploader/MapLoaderExceptionException-class.html">MapLoaderExceptionException</a></li>
</ol></div><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">maploader.dart</li>
</ol>
<div class="self-name">maploader</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="" data-below-sidebar="maploader/maploader-library-sidebar.html" id="dartdoc-main-content">
<div>
<h1>maploader library</h1>
</div>
<section class="summary offset-anchor" id="classes">
<h2>Classes</h2>
<dl>
<dt id="CatalogUpdateInfo">
/sdk-for-flutter-navigate-maploader-catalogupdateinfo-class
</dt>
<dd>
  Holds information for the catalog update intent.
</dd>
<dt id="CatalogUpdateProgressListener">
/sdk-for-flutter-navigate-maploader-catalogupdateprogresslistener-class
</dt>
<dd>
  Abstract class to get notified on status updates
when updating catalog, previously downloaded by /sdk-for-flutter-navigate-maploader-mapdownloader-class.
</dd>
<dt id="CatalogUpdateTask">
/sdk-for-flutter-navigate-maploader-catalogupdatetask-class
</dt>
<dd>
  A class to control the catalog update process.
</dd>
<dt id="DownloadRegionsStatusListener">
/sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class
</dt>
<dd>
  Abstract class to get notified on
status updates when downloading map regions.
</dd>
<dt id="InstalledCatalog">
/sdk-for-flutter-navigate-maploader-installedcatalog-class
</dt>
<dd>
  Represents installed catalog.
</dd>
<dt id="InstalledRegion">
/sdk-for-flutter-navigate-maploader-installedregion-class
</dt>
<dd>
  Represents a region, from persistent map storage.
</dd>
<dt id="MapDownloader">
/sdk-for-flutter-navigate-maploader-mapdownloader-class
</dt>
<dd>
  A class for downloading and managing map data for various regions worldwide.
</dd>
<dt id="MapDownloaderTask">
/sdk-for-flutter-navigate-maploader-mapdownloadertask-class
</dt>
<dd>
  A class to control map download process.
</dd>
<dt id="MapUpdateProgressListener">
/sdk-for-flutter-navigate-maploader-mapupdateprogresslistener-class
</dt>
<dd>
  Abstract class to get notified on status updates
when updating map data, previously downloaded by /sdk-for-flutter-navigate-maploader-mapdownloader-class.
</dd>
<dt id="MapUpdater">
/sdk-for-flutter-navigate-maploader-mapupdater-class
</dt>
<dd>
  A class for updating regions previously downloaded using the /sdk-for-flutter-navigate-maploader-mapdownloader-class.
</dd>
<dt id="MapUpdateTask">
/sdk-for-flutter-navigate-maploader-mapupdatetask-class
</dt>
<dd>
  A class to control the map update process.
</dd>
<dt id="MapVersionHandle">
/sdk-for-flutter-navigate-maploader-mapversionhandle-class
</dt>
<dd>
  Represents version of the map.
</dd>
<dt id="Region">
/sdk-for-flutter-navigate-maploader-region-class
</dt>
<dd>
  Defines an area, especially part of a country or the world that can be downloaded.
</dd>
<dt id="RegionId">
/sdk-for-flutter-navigate-maploader-regionid-class
</dt>
<dd>
  Specify a unique identifier for Region.
</dd>
<dt id="SDKCache">
/sdk-for-flutter-navigate-maploader-sdkcache-class
</dt>
<dd>
  A class to manage SDK Cache.
</dd>
<dt id="UpdateStatistics">
/sdk-for-flutter-navigate-maploader-updatestatistics-class
</dt>
<dd>
  Defines statistics related to the success or failure of patched bundles.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="enums">
<h2>Enums</h2>
<dl>
<dt id="CatalogUpdateState">
/sdk-for-flutter-navigate-maploader-catalogupdatestate
</dt>
<dd>
  Represents the state of catalog map updates.
</dd>
<dt id="InstalledRegionStatus">
/sdk-for-flutter-navigate-maploader-installedregionstatus
</dt>
<dd>
  Represents download status of region in the persistent map storage.
</dd>
<dt id="MapLoaderError">
/sdk-for-flutter-navigate-maploader-maploadererror
</dt>
<dd>
  Specifies possible errors that may result from map downloading/prefetching.
</dd>
<dt id="MapUpdaterMapUpdateVersionCommitPolicy">
/sdk-for-flutter-navigate-maploader-mapupdatermapupdateversioncommitpolicy
</dt>
<dd>
  Defines if installed regions and subregions are updated one-by-one or if all regions are
updated only once the updates for all installed regions have been downloaded entirely.
</dd>
<dt id="NavigabilityType">
/sdk-for-flutter-navigate-maploader-navigabilitytype
</dt>
<dd>
  Represents the navigability level of a map region.
</dd>
<dt id="PersistentMapRepairError">
/sdk-for-flutter-navigate-maploader-persistentmaprepairerror
</dt>
<dd>
  Specifies possible errors that may result after a map repair operation has been completed.
</dd>
<dt id="PersistentMapStatus">
/sdk-for-flutter-navigate-maploader-persistentmapstatus
</dt>
<dd>
  Specifies possible statuses of the already downloaded map regions as a whole.
</dd>
</dl>
</section>
<section class="summary offset-anchor" id="typedefs">
<h2>Typedefs</h2>
<dl>
<dt class="callable" id="CatalogsUpdateInfoCallback">
/sdk-for-flutter-navigate-maploader-catalogsupdateinfocallback
= void Function(/sdk-for-flutter-navigate-maploader-maploadererror? error, List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-catalogupdateinfo-class&gt;? catalogs)

</dt>
<dd>
    This method will be called on the main thread when /sdk-for-flutter-navigate-maploader-mapupdater-retrievecatalogsupdateinfo has been completed.
    

  </dd>
<dt class="callable" id="DeletedRegionsCallback">
/sdk-for-flutter-navigate-maploader-deletedregionscallback
= void Function(/sdk-for-flutter-navigate-maploader-maploadererror? maploaderError, List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-regionid-class&gt;? regions)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions has been completed.
    

  </dd>
<dt class="callable" id="DownloadableRegionsCallback">
/sdk-for-flutter-navigate-maploader-downloadableregionscallback
= void Function(/sdk-for-flutter-navigate-maploader-maploadererror? maploaderError, List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-region-class&gt;? regions)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode has been completed.
    

  </dd>
<dt class="callable" id="MapDownloaderConstructionCallback">
/sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback
= void Function(/sdk-for-flutter-navigate-maploader-mapdownloader-class mapDownloader)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync has been completed.
    

  </dd>
<dt class="callable" id="MapUpdaterConstructionCallback">
/sdk-for-flutter-navigate-maploader-mapupdaterconstructioncallback
= void Function(/sdk-for-flutter-navigate-maploader-mapupdater-class mapUpdater)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapupdater-fromsdkengineasync has been completed.
    

  </dd>
<dt class="callable" id="OfflineStorageSizeCallback">
/sdk-for-flutter-navigate-maploader-offlinestoragesizecallback
= void Function(/sdk-for-flutter-navigate-maploader-maploadererror? error, int? size)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync has been completed.
    

  </dd>
<dt class="callable" id="RepairPersistentMapCallback">
/sdk-for-flutter-navigate-maploader-repairpersistentmapcallback
= void Function(/sdk-for-flutter-navigate-maploader-persistentmaprepairerror? persistentMapRepairError)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap has been completed.
    

  </dd>
<dt class="callable" id="SDKCacheCallback">
/sdk-for-flutter-navigate-maploader-sdkcachecallback
= void Function(/sdk-for-flutter-navigate-maploader-maploadererror? maploaderError)

</dt>
<dd>
    A method which is called on the main thread when /sdk-for-flutter-navigate-maploader-sdkcache-clearappcache has been completed.
    

  </dd>
</dl>
</section>
<section class="summary offset-anchor" id="exceptions">
<h2>Exceptions / Errors</h2>
<dl>
<dt id="MapLoaderExceptionException">
/sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class
</dt>
<dd>
  Error occurred during map operation.
</dd>
</dl>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li class="self-crumb">maploader.dart</li>
</ol>
<h5>here_sdk package</h5>
<ol>
<li class="section-title">Libraries</li>
<li>/sdk-for-flutter-navigate-animation-animation-library</li>
<li>/sdk-for-flutter-navigate-core-core-library</li>
<li>/sdk-for-flutter-navigate-core-engine-core-engine-library</li>
<li>/sdk-for-flutter-navigate-core-errors-core-errors-library</li>
<li>/sdk-for-flutter-navigate-core-threading-core-threading-library</li>
<li>/sdk-for-flutter-navigate-electronic-horizon-electronic-horizon-library</li>
<li>/sdk-for-flutter-navigate-ev-ev-library</li>
<li>/sdk-for-flutter-navigate-gestures-gestures-library</li>
<li>/sdk-for-flutter-navigate-location-location-library</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-remote-connection-maploader-remote-connection-library</li>
<li>/sdk-for-flutter-navigate-mapmatcher-mapmatcher-library</li>
<li>/sdk-for-flutter-navigate-mapview-mapview-library</li>
<li>/sdk-for-flutter-navigate-mapview-datasource-mapview-datasource-library</li>
<li>/sdk-for-flutter-navigate-navigation-navigation-library</li>
<li>/sdk-for-flutter-navigate-prefetcher-prefetcher-library</li>
<li>/sdk-for-flutter-navigate-routing-routing-library</li>
<li>/sdk-for-flutter-navigate-search-search-library</li>
<li>/sdk-for-flutter-navigate-traffic-traffic-library</li>
<li>/sdk-for-flutter-navigate-trafficawarenavigation-trafficawarenavigation-library</li>
<li>/sdk-for-flutter-navigate-trafficbroadcast-trafficbroadcast-library</li>
<li>/sdk-for-flutter-navigate-transport-transport-library</li>
<li>/sdk-for-flutter-navigate-venue-venue-library</li>
<li>/sdk-for-flutter-navigate-venue-control-venue-control-library</li>
<li>/sdk-for-flutter-navigate-venue-data-venue-data-library</li>
<li>/sdk-for-flutter-navigate-venue-routing-venue-routing-library</li>
<li>/sdk-for-flutter-navigate-venue-service-venue-service-library</li>
<li>/sdk-for-flutter-navigate-venue-style-venue-style-library</li>
<li>/sdk-for-flutter-navigate-warner-warner-library</li>
</ol>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
<h5>maploader library</h5>
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>
