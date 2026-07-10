---
title: "MapUpdater (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-maploader-mapupdater"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-maploader-package-summary">com.here.sdk.maploader</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.maploader.MapUpdater → com.here.NativeBase com.here.sdk.maploader.MapUpdater → com.here.sdk.maploader.MapUpdater

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapUpdater</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

A class for updating regions previously downloaded using the MapDownloader . First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback) to check for available updates for any downloaded regions. If updates are available, regions can be updated asynchronously using updateCatalog(com.here.sdk.maploader.CatalogUpdateInfo, com.here.sdk.maploader.CatalogUpdateProgressListener) . The MapUpdateProgressListener provides update progress for each region. Incremental map updates are supported, by default: Instead of downloading an entire region, only the parts that have changed will be installed. This results in a faster update process. MapUpdater also aligns previously downloaded content with LayerConfiguration changes made via SDKOptions . Note that patching (also called "incremental updates") is only supported for up to 8 versions. For example, if an update started with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9. Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead. In case of an error, the previous map data remains available for use. It is only replaced after new map data has been successfully downloaded. Regions that fail to update must be retried in a new call. Paused updates can be resumed later. During the update process, MapUpdater internally retries failed downloads until a timeout occurs. If this happens, it is reported via MapUpdateProgressListener . If the user cancels the update process during the update phase, it is ignored. The update phase begins after all content has been downloaded, then the HERE SDK installs and replaces the existing regions. Cancellation is only possible during the download phase, and a successful cancellation is indicated via MapUpdateProgressListener.onComplete(com.here.sdk.maploader.MapLoaderError) . Note that a MapLoaderError.NOT_READY occurs when the MapDownloader is used in parallel. In general, background updates are not supported explicitly, as the OS can abort background processes. In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is in progress and it will be indicated by a MapLoaderError .

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" class="type-name-link" title="enum class in com.here.sdk.maploader"><code>MapUpdater.MapUpdateVersionCommitPolicy</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely.

  </div>

  </div>

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromEngineAsync ( SDKNativeEngine sdkEngine, MapUpdaterConstructionCallback mapUpdaterConstructionCallback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Gets a single instance of this class per provided SDKNativeEngine .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapversionhandle" title="class in com.here.sdk.maploader">`MapVersionHandle`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCurrentMapVersion ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a handle that contains the map version of the already downloaded and installed regions.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `long`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTaskCount ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the number of concurrent tasks for downloading a map.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-updatestatistics" title="class in com.here.sdk.maploader">`UpdateStatistics`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getUpdateStatistics ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Map update statistics for the ongoing session of the current application.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">`TaskHandle`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      retrieveCatalogsUpdateInfo ( CatalogsUpdateInfoCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Retrieves information of all catalogs that have newer version available.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setTaskCount (long value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the number of concurrent tasks for downloading a map.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVersionCommitPolicy ( MapUpdater.MapUpdateVersionCommitPolicy versionCommitPolicy)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the map update version policy.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatetask" title="class in com.here.sdk.maploader">`CatalogUpdateTask`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      updateCatalog ( CatalogUpdateInfo catalogInfo, CatalogUpdateProgressListener callback)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request for each catalog to update map data to the latest available version.

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

  - <div id="sdk-for-android-navigate-fromEngineAsync-com-here-sdk-core-engine-SDKNativeEngine-com-here-sdk-maploader-MapUpdaterConstructionCallback" class="section detail">

    ### fromEngineAsync

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type">void</span> <span class="element-name">fromEngineAsync</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-engine-sdknativeengine" title="class in com.here.sdk.core.engine">SDKNativeEngine</a> sdkEngine, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdaterconstructioncallback" title="interface in com.here.sdk.maploader">MapUpdaterConstructionCallback</a> mapUpdaterConstructionCallback)</span>

    </div>

    <div class="block">

    Gets a single instance of this class per provided SDKNativeEngine .

    </div>

    Parameters:  
    `sdkEngine` -

    An instance of the SDKNativeEngine

    `mapUpdaterConstructionCallback` -

    A callback that will receive the result of construction

    </div>

  - <div id="sdk-for-android-navigate-getCurrentMapVersion" class="section detail">

    ### getCurrentMapVersion

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-mapversionhandle" title="class in com.here.sdk.maploader">MapVersionHandle</a></span> <span class="element-name">getCurrentMapVersion</span>() throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">MapLoaderException</a></span>

    </div>

    <div class="block">

    Returns a handle that contains the map version of the already downloaded and installed regions. This information is only needed for debugging purposes.

    </div>

    Returns:  
    A handle to get the map version.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-maploader-maploaderexception" title="class in com.here.sdk.maploader">`MapLoaderException`</a> -

    Specifies reason, why current map version is not returned.

    </div>

  - <div id="sdk-for-android-navigate-updateCatalog-com-here-sdk-maploader-CatalogUpdateInfo-com-here-sdk-maploader-CatalogUpdateProgressListener" class="section detail">

    ### updateCatalog

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdatetask" title="class in com.here.sdk.maploader">CatalogUpdateTask</a></span> <span class="element-name">updateCatalog</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateinfo" title="class in com.here.sdk.maploader">CatalogUpdateInfo</a> catalogInfo, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogupdateprogresslistener" title="interface in com.here.sdk.maploader">CatalogUpdateProgressListener</a> callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request for each catalog to update map data to the latest available version. This applies to all previously installed Region map data and any incomplete downloads in a pending state. If no regions are downloaded, this method updates only the map version. The map cache and persisted regions are always bound to the same map version. If no updates are available, CatalogsUpdateInfoCallback from retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback) returns an empty list. In this case, MapUpdateProgressListener.onComplete(com.here.sdk.maploader.MapLoaderError) is called immediately. To check for available updates, use retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback) to retrieve catalogs with newer versions. Individual catalogs can then be updated using this method. Ensure that the device has enough free disk space to perform a catalog update. Information about the required disk space is available in CatalogUpdateInfo.diskSizeInBytes . If there is not enough space to perform the catalog update with the default MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE , try using MapUpdater.MapUpdateVersionCommitPolicy.ON_FIRST_REGION . This option requires less space but follows a different strategy for handling errors during the map update. If indexing is enabled through OfflineSearchEngine.setIndexOptions , the index is rebuilt after the map is updated. The index helps OfflineSearchEngine provide better search results. Note: Indexing is a beta feature and may have bugs or unexpected behavior.

    </div>

    Parameters:  
    `catalogInfo` -

    catalog to update. CatalogUpdateInfo should be get from [](sdk-for-android-navigate-com-here-sdk-maploader-mapupdater#retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback))

        retrieveCatalogsUpdateInfo(com.here.sdk.maploader.CatalogsUpdateInfoCallback)

    </a>

    </p>

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.

    </div>

  - <div id="sdk-for-android-navigate-retrieveCatalogsUpdateInfo-com-here-sdk-maploader-CatalogsUpdateInfoCallback" class="section detail">

    ### retrieveCatalogsUpdateInfo

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-threading-taskhandle" title="interface in com.here.sdk.core.threading">TaskHandle</a></span> <span class="element-name">retrieveCatalogsUpdateInfo</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-catalogsupdateinfocallback" title="interface in com.here.sdk.maploader">CatalogsUpdateInfoCallback</a> callback)</span>

    </div>

    <div class="block">

    Retrieves information of all catalogs that have newer version available. This method can also be used to query catalog information like HRN, current installed version and newer available version on server. An empty list in CatalogsUpdateInfoCallback represent no map updates.

    </div>

    Parameters:  
    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    A handle to cancel a pending operation.

    </div>

  - <div id="sdk-for-android-navigate-setVersionCommitPolicy-com-here-sdk-maploader-MapUpdater-MapUpdateVersionCommitPolicy" class="section detail">

    ### setVersionCommitPolicy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVersionCommitPolicy</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">MapUpdater.MapUpdateVersionCommitPolicy</a> versionCommitPolicy)</span>

    </div>

    <div class="block">

    Sets the map update version policy. Defaults to MapUpdater.MapUpdateVersionCommitPolicy.ON_COMPLETE .

    </div>

    Parameters:  
    `versionCommitPolicy` -

    to choose from <a href="sdk-for-android-navigate-com-here-sdk-maploader-mapupdater-mapupdateversioncommitpolicy" title="enum class in com.here.sdk.maploader">`MapUpdater.MapUpdateVersionCommitPolicy`</a>

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

  - <div id="sdk-for-android-navigate-getUpdateStatistics" class="section detail">

    ### getUpdateStatistics

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-maploader-updatestatistics" title="class in com.here.sdk.maploader">UpdateStatistics</a></span> <span class="element-name">getUpdateStatistics</span>()

    </div>

    <div class="block">

    Map update statistics for the ongoing session of the current application. In the event of binary updates, patches are downloaded and applied. This property helps to determine the success or failure rate of applied patches.

    </div>

    Returns:  
    Map update statistics for the current application session.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

