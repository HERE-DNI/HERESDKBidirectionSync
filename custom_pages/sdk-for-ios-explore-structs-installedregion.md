---
title: "InstalledRegion Structure Reference"
slug: "sdk-for-ios-explore-structs-installedregion"
---

# InstalledRegion

<div class="declaration">

<div class="language">

``` highlight
public struct InstalledRegion : Hashable
```

</div>

</div>

Represents a region, from persistent map storage.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15InstalledRegionV8regionIdAA0cE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-regionId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-installedregion#sdk-for-ios-explore-s-7heresdk15InstalledRegionV8regionIdAA0cE0Vvp" class="token"><code>regionId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier specifying a region.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var regionId: RegionId
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15InstalledRegionV8parentIdAA0cE0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-parentId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-installedregion#sdk-for-ios-explore-s-7heresdk15InstalledRegionV8parentIdAA0cE0Vvp" class="token"><code>parentId</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Parent region identifier. Continents have a parent_id of 0.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var parentId: RegionId
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15InstalledRegionV17sizeOnDiskInBytess5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sizeOnDiskInBytes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-installedregion#sdk-for-ios-explore-s-7heresdk15InstalledRegionV17sizeOnDiskInBytess5Int64Vvp" class="token"><code>sizeOnDiskInBytes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Region size on disk in bytes.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sizeOnDiskInBytes: Int64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15InstalledRegionV6statusAA0bC6StatusOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-status" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-installedregion#sdk-for-ios-explore-s-7heresdk15InstalledRegionV6statusAA0bC6StatusOvp" class="token"><code>status</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Status of the region in the persistent map storage.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var status: InstalledRegionStatus
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-installedregionstatus">InstalledRegionStatus</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15InstalledRegionV14lastUpdateTime10Foundation4DateVSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-lastUpdateTime" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-installedregion#sdk-for-ios-explore-s-7heresdk15InstalledRegionV14lastUpdateTime10Foundation4DateVSgvp" class="token"><code>lastUpdateTime</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The last update time of the region in the persistent map storage.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var lastUpdateTime: Date?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk15InstalledRegionV8regionId06parentE017sizeOnDiskInBytes6status14lastUpdateTimeAcA0cE0V_AJs5Int64VAA0bC6StatusO10Foundation4DateVSgtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-regionId-parentId-sizeOnDiskInBytes-status-lastUpdateTime" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-installedregion#sdk-for-ios-explore-s-7heresdk15InstalledRegionV8regionId06parentE017sizeOnDiskInBytes6status14lastUpdateTimeAcA0cE0V_AJs5Int64VAA0bC6StatusO10Foundation4DateVSgtcfc" class="token"><code>init(regionId:</code><wbr></wbr><code>parentId:</code><wbr></wbr><code>sizeOnDiskInBytes:</code><wbr></wbr><code>status:</code><wbr></wbr><code>lastUpdateTime:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(regionId: RegionId, parentId: RegionId, sizeOnDiskInBytes: Int64, status: InstalledRegionStatus, lastUpdateTime: Date? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>
  - <a href="sdk-for-ios-explore-enums-installedregionstatus">InstalledRegionStatus</a>

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

