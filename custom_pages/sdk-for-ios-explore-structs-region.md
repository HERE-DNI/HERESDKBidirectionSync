---
title: "Region Structure Reference"
slug: "sdk-for-ios-explore-structs-region"
---

# Region

<div class="declaration">

<div class="language">

``` highlight
public struct Region : Hashable
```

</div>

</div>

Defines an area, especially part of a country or the world that can be downloaded.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV8regionIdAA0bD0Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-regionId" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV8regionIdAA0bD0Vvp" class="token"><code>regionId</code></a> 

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

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV4nameSSvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-name" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV4nameSSvp" class="token"><code>name</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Name of region. Language is determined by the requested <a href="sdk-for-ios-explore-enums-languagecode">`LanguageCode`</a>. By default, it is in <a href="sdk-for-ios-explore-enums-languagecode#sdk-for-ios-explore-s-7heresdk12LanguageCodeO4enUsyA2CmF">`LanguageCode.enUs`</a>.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var name: String
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV17sizeOnDiskInBytess5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sizeOnDiskInBytes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV17sizeOnDiskInBytess5Int64Vvp" class="token"><code>sizeOnDiskInBytes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Represents the total size of the region on disk in bytes, assuming no pre-existing data on the disk. This value is a theoretical maximum for the region’s size allocation. Note: If overlapping regions exist or data is already present on the disk, the actual size occupied might be less than this value due to shared or reused map data.

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

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV20sizeOnNetworkInBytess5Int64Vvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-sizeOnNetworkInBytes" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV20sizeOnNetworkInBytess5Int64Vvp" class="token"><code>sizeOnNetworkInBytes</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Region size, for downloading/during network operations, in bytes. Regions are downloaded in compressed form and hence they have reduced size on network. Note: This value represents the theoretical maximum size required for the region during transfer. If overlapping data already exists, the actual size downloaded may be smaller due to map data reuse.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var sizeOnNetworkInBytes: Int64
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV12childRegionsSayACGSgvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-childRegions" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV12childRegionsSayACGSgvp" class="token"><code>childRegions</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  All child regions for current region. Note that each child can again contain multiple children. A downloadable region will contain the content of all children.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var childRegions: [Region]?
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV12navigabilityAA16NavigabilityTypeOvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-navigability" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV12navigabilityAA16NavigabilityTypeOvp" class="token"><code>navigability</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates the navigability type of this region.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var navigability: NavigabilityType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-enums-navigabilitytype">NavigabilityType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk6RegionV8regionId4name17sizeOnDiskInBytes0fg7NetworkiJ012childRegions12navigabilityAcA0bD0V_SSs5Int64VAMSayACGSgAA16NavigabilityTypeOtcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-regionId-name-sizeOnDiskInBytes-sizeOnNetworkInBytes-childRegions-navigability" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-region#sdk-for-ios-explore-s-7heresdk6RegionV8regionId4name17sizeOnDiskInBytes0fg7NetworkiJ012childRegions12navigabilityAcA0bD0V_SSs5Int64VAMSayACGSgAA16NavigabilityTypeOtcfc" class="token"><code>init(regionId:</code><wbr></wbr><code>name:</code><wbr></wbr><code>sizeOnDiskInBytes:</code><wbr></wbr><code>sizeOnNetworkInBytes:</code><wbr></wbr><code>childRegions:</code><wbr></wbr><code>navigability:</code><wbr></wbr><code>)</code></a> 

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
  public init(regionId: RegionId, name: String = "", sizeOnDiskInBytes: Int64 = 0, sizeOnNetworkInBytes: Int64 = 0, childRegions: [Region]? = nil, navigability: NavigabilityType = NavigabilityType.navigable)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-explore-structs-regionid">RegionId</a>
  - <a href="sdk-for-ios-explore-enums-navigabilitytype">NavigabilityType</a>

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

