---
title: "MapDownloader (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.maploader.MapDownloader → com.here.NativeBase com.here.sdk.maploader.MapDownloader → com.here.sdk.maploader.MapDownloader

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapDownloader</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

A class for downloading and managing map data for various regions worldwide. Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using fromEngineAsync(com.here.sdk.core.engine.SDKNativeEngine, com.here.sdk.maploader.MapDownloaderConstructionCallback) . The storage path for downloaded maps can be specified via SDKOptions.persistentMapStoragePath . To control the type of content included in a map download, use LayerConfiguration . Once applied, it affects both the map cache and offline maps. Satellite-based map schemes are not included in the downloaded region data. Note: During turn-by-turn navigation, while a map download or update is in progress, navigation may not function as expected, and the app may be blocked until the operation is completed. Ensure that all pending map operations are finished before starting navigation. This applies only to MapDownloader and MapUpdater . RoutePrefetcher operations are not affected.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      clearPersistentMapStorage ( SDKCacheCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous operation to clear the persistent map storage from all data.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      deleteRegions ( List < RegionId > regions, DeletedRegionsCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous operation to delete map data for regions specified by a list of RegionId .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">`MapDownloaderTask`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      downloadArea ( GeoPolygon area, DownloadRegionsStatusListener statusListener)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to download map data for area specified by a GeoPolygon.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">`MapDownloaderTask`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      downloadRegions ( List < RegionId > regions, DownloadRegionsStatusListener statusListener)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to download map data for regions specified by a list of RegionId instances.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromEngineAsync ( SDKNativeEngine sdkEngine, MapDownloaderConstructionCallback mapDownloaderConstructionCallback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets a single instance of this class per provided SDKNativeEngine .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDownloadableRegions ( LanguageCode languageCode, DownloadableRegionsCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to fetch a list of Region objects with Region.name in given languageCode , that can be used to download the actual map data in a separate request.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDownloadableRegions ( DownloadableRegionsCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request to fetch a list of Region objects for downloading map data in a separate request.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">`PersistentMapStatus`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInitialPersistentMapStatus ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the initial status of the already downloaded regions at start-up time of the app.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion" title="class in com.here.sdk.maploader">`InstalledRegion`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getInstalledRegions ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Method to get a list of map regions that are currently installed on the device.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOfflineMapsStorageSizeInBytes ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the total size of all downloaded regions currently persisted on disk at the location that is specified via SDKOptions.persistentMapStoragePath .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOfflineMapsStorageSizeInBytes ( OfflineStorageSizeCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Get the total size of all downloaded regions currently persisted on disk at the location that is specified via SDKOptions.persistentMapStoragePath .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTaskCount ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the number of concurrent tasks for downloading a map.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

      onEnterForeground ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4 method-summary-table-tab6">

  <div class="block">

  Deprecated. Only part of Internal variant.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      repairPersistentMap ( RepairPersistentMapCallback callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Tries to repair already downloaded regions that are in a corrupted state (see getInitialPersistentMapStatus() ).

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTaskCount (long value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the number of concurrent tasks for downloading a map.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-fromEngineAsync-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-maploader-MapDownloaderConstructionCallback" class="section detail">

    ### fromEngineAsync

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fromEngineAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloaderconstructioncallback" title="interface in com.here.sdk.maploader">MapDownloaderConstructionCallback</a> mapDownloaderConstructionCallback)</span>

    </div>

    <div class="block">

    Gets a single instance of this class per provided SDKNativeEngine .

    </div>

    Parameters:  
    `sdkEngine` -

    An instance of the SDKNativeEngine

    `mapDownloaderConstructionCallback` -

    A callback that will receive the result of construction

    </div>

  - <div id="sdk-for-android-navigate-getDownloadableRegions-com-here-sdk-maploader-DownloadableRegionsCallback" class="section detail">

    ### getDownloadableRegions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">getDownloadableRegions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to fetch a list of Region objects for downloading map data in a separate request. The default language for Region.name is LanguageCode.EN_US .

    </div>

    Parameters:  
    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

    </div>

  - <div id="sdk-for-android-navigate-getDownloadableRegions-com-here-sdk-core-LanguageCode-com-here-sdk-maploader-DownloadableRegionsCallback" class="section detail">

    ### getDownloadableRegions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">getDownloadableRegions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-languagecode" title="enum class in com.here.sdk.core">LanguageCode</a> languageCode, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadableregionscallback" title="interface in com.here.sdk.maploader">DownloadableRegionsCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to fetch a list of Region objects with Region.name in given languageCode , that can be used to download the actual map data in a separate request.

    </div>

    Parameters:  
    `languageCode` -

    The language code determines the language of <a href="sdk-for-android-navigate-com-here-sdk-maploader-region#name">`Region.name`</a>.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

    </div>

  - <div id="sdk-for-android-navigate-downloadRegions-java-util-List-com-here-sdk-maploader-DownloadRegionsStatusListener" class="section detail">

    ### downloadRegions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></span> <span class="element-name">downloadRegions</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>\> regions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to download map data for regions specified by a list of RegionId instances. statusListener receives notifications until DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called. The returned MapDownloaderTask can be used to pause or resume the download using MapDownloaderTask.pause(boolean) or MapDownloaderTask.resume() . To cancel the request, call MapDownloaderTask.cancel() on the returned MapDownloaderTask object. After cancellation, DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called with the error MapLoaderError.OPERATION_CANCELLED . MapDownloaderTask remains operational until DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called. To get list of downloadable regions use getDownloadableRegions(LanguageCode, DownloadableRegionsCallback) API. Simultaneous downloads of the same region are not supported. If this occurs, DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called with MapLoaderError.SERVICE_ACCESS_FAILED for the new request, while the previous one continues uninterrupted. If indexing is enabled through OfflineSearchEngine.setIndexOptions , then after the requested regions have been downloaded, the corresponding index will be created. The index is used by OfflineSearchEngine to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors. To control list of map content features for region download, use LayerConfiguration.enabledFeatures . Note: If an application is forcefully closed or crashes during a map download operation, then this method can be called again to resume the download. For example, if a download was interrupted at 60%, then the next call to download the same region will load the remaining 40%. Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected region three times before giving up. A connection will be timed out after one minute.

    </div>

    Parameters:  
    `regions` -

    List of regions to download. Can be fetched using [](sdk-for-android-navigate-com-here-sdk-maploader-mapdownloader#getDownloadableRegions(com.here.sdk.core.LanguageCode,com.here.sdk.maploader.DownloadableRegionsCallback))

        getDownloadableRegions(LanguageCode, DownloadableRegionsCallback)

    </a> API.

    </p>

    `statusListener` -

    Notifies on the download progress.

    Returns:  
    Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

    </div>

  - <div id="sdk-for-android-navigate-downloadArea-com-here-sdk-core-GeoPolygon-com-here-sdk-maploader-DownloadRegionsStatusListener" class="section detail">

    ### downloadArea

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapdownloadertask" title="class in com.here.sdk.maploader">MapDownloaderTask</a></span> <span class="element-name">downloadArea</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> area, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-downloadregionsstatuslistener" title="interface in com.here.sdk.maploader">DownloadRegionsStatusListener</a> statusListener)</span>

    </div>

    <div class="block">

    Performs an asynchronous request to download map data for area specified by a GeoPolygon. statusListener is receiving notifications until DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called. Returned MapDownloaderTask should be used to pause or resume started download, by invoking MapDownloaderTask.pause(boolean) or MapDownloaderTask.resume() . Request can be cancelled by calling MapDownloaderTask.cancel() on returned MapDownloaderTask object, afterwards DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called with error MapLoaderError.OPERATION_CANCELLED . MapDownloaderTask remains operational until DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called. Downloaded area will be associated to a unique id that will be reported via DownloadRegionsStatusListener . Simultaneous download of the same region twice is not supported. When such condition occurs then DownloadRegionsStatusListener.onDownloadRegionsComplete(com.here.sdk.maploader.MapLoaderError, java.util.List\<com.here.sdk.maploader.RegionId\>) is called with error MapLoaderError.SERVICE_ACCESS_FAILED for a new request, while previous one continues uninterrupted. If indexing is enabled through OfflineSearchEngine.setIndexOptions , then after the requested regions have been downloaded, the corresponding index will be created. The index is used by OfflineSearchEngine to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors. To control list of map content features for area download, use LayerConfiguration.enabledFeatures . Note: If an application is forcefully closed or crashes during a map download operation, then this method can be called again to resume the download. For example, if a download was interrupted at 60%, then the next call to download the same region will load the remaining 40%. Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected region three times before giving up. A connection will be timed out after one minute. Note: If user try to re-download same GeoPolygon the status will be reported as per the state of previous download operation.

    </div>

    Parameters:  
    `area` -

    Area to download.

    `statusListener` -

    Notifies on the download progress.

    Returns:  
    Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

    </div>

  - <div id="sdk-for-android-navigate-deleteRegions-java-util-List-com-here-sdk-maploader-DeletedRegionsCallback" class="section detail">

    ### deleteRegions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">deleteRegions</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-regionid" title="class in com.here.sdk.maploader">RegionId</a>\> regions, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-deletedregionscallback" title="interface in com.here.sdk.maploader">DeletedRegionsCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous operation to delete map data for regions specified by a list of RegionId . Note: Deleting a region when there is a pending download returns error MapLoaderError.INTERNAL_ERROR . Also, deleting a region when there is an ongoing download returns error MapLoaderError.PARALLEL_REQUEST . If indexing is enabled through OfflineSearchEngine.setIndexOptions , then after the requested regions have been deleted, the index over remaining regions will be rebuilt, so that entries related to deleted regions are removed. The index is used by OfflineSearchEngine to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

    </div>

    Parameters:  
    `regions` -

    List of regions to be deleted.

    `callback` -

    Callback which receives the result of deletion on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-clearPersistentMapStorage-com-here-sdk-maploader-SDKCacheCallback" class="section detail">

    ### clearPersistentMapStorage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">clearPersistentMapStorage</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-sdkcachecallback" title="interface in com.here.sdk.maploader">SDKCacheCallback</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous operation to clear the persistent map storage from all data. All downloaded regions will be removed. Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation. Any previously built index will also be deleted. See downloadRegions(java.util.List\<com.here.sdk.maploader.RegionId\>, com.here.sdk.maploader.DownloadRegionsStatusListener) to learn more about index.

    </div>

    Parameters:  
    `callback` -

    Callback which receives the result of clearing on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-getInstalledRegions" class="section detail">

    ### getInstalledRegions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-maploader-installedregion" title="class in com.here.sdk.maploader">InstalledRegion</a>\></span> <span class="element-name">getInstalledRegions</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span>

    </div>

    <div class="block">

    Method to get a list of map regions that are currently installed on the device. Throws if it's not possible to return list of installed regions. Returned list contains: successfully downloaded regions, indicated by InstalledRegionStatus.INSTALLED in InstalledRegion.status ; regions, that are in the download process, indicated by InstalledRegionStatus.PENDING in InstalledRegion.status ; regions, which were failed to be downloaded, indicated by InstalledRegionStatus.PENDING in InstalledRegion.status . Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is set to the InstalledRegionStatus.PENDING in InstalledRegion.status . Precise Japan content is available as an additional offering, please contact sales team for more information.

    </div>

    Returns:  
    List of IDs of regions that are installed on the device

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">`MapLoaderException`</a> -

    Specifies reason, why list of installed regions is not returned.

    </div>

  - <div id="sdk-for-android-navigate-getInitialPersistentMapStatus" class="section detail">

    ### getInitialPersistentMapStatus

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-persistentmapstatus" title="enum class in com.here.sdk.maploader">PersistentMapStatus</a></span> <span class="element-name">getInitialPersistentMapStatus</span>()

    </div>

    <div class="block">

    Gets the initial status of the already downloaded regions at start-up time of the app. It is not recommended to download or to upload map data while an app is running in background. However, it can happen, that an app gets shut down during an ongoing operation, for example, due to a crash. In such a case, some or all of the downloaded map data may be in a corrupted state. Refer to the PersistentMapStatus for exact healing procedure for specific status. Note: This value will not change during the lifetime of an app.

    </div>

    Returns:  
    Initial status of the persistent map.

    </div>

  - <div id="sdk-for-android-navigate-repairPersistentMap-com-here-sdk-maploader-RepairPersistentMapCallback" class="section detail">

    ### repairPersistentMap

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">repairPersistentMap</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-repairpersistentmapcallback" title="interface in com.here.sdk.maploader">RepairPersistentMapCallback</a> callback)</span>

    </div>

    <div class="block">

    Tries to repair already downloaded regions that are in a corrupted state (see getInitialPersistentMapStatus() ). If indexing is enabled through OfflineSearchEngine.setIndexOptions , then index will be rebuilt if existing index does not match with the installed map regions after this operation. The index is used by OfflineSearchEngine to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

    </div>

    Parameters:  
    `callback` -

    A callback which receives the result of the repair operation on the main thread.

    </div>

  - <div id="sdk-for-android-navigate-getOfflineMapsStorageSizeInBytes" class="section detail">

    ### getOfflineMapsStorageSizeInBytes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getOfflineMapsStorageSizeInBytes</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span>

    </div>

    <div class="block">

    Get the total size of all downloaded regions currently persisted on disk at the location that is specified via SDKOptions.persistentMapStoragePath . This includes also data that is currently being downloaded.

    </div>

    Returns:  
    Value of offline map size.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">`MapLoaderException`</a> -

    Specifies reason, why current map size is not returned.

    </div>

  - <div id="sdk-for-android-navigate-getOfflineMapsStorageSizeInBytes-com-here-sdk-maploader-OfflineStorageSizeCallback" class="section detail">

    ### getOfflineMapsStorageSizeInBytes

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">getOfflineMapsStorageSizeInBytes</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-offlinestoragesizecallback" title="interface in com.here.sdk.maploader">OfflineStorageSizeCallback</a> callback)</span>

    </div>

    <div class="block">

    Get the total size of all downloaded regions currently persisted on disk at the location that is specified via SDKOptions.persistentMapStoragePath . This includes also data that is currently being downloaded.

    </div>

    Parameters:  
    `callback` -

    A callback which receives the value of offline map size or error on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

    </div>

  - <div id="sdk-for-android-navigate-onEnterForeground" class="section detail">

    ### onEnterForeground

    <div class="member-signature">

    <span class="annotations"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Deprecated.html" class="external-link" title="class or interface in java.lang">@Deprecated</a> </span><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">onEnterForeground</span>()

    </div>

    <div class="deprecation-block">

    <span class="deprecated-label">Deprecated.</span>
    <div class="deprecation-comment">

    Only part of Internal variant. Please use `sdk.maploader.BackgroundMapOperationContext.onEnterForeground` instead.

    </div>

    </div>

    <div class="block">

    To enable background map downloads for iOS, this method must be invoked when the application moves from the foreground to the background, usually triggered when the user switches to another application or when the device's screen is turned off. Please note that this method is only relevant to the iOS platform. Robust handling of online requests finished while in the background depends on the integration with AppDelegate. How to integrate it see sdk.maploader.BackgroundMapOperationContext .

    </div>

    </div>

  - <div id="sdk-for-android-navigate-getTaskCount" class="section detail">

    ### getTaskCount

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getTaskCount</span>()

    </div>

    <div class="block">

    Gets the number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range: when passed in value is 0 or less, then task count is set to 1; when passed in value is 65 or more, then task count is set to 64.

    </div>

    Returns:  
    The number of concurrent tasks for downloading a map.

    </div>

  - <div id="sdk-for-android-navigate-setTaskCount-long" class="section detail">

    ### setTaskCount

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setTaskCount</span><wbr></wbr><span class="parameters">(long value)</span>

    </div>

    <div class="block">

    Sets the number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range: when passed in value is 0 or less, then task count is set to 1; when passed in value is 65 or more, then task count is set to 64.

    </div>

    Parameters:  
    `value` -

    The number of concurrent tasks for downloading a map.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

