---
title: "RoadUsages Structure Reference"
slug: "sdk-for-ios-explore-structs-roadusages"
---

# RoadUsages

<div class="declaration">

<div class="language">

``` highlight
public struct RoadUsages : Hashable
```

</div>

</div>

Road Usages of the segment.

***Note*** a road can have more than one attribute at the same time.

**Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10RoadUsagesV6isRampSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isRamp" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadusages#sdk-for-ios-explore-s-7heresdk10RoadUsagesV6isRampSbvp" class="token"><code>isRamp</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Range is a ramp: connects roads that do not intersect at grade. Ramp allows explication of maneuvers involving ramps (e.g., “Take the ramp”) and for route guidance when determining if sign text should be used.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isRamp: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10RoadUsagesV18isControlledAccessSbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isControlledAccess" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadusages#sdk-for-ios-explore-s-7heresdk10RoadUsagesV18isControlledAccessSbvp" class="token"><code>isControlledAccess</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Controlled access roads are roads with limited entrances and exits that allow uninterrupted high-speed traffic flow. For example, the Interstate/Freeway network in the United States or the Motorway network in Europe. Controlled Access can be used for map display, avoidance of freeway/motorway, publishing speed limits, and route guidance timing.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isControlledAccess: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10RoadUsagesV9isTollwaySbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isTollway" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadusages#sdk-for-ios-explore-s-7heresdk10RoadUsagesV9isTollwaySbvp" class="token"><code>isTollway</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Identifies a road for which a fee must be paid to use the road. Tollway may be used for map display (e.g., different rendering of toll roads) and routing. Tollway is flagged on roads that require a fee for traversal.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isTollway: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10RoadUsagesV010isPriorityB0Sbvp"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Property-isPriorityRoad" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadusages#sdk-for-ios-explore-s-7heresdk10RoadUsagesV010isPriorityB0Sbvp" class="token"><code>isPriorityRoad</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Indicates road stretches that have signs indicating priority on the road. On these roads all traffic has priority over the traffic on the incoming roads.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var isPriorityRoad: Bool
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-explore-s-7heresdk10RoadUsagesV6isRamp0D16ControlledAccess0D7Tollway0d8PriorityB0ACSb_S3btcfc"></span> <span id="sdk-for-ios-explore-apple_ref-swift-Method-init-isRamp-isControlledAccess-isTollway-isPriorityRoad" class="dashAnchor"></span> <a href="sdk-for-ios-explore-structs-roadusages#sdk-for-ios-explore-s-7heresdk10RoadUsagesV6isRamp0D16ControlledAccess0D7Tollway0d8PriorityB0ACSb_S3btcfc" class="token"><code>init(isRamp:</code><wbr></wbr><code>isControlledAccess:</code><wbr></wbr><code>isTollway:</code><wbr></wbr><code>isPriorityRoad:</code><wbr></wbr><code>)</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Creates a new instance with default values.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public init(isRamp: Bool = false, isControlledAccess: Bool = false, isTollway: Bool = false, isPriorityRoad: Bool = false)
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

