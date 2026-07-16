---
title: "CatalogUpdateInfo Structure Reference"
slug: "sdk-for-ios-explore-structs-catalogupdateinfo"
---

# CatalogUpdateInfo

<div class="declaration">

<div class="language">

``` highlight
public struct CatalogUpdateInfo : Hashable
```

</div>

</div>

Holds information for the catalog update intent. Provides information regarding installed catalog and its latest available version.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV09installedB0AA09InstalledB0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-installedCatalog" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV09installedB0AA09InstalledB0Vvp" class="token"><code>installedCatalog</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Installed catalog.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var installedCatalog: InstalledCatalog
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-installedcatalog">InstalledCatalog</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV13latestVersions5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-latestVersion" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV13latestVersions5Int64Vvp" class="token"><code>latestVersion</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Latest version available for a catalog.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var latestVersion: Int64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV5stateAA0bC5StateOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-state" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV5stateAA0bC5StateOvp" class="token"><code>state</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  State of current catalog update.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var state: CatalogUpdateState
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-catalogupdatestate">CatalogUpdateState</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV18networkSizeInBytess5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-networkSizeInBytes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV18networkSizeInBytess5Int64Vvp" class="token"><code>networkSizeInBytes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Total size in bytes that needs to be downloaded over the network to update the installed catalog.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var networkSizeInBytes: Int64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV15diskSizeInBytess5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-diskSizeInBytes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV15diskSizeInBytess5Int64Vvp" class="token"><code>diskSizeInBytes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Estimates the size of the offline maps after an update. **Note** In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with `disk_size_in_bytes + temporary_disk_requirement_in_bytes`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var diskSizeInBytes: Int64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV31temporaryDiskRequirementInBytess5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-temporaryDiskRequirementInBytes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-catalogupdateinfo#sdk-for-ios-explore-s-7heresdk17CatalogUpdateInfoV31temporaryDiskRequirementInBytess5Int64Vvp" class="token"><code>temporaryDiskRequirementInBytes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Performing an update requires additional storage on top of existing offline maps. This space is used to store intermittent copy of map content according to the specified <a href="sdk-for-ios-explore-classes-mapupdater-mapupdateversioncommitpolicy">`MapUpdater.MapUpdateVersionCommitPolicy`</a>. **Note** In order to estimate, if catalog update is feasible, given the amount of free space on the disk, application can compare amount of the free space on the disk with `disk_size_in_bytes + temporary_disk_requirement_in_bytes`.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var temporaryDiskRequirementInBytes: Int64
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

