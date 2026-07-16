---
title: "ElectronicHorizonUpdate Structure Reference"
slug: "sdk-for-ios-navigate-structs-electronichorizonupdate"
---

# ElectronicHorizonUpdate

<div class="declaration">

<div class="language">

``` highlight
public struct ElectronicHorizonUpdate : Hashable
```

</div>

</div>

A struct representing a full update delivered via <a href="sdk-for-ios-navigate-protocols-electronichorizondelegate">`ElectronicHorizonDelegate`</a> notifications.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV010electronicC0AA0bC0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-electronicHorizon" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-electronichorizonupdate#sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV010electronicC0AA0bC0VSgvp" class="token"><code>electronicHorizon</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The full electronic horizon recomputed for the current vehicle state. May be `nil` if there is no update.

  Contains the complete set of preferred paths.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var electronicHorizon: ElectronicHorizon?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-electronichorizon">ElectronicHorizon</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV14segmentChangesAA0bc7SegmentF0VSgvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-segmentChanges" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-electronichorizonupdate#sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV14segmentChangesAA0bc7SegmentF0VSgvp" class="token"><code>segmentChanges</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The difference between the previously emitted horizon and the newly computed one. Contains added and removed segments. May be `nil` if there is no update.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var segmentChanges: ElectronicHorizonSegmentChanges?
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV8positionAA0bC8PositionVvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-position" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-electronichorizonupdate#sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV8positionAA0bC8PositionVvp" class="token"><code>position</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The vehicle’s updated position relative to the electronic horizon. Always present. If no `electronic_horizon` is available, the position refers to the most recently known horizon.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var position: ElectronicHorizonPosition
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-electronichorizonposition">ElectronicHorizonPosition</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV010electronicC014segmentChanges8positionAcA0bC0VSg_AA0bc7SegmentG0VSgAA0bC8PositionVtcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-electronicHorizon-segmentChanges-position" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-electronichorizonupdate#sdk-for-ios-navigate-s-7heresdk23ElectronicHorizonUpdateV010electronicC014segmentChanges8positionAcA0bC0VSg_AA0bc7SegmentG0VSgAA0bC8PositionVtcfc" class="token"><code>init(electronicHorizon:</code><wbr></wbr><code>segmentChanges:</code><wbr></wbr><code>position:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance.

  Offline availability: This property is available online and offline.

  - Parameters

    - electronicHorizon: The full electronic horizon recomputed for the current vehicle state. May be `nil` if there is no update.

    Contains the complete set of preferred paths.

    - segmentChanges: The difference between the previously emitted horizon and the newly computed one. Contains added and removed segments. May be `nil` if there is no update.
    - position: The vehicle’s updated position relative to the electronic horizon. Always present. If no `electronic_horizon` is available, the position refers to the most recently known horizon.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(electronicHorizon: ElectronicHorizon? = nil, segmentChanges: ElectronicHorizonSegmentChanges? = nil, position: ElectronicHorizonPosition)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-structs-electronichorizon">ElectronicHorizon</a>
  - <a href="sdk-for-ios-navigate-structs-electronichorizonsegmentchanges">ElectronicHorizonSegmentChanges</a>
  - <a href="sdk-for-ios-navigate-structs-electronichorizonposition">ElectronicHorizonPosition</a>

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

