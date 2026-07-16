---
title: "PersistentMapRepairError Enumeration Reference"
slug: "sdk-for-ios-navigate-enums-persistentmaprepairerror"
---

# PersistentMapRepairError

<div class="declaration">

<div class="language">

``` highlight
public enum PersistentMapRepairError : UInt32, CaseIterable, Codable
```

</div>

</div>

Specifies possible errors that may result after a map repair operation has been completed.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO17partiallyRestoredyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-partiallyRestored" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO17partiallyRestoredyA2CmF" class="token"><code>partiallyRestored</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Persistent map is repaired, but some map data is lost. Lost regions marked with a PENDING status.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case partiallyRestored
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO11invalidPathyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-invalidPath" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO11invalidPathyA2CmF" class="token"><code>invalidPath</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Invalid persistent map path. The provided path to store the persistent map data doesn’t own the required Read/Write (RW) permissions. Try to choose a different path with RW permissions.

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

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO8brokenDbyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-brokenDb" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO8brokenDbyA2CmF" class="token"><code>brokenDb</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The persisted map data can’t be recovered and all map data was fully deleted. It is recommended, to ask the user if they want to try to download the lost regions again.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case brokenDb
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO16noOfflineVersionyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noOfflineVersion" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO16noOfflineVersionyA2CmF" class="token"><code>noOfflineVersion</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The map data version was not cached. The region list data will be cleared from the persisted storage. It is recommended to download the list of downloadable regions again. After this it is recommended to try to repair the corrupted map data again.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noOfflineVersion
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO9noJournalyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-noJournal" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO9noJournalyA2CmF" class="token"><code>noJournal</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  It is not possible to retrieve the list of downloaded regions. The region list data will be cleared from the persisted storage. It is recommended to download the list of downloadable regions again. After this it is recommended to try to repair the corrupted map data again.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case noJournal
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO12brokenUpdateyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-brokenUpdate" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO12brokenUpdateyA2CmF" class="token"><code>brokenUpdate</code></a> 

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

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO21operationAfterDisposeyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-operationAfterDispose" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO21operationAfterDisposeyA2CmF" class="token"><code>operationAfterDispose</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Repair is invoked on object connected to the disposed <a href="sdk-for-ios-navigate-classes-sdknativeengine">`SDKNativeEngine`</a>

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

   <span id="sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO7unknownyA2CmF"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Element-unknown" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-enums-persistentmaprepairerror#sdk-for-ios-navigate-s-7heresdk24PersistentMapRepairErrorO7unknownyA2CmF" class="token"><code>unknown</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  An unknown error occurred. Try to clear the persisted storage by calling `sdk.maploader.MapDownloader.clear_persistent_map_storage`. It is recommended, to ask the user if they want to try to download the lost regions again.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case unknown
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

