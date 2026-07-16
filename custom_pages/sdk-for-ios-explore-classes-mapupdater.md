---
title: "MapUpdater Class Reference"
slug: "sdk-for-ios-explore-classes-mapupdater"
---

# MapUpdater

<div class="declaration">

<div class="language">

``` highlight
public class MapUpdater
```

``` highlight
extension MapUpdater: NativeBase
```

``` highlight
extension MapUpdater: Hashable
```

</div>

</div>

A class for updating regions previously downloaded using the <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a>. First, updates for the regions are downloaded. Once the download is complete, the update process begins, installing the new content. It is recommended to regularly call <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">`MapUpdater.retrieveCatalogsUpdateInfo(...)`</a> to check for available updates for any downloaded regions.

If updates are available, regions can be updated asynchronously using <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF">`MapUpdater.updateCatalog(...)`</a>. The <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">`MapUpdateProgressListener`</a> provides update progress for each region.

Incremental map updates are supported, by default: Instead of downloading an entire region, only the parts that have changed will be installed. This results in a faster update process. MapUpdater also aligns previously downloaded content with <a href="sdk-for-ios-explore-structs-layerconfiguration">`LayerConfiguration`</a> changes made via <a href="sdk-for-ios-explore-structs-sdkoptions">`SDKOptions`</a>.

Note that patching (also called “incremental updates”) is only supported for up to 8 versions. For example, if an update started with version x.y.0 then it will be supported till x.y.8 and stopped starting with x.y.9. Usually, OCM updates are released weekly. Incremental updates will stop after 2 months and a full update is performed instead.

In case of an error, the previous map data remains available for use. It is only replaced after new map data has been successfully downloaded. Regions that fail to update must be retried in a new call. Paused updates can be resumed later.

During the update process, `MapUpdater` internally retries failed downloads until a timeout occurs. If this happens, it is reported via <a href="sdk-for-ios-explore-protocols-mapupdateprogresslistener">`MapUpdateProgressListener`</a>.

If the user cancels the update process during the update phase, it is ignored. The update phase begins after all content has been downloaded, then the HERE SDK installs and replaces the existing regions. Cancellation is only possible during the download phase, and a successful cancellation is indicated via

    onComplete(...)

.
</p>

