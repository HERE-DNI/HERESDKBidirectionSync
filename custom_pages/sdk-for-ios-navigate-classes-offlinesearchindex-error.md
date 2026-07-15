---
title: "Error Enumeration Reference"
slug: "sdk-for-ios-navigate-classes-offlinesearchindex-error"
---

# Error

<div class="declaration">

<div class="language">

``` highlight
public enum Error : UInt32, CaseIterable, Codable
```

</div>

</div>

Error corresponding to the offline search operation.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

  ` `<span id="/s:7heresdk18OfflineSearchIndexC5ErrorO21invalidPersistentPathyA2EmF"></span>` `<span id="//apple_ref/swift/Element/invalidPersistentPath" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-offlinesearchindex-error#/s:7heresdk18OfflineSearchIndexC5ErrorO21invalidPersistentPathyA2EmF" class="token"><code>invalidPersistentPath</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unreachable <a href="sdk-for-ios-navigate-structs-sdkoptions#/s:7heresdk10SDKOptionsV24persistentMapStoragePathSSvp">`SDKOptions.persistentMapStoragePath`</a> or lacking required permission to generate index inside.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case invalidPersistentPath
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18OfflineSearchIndexC5ErrorO03mapE0yA2EmF"></span>` `<span id="//apple_ref/swift/Element/mapError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-offlinesearchindex-error#/s:7heresdk18OfflineSearchIndexC5ErrorO03mapE0yA2EmF" class="token"><code>mapError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Failed to get installed regions in protected cache. Any previous available index would be deleted when this error occurs. Use method `MapDownloader.getInitialPersistentMapStatus` to get the status of the map and check `maploader.PersistentMapStatus` for exact healing procedure for specific status.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case mapError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18OfflineSearchIndexC5ErrorO08databaseE0yA2EmF"></span>` `<span id="//apple_ref/swift/Element/databaseError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-offlinesearchindex-error#/s:7heresdk18OfflineSearchIndexC5ErrorO08databaseE0yA2EmF" class="token"><code>databaseError</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unable to generate index due to failed database operation. Any previous available index would be deleted when this error occurs. Call `MapDownloader.repairPersistentMap` to retry index generation.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  case databaseError
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

  ` `<span id="/s:7heresdk18OfflineSearchIndexC5ErrorO18operationCancelledyA2EmF"></span>` `<span id="//apple_ref/swift/Element/operationCancelled" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-offlinesearchindex-error#/s:7heresdk18OfflineSearchIndexC5ErrorO18operationCancelledyA2EmF" class="token"><code>operationCancelled</code></a>` `

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indexing operation cancelled due to OS killing the application or when a new indexing operation is invoked by SDK after finishing a map operation while the previous indexing operation was in progress. Any previous available index would be deleted when this error occurs. In later case, SDK would finish the latest indexing operation successfully and it can be tracked through <a href="sdk-for-ios-navigate-protocols-offlinesearchindexlistener">`OfflineSearchIndexListener`</a>, otherwise call `MapDownloader.repairPersistentMap` to retry index generation.

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

  ` `<span id="/s:7heresdk18OfflineSearchIndexC5ErrorO08internalE0yA2EmF"></span>` `<span id="//apple_ref/swift/Element/internalError" class="dashAnchor"></span>` `<a href="sdk-for-ios-navigate-classes-offlinesearchindex-error#/s:7heresdk18OfflineSearchIndexC5ErrorO08internalE0yA2EmF" class="token"><code>internalError</code></a>` `

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

</div>

</div>

</div>

<div id="sdk-for-ios-navigate-footer" class="section">

© 2026 . All rights reserved. (Last updated: 2026-04-14)

Generated by <a href="https://github.com/realm/jazzy" class="link" rel="external noopener" target="_blank">jazzy ♪♫ v0.15.2</a>, a <a href="https://realm.io" class="link" rel="external noopener" target="_blank">Realm</a> project.

</div>

</article>

