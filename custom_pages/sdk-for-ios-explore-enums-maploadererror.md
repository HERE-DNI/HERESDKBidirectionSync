---
title: "MapLoaderError Enumeration Reference"
slug: "sdk-for-ios-explore-enums-maploadererror"
---

# MapLoaderError

<div class="declaration">

<div class="language">

``` highlight
public enum MapLoaderError : UInt32, CaseIterable, Codable
```

``` highlight
extension MapLoaderError : Error
```

</div>

</div>

Specifies possible errors that may result from map downloading/prefetching.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO16resourceNotFoundyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-resourceNotFound" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO16resourceNotFoundyA2CmF" class="token"><code>resourceNotFound</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The requested resource is not found.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case resourceNotFound = 1
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO8notReadyyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-notReady" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO8notReadyyA2CmF" class="token"><code>notReady</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  There’s a problem with an ongoing download or update: If an operation is in a paused state, you can resume or cancel it. If no operation is in a paused state: Either wait for active downloads to finish, or cancel existing `sdk.maploader.MapDownloader` requests and call `sdk.maploader.MapDownloader.get_initial_persistent_map_status`. If there is a problem, call `sdk.maploader.MapDownloader.repair_persistent_map` to repair before continuing with other `sdk.maploader.MapDownloader` operations. This error may occur when an on-going or paused operation prevents the requested task.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case notReady
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO15invalidArgumentyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-invalidArgument" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO15invalidArgumentyA2CmF" class="token"><code>invalidArgument</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The request passed invalid arguments.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidArgument
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO18operationCancelledyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-operationCancelled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO18operationCancelledyA2CmF" class="token"><code>operationCancelled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The request was cancelled (usually by the user).

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operationCancelled
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO16alreadyInstalledyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-alreadyInstalled" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO16alreadyInstalledyA2CmF" class="token"><code>alreadyInstalled</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All tiles of requested regions were already installed, no need for any download.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case alreadyInstalled
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO7timeOutyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-timeOut" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO7timeOutyA2CmF" class="token"><code>timeOut</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The request exceeded the timeout limit.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case timeOut
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO18serviceUnavailableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-serviceUnavailable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO18serviceUnavailableyA2CmF" class="token"><code>serviceUnavailable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The requested service is unavailable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serviceUnavailable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO12accessDeniedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-accessDenied" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO12accessDeniedyA2CmF" class="token"><code>accessDenied</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The access is denied due to invalid credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case accessDenied
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO19requestLimitReachedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-requestLimitReached" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO19requestLimitReachedyA2CmF" class="token"><code>requestLimitReached</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Request limit reached for set a credentials for a particular period of time.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case requestLimitReached
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO017networkConnectionD0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-networkConnectionError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO017networkConnectionD0yA2CmF" class="token"><code>networkConnectionError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A network connection error has happened.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case networkConnectionError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO9forbiddenyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-forbidden" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO9forbiddenyA2CmF" class="token"><code>forbidden</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The operation is forbidden, make sure your credentials grant the necessary permissions.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case forbidden
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO07mapDataD0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-mapDataError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO07mapDataD0yA2CmF" class="token"><code>mapDataError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Downloaded map data is invalid or a `sdk.maploader.RegionId` passed to the method `sdk.maploader.MapDownloader.delete_regions` is incorrect.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mapDataError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO24unexpectedServerResponseyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-unexpectedServerResponse" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO24unexpectedServerResponseyA2CmF" class="token"><code>unexpectedServerResponse</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Received unexpected response from the backend. It means the response is malformed or server returned an internal error. Try repeating the request.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unexpectedServerResponse
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO010mapManagerD0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-mapManagerError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO010mapManagerD0yA2CmF" class="token"><code>mapManagerError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Error occurred inside the map manager and might be related to network issues. Try repeating the request.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mapManagerError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO14incompleteDatayA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-incompleteData" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO14incompleteDatayA2CmF" class="token"><code>incompleteData</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The data to process is incomplete, failed decoding the tile.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case incompleteData
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-serviceAccessFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO19serviceAccessFailedyA2CmF" class="token"><code>serviceAccessFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The conditions to access the service are not satisfied. Check if correct `sdk.maploader.RegionId` was passed to `sdk.maploader.MapDownloader.download_regions` or download for passed `sdk.maploader.RegionId` already started. Further control for started download must be performed through `sdk.maploader.MapDownloaderTask`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case serviceAccessFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO08internalD0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-internalError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO08internalD0yA2CmF" class="token"><code>internalError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Internal error occurred.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case internalError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO7offlineyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-offline" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO7offlineyA2CmF" class="token"><code>offline</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Online operation is not permitted because offline mode is enabled.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case offline
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO07cacheIoD0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-cacheIoError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO07cacheIoD0yA2CmF" class="token"><code>cacheIoError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A cache IO error occurred.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case cacheIoError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO23protectedCacheCorruptedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-protectedCacheCorrupted" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO23protectedCacheCorruptedyA2CmF" class="token"><code>protectedCacheCorrupted</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Protected cache is corrupted. It can be a result of downloading the map in the background and the OS killing the application at that time. Use method `sdk.maploader.MapDownloader.get_initial_persistent_map_status` to get the status of the map and method repair_persistent_map in the MapDownloader to try to fix the cache if it is broken.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case protectedCacheCorrupted
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO17migrationRequiredyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-migrationRequired" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO17migrationRequiredyA2CmF" class="token"><code>migrationRequired</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Operation on the protected cache cannot be done due to required migration. Call `sdk.maploader.MapDownloader.repair_persistent_map` to perform migration.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case migrationRequired
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO21operationAfterDisposeyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-operationAfterDispose" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO21operationAfterDisposeyA2CmF" class="token"><code>operationAfterDispose</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Method is invoked on object connected to the disposed SDKNativeEngine.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case operationAfterDispose
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO020catalogConfigurationD0yA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-catalogConfigurationError" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO020catalogConfigurationD0yA2CmF" class="token"><code>catalogConfigurationError</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Misconfiguration of catalogs. This error may occur when `sdk.core.engine.CatalogConfiguration` is misconfigured and cannot be used for any operation with <a href="sdk-for-ios-explore-classes-mapdownloader">`MapDownloader`</a> or <a href="sdk-for-ios-explore-classes-mapupdater">`MapUpdater`</a>. Verify <a href="sdk-for-ios-explore-structs-sdkoptions#sdk-for-ios-explore-s-7heresdk10SDKOptionsV21catalogConfigurationsSayAA20CatalogConfigurationVGvp">`SDKOptions.catalogConfigurations`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case catalogConfigurationError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO13pendingUpdateyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-pendingUpdate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO13pendingUpdateyA2CmF" class="token"><code>pendingUpdate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Map regions update was interrupted. Indicates that the cache state is wrong after an update that was finished not in correct way (e.g sudden app shutdown). Prefetching or removing of map regions are blocked until the update has been completed successfully.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case pendingUpdate
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO29updateBlockedAsAnotherPendingyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-updateBlockedAsAnotherPending" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO29updateBlockedAsAnotherPendingyA2CmF" class="token"><code>updateBlockedAsAnotherPending</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Catalog update cannot proceed as another catalog update is in PENDING_UPDATE state. Update the catalog in PENDING_UPDATE state first, before trying to update another catalog.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case updateBlockedAsAnotherPending
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO12brokenUpdateyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-brokenUpdate" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO12brokenUpdateyA2CmF" class="token"><code>brokenUpdate</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unrecoverable error during construction of pending update parameters. Operations such as catalog updates or region downloads will fail. The healing procedure is to clean persistent map with `sdk.maploader.MapDownloader.clear_persistent_map_storage`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case brokenUpdate
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO15parallelRequestyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-parallelRequest" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO15parallelRequestyA2CmF" class="token"><code>parallelRequest</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parallel request is already running and conflicting with the current one (e.g updating map and deleting map regions)

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case parallelRequest
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO25proxyAuthenticationFailedyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-proxyAuthenticationFailed" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO25proxyAuthenticationFailedyA2CmF" class="token"><code>proxyAuthenticationFailed</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy is not authenticated. Check your proxy credentials.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case proxyAuthenticationFailed
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO22proxyServerUnreachableyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-proxyServerUnreachable" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO22proxyServerUnreachableyA2CmF" class="token"><code>proxyServerUnreachable</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Proxy server unreachable.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case proxyServerUnreachable
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-notEnoughSpace" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO14notEnoughSpaceyA2CmF" class="token"><code>notEnoughSpace</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  There’s no sufficient space on the disk to finish operation. For offline maps operation (download or update), it means that there’s not enough space on the device. For prefetch operations, it means that there’s not enough space in the mutable cache to store the prefetched data.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case notEnoughSpace
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO18onlineNavigateOnlyyA2CmF"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Element-onlineNavigateOnly" class="dashAnchor"></span> <a href="sdk-for-ios-explore-enums-maploadererror#sdk-for-ios-explore-s-7heresdk14MapLoaderErrorO18onlineNavigateOnlyyA2CmF" class="token"><code>onlineNavigateOnly</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  This version of HERE SDK does not support the ability to download maps. Contact the sales team to get access to the full version.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case onlineNavigateOnly
  ```

  </div>

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

