---
title: "MapDownloader Class Reference"
slug: "sdk-for-ios-navigate-classes-mapdownloader"
---

# MapDownloader

<div class="declaration">

<div class="language">

``` highlight
public class MapDownloader
```

``` highlight
extension MapDownloader: NativeBase
```

``` highlight
extension MapDownloader: Hashable
```

</div>

</div>

A class for downloading and managing map data for various regions worldwide. Downloaded map data is permanently stored on disk, enabling maps at all zoom levels, search, routing, and other features without an active data connection. Users can query available regions, download them to disk, or delete them. An instance of this class can be created using

    MapDownloader.fromEngineAsync(...)

.
</p>

The storage path for downloaded maps can be specified via <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>.

To control the type of content included in a map download, use <a href="sdk-for-ios-navigate-structs-layerconfiguration">`LayerConfiguration`</a>. Once applied, it affects both the map cache and offline maps. Satellite-based map schemes are not included in the downloaded region data.

**Note:** During turn-by-turn navigation, while a map download or update is in progress, navigation may not function as expected, and the app may be blocked until the operation is completed. Ensure that all pending map operations are finished before starting navigation. This applies only to `MapDownloader` and <a href="sdk-for-ios-navigate-classes-mapupdater">`MapUpdater`</a>. <a href="sdk-for-ios-navigate-classes-routeprefetcher">`RoutePrefetcher`</a> operations are not affected.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk13MapDownloaderC9taskCounts6UInt32Vvp"></span>` `<span id="//apple_ref/swift/Property/taskCount" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-mapdownloader#/s:7heresdk13MapDownloaderC9taskCounts6UInt32Vvp" class="token"><code>taskCount</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The number of concurrent tasks for downloading a map. A valid task count is between 1 to 64. When the value set is outside the valid range, then it is clamped to a valid range:

  - when passed in value is 0 or less, then task count is set to 1;
  - when passed in value is 65 or more, then task count is set to 64.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var taskCount: UInt32 { get set }
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

      fromEngineAsync(_: _: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets a single instance of this class per provided <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromEngineAsync ( _ sdkEngine : SDKNativeEngine , _ mapDownloaderConstructionCallback : @escaping MapDownloaderConstructionHandle )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>sdkEngine</code></em><code> </code></td>
  <td><div>
  <p>An instance of the SDKNativeEngine</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>mapDownloaderConstructionCallback</code></em><code> </code></td>
  <td><div>
  <p>A callback that will receive the result of construction</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getDownloadableRegions(completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to fetch a list of <a href="sdk-for-ios-navigate-structs-region">`Region`</a> objects for downloading map data in a separate request.

  The default language for <a href="sdk-for-ios-navigate-structs-region#/s:7heresdk6RegionV4nameSSvp">`Region.name`</a> is <a href="sdk-for-ios-navigate-enums-languagecode#/s:7heresdk12LanguageCodeO4enUsyA2CmF">`LanguageCode.enUs`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func getDownloadableRegions ( completion : @escaping CompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

  </div>

  </div>

  </div>

- <div>

      getDownloadableRegions(languageCode: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to fetch a list of <a href="sdk-for-ios-navigate-structs-region">`Region`</a> objects with <a href="sdk-for-ios-navigate-structs-region#/s:7heresdk6RegionV4nameSSvp">`Region.name`</a> in given

      MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler).languageCode

  , that can be used to download the actual map data in a separate request.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func getDownloadableRegions ( languageCode : LanguageCode , completion : @escaping CompletionHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>languageCode</code></em><code> </code></td>
  <td><div>
  <p>The language code determines the language of <a href="sdk-for-ios-navigate-structs-region#/s:7heresdk6RegionV4nameSSvp"><code>Region.name</code></a>.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

  </div>

  </div>

  </div>

- <div>

      downloadRegions(regions: statusListener: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to download map data for regions specified by a list of <a href="sdk-for-ios-navigate-structs-regionid">`RegionId`</a> instances.

      MapDownloader.downloadRegions(...).statusListener

  receives notifications until
      onDownloadRegionsComplete(...)

  is called. The returned <a href="sdk-for-ios-navigate-classes-mapdownloadertask">`MapDownloaderTask`</a> can be used to pause or resume the download using
      MapDownloaderTask.pause(Bool)

  or
      MapDownloaderTask.resume(...)

  .
  </p>

  To cancel the request, call

      MapDownloaderTask.cancel(...)

  on the returned <a href="sdk-for-ios-navigate-classes-mapdownloadertask">`MapDownloaderTask`</a> object. After cancellation,
      onDownloadRegionsComplete(...)

  is called with the error <a href="sdk-for-ios-navigate-enums-maploadererror#/s:7heresdk14MapLoaderErrorO18operationCancelledyA2CmF">`MapLoaderError.operationCancelled`</a>.
  </p>

  <a href="sdk-for-ios-navigate-classes-mapdownloadertask">`MapDownloaderTask`</a> remains operational until

      onDownloadRegionsComplete(...)

  is called.
  </p>

  To get list of downloadable regions use

      MapDownloader.getDownloadableRegions(LanguageCode, CompletionHandler)

  API.
  </p>

  Simultaneous downloads of the same region are not supported. If this occurs,

      onDownloadRegionsComplete(...)

  is called with <a href="sdk-for-ios-navigate-enums-maploadererror#/s:7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF">`MapLoaderError.serviceAccessFailed`</a> for the new request, while the previous one continues uninterrupted.
  </p>

  If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then after the requested regions have been downloaded, the corresponding index will be created. The index is used by <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

  To control list of map content features for region download, use <a href="sdk-for-ios-navigate-structs-layerconfiguration#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.

  \
  Note: If an application is forcefully closed or crashes during a map download operation, then this method can be called again to resume the download. For example, if a download was interrupted at 60%, then the next call to download the same region will load the remaining 40%.\
  Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected region three times before giving up. A connection will be timed out after one minute.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  @discardableResult public func downloadRegions ( regions : [ RegionId ], statusListener : DownloadRegionsStatusListener ) -> MapDownloaderTask
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

  </div>

  </div>

  </div>

- <div>

      downloadArea(area: statusListener: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request to download map data for area specified by a GeoPolygon.

      MapDownloader.downloadArea(...).statusListener

  is receiving notifications until
      onDownloadRegionsComplete(...)

  is called. Returned <a href="sdk-for-ios-navigate-classes-mapdownloadertask">`MapDownloaderTask`</a> should be used to pause or resume started download, by invoking
      MapDownloaderTask.pause(Bool)

  or
      MapDownloaderTask.resume(...)

  . Request can be cancelled by calling
      MapDownloaderTask.cancel(...)

  on returned <a href="sdk-for-ios-navigate-classes-mapdownloadertask">`MapDownloaderTask`</a> object, afterwards
      onDownloadRegionsComplete(...)

  is called with error <a href="sdk-for-ios-navigate-enums-maploadererror#/s:7heresdk14MapLoaderErrorO18operationCancelledyA2CmF">`MapLoaderError.operationCancelled`</a>.
  </p>

  <a href="sdk-for-ios-navigate-classes-mapdownloadertask">`MapDownloaderTask`</a> remains operational until

      onDownloadRegionsComplete(...)

  is called.
  </p>

  Downloaded area will be associated to a unique id that will be reported via <a href="sdk-for-ios-navigate-protocols-downloadregionsstatuslistener">`DownloadRegionsStatusListener`</a>.

  Simultaneous download of the same region twice is not supported. When such condition occurs then

      onDownloadRegionsComplete(...)

  is called with error <a href="sdk-for-ios-navigate-enums-maploadererror#/s:7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF">`MapLoaderError.serviceAccessFailed`</a> for a new request, while previous one continues uninterrupted.
  </p>

  If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then after the requested regions have been downloaded, the corresponding index will be created. The index is used by <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

  To control list of map content features for area download, use <a href="sdk-for-ios-navigate-structs-layerconfiguration#/s:7heresdk18LayerConfigurationV15enabledFeaturesSayAC7FeatureOGvp">`LayerConfiguration.enabledFeatures`</a>.

  \
  Note: If an application is forcefully closed or crashes during a map download operation, then this method can be called again to resume the download. For example, if a download was interrupted at 60%, then the next call to download the same region will load the remaining 40%.\
  Note: If a download fails during runtime, then the HERE SDK will automatically retry to download the affected region three times before giving up. A connection will be timed out after one minute.\
  Note: If user try to re-download same GeoPolygon the status will be reported as per the state of previous download operation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func downloadArea ( area : GeoPolygon , statusListener : DownloadRegionsStatusListener ) -> MapDownloaderTask
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

  </div>

  </div>

  </div>

- <div>

      deleteRegions(regions: completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous operation to delete map data for regions specified by a list of <a href="sdk-for-ios-navigate-structs-regionid">`RegionId`</a>. Note: Deleting a region when there is a pending download returns error <a href="sdk-for-ios-navigate-enums-maploadererror#/s:7heresdk14MapLoaderErrorO08internalD0yA2CmF">`MapLoaderError.internalError`</a>. Also, deleting a region when there is an ongoing download returns error <a href="sdk-for-ios-navigate-enums-maploadererror#/s:7heresdk14MapLoaderErrorO15parallelRequestyA2CmF">`MapLoaderError.parallelRequest`</a>.

  If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then after the requested regions have been deleted, the index over remaining regions will be rebuilt, so that entries related to deleted regions are removed. The index is used by <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func deleteRegions ( regions : [ RegionId ], completion : @escaping DeleteRegionsCompletionHandler )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>regions</code></em><code> </code></td>
  <td><div>
  <p>List of regions to be deleted.</p>
  </div></td>
  </tr>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result of deletion on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      clearPersistentMapStorage(completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous operation to clear the persistent map storage from all data. All downloaded regions will be removed. Note: Must be called only when no other region operation is ongoing. Returns an error if there is any active operation.

  Any previously built index will also be deleted. See

      MapDownloader.downloadRegions(...)

  to learn more about index.
  </p>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func clearPersistentMapStorage ( completion : @escaping CacheCallbackCompletionHandler )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result of clearing on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getInstalledRegions()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Method to get a list of map regions that are currently installed on the device. Throws if it’s not possible to return list of installed regions. Returned list contains:

  - successfully downloaded regions, indicated by <a href="sdk-for-ios-navigate-enums-installedregionstatus#/s:7heresdk21InstalledRegionStatusO9installedyA2CmF">`InstalledRegionStatus.installed`</a> in <a href="sdk-for-ios-navigate-structs-installedregion#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">`InstalledRegion.status`</a>;
  - regions, that are in the download process, indicated by <a href="sdk-for-ios-navigate-enums-installedregionstatus#/s:7heresdk21InstalledRegionStatusO7pendingyA2CmF">`InstalledRegionStatus.pending`</a> in <a href="sdk-for-ios-navigate-structs-installedregion#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">`InstalledRegion.status`</a>;
  - regions, which were failed to be downloaded, indicated by <a href="sdk-for-ios-navigate-enums-installedregionstatus#/s:7heresdk21InstalledRegionStatusO7pendingyA2CmF">`InstalledRegionStatus.pending`</a> in <a href="sdk-for-ios-navigate-structs-installedregion#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">`InstalledRegion.status`</a>. Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is set to the <a href="sdk-for-ios-navigate-enums-installedregionstatus#/s:7heresdk21InstalledRegionStatusO7pendingyA2CmF">`InstalledRegionStatus.pending`</a> in <a href="sdk-for-ios-navigate-structs-installedregion#/s:7heresdk15InstalledRegionV6statusAA0bC6StatusOvp">`InstalledRegion.status`</a>. Precise Japan content is available as an additional offering, please contact sales team for more information.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-maploader#/s:7heresdk18MapLoaderExceptiona">`MapLoaderException`</a> Specifies reason, why list of installed regions is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getInstalledRegions () throws -> [ InstalledRegion ]
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  List of IDs of regions that are installed on the device

  </div>

  </div>

  </div>

- <div>

      getInitialPersistentMapStatus()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets the initial status of the already downloaded regions at start-up time of the app. It is not recommended to download or to upload map data while an app is running in background. However, it can happen, that an app gets shut down during an ongoing operation, for example, due to a crash. In such a case, some or all of the downloaded map data may be in a corrupted state. Refer to the <a href="sdk-for-ios-navigate-enums-persistentmapstatus">`PersistentMapStatus`</a> for exact healing procedure for specific status. Note: This value will not change during the lifetime of an app.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getInitialPersistentMapStatus () -> PersistentMapStatus
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Initial status of the persistent map.

  </div>

  </div>

  </div>

- <div>

      repairPersistentMap(completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Tries to repair already downloaded regions that are in a corrupted state (see

      MapDownloader.getInitialPersistentMapStatus(...)

  ).
  </p>

  If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, then index will be rebuilt if existing index does not match with the installed map regions after this operation. The index is used by <a href="sdk-for-ios-navigate-classes-offlinesearchengine">`OfflineSearchEngine`</a> to find better results. Note: Indexing is a beta feature, so there could be a few bugs and unexpected behaviors.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func repairPersistentMap ( completion : @escaping RepairCompletionHandler )
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>A callback which receives the result of the repair operation on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

- <div>

      getOfflineMapsStorageSizeInBytes()

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>. This includes also data that is currently being downloaded.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-navigate-maploader#/s:7heresdk18MapLoaderExceptiona">`MapLoaderException`</a> Specifies reason, why current map size is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getOfflineMapsStorageSizeInBytes () throws -> UInt64
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Return Value

  Value of offline map size.

  </div>

  </div>

  </div>

- <div>

      getOfflineMapsStorageSizeInBytes(completion: )

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Get the total size of all downloaded regions currently persisted on disk at the location that is specified via <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>. This includes also data that is currently being downloaded.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getOfflineMapsStorageSizeInBytes ( completion : @escaping OfflineStorageSizeHandler ) -> TaskHandle
  ```

  </pre>

  </div>

  </div>

  <div>

  #### Parameters

  <table class="graybox">
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <tbody>
  <tr>
  <td><code> </code><em><code>completion</code></em><code> </code></td>
  <td><div>
  <p>A callback which receives the value of offline map size or error on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  Handle that will be used to manipulate the execution of the task, for example, to cancel on ongoing request.

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

