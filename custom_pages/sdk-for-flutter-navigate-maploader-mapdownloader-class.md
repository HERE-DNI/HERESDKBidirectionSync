---
title: "MapDownloader class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/MapDownloader-class-sidebar.html">

<div>

# <span class="kind-class">MapDownloader</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

A class for downloading and managing map data for various regions worldwide.

Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using <a href="sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">MapDownloader.fromSdkEngineAsync</a>.

The storage path for downloaded maps can be specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.

To control the type of content included in a map download, use `LayerConfiguration`. Once applied, it affects both the map cache and offline maps. Satellite-based map schemes are not included in the downloaded region data.

**Note:** During turn-by-turn navigation, while a map download or update is in progress, navigation may not function as expected, and the app may be blocked until the operation is completed. Ensure that all pending map operations are finished before starting navigation. This applies only to `MapDownloader` and `MapUpdater`. `RoutePrefetcher` operations are not affected.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-mapdownloader">MapDownloader</a></span><span class="signature">()</span>  

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-taskcount">taskCount</a></span> <span class="signature">↔ int</span>  
The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:

<div class="features">

<span class="feature">getter/setter pair</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-clearpersistentmapstorage">clearPersistentMapStorage</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-clearPersistentMapStorage-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-sdkcachecallback">SDKCacheCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Performs an asynchronous operation to clear the persistent map storage from all data.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-deleteregions">deleteRegions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-deleteRegions-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span></span> <span class="parameter-name">regions</span>, </span><span id="sdk-for-flutter-navigate-deleteRegions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-deletedregionscallback">DeletedRegionsCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-downloadarea">downloadArea</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-downloadArea-param-area" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-geopolygon-class">GeoPolygon</a></span> <span class="parameter-name">area</span>, </span><span id="sdk-for-flutter-navigate-downloadArea-param-statusListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a></span> <span class="parameter-name">statusListener</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a></span> </span>  
Performs an asynchronous request to download map data for area specified by a GeoPolygon.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-downloadregions">downloadRegions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-downloadRegions-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span></span> <span class="parameter-name">regions</span>, </span><span id="sdk-for-flutter-navigate-downloadRegions-param-statusListener" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class">DownloadRegionsStatusListener</a></span> <span class="parameter-name">statusListener</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-maploader-mapdownloadertask-class">MapDownloaderTask</a></span> </span>  
Performs an asynchronous request to download map data for regions specified by a list of <a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a> instances.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregions">getDownloadableRegions</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDownloadableRegions-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to fetch a list of <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> objects for downloading map data in a separate request.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getdownloadableregionswithlanguagecode">getDownloadableRegionsWithLanguageCode</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getDownloadableRegionsWithLanguageCode-param-languageCode" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-languagecode">LanguageCode</a></span> <span class="parameter-name">languageCode</span>, </span><span id="sdk-for-flutter-navigate-getDownloadableRegionsWithLanguageCode-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-downloadableregionscallback">DownloadableRegionsCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Performs an asynchronous request to fetch a list of <a href="sdk-for-flutter-navigate-maploader-region-class">Region</a> objects with <a href="sdk-for-flutter-navigate-maploader-region-name">Region.name</a> in given `MapDownloader.getDownloadableRegionsWithLanguageCode.languageCode`, that can be used to download the actual map data in a separate request.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus">getInitialPersistentMapStatus</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-maploader-persistentmapstatus">PersistentMapStatus</a></span> </span>  
Gets the initial status of the already downloaded regions at start-up time of the app.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinstalledregions">getInstalledRegions</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-installedregion-class">InstalledRegion</a></span>\></span></span> </span>  
Method to get a list of map regions that are currently installed on the device.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytes">getOfflineMapsStorageSizeInBytes</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ int</span> </span>  
Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-getofflinemapsstoragesizeinbytesasync">getOfflineMapsStorageSizeInBytesAsync</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-getOfflineMapsStorageSizeInBytesAsync-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-offlinestoragesizecallback">OfflineStorageSizeCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ <a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a></span> </span>  
Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="sdk-for-flutter-navigate-core-engine-sdkoptions-persistentmapstoragepath">SDKOptions.persistentMapStoragePath</a>.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-repairpersistentmap">repairPersistentMap</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-repairPersistentMap-param-callback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-repairpersistentmapcallback">RepairPersistentMapCallback</a></span> <span class="parameter-name">callback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Tries to repair already downloaded regions that are in a corrupted state (see <a href="sdk-for-flutter-navigate-maploader-mapdownloader-getinitialpersistentmapstatus">MapDownloader.getInitialPersistentMapStatus</a>).

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

## Static Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-mapdownloader-fromsdkengineasync">fromSdkEngineAsync</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-fromSdkEngineAsync-param-sdkEngine" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a></span> <span class="parameter-name">sdkEngine</span>, </span><span id="sdk-for-flutter-navigate-fromSdkEngineAsync-param-mapDownloaderConstructionCallback" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-mapdownloaderconstructioncallback">MapDownloaderConstructionCallback</a></span> <span class="parameter-name">mapDownloaderConstructionCallback</span></span>) <span class="returntype parameter">→ void</span> </span>  
Gets a single instance of this class per provided <a href="sdk-for-flutter-navigate-core-engine-sdknativeengine-class">SDKNativeEngine</a>.

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>