Note that a <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO8notReadyyA2CmF">`MapLoaderError.notReady`</a> occurs when the <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> is used in parallel. In general, background updates are not supported explicitly, as the OS can abort background processes. In addition, the OfflineSearchEngine and the OfflineRoutingEngine cannot be used while a map update is in progress and it will be indicated by a <a href="sdk-for-ios-explore-enums-maploadererror">`MapLoaderError`</a>.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC9taskCounts6UInt32Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-taskCount" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC9taskCounts6UInt32Vvp" class="token"><code>taskCount</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC16updateStatisticsAA06UpdateE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-updateStatistics" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC16updateStatisticsAA06UpdateE0Vvp" class="token"><code>updateStatistics</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map update statistics for the current application session. In the event of binary updates, patches are downloaded and applied. This property helps to determine the success or failure rate of applied patches.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var updateStatistics: UpdateStatistics { get }
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-updatestatistics">UpdateStatistics</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Enum-MapUpdateVersionCommitPolicy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO" class="token"><code>MapUpdateVersionCommitPolicy</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Defines if installed regions and subregions are updated one-by-one or if all regions are updated only once the updates for all installed regions have been downloaded entirely. This influences the required size of the storage during an update. Regardless of the set policy, during an update, the previous region data is kept until the new region data is committed successfully to the persisted storage. This allows to revert to the previous version in case the update fails. With <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onComplete`</a>, more data has to be kept until the update process finishes, while <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion`</a> allows to make faster use of the downloaded region and requires less disk space as only the currently updated region is kept until the process completes. However, with an <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion`</a> policy the overall process can be less reliable and bears a higher risk of errors.

  <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy" class="slightly-smaller">See more</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public enum MapUpdateVersionCommitPolicy : UInt32, CaseIterable, Codable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-fromEngineAsync-_-_" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC15fromEngineAsyncyyAA09SDKNativeE0C_yACctFZ" class="token"><code>fromEngineAsync(_:</code><wbr></wbr><code>_:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Gets a single instance of this class per provided <a href="sdk-for-ios-explore-classes-sdknativeengine">`SDKNativeEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public static func fromEngineAsync(_ sdkEngine: SDKNativeEngine, _ mapUpdaterConstructionCallback: @escaping MapUpdaterConstructionHandler)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-sdknativeengine">SDKNativeEngine</a>
  - <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk29MapUpdaterConstructionHandlera">MapUpdaterConstructionHandler</a>

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
  <td><code> </code><em><code>mapUpdaterConstructionCallback</code></em><code> </code></td>
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

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC010getCurrentB7VersionAA0bF6HandleCyKF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-getCurrentMapVersion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC010getCurrentB7VersionAA0bF6HandleCyKF" class="token"><code>getCurrentMapVersion()</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Returns a handle that contains the map version of the already downloaded and installed regions. This information is only needed for debugging purposes.

  <div class="aside aside-throws">

  Throws

  <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk18MapLoaderExceptiona">`MapLoaderException`</a> Specifies reason, why current map version is not returned.

  </div>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func getCurrentMapVersion() throws -> MapVersionHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapversionhandle">MapVersionHandle</a>

  </div>

  <div>

  #### Return Value

  A handle to get the map version.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-updateCatalog-catalogInfo-completion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC13updateCatalog11catalogInfo10completionAA0E10UpdateTaskCAA0eiG0V_AA0eI16ProgressListener_ptF" class="token"><code>updateCatalog(catalogInfo:</code><wbr></wbr><code>completion:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performs an asynchronous request for each catalog to update map data to the latest available version. This applies to all previously installed <a href="sdk-for-ios-explore-structs-region">`Region`</a> map data and any incomplete downloads in a pending state.

  If no regions are downloaded, this method updates only the map version. The map cache and persisted regions are always bound to the same map version.

  If no updates are available, <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk26CatalogsUpdateInfoCallbacka">`CatalogsUpdateInfoCallback`</a> from <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">`MapUpdater.retrieveCatalogsUpdateInfo(...)`</a> returns an empty list. In this case,

      onComplete(...)

  is called immediately.
  </p>

  To check for available updates, use <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF">`MapUpdater.retrieveCatalogsUpdateInfo(...)`</a> to retrieve catalogs with newer versions. Individual catalogs can then be updated using this method. Ensure that the device has enough free disk space to perform a catalog update. Information about the required disk space is available in <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV15diskSizeInBytess5Int64Vvp">`CatalogUpdateInfo.diskSizeInBytes`</a>.

  If there is not enough space to perform the catalog update with the default <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onComplete`</a>, try using <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO13onFirstRegionyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onFirstRegion`</a>. This option requires less space but follows a different strategy for handling errors during the map update.

  If indexing is enabled through `OfflineSearchEngine.setIndexOptions`, the index is rebuilt after the map is updated. The index helps <a href="sdk-for-ios-explore-classes-offlinesearchengine">`OfflineSearchEngine`</a> provide better search results.

  Note: Indexing is a beta feature and may have bugs or unexpected behavior.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func updateCatalog(catalogInfo: CatalogUpdateInfo, completion: CatalogUpdateProgressListener) -> CatalogUpdateTask
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-catalogupdateinfo">CatalogUpdateInfo</a>
  - <a href="sdk-for-ios-explore-protocols-catalogupdateprogresslistener">CatalogUpdateProgressListener</a>
  - <a href="sdk-for-ios-explore-classes-catalogupdatetask">CatalogUpdateTask</a>

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
  <td><code> </code><em><code>catalogInfo</code></em><code> </code></td>
  <td><div>
  <p>catalog to update. CatalogUpdateInfo should be get from <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF"><code>MapUpdater.retrieveCatalogsUpdateInfo(...)</code></a></p>
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

  A handle that will be used to manipulate the execution of the task, for example, to cancel an ongoing request.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-retrieveCatalogsUpdateInfo-callback" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC26retrieveCatalogsUpdateInfo8callbackAA10TaskHandle_pyAA0B11LoaderErrorOSg_SayAA07CatalogfG0VGSgtc_tF" class="token"><code>retrieveCatalogsUpdateInfo(callback:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Retrieves information of all catalogs that have newer version available. This method can also be used to query catalog information like HRN, current installed version and newer available version on server. An empty list in <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk26CatalogsUpdateInfoCallbacka">`CatalogsUpdateInfoCallback`</a> represent no map updates.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func retrieveCatalogsUpdateInfo(callback: @escaping CatalogsUpdateInfoCallback) -> TaskHandle
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-maploader#sdk-for-ios-explore-s-7heresdk26CatalogsUpdateInfoCallbacka">CatalogsUpdateInfoCallback</a>
  - <a href="sdk-for-ios-explore-protocols-taskhandle">TaskHandle</a>

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
  <td><code> </code><em><code>callback</code></em><code> </code></td>
  <td><div>
  <p>Callback which receives the result on the main thread.</p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  <div>

  #### Return Value

  A handle to cancel a pending operation.

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10MapUpdaterC22setVersionCommitPolicy07versionfG0yAC0b6UpdateefG0O_tF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-setVersionCommitPolicy-versionCommitPolicy" class="dashAnchor"></span> <a href="sdk-for-ios-explore-classes-mapupdater#sdk-for-ios-explore-s-7heresdk10MapUpdaterC22setVersionCommitPolicy07versionfG0yAC0b6UpdateefG0O_tF" class="token"><code>setVersionCommitPolicy(versionCommitPolicy:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Sets the map update version policy. Defaults to <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy#sdk-for-ios-explore-s-7heresdk10MapUpdaterC0B25UpdateVersionCommitPolicyO10onCompleteyA2EmF">`MapUpdater.MapUpdateVersionCommitPolicy.onComplete`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public func setVersionCommitPolicy(versionCommitPolicy: MapUpdater.MapUpdateVersionCommitPolicy)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy">MapUpdateVersionCommitPolicy</a>

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
  <td><code> </code><em><code>versionCommitPolicy</code></em><code> </code></td>
  <td><div>
  <p>to choose from <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy"><code>MapUpdater.MapUpdateVersionCommitPolicy</code></a></p>
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

</div>

</div>

<div id="sdk-for-ios-explore-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

