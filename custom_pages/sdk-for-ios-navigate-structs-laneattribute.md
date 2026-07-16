---
title: "LaneAttribute Structure Reference"
slug: "sdk-for-ios-navigate-structs-laneattribute"
---

# LaneAttribute

<div class="declaration">

<div class="language">

``` highlight
public struct LaneAttribute : Hashable
```

</div>

</div>

A struct that describes attributes assigned to a specific section of a lane. It includes lane markings, allowed travel directions, tolling info, access restrictions, and optional lane type.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13LaneAttributeV19startOffsetInMeterss5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-startOffsetInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-laneattribute#sdk-for-ios-navigate-s-7heresdk13LaneAttributeV19startOffsetInMeterss5Int32Vvp" class="token"><code>startOffsetInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The start offset of the lane in meters from the beginning of the segment

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var startOffsetInMeters: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13LaneAttributeV8markingsAA0B8MarkingsVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-markings" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-laneattribute#sdk-for-ios-navigate-s-7heresdk13LaneAttributeV8markingsAA0B8MarkingsVvp" class="token"><code>markings</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicate the markings on the road

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var markings: LaneMarkings
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lanemarkings">LaneMarkings</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13LaneAttributeV6accessAA0B6AccessVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-access" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-laneattribute#sdk-for-ios-navigate-s-7heresdk13LaneAttributeV6accessAA0B6AccessVvp" class="token"><code>access</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Access characteristics of the lane that identifies the vehicle type(s) allowed to access a lane.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var access: LaneAccess
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-laneaccess">LaneAccess</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13LaneAttributeV14tollStructuresSayAA13TollStructureVGvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-tollStructures" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-laneattribute#sdk-for-ios-navigate-s-7heresdk13LaneAttributeV14tollStructuresSayAA13TollStructureVGvp" class="token"><code>tollStructures</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  List of Toll Structure that identifies the presence of physical toll structures or automatic controls on the lane at entry and exit points along a toll road which requires payment (cash, electronic, etc.) or ticket

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var tollStructures: [TollStructure]
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-tollstructure">TollStructure</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13LaneAttributeV4typeAA0B4TypeVSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-laneattribute#sdk-for-ios-navigate-s-7heresdk13LaneAttributeV4typeAA0B4TypeVSgvp" class="token"><code>type</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Specifies the functional and regulatory roles a lane may serve, such as turn, express, HOV, or bike use

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var type: LaneType?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lanetype">LaneType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk13LaneAttributeV19startOffsetInMeters8markings6access14tollStructures4typeACs5Int32V_AA0B8MarkingsVAA0B6AccessVSayAA13TollStructureVGAA0B4TypeVSgtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-startOffsetInMeters-markings-access-tollStructures-type" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-laneattribute#sdk-for-ios-navigate-s-7heresdk13LaneAttributeV19startOffsetInMeters8markings6access14tollStructures4typeACs5Int32V_AA0B8MarkingsVAA0B6AccessVSayAA13TollStructureVGAA0B4TypeVSgtcfc" class="token"><code>init(startOffsetInMeters:</code><wbr></wbr><code>markings:</code><wbr></wbr><code>access:</code><wbr></wbr><code>tollStructures:</code><wbr></wbr><code>type:</code><wbr></wbr><code>)</code></a> 

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
  public init(startOffsetInMeters: Int32, markings: LaneMarkings, access: LaneAccess, tollStructures: [TollStructure], type: LaneType? = nil)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-lanemarkings">LaneMarkings</a>
  - <a href="sdk-for-ios-navigate-structs-laneaccess">LaneAccess</a>
  - <a href="sdk-for-ios-navigate-structs-tollstructure">TollStructure</a>
  - <a href="sdk-for-ios-navigate-structs-lanetype">LaneType</a>

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

