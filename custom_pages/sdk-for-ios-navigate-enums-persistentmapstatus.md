---
title: "PersistentMapStatus Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-persistentmapstatus"
---

# PersistentMapStatus

<div class="declaration">

<div class="language">

``` highlight
public enum PersistentMapStatus : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies possible statuses of the already downloaded map regions as a whole. Note: This can be valid only for a single region in case of a <a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF">`PersistentMapStatus.corrupted`</a> state.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO2okyA2CmF"></span>` `<span id="//apple_ref/swift/Element/ok" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO2okyA2CmF" class="token"><code>ok</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All downloaded regions are in a workable state, no issues found.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case ok
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/corrupted" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO9corruptedyA2CmF" class="token"><code>corrupted</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  One or more downloaded regions failed to open and a repair action should be performed to mitigate this issue. All map download and map update operations (except for `sdk.maploader.MapDownloader.repair_persistent_map`) will return `sdk.maploader.MapLoaderError.NOT_READY`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case corrupted
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO12brokenUpdateyA2CmF"></span>` `<span id="//apple_ref/swift/Element/brokenUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO12brokenUpdateyA2CmF" class="token"><code>brokenUpdate</code></a>` `

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

  ` `<span id="/s:7heresdk19PersistentMapStatusO15migrationNeededyA2CmF"></span>` `<span id="//apple_ref/swift/Element/migrationNeeded" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO15migrationNeededyA2CmF" class="token"><code>migrationNeeded</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates that the downloaded regions need to be migrated to a new internal format by calling `sdk.maploader.MapDownloader.repair_persistent_map`. This error is not a result of a data loss, nor any data will be lost when performing the repair operation and the map version will stay unchanged afterwards.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case migrationNeeded
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO13pendingUpdateyA2CmF"></span>` `<span id="//apple_ref/swift/Element/pendingUpdate" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO13pendingUpdateyA2CmF" class="token"><code>pendingUpdate</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  A map update operation initiated by a user has been interrupted. Calls to `sdk.maploader.MapDownloader.download_regions` and `sdk.maploader.MapDownloader.delete_regions` will fail with `sdk.maploader.MapLoaderError.INTERNAL_ERROR`. To repair a map, call again `sdk.maploader.MapUpdater.update_catalog` for the affected catalog. `sdk.maploader.MapUpdater.retrieve_catalogs_update_info` returns a list of `sdk.maploader.CatalogUpdateInfo` items: The affected catalog can be identified by the state, which is set to `sdk.maploader.CatalogUpdateState.PENDING_UPDATE`. To know if a map needs to be repaired, check if `sdk.maploader.MapLoaderError.PENDING_UPDATE` has occurred.

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

  ` `<span id="/s:7heresdk19PersistentMapStatusO11invalidPathyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidPath" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO11invalidPathyA2CmF" class="token"><code>invalidPath</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unreachable <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV9cachePathSSvp">`SDKOptions.cachePath`</a> or <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>. Make sure that <a href="sdk-for-ios-navigate-structs-sdkoptions">`SDKOptions`</a> has accessible <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV9cachePathSSvp">`SDKOptions.cachePath`</a> and <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a>

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidPath
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO12invalidStateyA2CmF"></span>` `<span id="//apple_ref/swift/Element/invalidState" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO12invalidStateyA2CmF" class="token"><code>invalidState</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unrecoverable error during construction of internal map access object. The healing procedure is to clean persistent map with `sdk.maploader.MapDownloader.clear_persistent_map_storage`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidState
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk19PersistentMapStatusO13storageClosedyA2CmF"></span>` `<span id="//apple_ref/swift/Element/storageClosed" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-enums-persistentmapstatus#/s:7heresdk19PersistentMapStatusO13storageClosedyA2CmF" class="token"><code>storageClosed</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates that the status cannot be retrieved as the map storage is already closed due to disposal of <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case storageClosed
  ```

  </div>

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

