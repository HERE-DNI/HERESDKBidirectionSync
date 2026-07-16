---
title: "TrafficMergeWarning Structure Reference"
slug: "sdk-for-ios-navigate-structs-trafficmergewarning"
---

# TrafficMergeWarning

<div class="declaration">

<div class="language">

``` highlight
public struct TrafficMergeWarning : Hashable
```

</div>

</div>

A struct that provides warning for merging traffic. The main field describing the merging traffic is `TrafficMergeWarning.road_type` specifying the type of road containing traffic which is merging with the current road. Use `TrafficMergeWarningListener` to get notifications about upcoming merging traffic.

</div>

<div class="section section task-group-section">

<div class="task-group">

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV2ids5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-id" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV2ids5Int32Vvp" class="token"><code>id</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Unique identifier for this specific traffic merge warning instance. Each warning type (truck restrictions, speed warnings, etc.) maintains its own independent ID namespace. Use this ID to track, update, or dismiss individual warning instances of this type.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var id: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV010distanceTobC8InMetersSdvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-distanceToTrafficMergeInMeters" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV010distanceTobC8InMetersSdvp" class="token"><code>distanceToTrafficMergeInMeters</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Distance to merging traffic in meters.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceToTrafficMergeInMeters: Double
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV8roadTypeAA0bc4RoadF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-roadType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV8roadTypeAA0bc4RoadF0Ovp" class="token"><code>roadType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Type of road which contains the merging traffic.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var roadType: TrafficMergeRoadType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-trafficmergeroadtype">TrafficMergeRoadType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV4sideAA0bC4SideOvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-side" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV4sideAA0bC4SideOvp" class="token"><code>side</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The side from which the traffic is merging.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var side: TrafficMergeSide
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-trafficmergeside">TrafficMergeSide</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV9laneCounts5Int32Vvp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-laneCount" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV9laneCounts5Int32Vvp" class="token"><code>laneCount</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  Number of lanes of the merging road containing the traffic. If the road has no lanes defined, than the number of lanes returned will be 1.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var laneCount: Int32
  ```

  </div>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV12distanceTypeAA08DistanceF0Ovp"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Property-distanceType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV12distanceTypeAA08DistanceF0Ovp" class="token"><code>distanceType</code></a> 

  </div>

  <div class="height-container">

  <div class="pointer-container">

  </div>

  <div class="section section">

  <div class="pointer">

  </div>

  <div class="abstract">

  The distance type for the warning, e.g. a warning for a new traffic merge location ahead or a warning for passing a traffic merge location. Since the traffic merge warning is given relative to a single position on the route, `DistanceType.REACHED` will never be given for this warning.

  </div>

  <div class="declaration">

  #### Declaration

  <div class="language">

  Swift

  ``` highlight
  public var distanceType: DistanceType
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-distancetype">DistanceType</a>

  </div>

  </div>

  </div>

- <div>

   <span id="sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV2id010distanceTobC8InMeters8roadType4side9laneCount0fK0ACs5Int32V_SdAA0bc4RoadK0OAA0bC4SideOAkA08DistanceK0Otcfc"></span> <span id="sdk-for-ios-navigate-apple_ref-swift-Method-init-id-distanceToTrafficMergeInMeters-roadType-side-laneCount-distanceType" class="dashAnchor"></span> <a href="sdk-for-ios-navigate-structs-trafficmergewarning#sdk-for-ios-navigate-s-7heresdk19TrafficMergeWarningV2id010distanceTobC8InMeters8roadType4side9laneCount0fK0ACs5Int32V_SdAA0bc4RoadK0OAA0bC4SideOAkA08DistanceK0Otcfc" class="token"><code>init(id:</code><wbr></wbr><code>distanceToTrafficMergeInMeters:</code><wbr></wbr><code>roadType:</code><wbr></wbr><code>side:</code><wbr></wbr><code>laneCount:</code><wbr></wbr><code>distanceType:</code><wbr></wbr><code>)</code></a> 

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
  public init(id: Int32 = 0, distanceToTrafficMergeInMeters: Double, roadType: TrafficMergeRoadType = TrafficMergeRoadType.sliproad, side: TrafficMergeSide = TrafficMergeSide.right, laneCount: Int32 = 1, distanceType: DistanceType)
  ```

  </div>

  Related types:

  - <a href="sdk-for-ios-navigate-enums-trafficmergeroadtype">TrafficMergeRoadType</a>
  - <a href="sdk-for-ios-navigate-enums-trafficmergeside">TrafficMergeSide</a>
  - <a href="sdk-for-ios-navigate-enums-distancetype">DistanceType</a>

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

